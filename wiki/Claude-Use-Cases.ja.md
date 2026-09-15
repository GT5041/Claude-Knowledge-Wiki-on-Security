# Claude 公式ユースケース集

> Anthropic／Claude が公式に公表しているユースケースを、出典を追跡できる形で整理した一覧です。Claude Code の開発ワークフローから、非開発部門での使われ方、Claude API／Agent SDK で構築するアプリケーションまでを対象にしています。
>
> **最終確認日:** 2026-09-15 ／ **管理者:** 本リポジトリのオーナー ／ **主な一次情報源:** [Claude Code ドキュメント](https://code.claude.com/docs/en/overview)・[Claude プラットフォームドキュメント](https://platform.claude.com/docs/en/about-claude/use-case-guides/overview)

---

## 検証ステータス

本ページは、記載の大半を**公式ドキュメントから直接取得して確認**しています。ただし一部の情報源（`claude.com` のブログ・ソリューションページ、`anthropic.com`）は作成環境のエグレス制限により直接取得できず、検索経由の要約に基づいています。

| 記号 | 意味 | 本ページでの該当範囲 |
|---|---|---|
| ✅ | 公式ドキュメントを**直接取得して確認済** | [A](#cat-a)〜[D](#cat-d)、[F](#cat-f) の大半 |
| 🔎 | 公式 URL の実在は確認。内容は検索経由の要約で原文は未読 | [E](#cat-e)（Anthropic 社内事例）、[業界別ソリューション](#solutions) |

数値や固有の表現を社外資料に引用する場合は、🔎 の項目については必ず出典 URL を開いて原文を確認してください。

---

<a id="how-to-use"></a>
## このページの使い方

| 入口 | こんなとき | 移動先 |
|---|---|---|
| **カテゴリから探す** | どんなことができるのか全体像を知りたい | [カテゴリ索引](#cat-index) → `U1`〜`U41` |
| **目的から探す** | 「〜したい」が決まっている | [目的別索引](#goal-index) |
| **立場から探す** | 自分の職種での使い道を知りたい | [立場別索引](#role-index) |

**ID 体系：** `U#` = ユースケース、`S#` = [出典レジスタ](#sources)。本リポジトリの他ページ（[Claude セキュリティ](Claude-Security.ja.md)、[導入事例](Claude-Code-Enterprise-Adoption.ja.md)）と同じ運用方針です。

> **関連ページ：** 「どの企業が使っているか」は [Claude Code エンタープライズ導入事例](Claude-Code-Enterprise-Adoption.ja.md)、「安全に使うには」は [Claude セキュリティ](Claude-Security.ja.md) を参照してください。本ページは「**何ができるか**」を扱います。

---

<a id="cat-index"></a>
## カテゴリ索引

| カテゴリ | 内容 | ID | 主な出典 |
|---|---|---|---|
| [A. 日常の開発ワークフロー](#cat-a) | コード理解、バグ修正、リファクタリング、テスト、PR、ドキュメント | `U1`〜`U12` | `[S1]` `[S2]` |
| [B. 自動化・CI/CD・定期実行](#cat-b) | GitHub Actions、コードレビュー、セキュリティスキャン、スケジュール実行 | `U13`〜`U21` | `[S3]` |
| [C. 大規模・マルチエージェント](#cat-c) | サブエージェント、並列セッション、動的ワークフロー、大規模移行 | `U22`〜`U27` | `[S3]` `[S8]` |
| [D. 拡張・外部連携](#cat-d) | スキル、プラグイン、MCP、ブラウザ操作、Agent SDK | `U28`〜`U34` | `[S3]` |
| [E. 非開発部門での利用](#cat-e) | マーケティング、法務、データ分析、デザイン、セキュリティ | `U35`〜`U41` | `[S6]` `[S7]` |
| [F. API で構築するアプリケーション](#cat-f) | チケット振り分け、カスタマーサポート、コンテンツモデレーション等 | `U42`〜`U46` | `[S4]` |

---

<a id="cat-a"></a>
## A. 日常の開発ワークフロー

Claude Code の公式ドキュメント「Common workflows」`[S1]` と「Overview」`[S2]` に記載されたユースケースです。いずれも具体的なプロンプト例つきで公開されています。

| ID | ユースケース | 何をするか | 公式のプロンプト例 | 状態 |
|---|---|---|---|---|
| `U1` | **コードベースの全体把握** | 参画直後に構造・アーキテクチャ・データモデル・認証方式を把握する | `give me an overview of this codebase` → `explain the main architecture patterns used here` | ✅ |
| `U2` | **関連コードの特定** | 機能に関係するファイルを探し、相互作用と実行フローを追う | `find the files that handle user authentication` → `trace the login process from front-end to database` | ✅ |
| `U3` | **バグ修正** | エラーを共有し、修正案を複数得てから適用する | `I'm seeing an error when I run npm test` → `suggest a few ways to fix the @ts-ignore in user.ts` | ✅ |
| `U4` | **リファクタリング** | 非推奨 API の洗い出しから、後方互換を保った近代化とテスト検証まで | `find deprecated API usage in our codebase` → `refactor utils.js to use ES2024 features while maintaining the same behavior` | ✅ |
| `U5` | **テストの作成** | 未カバー箇所の特定 → 雛形生成 → 境界条件の追加 → 実行と修正 | `find functions in NotificationsService.swift that are not covered by tests` | ✅ |
| `U6` | **プルリクエスト作成** | 変更の要約から PR 作成、説明文の改善まで | `create a pr` → `enhance the PR description with more context about the security improvements` | ✅ |
| `U7` | **ドキュメント整備** | 未記載関数の特定 → JSDoc 生成 → 社内標準への適合確認 | `add JSDoc comments to the undocumented functions in auth.js` | ✅ |
| `U8` | **画像・スクリーンショットの活用** | エラー画面、UI モックアップ、DB スキーマ図を渡してコードを得る | `Generate CSS to match this design mockup` / `Here's a screenshot of the error. What's causing it?` | ✅ |
| `U9` | **非コードフォルダでの作業** | ノート、ドキュメントフォルダ等の Markdown 群の検索・編集・再構成 | （任意のディレクトリで `claude` を起動） | ✅ |
| `U10` | **プランモードでの事前レビュー** | ディスクに触れる前に変更計画を提示させ、承認してから実行する | `claude --permission-mode plan`（または `Shift+Tab`） | ✅ |
| `U11` | **スクリプトへのパイプ** | Unix ツールとして組み合わせ、CI やバッチ処理に使う | `git log --oneline -20 \| claude -p "summarize these recent commits"` | ✅ |
| `U12` | **Claude 自身への機能質問** | Claude Code の機能・制限をドキュメント基盤で回答させる | `how does Claude Code handle permissions?` | ✅ |

> 公式が挙げる「放置しがちな作業の自動化」の例：未テストコードへのテスト作成、プロジェクト全体の lint エラー修正、マージコンフリクト解消、依存関係の更新、リリースノート作成。`[S2]`

---

<a id="cat-b"></a>
## B. 自動化・CI/CD・定期実行

| ID | ユースケース | 何をするか | 手段 | 状態 |
|---|---|---|---|---|
| `U13` | **PR の自動コードレビュー** | 論理エラー、脆弱性、リグレッションを PR ごとに自動検出 | GitHub Code Review | ✅ |
| `U14` | **深掘りレビュー（ultrareview）** | クラウド上でマルチエージェントによる徹底レビュー | `/code-review ultra` | ✅ |
| `U15` | **書きながらの脆弱性検出** | Claude 自身のコード変更を脆弱性観点でレビュー・修正 | security-guidance プラグイン | ✅ |
| `U16` | **コードベースの脆弱性スキャン** | 既存コードをスキャンし、検出結果をパッチに変換 | Claude Security プラグイン | ✅ |
| `U17` | **GitHub Actions 連携** | `@claude` メンションへの応答、Issue の PR 化、タスク自動化 | GitHub Actions（Bedrock／Google Cloud／Foundry 経由も可） | ✅ |
| `U18` | **GitLab CI/CD 連携** | GitLab パイプラインへの組み込み | GitLab CI/CD | ✅ |
| `U19` | **クラウドでの定期実行** | PC の電源が落ちていても動く定期タスク。API 呼び出しや GitHub イベントでも起動可 | Routines（`/schedule`、claude.ai/code/routines） | ✅ |
| `U20` | **ローカルでの定期実行** | ローカルファイル・ツール・未コミット変更にアクセスが必要な定期タスク | Desktop scheduled tasks | ✅ |
| `U21` | **チャット・外部イベントからの起動** | Slack で `@Claude` にバグ報告 → PR が返る。Telegram／Discord／iMessage／独自 Webhook からセッションへイベント投入 | Slack 連携、Channels | ✅ |

**公式が挙げる定期実行の例：** 毎朝の PR レビュー、夜間の CI 失敗分析、週次の依存関係監査、PR マージ後のドキュメント同期。`[S1]` `[S2]`

> **定期タスクのプロンプトの書き方（公式の助言）:** 自律実行されるため確認の質問ができない。**何をもって成功とするか、結果をどうするかを明示する**。例：「`needs-review` ラベルの付いた PR をレビューし、問題があれば行コメントを付け、`#eng-reviews` に要約を投稿する」`[S1]`

---

<a id="cat-c"></a>
## C. 大規模コードベース・マルチエージェント

| ID | ユースケース | 何をするか | 手段 | 状態 |
|---|---|---|---|---|
| `U22` | **調査のサブエージェント委譲** | 大規模コードベースの探索でコンテキストが埋まるのを防ぎ、結果だけ受け取る | `use a subagent to investigate how our auth system handles token refresh` | ✅ |
| `U23` | **並列セッション（worktree）** | 一方で機能開発、もう一方でバグ修正を、編集を衝突させずに進める | `claude --worktree feature-auth` | ✅ |
| `U24` | **複数セッションの一元管理** | 多数のセッションを 1 画面から起動・監視する | agent view（バックグラウンドエージェント） | ✅ |
| `U25` | **エージェントチームの編成** | 共有タスクとエージェント間メッセージングで複数インスタンスを協調させる | agent teams | ✅ |
| `U26` | **動的ワークフローによる大規模実行** | コードベース監査、大規模移行、相互検証つき調査でサブエージェントを大量に統率 | dynamic workflows | ✅ |
| `U27` | **モノレポ・大規模リポジトリ対応** | ネストした `CLAUDE.md`、sparse worktree、パッケージ単位のスキル | large codebases 設定 | ✅ |

**大規模コード移行：** Anthropic は自社での大規模コード移行の方法論を公開しています `[S8]`。Bun 移行では未キャッシュ入力 59 億トークン・出力 6.9 億トークン（API 料金換算で約 16.5 万ドル）を要したと公表されています（🔎）。移行系の企業事例は[導入事例ページ](Claude-Code-Enterprise-Adoption.ja.md#patterns)のパターン A を参照。

---

<a id="cat-d"></a>
## D. 拡張・外部連携

| ID | ユースケース | 何をするか | 手段 | 状態 |
|---|---|---|---|---|
| `U28` | **チーム共通ワークフローの部品化** | `/review-pr`、`/deploy-staging` のような反復作業をスキル化して共有する | Skills | ✅ |
| `U29` | **プロジェクト規約の常時適用** | コーディング規約、アーキテクチャ決定、推奨ライブラリ、レビュー観点を毎セッション読ませる | `CLAUDE.md`、auto memory | ✅ |
| `U30` | **アクション前後の自動処理** | 編集後の自動フォーマット、コミット前の lint など | Hooks | ✅ |
| `U31` | **社内ツール・データ連携** | Google Drive の設計書を読む、Jira のチケットを更新する、Slack からデータを取る | MCP | ✅ |
| `U32` | **Web アプリのデバッグ・ブラウザ自動化** | コンソールログのデバッグ、フォーム自動入力、データ抽出 | Chrome 連携 | ✅ |
| `U33` | **独自エージェントの構築** | Claude Code のツール群を使い、統率・ツールアクセス・権限を自前で制御する | Agent SDK（CLI／Python／TypeScript） | ✅ |
| `U34` | **成果物の共有** | セッションの成果をインタラクティブなページとして claude.ai 上に公開する | Artifacts | ✅ |

> **関連：** MCP サーバーは Anthropic のセキュリティ監査対象外です。導入時は [Claude セキュリティ `T11`](Claude-Security.ja.md#t11) を参照してください。

---

<a id="cat-e"></a>
## E. 非開発部門・社内業務での利用

Anthropic 自身が公表している、社内各チームでの使われ方です。**「Claude Code はエンジニアだけのものではない」ことを示す実例**として参照できます。

> ⚠️ このセクションの出典（`claude.com` のブログ、`anthropic.com`）は作成環境から直接取得できず、内容は検索経由の要約です（🔎）。引用前に原文確認を推奨します。

| ID | 部門 | 使い方 | 公表されている効果 | 状態 |
|---|---|---|---|---|
| `U35` | **グロースマーケティング** | 数百件の広告 CSV を処理し、成績の低いものを特定して文字数制限つきで新バリエーションを生成する**エージェント型ワークフロー**（2 つのサブエージェント構成） | 数時間かかっていた作業が**数分**に | 🔎 |
| `U36` | **グロースマーケティング** | Figma プラグインを内製し、フレームを識別して見出し・説明文を差し替えた**最大 100 通りの広告バリエーション**を自動生成 | コピー&ペースト数時間 →**1 バッチ 0.5 秒** | 🔎 |
| `U37` | **法務** | 「社内の誰に相談すべきか」を案内する電話ツリー型システムを**開発リソースなしで**プロトタイプ | 部門が自前でツールを作れることの実証 | 🔎 |
| `U38` | **データサイエンス／インフラ** | 新任データサイエンティストがコードベース全体を Claude Code に読ませ、`CLAUDE.md` から依存関係とダッシュボードの上流データソースを把握 | 従来のデータカタログツールを代替 | 🔎 |
| `U39` | **データサイエンス** | ビジネス分析クエリの自動化 | クエリの **95% を自動化**（集計精度 約95%）。チームは因果推論・予測・機械学習に注力 | 🔎 |
| `U40` | **プロダクトデザイン** | Figma のデザインファイルを渡し、実装 → テスト実行 → 反復を**自律ループ**で回す。GitHub Actions で PR コメントも自動化 | フォーマット修正やテストのリファクタを自動処理 | 🔎 |
| `U41` | **セキュリティエンジニアリング** | 疑似コードを先に出させ、テスト駆動で誘導し、定期的に確認する進め方へ転換 | 「設計書 → 雑なコード → リファクタ → テストを諦める」から脱却 | 🔎 |

**その他の公表値（🔎）:** プロダクトエンジニアリングチームは Claude Code をあらゆるプログラミング作業の「first stop」と呼ぶ。推論チームでは ML 背景のないメンバーのモデル固有関数の調査時間が **80% 削減**。`[S7]`

---

<a id="cat-f"></a>
## F. Claude API／Agent SDK で構築するアプリケーション

Anthropic が**本番構築向けガイドとして公開している**ユースケースです `[S4]`。いずれも実装ガイドが付属します。

| ID | ユースケース | 内容 | ガイド | 状態 |
|---|---|---|---|---|
| `U42` | **チケット振り分け（Ticket routing）** | カスタマーサポートのチケットを大規模に分類・ルーティングする | [ticket-routing](https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing) | ✅ |
| `U43` | **カスタマーサポートエージェント** | 文脈を理解するチャットボットを構築する | [customer-support-chat](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat) | ✅ |
| `U44` | **コンテンツモデレーション** | コンテンツフィルタリングとモデレーションを行う | [content-moderation](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation) | ✅ |
| `U45` | **法務文書の要約** | 法的文書から要点を抽出し、調査を高速化する | [legal-summarization](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization) | ✅ |
| `U46` | **コマースエージェント** | ショッピング／マーチャント向けエージェントをオープンソースの雛形から構築 | [commerce-agents](https://platform.claude.com/docs/en/about-claude/use-case-guides/commerce-agents) | ✅ |

### 3 つの構築パス

公式は、自社で持つ制御の量に応じて 3 つの選択肢を提示しています `[S4]`。

| パス | 誰がエージェントループを持つか | 選ぶ基準 |
|---|---|---|
| **Messages API** | 自社。ツールもインフラも自前 | 制御を最大限に握りたい |
| **Claude Agent SDK** | SDK が提供、実行は自社プロセス | ループは任せたいが自社で動かしたい |
| **Claude Managed Agents** | Anthropic がループ・ツール実行・ランタイムをホスト | 委ねられる範囲を最大にしたい |

---

<a id="solutions"></a>
## 業界・領域別ソリューション（参考）

`claude.com/solutions` 配下で公開されている領域別ページです。直接取得できていないため、内容は検索経由の要約です（🔎）。

| 領域 | 公表されている位置づけ | URL |
|---|---|---|
| コーディング | Claude.ai と Claude API を通じたエンジニアリングワークフローの変革 | <https://claude.com/solutions/coding> |
| コード近代化 | 依存グラフ生成、デッドコード特定、複雑度とビジネス影響に基づくリファクタ優先順位付け | <https://claude.com/solutions/code-modernization> |
| 金融サービス | リサーチ、ディール業務、引受、保険金、モデルレビュー、月次決算。チャット／Cowork／Claude Code／M365 の併用が一般的 | <https://claude.com/solutions/financial-services> |
| ライフサイエンス | レガシー科学計算コードの読解、GxP 規制環境向けの堅牢なコード、PR レビューでのコンプライアンス問題の検出 | <https://claude.com/solutions/life-sciences> |
| エンタープライズ | Claude Enterprise プランの機能 | <https://claude.com/solutions/enterprise> |

---

<a id="goal-index"></a>
## 目的別索引

| やりたいこと | 該当ユースケース |
|---|---|
| 初めて触るコードベースを理解したい | [`U1`](#cat-a) [`U2`](#cat-a) [`U22`](#cat-c) [`U38`](#cat-e) |
| バグを直したい | [`U3`](#cat-a) [`U8`](#cat-a) |
| レガシーコードを近代化したい | [`U4`](#cat-a) [`U26`](#cat-c) ／ [導入事例パターン A](Claude-Code-Enterprise-Adoption.ja.md#patterns) |
| テストを増やしたい | [`U5`](#cat-a) [`U40`](#cat-e) [`U41`](#cat-e) |
| レビュー負荷を下げたい | [`U13`](#cat-b) [`U14`](#cat-b) [`U17`](#cat-b) |
| 脆弱性を早期に見つけたい | [`U15`](#cat-b) [`U16`](#cat-b) |
| 繰り返し作業を自動化したい | [`U19`](#cat-b) [`U20`](#cat-b) [`U11`](#cat-a) |
| チームでやり方を標準化したい | [`U28`](#cat-d) [`U29`](#cat-d) [`U30`](#cat-d) |
| 社内システムと連携させたい | [`U31`](#cat-d) [`U21`](#cat-b) |
| 大規模な作業を並列で回したい | [`U23`](#cat-c) [`U24`](#cat-c) [`U25`](#cat-c) [`U26`](#cat-c) |
| 実行前に内容を確認したい | [`U10`](#cat-a) |
| デザインから実装したい | [`U8`](#cat-a) [`U40`](#cat-e) |
| 非エンジニア部門に広げたい | [`U9`](#cat-a) [`U35`](#cat-e)〜[`U39`](#cat-e) |
| 自社プロダクトに組み込みたい | [`U33`](#cat-d) [`U42`](#cat-f)〜[`U46`](#cat-f) |

---

<a id="role-index"></a>
## 立場別索引

- **開発者（個人）:** [`U1`](#cat-a)〜[`U12`](#cat-a) から始める。特に `U1` `U3` `U5` `U10` は導入初日に効果が出やすい。
- **テックリード／EM:** [`U13`](#cat-b) [`U28`](#cat-d) [`U29`](#cat-d) — レビューと規約をチームの仕組みに落とす。
- **プラットフォーム／SRE:** [`U17`](#cat-b)〜[`U21`](#cat-b) [`U27`](#cat-c) — CI/CD と定期実行、大規模リポジトリ対応。
- **セキュリティ担当:** [`U15`](#cat-b) [`U16`](#cat-b) [`U41`](#cat-e) ＋ [Claude セキュリティ Wiki](Claude-Security.ja.md) を併読。
- **プロダクト／デザイン:** [`U8`](#cat-a) [`U40`](#cat-e) [`U34`](#cat-d)。
- **データ・分析:** [`U38`](#cat-e) [`U39`](#cat-e) [`U11`](#cat-a)。
- **コーポレート部門（法務・マーケ等）:** [`U9`](#cat-a) [`U35`](#cat-e)〜[`U37`](#cat-e)。
- **アプリケーション開発（自社プロダクト）:** [`U33`](#cat-d) [`U42`](#cat-f)〜[`U46`](#cat-f) ＋ [3 つの構築パス](#cat-f)。

---

<a id="caveats"></a>
## 読み方の注意

1. **公式が「できる」と書いていることと、自社で成果が出ることは別。** ドキュメントのユースケースは機能の提示であり、効果の保証ではありません。効果の実測については[導入事例ページの注意点](Claude-Code-Enterprise-Adoption.ja.md#caveats)を参照してください。
2. **社内事例（[E](#cat-e)）はツール提供元の自社利用である。** Anthropic は最も習熟した利用者であり、数値をそのまま外挿するのは危険です。
3. **機能は頻繁に増減する。** 本ページの機能名・コマンド名は 2026-09-15 時点のものです。`/loop`、Routines、agent teams のような比較的新しい機能は仕様変更の可能性があります。
4. **自動化・自律実行のユースケースにはセキュリティ設計が必須。** 特に [`U17`](#cat-b) [`U19`](#cat-b)〜[`U21`](#cat-b) [`U26`](#cat-c) のように**人の承認を経ずに動く**構成は、[Claude セキュリティ `T5`（プロンプトインジェクション）](Claude-Security.ja.md#t5)・[`T6`（権限）](Claude-Security.ja.md#t6)・[`T7`（分離）](Claude-Security.ja.md#t7) を必ず併読してください。外部から誰でも書ける Issue 本文や PR 本文をトリガーにする構成は、間接プロンプトインジェクションの典型的な入口です。
5. **実装方針を具体化したい場合**は、本リポジトリの[実装方針アドバイザー](../agent/README.md)（`agent/`）に要求を入力すると、実装案とセキュリティ考慮事項がレポートとして出力されます。

---

<a id="sources"></a>
## 出典レジスタ

| ID | 出典 | URL | 状態 |
|---|---|---|---|
| `S1` | Claude Code — Common workflows | <https://code.claude.com/docs/en/common-workflows> | ✅ 直接取得済 |
| `S2` | Claude Code — Overview（What you can do） | <https://code.claude.com/docs/en/overview> | ✅ 直接取得済 |
| `S3` | Claude Code ドキュメント索引（code review／security／CI/CD／routines／agents／skills／MCP／Agent SDK 各ページ） | <https://code.claude.com/docs/llms.txt> | ✅ 直接取得済 |
| `S4` | Claude プラットフォーム — Guides to common use cases | <https://platform.claude.com/docs/en/about-claude/use-case-guides/overview> | ✅ 直接取得済 |
| `S5` | Claude Code — Best practices | <https://code.claude.com/docs/en/best-practices> | ✅ 到達確認済 |
| `S6` | Anthropic News — How Anthropic teams use Claude Code | <https://www.anthropic.com/news/how-anthropic-teams-use-claude-code> | 🔎 検索経由 |
| `S7` | Claude Blog — How Anthropic teams use Claude Code | <https://claude.com/blog/how-anthropic-teams-use-claude-code> | 🔎 検索経由 |
| `S8` | Claude Blog — How Anthropic runs large-scale code migrations with Claude Code | <https://claude.com/blog/ai-code-migration> | 🔎 検索経由 |
| `S9` | Claude Blog — How Anthropic enables self-service data analytics with Claude | <https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude> | 🔎 検索経由 |
| `S10` | Claude Blog — How Anthropic uses Claude in Marketing | <https://claude.com/blog/how-anthropic-uses-claude-marketing> | 🔎 検索経由 |
| `S11` | Claude Blog — How to scale agentic coding across your engineering organization | <https://claude.com/blog/scaling-agentic-coding> | 🔎 検索経由 |
| `S12` | Claude Solutions（coding／code-modernization／financial-services／life-sciences／enterprise） | <https://claude.com/solutions/coding> ほか | 🔎 検索経由 |
| `S13` | Claude Code — Agent SDK overview | <https://code.claude.com/docs/en/agent-sdk/overview> | ✅ 索引経由で確認 |

### 掲載しなかったもの

- **プロンプトライブラリ:** `platform.claude.com/docs/en/resources/prompt-library/library` は現在プロンプトエンジニアリングのベストプラクティスページへリダイレクトされており、独立したユースケース集としては存在しません。
- **サードパーティの「活用事例まとめ」記事:** 公表主体と出典が不明確なため除外しています。

---

<a id="maintain"></a>
## 本ページのメンテナンス

1. **🔎 を ✅ にすることを最優先とする。** エグレス制限のない環境で `claude.com` / `anthropic.com` の該当ページを直接確認し、状態欄と内容を更新してください。
2. **機能名・コマンド名は原語のまま残す。** 翻訳すると公式ドキュメントで検索できなくなります。
3. **四半期ごとに `code.claude.com/docs/llms.txt` を再取得する。** 新機能のページが増えていればカテゴリ [B](#cat-b)〜[D](#cat-d) に追加してください。冒頭の*最終確認日*を更新します。
4. **「できること」と「効果」を混ぜない。** 本ページは機能とユースケース、効果の実測値は[導入事例ページ](Claude-Code-Enterprise-Adoption.ja.md)が担当です。
5. **自動化系ユースケースを追加したら、[注意 4](#caveats) のセキュリティ参照も更新する。**

*本ページは当リポジトリで管理する社内の参照用資料です。Anthropic の公式刊行物ではありません。仕様は変更されるため、実装前に必ず一次情報を確認してください。*
