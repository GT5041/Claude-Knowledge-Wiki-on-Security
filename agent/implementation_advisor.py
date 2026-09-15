#!/usr/bin/env python3
"""Claude Code 実装方針アドバイザー (対話型 CLI エージェント)

質問者が「Claude Code で実装したいこと」を自然文で入力すると、

  1. 方針決定に必要な情報が足りているかを判定し、
  2. 足りなければ決まった質問フォーマットで質問して方針を確認し、
  3. 実装案（複数）とセキュリティ上の考慮事項を Markdown レポートとして出力する。

セキュリティ観点は agent/knowledge/security_checklist.md を知識源とし、
本リポジトリの Claude セキュリティ Wiki のテーマ ID (T#) / FAQ ID (Q#) に紐づけて出力する。

使い方:
    export ANTHROPIC_API_KEY=sk-ant-...          # または `ant auth login`
    python3 agent/implementation_advisor.py       # 対話モード
    python3 agent/implementation_advisor.py -r "社内APIのテストを自動生成したい"
    python3 agent/implementation_advisor.py --max-rounds 1 --out reports/
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import textwrap
from pathlib import Path
from typing import List, Literal, Optional

try:
    import anthropic
    from pydantic import BaseModel, Field
except ImportError:  # pragma: no cover - 依存未導入時の案内
    sys.exit(
        "依存パッケージが見つかりません。次を実行してください:\n"
        "    pip install -r agent/requirements.txt"
    )

# --- 設定 -------------------------------------------------------------------

MODEL = "claude-opus-5"
MAX_TOKENS = 16000
DEFAULT_MAX_ROUNDS = 3  # 追加質問の最大ラウンド数

AGENT_DIR = Path(__file__).resolve().parent
REPO_ROOT = AGENT_DIR.parent
CHECKLIST_PATH = AGENT_DIR / "knowledge" / "security_checklist.md"
WIKI_PATH = REPO_ROOT / "wiki" / "Claude-Security.ja.md"
DEFAULT_OUT_DIR = AGENT_DIR / "reports"

# 追加の任意知識源。存在すればシステムプロンプトに載せる。
OPTIONAL_KNOWLEDGE = [WIKI_PATH]


# --- 出力スキーマ -----------------------------------------------------------
# structured outputs で受け取る形。ここが CLI とモデルの間の契約になる。


class QuestionOption(BaseModel):
    """質問の選択肢。質問者が番号で答えられるようにする。"""

    label: str = Field(description="選択肢の短い名称（20字以内）")
    description: str = Field(description="この選択肢を選ぶと何が決まるか、1〜2文")
    is_recommended: bool = Field(description="現時点の情報から見た推奨か")


class Question(BaseModel):
    """方針確認のための質問 1 件。"""

    id: str = Field(description="Q1, Q2 ... の形式の連番 ID")
    category: Literal[
        "目的・スコープ", "対象データ", "実行環境", "権限・自動化",
        "既存資産・制約", "コンプライアンス", "運用・体制",
    ] = Field(description="質問の分類")
    question: str = Field(description="質問文。一問一答で答えられる粒度にする")
    why_needed: str = Field(
        description="なぜこの質問が必要か。回答によって実装案やセキュリティ要件がどう変わるかを1〜2文で"
    )
    options: List[QuestionOption] = Field(
        description="選択肢。2〜4個。自由記述のみで答えるべき質問なら空配列",
        default_factory=list,
    )
    assumption_if_unanswered: str = Field(
        description="回答が得られない場合に置く既定の仮定。レポートには仮定として明記する"
    )


class Clarification(BaseModel):
    """要件確認フェーズの出力。"""

    understanding: str = Field(description="現時点で理解した要求の要約。2〜4文")
    status: Literal["need_info", "ready"] = Field(
        description="レポート生成に十分な情報が揃っていれば ready、足りなければ need_info"
    )
    questions: List[Question] = Field(
        description="status が need_info のときのみ 1〜4 件。ready なら空配列",
        default_factory=list,
    )


class ImplementationOption(BaseModel):
    """実装案 1 件。"""

    id: str = Field(description="A, B, C の形式")
    name: str = Field(description="案の名称。何をどう作るかが一目で分かるもの")
    summary: str = Field(description="1〜3文の概要")
    steps: List[str] = Field(description="実装手順。3〜7ステップ。各ステップは具体的な作業")
    claude_code_features: List[str] = Field(
        description="使う Claude Code の機能（スキル、フック、サブエージェント、MCP、CI連携、権限設定など）"
    )
    pros: List[str] = Field(description="この案の利点。2〜4項目")
    cons: List[str] = Field(description="この案の欠点・制約。2〜4項目")
    effort: Literal["小（数時間〜1日）", "中（数日）", "大（1週間以上）"] = Field(
        description="おおよその実装工数"
    )
    fit_for: str = Field(description="どういう条件のときにこの案が最適か")


class SecurityConsideration(BaseModel):
    """セキュリティ考慮事項 1 件。"""

    id: str = Field(description="S1, S2 ... の形式の連番 ID")
    title: str = Field(description="考慮事項の見出し")
    checklist_ref: str = Field(
        description="knowledge/security_checklist.md の観点 ID。例: SEC-04"
    )
    wiki_ref: str = Field(
        description="Wiki のテーマ/FAQ ID をカンマ区切りで。例: T5, Q8, Q13"
    )
    severity: Literal["高", "中", "低"] = Field(
        description="この実装に対する重大度。権限 × 到達範囲 × 非信頼入力の有無で判断する"
    )
    risk: str = Field(description="何が起きうるか。この実装に即した具体的なシナリオで書く")
    mitigations: List[str] = Field(
        description="緩和策。設定名・コマンド・構成レベルで具体的に。2〜5項目。"
                    "「注意する」のような抽象的な記述は書かない"
    )
    applies_to: List[str] = Field(
        description="関係する実装案の ID（A/B/C）。全案に共通なら [\"全案\"]"
    )


class Report(BaseModel):
    """最終レポート。"""

    title: str = Field(description="レポートのタイトル。何を実装する話かが分かるもの")
    understanding: str = Field(description="要求の理解。3〜5文")
    assumptions: List[str] = Field(
        description="回答が得られず仮定を置いた点、および暗黙に前提とした事項"
    )
    options: List[ImplementationOption] = Field(description="実装案。2〜3件")
    recommended_option_id: str = Field(description="推奨する案の ID")
    recommendation_reason: str = Field(description="なぜその案を推すか。2〜4文")
    security_considerations: List[SecurityConsideration] = Field(
        description="セキュリティ考慮事項。重大度の高い順に 4〜10件"
    )
    open_risks: List[str] = Field(
        description="このレポートでは判断できず、質問者側で確認が必要な残論点"
    )
    next_steps: List[str] = Field(description="質問者が次に取るべき具体的な行動。3〜5項目")


# --- プロンプト -------------------------------------------------------------

ROLE = textwrap.dedent(
    """\
    あなたは Claude Code の導入・実装を支援するソリューションアーキテクトです。
    エンタープライズのセキュリティ要件を理解しており、実装案を出すときは必ず
    セキュリティ上の影響をセットで提示します。

    守るべき原則:
    - 実装案は具体的に。「Claude Code を使う」ではなく、どの機能をどう構成するかまで書く。
    - セキュリティ考慮事項は、その実装に即した具体的なシナリオで書く。一般論を並べない。
    - 緩和策は設定名・コマンド・構成レベルで書く。「注意する」は緩和策ではない。
    - 断定できないことは仮定または残論点として明示する。推測を事実のように書かない。
    - 出力はすべて日本語。ただし設定キー・コマンド・製品名は原語のまま。
    """
)

CLARIFY_TASK = textwrap.dedent(
    """\
    # タスク: 要件の充足判定と質問

    質問者の要求を読み、実装案とセキュリティ考慮事項を出すのに十分な情報があるか判定してください。

    ## ready（十分）と判定してよい条件
    次がすべて読み取れる、または合理的な既定値を置ける場合:
    1. 何を作る/自動化するのか（対象と成果物）
    2. 誰が実行するのか、人の承認が入るか
    3. 扱うデータの機微度（社外秘・個人情報・PHI などを含むか）
    4. 実行環境（開発者のローカル / CI / サーバー / クラウド）

    ## need_info と判定する条件
    上記のうち、**回答によって実装案そのものが変わる**ものが欠けている場合。
    「あれば嬉しい」程度の情報のために質問しないでください。質問は最大 4 件。

    ## 質問の作り方
    - 一問一答で答えられる粒度にする。複数論点を1つの質問に詰め込まない。
    - 選択肢は 2〜4 個。質問者が番号で即答できるようにする。
    - why_needed には「この回答で実装案/セキュリティ要件がどう変わるか」を書く。
      単なる言い換えを書かない。
    - assumption_if_unanswered には、回答が無い場合に置く既定の仮定を書く。
      安全側（より制約が強い側）に倒すこと。
    """
)

REPORT_TASK = textwrap.dedent(
    """\
    # タスク: 実装レポートの作成

    ここまでのやり取りを踏まえ、実装案とセキュリティ考慮事項のレポートを作成してください。

    ## 実装案
    - 2〜3 案。案は**トレードオフが異なる**ものにする（同じ方針の細部違いにしない）。
      例: 手元で対話的に使う案 / スキル化して標準化する案 / CI に組み込む案。
    - 各案について、使う Claude Code の機能を具体的に挙げる。
    - 推奨案を 1 つ選び、理由を書く。「どれも良い」と逃げない。

    ## セキュリティ考慮事項
    - 提供されたチェックリストの観点 ID（SEC-xx）と Wiki の ID（T#/Q#）を必ず紐づける。
    - **この実装に該当しない観点は書かない。** 網羅より関連性を優先する。
    - 重大度は「権限 × 到達範囲 × 非信頼入力の有無」で判断する。
      外部由来のテキストを読み、書き込み権限があり、外部通信できる構成は最も危険。
    - 案ごとにリスクが違う場合は applies_to で区別する。
    - 実装案が外部由来のコンテンツ（Issue/PR 本文、Web、メール、依存パッケージ等）に
      触れる場合、間接プロンプトインジェクション（SEC-04）は必ず含める。
    - 無人実行・自動実行が含まれる場合、権限モデル（SEC-05）と分離（SEC-06）は必ず含める。
    """
)


def load_knowledge() -> str:
    """セキュリティチェックリストと（あれば）Wiki を読み込む。"""
    if not CHECKLIST_PATH.exists():
        sys.exit(f"知識ファイルが見つかりません: {CHECKLIST_PATH}")

    parts = [
        "# 知識源 1: セキュリティ観点チェックリスト\n\n" + CHECKLIST_PATH.read_text(encoding="utf-8")
    ]
    for i, path in enumerate(OPTIONAL_KNOWLEDGE, start=2):
        if path.exists():
            parts.append(
                f"# 知識源 {i}: {path.name}（参照用。ID の対応付けに使う）\n\n"
                + path.read_text(encoding="utf-8")
            )
    return "\n\n---\n\n".join(parts)


def build_system(knowledge: str) -> list[dict]:
    """システムプロンプト。知識部分は毎ターン同一なのでキャッシュさせる。"""
    return [
        {"type": "text", "text": ROLE},
        {
            "type": "text",
            "text": knowledge,
            # 知識は全ターン共通の固定接頭辞。ここでキャッシュを効かせる。
            "cache_control": {"type": "ephemeral"},
        },
    ]


# --- API 呼び出し -----------------------------------------------------------


def call_model(client, system, messages, output_format):
    """structured outputs で 1 回応答を得る。

    Claude Opus 5 はセーフティ分類器により stop_reason="refusal" を返しうる。
    サーバーサイドフォールバックが使える環境ではそれを使い、
    使えなければ通常パスに落として refusal を明示的に扱う。
    """
    try:
        response = client.beta.messages.parse(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system,
            messages=messages,
            output_format=output_format,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
    except (TypeError, AttributeError, anthropic.BadRequestError):
        # beta パス／fallbacks 非対応の SDK・環境では通常パスで実行する
        response = client.messages.parse(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system,
            messages=messages,
            output_format=output_format,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
        )

    if response.stop_reason == "refusal":
        detail = getattr(response, "stop_details", None)
        category = getattr(detail, "category", None) if detail else None
        sys.exit(
            "モデルが安全性の理由で応答を拒否しました"
            + (f"（category: {category}）" if category else "")
            + "。入力内容を見直してください。"
        )
    if response.stop_reason == "max_tokens":
        sys.exit("応答が max_tokens に達して打ち切られました。要求を分割して再実行してください。")

    return response.parsed_output


# --- CLI 表示 ---------------------------------------------------------------

RULE = "─" * 72


def render_questions(clarification: Clarification, round_no: int) -> None:
    """質問フォーマットで出力する。ここが質問者に見える画面。"""
    print(f"\n{RULE}")
    print(f"  確認させてください（{round_no} 回目 / 質問 {len(clarification.questions)} 件）")
    print(RULE)
    print(f"\n【現時点の理解】\n{textwrap.indent(clarification.understanding, '  ')}\n")

    for q in clarification.questions:
        print(f"■ {q.id} [{q.category}] {q.question}")
        print(f"  └ なぜ聞くか: {q.why_needed}")
        if q.options:
            for n, opt in enumerate(q.options, start=1):
                mark = " ★推奨" if opt.is_recommended else ""
                print(f"     {n}. {opt.label}{mark} — {opt.description}")
            print(f"     0. わからない／未定 → 仮定「{q.assumption_if_unanswered}」を置いて進めます")
        else:
            print("     （自由記述でお答えください）")
            print(f"     空欄の場合の仮定: {q.assumption_if_unanswered}")
        print()


def collect_answers(clarification: Clarification) -> str:
    """質問への回答を対話的に集め、モデルに返す 1 本のテキストにまとめる。"""
    lines = []
    for q in clarification.questions:
        while True:
            try:
                raw = input(f"{q.id} への回答 > ").strip()
            except EOFError:
                raw = ""
            if not raw:
                lines.append(f"{q.id}: （未回答。仮定「{q.assumption_if_unanswered}」で進めてよい）")
                break
            if q.options and raw.isdigit():
                n = int(raw)
                if n == 0:
                    lines.append(
                        f"{q.id}: わからない／未定。仮定「{q.assumption_if_unanswered}」で進めてよい"
                    )
                    break
                if 1 <= n <= len(q.options):
                    lines.append(f"{q.id}: {q.options[n - 1].label}（{q.options[n - 1].description}）")
                    break
                print(f"  1〜{len(q.options)} または 0 で答えてください。自由記述も可。")
                continue
            lines.append(f"{q.id}: {raw}")
            break
    return "以下が回答です。\n" + "\n".join(lines)


# --- レポート整形 -----------------------------------------------------------

SEVERITY_MARK = {"高": "🔴 高", "中": "🟡 中", "低": "🟢 低"}


def render_report(report: Report, request: str, transcript: List[str]) -> str:
    """Report を Markdown に整形する。"""
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    out: List[str] = []
    a = out.append

    a(f"# {report.title}\n")
    a(f"> Claude Code 実装方針レポート ／ 生成日時: {now}")
    a(f"> 生成: `agent/implementation_advisor.py`（model: `{MODEL}`）\n")
    a("---\n")

    a("## 1. 元の要求\n")
    a("```")
    a(request.strip())
    a("```\n")

    a("## 2. 要求の理解\n")
    a(report.understanding + "\n")

    if report.assumptions:
        a("### 置いた仮定\n")
        a("> 以下は確認が取れなかった、または暗黙に前提とした事項です。**認識が違う場合は結論が変わります。**\n")
        for x in report.assumptions:
            a(f"- {x}")
        a("")

    a("## 3. 実装案\n")
    a("| 案 | 名称 | 工数 | 適する条件 |")
    a("|---|---|---|---|")
    for o in report.options:
        star = " ★推奨" if o.id == report.recommended_option_id else ""
        a(f"| **{o.id}**{star} | {o.name} | {o.effort} | {o.fit_for} |")
    a("")

    for o in report.options:
        star = "  ★ 推奨案" if o.id == report.recommended_option_id else ""
        a(f"### 案 {o.id}: {o.name}{star}\n")
        a(o.summary + "\n")
        a("**実装手順**\n")
        for i, s in enumerate(o.steps, start=1):
            a(f"{i}. {s}")
        a("")
        a("**使用する Claude Code の機能**\n")
        for f in o.claude_code_features:
            a(f"- {f}")
        a("")
        a("| 利点 | 欠点・制約 |")
        a("|---|---|")
        for i in range(max(len(o.pros), len(o.cons))):
            p = o.pros[i] if i < len(o.pros) else ""
            c = o.cons[i] if i < len(o.cons) else ""
            a(f"| {p} | {c} |")
        a("")

    a(f"### 推奨: 案 {report.recommended_option_id}\n")
    a(report.recommendation_reason + "\n")

    a("## 4. セキュリティ上の考慮事項\n")
    a("各項目は `agent/knowledge/security_checklist.md` の観点 ID と、")
    a("[Claude セキュリティ Wiki](../../wiki/Claude-Security.ja.md) のテーマ／FAQ ID に紐づいています。\n")
    a("| # | 重大度 | 考慮事項 | 対象 | 観点 | Wiki |")
    a("|---|---|---|---|---|---|")
    for s in report.security_considerations:
        sev = SEVERITY_MARK.get(s.severity, s.severity)
        a(f"| {s.id} | {sev} | {s.title} | {', '.join(s.applies_to)} | `{s.checklist_ref}` | {s.wiki_ref} |")
    a("")

    for s in report.security_considerations:
        sev = SEVERITY_MARK.get(s.severity, s.severity)
        a(f"### {s.id} [{sev}] {s.title}\n")
        a(f"- **対象:** {', '.join(s.applies_to)}　**観点:** `{s.checklist_ref}`　**Wiki:** {s.wiki_ref}")
        a(f"- **リスク:** {s.risk}")
        a("- **緩和策:**")
        for m in s.mitigations:
            a(f"  - {m}")
        a("")

    if report.open_risks:
        a("## 5. 残論点（質問者側での確認が必要）\n")
        for x in report.open_risks:
            a(f"- {x}")
        a("")

    a("## 6. 次のアクション\n")
    for i, x in enumerate(report.next_steps, start=1):
        a(f"{i}. {x}")
    a("")

    if transcript:
        a("---\n")
        a("<details>\n<summary>付録: 確認のやり取り</summary>\n")
        for t in transcript:
            a("```")
            a(t.strip())
            a("```\n")
        a("</details>\n")

    a("---\n")
    a("*本レポートは Claude が生成した実装方針の**たたき台**です。"
      "セキュリティ考慮事項は網羅を保証するものではありません。"
      "本番適用前に、自社のセキュリティ／コンプライアンス担当によるレビューを受けてください。*")

    return "\n".join(out) + "\n"


def slugify(text: str, limit: int = 32) -> str:
    s = re.sub(r"[^\w぀-ヿ一-鿿-]+", "-", text).strip("-")
    return (s[:limit] or "report").rstrip("-")


# --- メイン -----------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Claude Code で実装したいことを入力すると、実装案とセキュリティ考慮事項のレポートを生成します。"
    )
    parser.add_argument("-r", "--request", help="実装したいこと。省略すると対話的に入力を求めます")
    parser.add_argument(
        "--max-rounds", type=int, default=DEFAULT_MAX_ROUNDS,
        help=f"追加質問の最大ラウンド数 (既定: {DEFAULT_MAX_ROUNDS}、0 で質問せず即レポート)",
    )
    parser.add_argument("--out", default=str(DEFAULT_OUT_DIR), help="レポートの出力先ディレクトリ")
    parser.add_argument("--json", action="store_true", help="レポートの生 JSON も併せて保存する")
    args = parser.parse_args()

    if not (os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN")):
        print(
            "[注意] ANTHROPIC_API_KEY が未設定です。`ant auth login` 済みのプロファイルがあれば"
            "そのまま動作します。認証が無い場合は API キーを設定してください。\n",
            file=sys.stderr,
        )

    print(RULE)
    print("  Claude Code 実装方針アドバイザー")
    print(RULE)

    request = args.request
    if not request:
        print("\nClaude Code で実装したいことを入力してください。")
        print("（複数行可。入力し終えたら空行で Enter）\n")
        lines: List[str] = []
        while True:
            try:
                line = input("> " if not lines else "  ")
            except EOFError:
                break
            if not line.strip() and lines:
                break
            if line.strip():
                lines.append(line)
        request = "\n".join(lines)

    if not request.strip():
        print("入力がありません。終了します。")
        return 1

    client = anthropic.Anthropic()
    system = build_system(load_knowledge())
    messages: List[dict] = [
        {"role": "user", "content": f"{CLARIFY_TASK}\n\n# 質問者の要求\n\n{request.strip()}"}
    ]
    transcript: List[str] = []

    # --- 要件確認ループ ---
    for round_no in range(1, max(args.max_rounds, 0) + 1):
        print(f"\n…要件を確認しています（{round_no}/{args.max_rounds}）")
        clarification: Clarification = call_model(client, system, messages, Clarification)

        if clarification.status == "ready" or not clarification.questions:
            print(f"\n【理解】{clarification.understanding}")
            print("\n情報が揃いました。レポートを作成します。")
            messages.append({"role": "assistant", "content": clarification.model_dump_json()})
            break

        render_questions(clarification, round_no)
        answers = collect_answers(clarification)
        transcript.append(
            "\n".join(f"{q.id} [{q.category}] {q.question}" for q in clarification.questions)
            + "\n\n"
            + answers
        )
        messages.append({"role": "assistant", "content": clarification.model_dump_json()})
        messages.append({"role": "user", "content": answers})
    else:
        if args.max_rounds > 0:
            print("\n質問の上限に達しました。ここまでの情報でレポートを作成します。")

    # --- レポート生成 ---
    print("\n…レポートを作成しています（1〜2 分かかることがあります）")
    messages.append({"role": "user", "content": REPORT_TASK})
    report: Report = call_model(client, system, messages, Report)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    md_path = out_dir / f"{stamp}-{slugify(report.title)}.md"
    md_path.write_text(render_report(report, request, transcript), encoding="utf-8")

    if args.json:
        json_path = md_path.with_suffix(".json")
        json_path.write_text(
            json.dumps(report.model_dump(), ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"  JSON: {json_path}")

    print(f"\n{RULE}")
    print("  レポートを出力しました")
    print(RULE)
    print(f"\n  {md_path}\n")
    print(f"  実装案: {len(report.options)} 件（推奨: 案 {report.recommended_option_id}）")
    high = sum(1 for s in report.security_considerations if s.severity == "高")
    print(f"  セキュリティ考慮事項: {len(report.security_considerations)} 件（うち重大度「高」 {high} 件）\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n中断しました。")
        sys.exit(130)
    except anthropic.APIStatusError as exc:
        sys.exit(f"API エラー ({exc.status_code}): {exc.message}")
    except anthropic.APIConnectionError as exc:
        sys.exit(f"API に接続できませんでした: {exc}")
