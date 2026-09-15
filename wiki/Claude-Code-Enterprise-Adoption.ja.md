# Claude Code エンタープライズ導入事例 一覧

> Claude Code の企業導入事例を、Anthropic 公式（claude.com／anthropic.com）を一次ソースとし、Web 上の二次ソースを補助として整理した一覧です。
>
> **最終確認日:** 2026-09-15 ／ **管理者:** 本リポジトリのオーナー ／ **一次情報源:** [Claude Customer Stories](https://claude.com/customers)・[Anthropic News](https://www.anthropic.com/news)

---

## ⚠️ 本ページの検証ステータス（最初に読んでください）

**本ページ作成環境からは `claude.com` および `www.anthropic.com` に直接アクセスできませんでした（ネットワークのエグレス制限）。** したがって本ページの数値・記述は、**公式ページそのものを読んで確認したものではなく**、検索エンジン経由で得られた当該公式ページの要約に基づいています。

| 記号 | 意味 |
|---|---|
| 🔎 | **公式 URL は実在を確認。内容は検索経由の要約**。本ページ作成者が原文を直接読んで検証したものではない |
| ✅ | 公式ドキュメントを直接取得して確認済（本ページでは `code.claude.com` 系のみ） |
| ⚠️ | 二次ソース由来、または公表主体が不明確。裏取り必須 |

**したがって、本ページの数値を社外提案・稟議・監査資料に引用する場合は、必ず各行の公式 URL を開いて原文を確認してください。** 本ページの役割は「どの事例がどこにあるかの地図」であり、「数値の証跡」ではありません。

さらに、掲載した数値の大半は **ベンダーおよび導入企業が公表した自己申告値**です。測定方法・対象範囲・比較対象は事例ごとに異なり、そのまま横並び比較はできません。詳しくは[事例の読み方と注意点](#caveats)を必ず参照してください。

---

<a id="how-to-use"></a>
## このページの使い方

| 入口 | こんなとき | 移動先 |
|---|---|---|
| **一覧から探す** | まず全体像を把握したい | [導入事例一覧](#case-list) → `C1`〜`C18` |
| **大規模展開から探す** | 数万人規模の全社展開の実例を知りたい | [大規模パートナーシップ型展開](#partnerships) → `P1`〜`P9` |
| **導入パターンから探す** | 自社の想定用途に近い事例を探したい | [導入パターン別分類](#patterns) |
| **数値から探す** | 効果試算・ビジネスケースの材料が欲しい | [公表指標一覧](#metrics) |
| **業種・地域から探す** | 同業種／日本企業の事例を知りたい | [業種・地域別索引](#industry-index) |

**ID 体系：** `C#` = 個別導入事例、`P#` = パートナーシップ型の大規模展開、`S#` = [出典レジスタ](#sources)。本リポジトリの他ページ（[Claude セキュリティ](Claude-Security.ja.md)）と同じ運用方針です。

---

<a id="case-list"></a>
## 導入事例一覧

Claude Code が主題として明示されている事例を上段に、Claude Enterprise／Cowork など隣接製品の事例を下段に分けています。**「公表されている主な成果」は各社・Anthropic の公表値であり、本ページ作成者による検証値ではありません。**

### Claude Code が主題の事例

| ID | 企業 | 業種 | 地域 | 公表されている主な成果 | 出典 | 状態 |
|---|---|---|---|---|---|---|
| `C1` | **Stripe** | 金融インフラ／決済 | 米国 | エンジニア **1,370 名**へ展開。Scala **1 万行**の Java 移行を **4 日**で完了（手作業見積 **10 エンジニア週**）。JDK 更新が進み、滞留していた性能改善が可能に | `[S2]` | 🔎 |
| `C2` | **楽天（Rakuten）** | EC／インターネットサービス | 日本 | 新機能の市場投入までの平均日数が **24 営業日 → 5 営業日**（**79% 短縮**） | `[S3]` | 🔎 |
| `C3` | **LG CNS** | SI／ITサービス | 韓国 | **20 年もの**の基幹システム移行。**2,913 API 中 2,888（99.1%）**を変換し、**7 か月**で完了。従来型の再構築比 **約 50% のコスト** | `[S4]` | 🔎 |
| `C4` | **Ramp** | フィンテック | 米国 | 月間 **100 万行超**の AI 提案コードを処理。多数のエンジニアが日次利用、**約 50%** が週次利用。営業・リスク・経理・財務・採用など**非エンジニア部門**にも展開 | `[S5]` | 🔎 |
| `C5` | **クラスメソッド（Classmethod）** | SI／クラウドインテグレーション | 日本 | AI 駆動開発で **最大 10 倍**の生産性。マージ済 PR が **月 108 件（1月）→ 165 件（5〜6月）**。24 時間かかっていた作業が **1 時間** | `[S6]` | 🔎 |
| `C6` | **Cox Communications** | 通信／メディア | 米国 | 全社ロールアウトで **2,500 ユーザー**規模へ。市場投入 **55% 高速化**、キャンペーン効率 **40% 向上**、AI 投資初年度で **7 倍の ROI** | `[S7]` `[S8]` | 🔎 |
| `C7` | **PwC** | プロフェッショナルサービス | グローバル | **1 回のセッションで 400 名**のコンサルタントに Claude Code をトレーニング | `[S9]` | 🔎 |
| `C8` | **Satispay** | 決済／フィンテック | イタリア | 2025 年半ばに実チケットで **30 日間の構造化評価**を実施し他ツールと比較。**Java 8 → 21** と Spring の大型アップグレードを **4 日未満**で完了（当初見積 **4 週間**） | `[S10]` | 🔎 |
| `C9` | **HubSpot** | SaaS／CRM | 米国 | 2025 年のリブランドで、数か月規模と見込まれたフロントエンド移行を加速。開発者オンボーディングを短縮（※公式では Claude Platform (API) 事例として分類） | `[S11]` | 🔎 |
| `C10` | **Behavox** | コンプライアンス／金融IT | 米国・グローバル | **数百名**の開発者へ Claude Code 込みで展開。常用のペアプログラマとして定着し、他エージェントを上回ると評価 | `[S12]` | 🔎 |
| `C11` | **Altana** | サプライチェーンAI | 米国 | 開発速度が **2〜10 倍**に加速 | `[S12]` | 🔎 |
| `C12` | **Zapier** | 自動化SaaS | 米国（リモート） | Slack スレッドに**絵文字を付けるだけ**で Claude が文脈を解析し、コード生成から**マージリクエスト作成**まで数分で実行する仕組みを CTO が構築 | `[S13]` | 🔎 |

### 隣接製品（Claude Enterprise／Cowork）の事例 — 全社展開の参考として

| ID | 企業 | 製品 | 公表されている主な成果 | 出典 | 状態 |
|---|---|---|---|---|---|
| `C13` | **GitLab** | Claude Enterprise | 初期パイロットで回答者の **98%** が「満足」または「非常に満足」 | `[S14]` | 🔎 |
| `C14` | **Canva** | Claude Enterprise | 従業員 **5,000 名超**。急速な需要拡大と全社的な普及 | `[S15]` | 🔎 |
| `C15` | **Cyera** | Claude Cowork | スタック内 **40 ツール**と接続し **1,500 名**が利用 | `[S16]` | 🔎 |
| `C16` | **Brainlabs** | Claude Cowork | メディアエージェンシーの**全従業員**へ展開。従業員自身が**数百のスキル・自動化**を作成 | `[S17]` | 🔎 |
| `C17` | **Jamf** | Claude Enterprise | Apple デバイスを **7 万社超**に提供。全従業員が使えるツールとして Claude Enterprise を選定 | `[S18]` | 🔎 |
| `C18` | **Thomson Reuters** | Claude Enterprise + Cowork | Claude Enterprise を中核 AI 機能として追加し、Cowork のパイロットを開始 | `[S19]` | 🔎 |

> **凡例に関する注記：** 上表の「業種」「地域」は公開情報から本ページ作成者が付与した分類であり、Anthropic の公式分類ではありません。

---

<a id="partnerships"></a>
## 大規模パートナーシップ型展開

個社の PoC ではなく、**数万〜数十万人規模**で Claude／Claude Code を展開する発表です。自社の全社展開を構想する際の規模感の参照に使えます。

| ID | 企業 | 公表規模 | Claude Code に関する内容 | 出典 | 状態 |
|---|---|---|---|---|---|
| `P1` | **Deloitte** | **470,000 名**（グローバルネットワーク全体） | 発表時点で Anthropic 最大のエンタープライズ展開と説明。**15,000 名**の認定プログラムを共同開発 | `[S20]` | 🔎 |
| `P2` | **Cognizant** | **最大 350,000 名** | コーディング、テスト、ドキュメント作成、DevOps ワークフローの高速化に **Claude Code** を利用 | `[S21]` | 🔎 |
| `P3` | **Accenture** | **数万名の開発者**が Claude Code を利用 | 発表時点で Anthropic 史上最大のデプロイと説明。約 **30,000 名**が Claude のトレーニングを受講 | `[S22]` | 🔎 |
| `P4` | **PwC** | 数十万名規模のグローバル従業員へ拡大予定 | **Claude Code と Cowork** を米国チームから展開開始。**30,000 名**の認定プログラム | `[S23]` `[S9]` | 🔎 |
| `P5` | **NEC** | **約 30,000 名**（NEC グループ全世界） | 日本最大級の AI ネイティブなエンジニアリング組織構築。**NEC BluStellar Scenario** に Claude Code を組み込み | `[S24]` | 🔎 |
| `P6` | **Salesforce** | グローバルエンジニアリング組織全体 | **Claude Code を全社エンジニアリング組織に展開**。Agentforce では Claude が優先モデルに | `[S25]` | 🔎 |
| `P7` | **Snowflake** | 2 億ドル規模の複数年契約 | Snowflake 自社のエンジニアリング組織で **Claude Code** を活用。Claude モデルを 12,600 社超の顧客へ提供 | `[S26]` | 🔎 |
| `P8` | **Infosys** | 規制産業向け（通信ほか） | Claude モデルと **Claude Code** を Infosys Topaz に統合。Claude Agent SDK でエージェント構築 | `[S27]` | 🔎 |
| `P9` | **Claude Partner Network** | 初期 **1 億ドル**を拠出 | 企業の Claude 導入を支援するパートナー向けプログラム（トレーニング、技術支援、共同市場開拓） | `[S28]` | 🔎 |

> ⚠️ **「最大規模」表現の矛盾について：** `P1`（Deloitte）と `P3`（Accenture）は、いずれも発表時点で「Anthropic 最大のデプロイ」と説明されています。発表時期が異なるため相互に矛盾するものではありませんが、**この種の最上級表現は発表時点の相対値**であることに注意してください。規模を比較する際は、人数の定義（全従業員か／開発者のみか／ライセンス数か／トレーニング受講者数か）が事例ごとに異なる点も確認が必要です。

---

<a id="anthropic-internal"></a>
## Anthropic 自社での利用（ドッグフーディング）

導入企業の事例ではありませんが、「Claude Code を極限まで使うとどうなるか」の参照点として有用です。**ただし Anthropic 自社の数値は、ツール提供元による自社利用の公表値であり、一般企業への外挿には最も慎重さが必要です。**

| 項目 | 公表値 | 出典 | 状態 |
|---|---|---|---|
| コードベースにマージされるコードのうち Claude が作成した割合 | **約 80%**（経営陣はスクリプト・実験コードを含めると 90% 以上と発言） | `[S29]` `[S30]` | 🔎 |
| エンジニア 1 人あたり四半期出荷コード量 | 2021〜2025 年比で **約 8 倍** | `[S29]` | 🔎 |
| 大規模移行の実コスト例（Bun 移行） | 未キャッシュ入力 **59 億トークン**、出力 **6.9 億トークン** ＝ API 料金換算で **約 16.5 万ドル** | `[S31]` | 🔎 |
| 推論チームでの効果 | ML 背景のないメンバーがモデル固有関数の理解に要する調査時間を **80% 削減** | `[S32]` | 🔎 |
| API エラー対応の事例 | Claude が **800 件超**の個別修正を投入し、エラー率を **1,000 分の 1** に低減（2026 年 4 月） | `[S33]` | ⚠️ |

Anthropic は自社の AI ネイティブな開発ライフサイクルのセキュリティ確保についても記事を公開しており `[S34]`、導入検討時にセキュリティ設計の参考になります（本リポジトリの [Claude セキュリティ](Claude-Security.ja.md) と併せて参照してください）。

---

<a id="patterns"></a>
## 導入パターン別分類

事例を「何に効いたか」で分類したものです。自社の想定用途に最も近いパターンの事例から読むことを推奨します。

### パターン A — レガシー移行・モダナイゼーション（最も数値が明確に出るパターン）
`C1` Stripe（Scala→Java、10 人週→4 日） ／ `C3` LG CNS（20 年もの基幹、99.1% API 変換、コスト半減） ／ `C8` Satispay（Java 8→21 ＋ Spring、4 週→4 日未満） ／ `C9` HubSpot（フロントエンド移行）

**特徴：** 「従来の手作業見積」との対比で効果が定量化しやすく、稟議の材料にしやすい。一方で**見積自体が事後の推定**であることが多く、比較の厳密さには限界があります。Anthropic 自身も大規模コード移行の方法論を公開しています `[S31]`。

### パターン B — 開発速度・リードタイム短縮
`C2` 楽天（24 日→5 日、79% 短縮） ／ `C5` クラスメソッド（最大 10 倍、PR 数 1.5 倍） ／ `C11` Altana（2〜10 倍） ／ `C6` Cox（市場投入 55% 高速化）

**特徴：** 組織全体のリードタイム指標。**測定期間・対象チーム・ベースラインの取り方**で数値が大きく変わるため、自社試算では同じ定義で測れるかを先に確認してください。

### パターン C — 大規模ロールアウトと人材育成
`P1` Deloitte（47 万名／1.5 万名認定） ／ `P3` Accenture（数万開発者／3 万名研修） ／ `P4` PwC（`C7` の 1 セッション 400 名研修を含む） ／ `P5` NEC（3 万名） ／ `C6` Cox（2,500 ユーザー）

**特徴：** ツール配布そのものより、**トレーニング・認定プログラムが併走**している点が共通しています。全社展開を構想する場合、ライセンス調達と同時に育成設計が要るという示唆になります。

### パターン D — 非エンジニア部門への波及
`C4` Ramp（営業・リスク・経理・財務・採用が自らデータを抽出） ／ `C16` Brainlabs（従業員が数百のスキルを自作） ／ `C15` Cyera（40 ツール接続、1,500 名）

**特徴：** Claude Code の「開発ツール」の枠を越えた使われ方。ただし `C15` `C16` は **Cowork** の事例であり、Claude Code そのものではない点に注意してください。

### パターン E — ワークフロー自動化・組み込み
`C12` Zapier（Slack 絵文字 → MR 自動生成） ／ `P5` NEC（自社製品 BluStellar Scenario への組み込み） ／ `P8` Infosys（Topaz への統合）

**特徴：** Claude Code を CI/CD や社内プラットフォームに**組み込む**段階。本リポジトリのセキュリティ Wiki の [`T6` 権限モデル](Claude-Security.ja.md#t6)・[`T7` 分離](Claude-Security.ja.md#t7) と併せた設計が必要になります。

---

<a id="metrics"></a>
## 公表指標一覧（数値のみ抜粋）

効果試算の初期仮説を置く際の参照用です。**すべて公表主体の自己申告値**であり、測定方法は事例ごとに異なります。

| 指標カテゴリ | 公表値 | 事例 |
|---|---|---|
| リードタイム短縮 | 24 営業日 → 5 営業日（**79% 減**） | `C2` 楽天 |
| リードタイム短縮 | 市場投入 **55% 高速化** | `C6` Cox |
| 移行工数削減 | 10 エンジニア週 → **4 日** | `C1` Stripe |
| 移行工数削減 | 4 週間 → **4 日未満** | `C8` Satispay |
| 移行コスト削減 | 従来型再構築の **約 50%** | `C3` LG CNS |
| 移行完了率 | 2,913 API 中 **2,888（99.1%）** | `C3` LG CNS |
| 生産性倍率 | **最大 10 倍** | `C5` クラスメソッド |
| 生産性倍率 | **2〜10 倍** | `C11` Altana |
| アウトプット量 | マージ PR 月 108 → **165 件** | `C5` クラスメソッド |
| アウトプット量 | 月 **100 万行超**の AI 提案コード | `C4` Ramp |
| 定着率 | エンジニアの **約 50%** が週次利用 | `C4` Ramp |
| 満足度 | パイロット回答者の **98%** が満足以上 | `C13` GitLab |
| ROI | AI 投資初年度で **7 倍** | `C6` Cox |
| 作業時間短縮 | 24 時間 → **1 時間** | `C5` クラスメソッド |
| 展開規模 | **1,370 名**のエンジニア | `C1` Stripe |
| 展開規模 | **470,000 名** | `P1` Deloitte |

---

<a id="industry-index"></a>
## 業種・地域別索引

### 業種別
- **金融・決済・フィンテック：** `C1` Stripe ／ `C4` Ramp ／ `C8` Satispay ／ `C10` Behavox
- **通信・メディア：** `C6` Cox Communications ／ `P8` Infosys（通信向け）
- **EC・インターネットサービス：** `C2` 楽天 ／ `C12` Zapier
- **SI・ITサービス：** `C3` LG CNS ／ `C5` クラスメソッド ／ `P5` NEC ／ `P2` Cognizant ／ `P3` Accenture ／ `P8` Infosys
- **プロフェッショナルサービス（監査・コンサル）：** `C7` `P4` PwC ／ `P1` Deloitte ／ `C18` Thomson Reuters
- **SaaS・開発者向け製品：** `C9` HubSpot ／ `C13` GitLab ／ `C14` Canva ／ `C17` Jamf ／ `P6` Salesforce ／ `P7` Snowflake
- **セキュリティ・コンプライアンス：** `C10` Behavox ／ `C15` Cyera
- **サプライチェーン：** `C11` Altana

### 地域別
- **日本：** `C2` 楽天 ／ `C5` クラスメソッド ／ `P5` NEC ／（隣接：野村総合研究所（NRI）は Claude Platform (API) 事例として公開 `[S35]`）
- **韓国：** `C3` LG CNS
- **米国：** `C1` `C4` `C6` `C9` `C10` `C11` `C12` `C14`〜`C18`
- **欧州：** `C8` Satispay（イタリア）
- **グローバル／複数地域：** `C7` `P1`〜`P9`

> **日本企業の事例について：** 上記のほか、日本語圏の Web 上には多数の「Claude Code 導入事例」記事が存在しますが、その多くは**導入支援ベンダー自身のマーケティング記事**で、導入企業名・測定方法・公表主体が明示されていないものが目立ちます。本ページでは**公表主体を特定できないものは意図的に掲載していません**。日本企業の一次事例を探す場合は、`claude.com/customers` の絞り込みと、各社自身のエンジニアリングブログ・IR 資料を当たることを推奨します。

---

<a id="caveats"></a>
## 事例の読み方と注意点

導入事例を自社の意思決定に使う際、本ページの数値をそのまま持ち込むと判断を誤ります。少なくとも以下を踏まえてください。

1. **すべてベンダー／導入企業の公表値である。** 第三者による検証を経た数値ではありません。成功事例のみが公表されるという**生存者バイアス**が構造的に存在します。効果が出なかった導入は事例化されません。
2. **測定の定義が事例ごとに異なる。** 「生産性 10 倍」「79% 短縮」が、何を分母・分子に、どの期間・どの対象で測ったものかは公表内容から判別できないことが大半です。**同じ指標名でも比較可能とは限りません。**
3. **「従来の見積」との比較には推定が含まれる。** `C1` の「10 エンジニア週」`C8` の「4 週間」は、実際にその工数で実施した結果ではなく**事前・事後の見積**です。見積自体の精度が効果の見かけを左右します。
4. **移行系タスクは最も効果が出やすい領域である。** 正解が機械的に定義でき、テストで検証できる作業（言語・フレームワーク移行）は AI エージェントの得意領域です。**新規設計や要件が曖昧な開発に同じ倍率は期待できません。**
5. **展開人数 ≠ 実利用者数。** `P1`〜`P5` の人数は多くが「提供対象者数」であり、日常的な利用者数とは異なります。`C4` Ramp の「約 50% が週次利用」のような**定着率の指標**の方が、実態の把握には有用です。
6. **製品の区別に注意。** 公式サイトは事例を Claude Code／Claude Enterprise／Claude Cowork／Claude Platform (API) に分類しています。**「Claude 導入事例」と「Claude Code 導入事例」は同一ではありません。** 本ページでは表を分離していますが、引用時は必ず原典の分類を確認してください。
7. **セキュリティ・ガバナンス要件は事例からは読み取れない。** 導入可否の判断には、本リポジトリの [Claude セキュリティ](Claude-Security.ja.md)（特に [`T3` ZDR](Claude-Security.ja.md#t3)・[`T8` 管理](Claude-Security.ja.md#t8)・[`T10` 監査](Claude-Security.ja.md#t10)）を併読してください。事例の華やかさと、自社のコンプライアンス要件を満たせるかは別問題です。

### 自社で効果を測るなら

事例の数値を借りるより、**自社で同じ定義の指標を取る**方が確実です。Claude Code には Analytics ダッシュボードと OpenTelemetry によるメトリクス出力があり、PR 数・コミット量などを自社で計測できます `[S1]`。`C8` Satispay のように**実チケットで期間を区切った構造化評価**を先に行うアプローチは、他社数値の借用より再現性があります。

---

<a id="sources"></a>
## 出典レジスタ

ステータス： **✅ 直接取得済** ＝ 本ページ作成時に内容を直接取得・確認。**🔎 検索経由** ＝ URL の実在は確認したが、内容は検索エンジン経由の要約で、原文は未読（claude.com／anthropic.com はエグレス制限により直接取得不可）。**⚠️ 要裏取り** ＝ 二次ソース由来、または公表主体が不明確。

| ID | 出典 | URL | 状態 |
|---|---|---|---|
| `S1` | Claude Code for Enterprise（製品ページ） | <https://claude.com/product/claude-code/enterprise> | 🔎 |
| `S2` | Stripe — Claude Code 事例 | <https://claude.com/customers/stripe> | 🔎 |
| `S3` | 楽天（Rakuten） — Claude Code 事例 | <https://claude.com/customers/rakuten> | 🔎 |
| `S4` | LG CNS — Claude Code 事例 | <https://claude.com/customers/lg-cns> | 🔎 |
| `S5` | Ramp — Claude Code 事例 | <https://claude.com/customers/ramp> | 🔎 |
| `S6` | クラスメソッド — Claude Code 事例 | <https://claude.com/customers/classmethod> | 🔎 |
| `S7` | Cox Communications — Claude Code 事例 | <https://claude.com/customers/cox-communications-qa> | 🔎 |
| `S8` | Cox Communications × Accenture — Claude 事例 | <https://claude.com/customers/cox-and-accenture> | 🔎 |
| `S9` | PwC — Claude Code 事例 | <https://claude.com/customers/pwc-qa> | 🔎 |
| `S10` | Satispay — Claude 事例 | <https://claude.com/customers/satispay> | 🔎 |
| `S11` | HubSpot — Claude Platform (API) 事例 | <https://claude.com/customers/hubspot> | 🔎 |
| `S12` | Claude Code for Enterprise 製品ページ内の顧客言及（Behavox／Altana） | <https://claude.com/product/claude-code/enterprise> | 🔎 |
| `S13` | Zapier — Claude Enterprise 事例 | <https://claude.com/customers/zapier> | 🔎 |
| `S14` | GitLab — Claude Enterprise 事例 | <https://claude.com/customers/gitlab-enterprise> | 🔎 |
| `S15` | Canva — Claude Enterprise 事例 | <https://claude.com/customers/canva> | 🔎 |
| `S16` | Cyera — Claude Cowork 事例 | <https://claude.com/customers/cyera-qa> | 🔎 |
| `S17` | Brainlabs — Claude Cowork 事例 | <https://claude.com/customers/brainlabs> | 🔎 |
| `S18` | Jamf — Claude Enterprise 事例 | <https://claude.com/customers/jamf> | 🔎 |
| `S19` | Thomson Reuters — Claude Cowork 事例 | <https://claude.com/customers/thomson-reuters-qa> | 🔎 |
| `S20` | Anthropic News — Deloitte パートナーシップ | <https://www.anthropic.com/news/deloitte-anthropic-partnership> | 🔎 |
| `S21` | Anthropic News — Cognizant パートナーシップ | <https://www.anthropic.com/news/cognizant-partnership> | 🔎 |
| `S22` | Anthropic News — Accenture パートナーシップ | <https://www.anthropic.com/news/anthropic-accenture-partnership> | 🔎 |
| `S23` | Anthropic News — PwC 拡大パートナーシップ | <https://www.anthropic.com/news/pwc-expanded-partnership> | 🔎 |
| `S24` | Anthropic News — NEC パートナーシップ | <https://www.anthropic.com/news/anthropic-nec> | 🔎 |
| `S25` | Anthropic News — Salesforce 拡大パートナーシップ | <https://www.anthropic.com/news/salesforce-anthropic-expanded-partnership> | 🔎 |
| `S26` | Anthropic News — Snowflake パートナーシップ（2 億ドル） | <https://www.anthropic.com/news/snowflake-anthropic-expanded-partnership> | 🔎 |
| `S27` | Anthropic News — Infosys 協業 | <https://www.anthropic.com/news/anthropic-infosys> | 🔎 |
| `S28` | Anthropic News — Claude Partner Network（1 億ドル） | <https://www.anthropic.com/news/claude-partner-network> | 🔎 |
| `S29` | Anthropic — When AI builds itself | <https://www.anthropic.com/institute/recursive-self-improvement> | 🔎 |
| `S30` | VentureBeat — Anthropic says 80% of its new production code is now authored by Claude | <https://venturebeat.com/technology/anthropic-says-80-of-its-new-production-code-is-now-authored-by-claude-how-your-enterprise-can-keep-up> | ⚠️ |
| `S31` | Claude Blog — How Anthropic runs large-scale code migrations with Claude Code | <https://claude.com/blog/ai-code-migration> | 🔎 |
| `S32` | Claude Blog — How Anthropic teams use Claude Code | <https://claude.com/blog/how-anthropic-teams-use-claude-code> | 🔎 |
| `S33` | 報道各社（Reuters ほか）による Anthropic 業績・事例報道 | — | ⚠️ |
| `S34` | Claude Blog — How Anthropic secures its AI-native software development lifecycle | <https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle> | 🔎 |
| `S35` | 野村総合研究所（NRI） — Claude Platform (API) 事例 | <https://claude.com/customers/nri> | 🔎 |
| `S36` | Claude Customer Stories（一覧トップ） | <https://claude.com/customers> | 🔎 |
| `S37` | Claude Blog — How to scale agentic coding across your engineering organization | <https://claude.com/blog/scaling-agentic-coding> | 🔎 |

### 意図的に掲載しなかったもの

- **導入支援ベンダーのマーケティング記事**（日本語圏に多数）：導入企業名・測定方法・公表主体のいずれかが不明確なものは除外しました。
- **統計まとめ系アグリゲーションサイト**：「Anthropic が Netflix／Microsoft／Uber 等を Claude Code 採用企業として公表している」旨の記述を複数の集約サイトで確認しましたが、**Anthropic 公式での裏付けを取れなかったため掲載していません**。掲載を検討する場合は一次発表の特定が必要です。

---

<a id="maintain"></a>
## 本ページのメンテナンス

1. **検証ステータスを必ず更新する。** ネットワーク制限のない環境で各公式 URL を直接確認できたら、当該行を 🔎 から ✅ に変更し、数値の差分を修正してください。**これが本ページの最優先の改善項目です。**
2. **公表主体が特定できない事例は載せない。** 企業名・数値・出典 URL の 3 点が揃わないものは除外します。
3. **製品の区別を維持する。** Claude Code／Claude Enterprise／Claude Cowork／Claude Platform (API) の表は分けたまま運用してください。
4. **四半期ごとに `claude.com/customers` と `anthropic.com/news` を再確認する。** 事例は継続的に追加されます。冒頭の*最終確認日*を更新してください。
5. **数値は転記よりリンクを優先する。** 事例ページは改訂されることがあります。
6. **効果測定の議論では[注意点](#caveats)へのリンクを必ず併記する。** 数値の一人歩きを防ぐためです。

*本ページは当リポジトリで管理する社内の参照用資料です。Anthropic の公式刊行物ではなく、掲載した数値の正確性についていかなる保証も伴いません。提案・稟議・監査等の目的では、必ず一次情報源を直接確認のうえ引用してください。*
