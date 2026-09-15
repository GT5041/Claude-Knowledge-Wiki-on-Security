# Claude-Knowledge-Wiki-on-Security

Wiki specialized on Claude security — a source-traceable reference covering the Claude models, the Claude API, Claude Code, and the enterprise products.

Claude セキュリティに特化した Wiki です。Claude のモデル本体、Claude API、Claude Code、エンタープライズ製品を対象に、出典を追跡できる形でまとめています。

## Pages / ページ

| Page | Language | What it covers |
|---|---|---|
| **[Claude Security](wiki/Claude-Security.md)** | English | 11 themes, 7 role-based reading paths, 22 FAQs, and a register of the official sources every claim is tagged to |
| **[Claude セキュリティ](wiki/Claude-Security.ja.md)** | 日本語 | 11 のテーマ、7 つの役割別の読む順序、22 の FAQ、全記述が紐づく公式出典レジスタ |
| **[Claude Code エンタープライズ導入事例](wiki/Claude-Code-Enterprise-Adoption.ja.md)** | 日本語 | Claude Code の企業導入事例 18 件と大規模展開 9 件の一覧。業種・地域・導入パターン・公表指標の索引つき |
| **[Claude 公式ユースケース集](wiki/Claude-Use-Cases.ja.md)** | 日本語 | 公式が公表しているユースケース 46 件。開発ワークフロー、自動化・CI/CD、マルチエージェント、非開発部門での利用、API でのアプリ構築。目的別・立場別の索引つき |
| **[Claude for Small Business](wiki/Claude-for-Small-Business.ja.md)** | 日本語 | 中小企業向けパッケージの概要・前提条件・同梱ワークフローと、導入前に確認すべきデータ取り扱いの論点 |

The security page is available in both languages; the adoption, use-case and small-business pages are Japanese only for now.

Both security versions share the same `T#` / `I#` / `Q#` / `S#` identifiers, so a finding can be cited by ID regardless of which language the reader used.

両版は `T#` ／ `I#` ／ `Q#` ／ `S#` の ID 体系を共有しています。読者がどちらの言語を見ていても、ID で同じ箇所を参照できます。

## Tools / ツール

| Tool | What it does |
|---|---|
| **[実装方針アドバイザー](agent/README.md)** (`agent/`) | Claude Code で実装したいことを自然文で入力すると、不足情報を質問フォーマットで確認したうえで、実装案とセキュリティ考慮事項を Markdown レポートとして出力する対話型 CLI エージェント。セキュリティ考点は本リポジトリの Wiki の ID（`T#`/`Q#`）に紐づけて出力されます |

## Principles / 方針

- **Traceable.** Every claim carries a source tag (`[S1]`, `[S2]`, …) that resolves in the page's source register. Claims sourced from pages that could not be directly retrieved are marked as such rather than asserted.
  — すべての記述に出典タグを付け、出典レジスタで解決できるようにしています。直接取得できなかった情報源に基づく記述は、断定せずその旨を明示しています。
- **Three ways in.** The same material is indexed *by theme* (`T1`–`T11`), *by interest / role* (`I1`–`I7`), and *by question* (`Q1`–`Q22`).
  — 同じ内容を「テーマ別」「関心・役割別」「質問別」の 3 軸で索引化しています。
- **Primary sources win.** Anthropic's own documentation and your contract supersede anything written here. Start from the [Anthropic Trust Center](https://trust.anthropic.com).
  — 公式情報と契約が優先します。まず [Anthropic Trust Center](https://trust.anthropic.com) を参照してください。

## Key upstream sources / 主な一次情報源

- [Anthropic Trust Center](https://trust.anthropic.com) — certifications, sub-processors, security documentation
- [Claude Code — Security](https://code.claude.com/docs/en/security) · [Data usage](https://code.claude.com/docs/en/data-usage) · [Zero data retention](https://code.claude.com/docs/en/zero-data-retention) · [Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- [Claude API — API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) · [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api)
- [Securely deploying AI agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment) · [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)

## Contributing / メンテナンス

See [Maintaining this page](wiki/Claude-Security.md#maintaining-this-page) / [本ページのメンテナンス](wiki/Claude-Security.ja.md#maintain).

In short: tag every claim with a source, re-verify quarterly, keep the theme/interest/FAQ indexes in sync, keep the two language versions at ID parity, and never paste NDA-restricted material into this repository.

要点：すべての記述に出典タグを付ける／四半期ごとに再確認する／3 つの索引を同期させる／日英で ID を揃える／NDA 対象資料は本リポジトリに置かない。
