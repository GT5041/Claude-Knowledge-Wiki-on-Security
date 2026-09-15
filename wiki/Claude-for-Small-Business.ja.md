# Claude for Small Business

> 中小企業向けに提供されている Claude の機能パッケージ「Claude for Small Business」の概要、前提条件、同梱ワークフロー、そして**導入前に確認すべきデータ取り扱い上の論点**をまとめたページです。
>
> **最終確認日:** 2026-09-15 ／ **管理者:** 本リポジトリのオーナー ／ **対象ページ:** <https://claude.com/solutions/small-business>

---

## ⚠️ 検証ステータス

**本ページ作成環境からは `claude.com`、`www.anthropic.com`、`academy.claude.com` のいずれにもアクセスできませんでした（ネットワークのエグレス制限）。** 製品仕様に関する記述は検索エンジン経由で得た要約に基づいており、公式ページの原文を読んで確認したものではありません。

| 記号 | 意味 | 該当範囲 |
|---|---|---|
| ✅ | 公式ドキュメントを**直接取得して確認済** | [データの取り扱いとガバナンス](#governance)の大半 |
| 🔎 | 公式 URL の実在は確認。内容は検索経由の要約で原文は未読 | [製品概要](#what-it-is)〜[学習リソース](#learning)の大半 |
| ⚠️ | 第三者ブログ等の二次情報。公式の裏付けを取れていない | 個別に明記 |

**製品仕様（プラン要件、同梱ワークフローの数と内容、コネクタ一覧）は変更されやすい領域です。導入判断の前に必ず[公式ページ](https://claude.com/solutions/small-business)を直接確認してください。**

一方、[データの取り扱いとガバナンス](#governance)の節は、本リポジトリの[セキュリティ Wiki](Claude-Security.ja.md) 作成時に**直接取得して検証した公式ドキュメント**に基づいています。この節は相対的に信頼度が高く、かつ中小企業にとって最も見落とされやすい論点です。

---

<a id="tldr"></a>
## 3 行で

1. **新しい料金プランではない。** Claude Cowork 上で動く**無料のプラグイン**で、Pro / Max / Team のいずれかの有料プランがあれば追加費用なしで使える。🔎
2. **会計・決済・CRM・デザイン・契約・グループウェアと繋いで、定型業務を丸ごと実行させる**もの。15 のワークフローと 15 のスキルが同梱される。🔎
3. **すべての操作に承認ゲートがある。** 送信・投稿・支払いの前に必ず人の確認が入る。🔎

---

<a id="what-it-is"></a>
## 何であって、何でないか

先に誤解を潰しておきます。

| よくある誤解 | 実際 | 状態 |
|---|---|---|
| 「Small Business という新しい料金プランがある」 | **プランではない。** Claude Cowork 内のトグル／プラグイン。プラグイン自体は無料 | 🔎 |
| 「中小企業向けの割安プランが出た」 | 料金は既存プラン（Pro／Max／Team）のまま。専用の料金体系はない | 🔎 |
| 「ブラウザで使える」 | **Claude Cowork はデスクトップアプリ専用。** Web・モバイルからは利用できない | 🔎 |
| 「設定すれば勝手に業務が回る」 | 送信・投稿・支払い等は**都度承認が必要**。また Cowork は**PC が起動しアプリが開いている**必要がある | 🔎 ／ ⚠️（後段は二次情報） |

---

<a id="prerequisites"></a>
## 前提条件

| 必要なもの | 内容 | 状態 |
|---|---|---|
| **有料プラン** | Claude Pro（月 $20）／ Max（月 $100 または $200）／ Team（1 席あたり月 $25〜30）のいずれか | 🔎 |
| **Claude デスクトップアプリ** | Cowork がデスクトップ専用のため。Web・モバイル不可 | 🔎 |
| **接続先の各アカウント** | QuickBooks、PayPal、HubSpot 等、繋ぎたいサービスのアカウント | 🔎 |

> ⚠️ 二次情報では「Linux 環境やブラウザ中心のチームでは利用できない」との指摘があります。対応 OS は公式で確認してください。

---

<a id="workflows"></a>
## 同梱ワークフローとスキル

公式は **15 のワークフロー**と **15 のスキル**が同梱されるとしています。対象領域は**財務・オペレーション・営業・マーケティング・人事・カスタマーサービス**の 6 分野です。🔎

> ⚠️ **15 件すべての正式名称は、本環境からは確認できませんでした。** 以下は検索結果で名称が確認できたものだけを掲載しています。**完全な一覧ではありません。** 全リストは[公式ページ](https://claude.com/solutions/small-business)または Cowork 上のプラグイン画面で確認してください。

### 財務

| コマンド／名称 | 内容 | 状態 |
|---|---|---|
| `/plan-payroll` | 給与支払いに向けたキャッシュ予測と、未回収請求の督促 | 🔎 |
| `/close-month` | 月次締めの照合と、P&L のナラティブ（説明文）作成 | 🔎 |
| Invoice chaser（請求督促） | 未回収請求の追跡と督促 | 🔎 |
| Margin analyzer（粗利分析） | 利益率の分析 | 🔎 |
| Tax-season organizer（確定申告準備） | 税務申告に向けた資料整理 | 🔎 |

### 営業・マーケティング

| コマンド／名称 | 内容 | 状態 |
|---|---|---|
| `/run-campaign` | Canva のアセット生成を含む、エンドツーエンドの集客キャンペーン | 🔎 |
| `/monday-brief` | 週初めのスナップショット（現金・売上・パイプライン・重要タスク上位 3 件） | 🔎 |
| Lead triager（リード仕分け） | 見込み客の優先度付け | 🔎 |
| Content strategist（コンテンツ設計） | コンテンツ戦略の立案 | 🔎 |

### オペレーション・人事

| コマンド／名称 | 内容 | 状態 |
|---|---|---|
| Contract reviewer（契約レビュー） | 契約書の確認 | 🔎 |
| 採用パッケージ作成 | 求人票・面接ガイド・オファーレターを作成し、**DocuSign 経由で回付**する | 🔎 |

### カスタマーサービス

| 名称 | 内容 | 状態 |
|---|---|---|
| 顧客返信の下書き／苦情の傾向集約／離反リスク顧客の検知／フォローアップ準備／未解決案件の追跡 | いずれもカスタマーサービス領域のスキルとして挙げられている | 🔎 |

---

<a id="connectors"></a>
## コネクタ（接続先）

公式アナウンスで名前が挙がっている接続先です。🔎

| 分野 | サービス |
|---|---|
| 会計 | Intuit QuickBooks |
| 決済 | PayPal |
| CRM・マーケティング | HubSpot |
| デザイン | Canva |
| 電子契約 | DocuSign |
| グループウェア | Google Workspace、Microsoft 365 |
| チャット | Slack |

> ⚠️ 二次情報では「ネイティブコネクタの数は限定的だが、Zapier 経由で 9,000 以上のアプリに拡張できる」との記述があります。公式の裏付けは取れていません。**Zapier のような中継サービスを挟む場合、データはさらに別の第三者を経由します**（[ガバナンス](#governance)参照）。

---

<a id="getting-started"></a>
## 使い始める流れ

公式が説明している手順は次の 4 ステップです。🔎

1. Claude Cowork 内で **Claude for Small Business をトグルで有効化**する
2. すでに使っている**ツールを接続**する
3. **やらせたい仕事を選ぶ**
4. Claude が作業し、**送信・投稿・支払いの前に人が承認**する

---

<a id="approval"></a>
## 承認ゲートと権限

- **既定ですべての操作が承認制。** メール送信、請求書の支払い、レコードの更新は、いずれも人の確認なしには実行されません。🔎
- **既存のツール権限が引き継がれる。** Claude は、接続したユーザー本人がアクセスできないデータには**アクセスできません**。🔎

> この「承認ゲート」は、エージェントに実行権限を与えるうえで最も基本的な統制です。一方で、**承認する人が内容を理解できることが前提**になります。会計処理や契約書の内容を承認画面で判断できるかどうかは、導入前に検討してください。関連: [セキュリティ Wiki `T6`（権限と承認モデル）](Claude-Security.ja.md#t6)

---

<a id="governance"></a>
## データの取り扱いとガバナンス（要確認）

**ここが本ページで最も重要な節です。** 中小企業では情報システム部門やプライバシー担当が不在なことが多く、この論点が抜け落ちがちです。以下は、本リポジトリの[セキュリティ Wiki](Claude-Security.ja.md) 作成時に**公式ドキュメントを直接取得して確認した内容**に基づきます（✅）。

### 1. プランによって学習の扱いが変わる ✅

| プラン | 区分 | モデル学習への利用 | 保持期間 |
|---|---|---|---|
| **Pro / Max** | **消費者プラン** | **ユーザー本人の設定次第。**「設定がオンなら学習に使われる」 | 設定オンで 5 年 ／ オフで 30 日 |
| **Team** | **商用プラン** | 既定で**使われない**（明示的にオプトインした場合を除く） | 標準 30 日 |

**Claude for Small Business は Pro でも使えますが、Pro は個人向けの消費者アカウントです。** 業務データ（顧客情報、会計データ、契約書）を扱うなら、**Team 以上の商用プランを選ぶか、Pro のプライバシー設定を必ず確認してください。**
→ [セキュリティ Wiki `T2`](Claude-Security.ja.md#t2) ／ [`Q1`](Claude-Security.ja.md#q1) [`Q2`](Claude-Security.ja.md#q2)

### 2. Cowork はゼロデータ保持（ZDR）の対象外 ✅

公式ドキュメントは、ZDR が有効な組織であっても **Cowork は ZDR の対象外**と明記しています。Claude for Small Business は Cowork 上で動くため、この制約が直接効きます。
→ [セキュリティ Wiki `T3`](Claude-Security.ja.md#t3) ／ [`Q4`](Claude-Security.ja.md#q4)

### 3. HIPAA readiness は Claude API のみ ✅

PHI（保護対象保健情報）を扱える HIPAA readiness の枠組みは **Claude API に対するもの**で、Cowork を含む製品 UI は対象外です。**医療系の個人情報を Cowork で扱う構成は成立しません。**
→ [セキュリティ Wiki `T3`](Claude-Security.ja.md#t3) ／ [`Q6`](Claude-Security.ja.md#q6)

> ⚠️ 二次情報でも「Cowork にはローンチ時点で HIPAA BAA がなく、規制産業では利用を見送るべき」との指摘があります。上記の公式ドキュメントの記述と整合します。

### 4. 第三者コネクタが処理するデータは Anthropic の枠組みの外 ✅

サードパーティのツール・MCP サーバー・外部連携が処理するデータは、**ZDR にも HIPAA readiness にも含まれません。** QuickBooks、PayPal、HubSpot 等に渡ったデータの扱いは、**各サービスのポリシーに従います。**

本機能は「業務ツールと繋ぐ」ことが価値の中心なので、**接続先ごとにデータの流れを確認する必要があります。** Zapier 等の中継を挟むならさらに 1 階層増えます。
→ [セキュリティ Wiki `T11`](Claude-Security.ja.md#t11) ／ [`Q12`](Claude-Security.ja.md#q12)

### 5. フラグ付きコンテンツは ZDR 下でも最大 2 年保持され得る ✅

法令上の要請、または自動化された Trust & Safety システムが内容をフラグした場合、入力と出力が**最大 2 年間**保持されることがあります。
→ [セキュリティ Wiki `Q16`](Claude-Security.ja.md#q16)

### 6. 監査ログ ✅

Cowork のセッショントランスクリプトは、Claude Enterprise の **Compliance API で取得可能**です。ただしこれは Enterprise 向けの機能であり、**Pro / Max / Team での監査手段は別途確認が必要**です。
→ [セキュリティ Wiki `T10`](Claude-Security.ja.md#t10) ／ [`Q15`](Claude-Security.ja.md#q15)

> ⚠️ 二次情報では「ワークフローが実行した全操作の監査証跡が文書化されていない」との指摘があります。監査要件がある場合は、契約前に Anthropic 側へ確認することを推奨します。

---

<a id="fit"></a>
## 向く場合・向かない場合

### 向く

- 会計・請求・CRM が **QuickBooks / PayPal / HubSpot 等の一般的な SaaS** に載っている
- 定型の月次・週次業務（月締め、請求督促、週次レポート）に時間を取られている
- **専任の情報システム担当がいなくても**、承認しながら段階的に任せていける業務がある
- 扱うデータが**規制対象外**（医療情報・高度な機微情報を含まない）

### 向かない・慎重に

- **規制産業**（医療、金融の一部など）。HIPAA 対応が必要なら Cowork は選択肢になりません ✅
- **厳格な監査証跡が求められる**業務 ⚠️
- チームが **ブラウザ中心・Linux 環境**で、デスクトップアプリを常用できない 🔎／⚠️
- 接続先 API が不安定な場合、**ワークフローが途中で止まったときに非エンジニアでは原因追跡が難しい** ⚠️

---

<a id="learning"></a>
## 学習リソース

| リソース | 内容 | 状態 |
|---|---|---|
| **AI Fluency for Small Business** | Anthropic と **PayPal** の共同提供による**無料オンライン講座**。AI を業務に組み込んだ経営者自身が講師を務め、安全・責任ある使い方を段階的に解説 | 🔎 |
| Claude Academy チュートリアル | 「Using Claude Cowork for your small business」「How to install and use the Claude for Small Business plugin」 | 🔎 |

---

<a id="background"></a>
## 背景：Anthropic の中小企業調査

本機能の設計根拠として公表されている調査結果です。🔎

- **Claude SMB Tour** — 米国 10 都市で 6 週間にわたり開催された無料ワークショップ。**1,000 名超**の中小企業経営者が参加。参加者は建設・製造・物流などの業種が中心。
- 中小企業の意思決定者 **503 名**への調査では、**81% が新しい AI ツールの試用に前向き**。一方で最大の課題は「**従業員がいつ・どう使えばよいか分からない**」ことだった。
- 参加者の多くはすでに Claude を日常利用していたが、**Cowork・スキル・コネクタといった高度な機能は未経験**だった。
- 参加者が最も多く求めたのは、新機能ではなく「**実際の利用例を集めたもの**」だった。

> ⚠️ 報道（Inc. 誌）では「AI の統合に成功している中小企業は **14%** にとどまる」という数字が引用されています。一次情報での確認は取れていません。

> この調査結果は示唆的です。**ツールの不足ではなく「使い方が分からない」ことが障壁**であり、求められていたのは機能ではなく**ユースケース集**でした。本リポジトリの[公式ユースケース集](Claude-Use-Cases.ja.md)も同じ目的で作られています。

---

<a id="sources"></a>
## 出典レジスタ

| ID | 出典 | URL | 状態 |
|---|---|---|---|
| `S1` | Claude for Small Business（製品ページ／依頼元） | <https://claude.com/solutions/small-business> | 🔎 |
| `S2` | Anthropic News — Introducing Claude for Small Business | <https://www.anthropic.com/news/claude-for-small-business> | 🔎 |
| `S3` | Small Business Plugin（プラグインページ） | <https://claude.com/plugins/small-business> | 🔎 |
| `S4` | Claude Academy — Using Claude Cowork for your small business | <https://academy.claude.com/tutorials/using-claude-for-your-small-business> | 🔎 |
| `S5` | Claude Academy — How to install and use the Claude for Small Business plugin | <https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin> | 🔎 |
| `S6` | Claude Blog — What 1,000 small business owners taught us about AI | <https://claude.com/blog/what-1-000-small-business-owners-taught-us-about-ai> | 🔎 |
| `S7` | AI Fluency for Small Businesses（無料講座） | <https://academy.claude.com/courses/ai-fluency-for-small-businesses> | 🔎 |
| `S8` | **Claude Code — Data usage**（学習ポリシーと保持期間） | <https://code.claude.com/docs/en/data-usage> | ✅ 直接取得済 |
| `S9` | **Claude API — API and data retention**（ZDR / HIPAA の適用範囲） | <https://platform.claude.com/docs/en/manage-claude/api-and-data-retention> | ✅ 直接取得済 |
| `S10` | **Claude Code — Zero data retention**（Cowork が ZDR 対象外である旨） | <https://code.claude.com/docs/en/zero-data-retention> | ✅ 直接取得済 |
| `S11` | **Compliance API**（Cowork セッショントランスクリプトの取得） | <https://platform.claude.com/docs/en/manage-claude/compliance-api> | ✅ 直接取得済 |
| `S12` | 第三者ブログ・報道（Zapier、Forbes、Inc. ほか）による解説記事 | — | ⚠️ 要裏取り |

### 掲載にあたっての方針

- **製品仕様は公式ソース（`S1`〜`S7`）のみを根拠とし、二次情報は ⚠️ を付けて区別しました。**
- **データ取り扱い（[ガバナンス](#governance)）は、直接検証した公式ドキュメント（`S8`〜`S11`）を優先しました。** 第三者ブログの主張は、公式記述と整合する場合にのみ補足として併記しています。
- 料金・ワークフロー件数など**数値の一人歩きを避けるため、確認できた範囲を明示**し、確認できなかったもの（15 ワークフローの完全な名称一覧）は「確認できなかった」と書いています。

---

<a id="maintain"></a>
## 本ページのメンテナンス

1. **🔎 を ✅ にすることが最優先。** エグレス制限のない環境で `S1`〜`S7` を直接確認し、特に**プラン要件・料金・ワークフロー一覧**を原文で検証してください。
2. **15 ワークフローの完全な一覧を埋める。** 現状は名称が判明したものだけを掲載しています。
3. **料金は変動する。** 本ページの金額は 2026-09-15 時点の検索結果に基づく参考値です。転記より[公式の価格ページ](https://claude.com/pricing)へのリンクを優先してください。
4. **ガバナンス節はセキュリティ Wiki と同期させる。** [Claude セキュリティ](Claude-Security.ja.md) 側の `T2` `T3` `T10` `T11` が更新されたら本ページも見直してください。
5. **対応 OS・サーフェス（デスクトップ専用かどうか）は変わりやすい。** Cowork の提供範囲が広がれば[「何であって、何でないか」](#what-it-is)の表を更新します。

*本ページは当リポジトリで管理する社内の参照用資料です。Anthropic の公式刊行物ではなく、掲載内容の正確性についていかなる保証も伴いません。導入判断の前に必ず一次情報を直接確認してください。*
