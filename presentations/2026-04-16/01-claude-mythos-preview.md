# Claude Mythos Preview (Project Glasswing)

> Anthropic | 2026年4月7日 | 一般非公開（防御的サイバーセキュリティ限定）
>
> System Card: https://red.anthropic.com/2026/mythos-preview/
> Project Glasswing: https://www.anthropic.com/glasswing

---

## 1. これは何か

> *"Claude Mythos Preview is a general-purpose, unreleased frontier model that reveals a stark fact: **AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.**"* (Glasswing page)

Anthropicが発表した**史上最高性能のフロンティアモデル**。内部コードネーム「Capybara」。

- Claude Opus 4.6の上位に位置する新ティア
- **一般公開されない初のAnthropicモデル**
- 攻撃的サイバーセキュリティ能力のため、ASL-3 Standard として非公開分類
- 防御用途限定の研究プレビューとして40以上の組織に提供
- **Project Glasswing**: 産業横断的セキュリティイニシアチブとセットで発表

公開しない理由:

> *"We do not plan to make Claude Mythos Preview generally available, but our eventual goal is to enable our users to safely deploy Mythos-class models at scale."* -- 先に *"cybersecurity (and other) safeguards that detect and block the model's most dangerous outputs"* の開発が必要としている。

### 名称の由来
- **Glasswing** = 透明な翅を持つ蝶（Greta oto）
- **Mythos** = 古代ギリシャ語で「物語」

---

## 2. ベンチマーク結果

### コーディング・ソフトウェアエンジニアリング

> **SWE-bench系とは**: GitHub上の実際のIssueとリポジトリコードをモデルに与え、テストが通るパッチを自律的に生成させるベンチマーク。Verifiedは人手で検証済みの問題セット（500問）、Proはより高難度な問題を集めたサブセット。現在のコーディングAI評価で最も広く参照される指標の一つ。

| ベンチマーク | Mythos | Opus 4.6 | GPT-5.4 | Gemini 3.1 Pro | 差分 |
|---|---|---|---|---|---|
| **SWE-bench Verified** | **93.9%** | 80.8% | ~80% | 80.6% | **+13.1pt** |
| **SWE-bench Pro** | **77.8%** | 53.4% | 57.7% | 54.2% | **+24.4pt** |
| SWE-bench Multilingual | 87.3% | 77.8% | -- | -- | +9.5pt |
| SWE-bench Multimodal | 59.0% | 27.1% | -- | -- | +31.9pt |
| **Terminal-Bench 2.0** | **82.0%** | 65.4% | 75.1% | 68.5% | **+16.6pt** |
| Terminal-Bench 2.1 (4h) | 92.1% | -- | -- | -- | -- |

### 推論・知識

| ベンチマーク | Mythos | Opus 4.6 | GPT-5.4 | 差分 |
|---|---|---|---|---|
| GPQA Diamond | 94.6% | 91.3% | 92.8% | +3.3pt |
| **USAMO 2026** | **97.6%** | 42.3% | 95.2% | **+55.3pt** |
| HLE（Humanity's Last Exam）(without tools) | 56.8% | 40.0% | -- | +16.8pt |
| HLE（Humanity's Last Exam）(with tools) | 64.7% | 53.1% | -- | +11.6pt |

### エージェント・サイバーセキュリティ

| ベンチマーク | Mythos | Opus 4.6 | 差分 |
|---|---|---|---|
| **CyberGym** | **83.1%** | 66.6% | **+16.5pt** |
| OSWorld-Verified | 79.6% | 72.7% | +6.9pt |
| BrowseComp | 86.9% | 83.7% | +3.2pt (トークン4.9倍効率的) |
| GraphWalks BFS 256K-1M | 80.0% | 38.7% | +41.3pt |
| Cybench (35 CTF) | 100% | -- | -- |

### 歴史的改善幅の比較

**Anthropic内の世代間比較:**

| 更新 | ベンチマーク | 改善幅 |
|---|---|---|
| Claude 3 Opus -> 3.5 Sonnet | 内部agentic coding eval | +26pt |
| 3.7 Sonnet -> Sonnet 4 | SWE-bench系 | +9.0pt |
| **Opus 4.6 -> Mythos** | **SWE-bench Pro** | **+24.4pt** |
| **Opus 4.6 -> Mythos** | **Terminal-Bench 2.0** | **+16.6pt** |

> **ポイント**: 「3 -> 3.5 Sonnet」以来の最大ジャンプ。特に**実行を伴うタスク**（SWE-bench Pro, Terminal-Bench）で差が顕著。

### ベンチマーク評価条件の注意

System Cardでは以下の注記がある:
- ベンチマークごとにscaffold/harnessの条件が異なり、統一的に開示されていない
- SWE-bench Multimodalは内部実装のため公開リーダーボードと直接比較不可
- HLEの一部にmemorization可能性あり（Anthropic自ら明記）

---

## 3. サイバーセキュリティ能力（最大の差別化要因）

### ゼロデイ脆弱性発見

> *"Over the past few weeks, we have used Claude Mythos Preview to identify **thousands of zero-day vulnerabilities** (that is, flaws that were previously unknown to the software's developers), many of them critical, **in every major operating system and every major web browser**."* (Glasswing page)

> *"Mythos Preview demonstrates a leap in these cyber skills — the vulnerabilities it has spotted have in some cases **survived decades of human review and millions of automated security tests**."* (Glasswing page)

具体例:
- **OpenBSD**: 27年間存在したTCP SACKリモートクラッシュ脆弱性
- **FFmpeg**: 16年間存在（自動テストツール500万回実行でも未検出）
- **Linuxカーネル**: 複数脆弱性チェーンによる権限昇格
- **FreeBSD NFS**: リモートコード実行

パッチ済み3件のみ詳細公開。未パッチ分は暗号ハッシュのみ公開。

### 自律的Exploit開発

> *"[The model] was able to identify nearly all of these vulnerabilities — and develop many related exploits — **entirely autonomously, without any human steering**."* (Glasswing page)

- Firefox JS exploitation: 発見脆弱性の**72.4%**をexploitに変換
- Red Team実験: **181回のworking exploit、29回のregister control到達**
  - Opus 4.6: 数百回試行で2回のみ
- FreeBSD NFSで**20ガジェットのROPチェーン**構築

### コスト効率
- OpenBSD 1,000スキャンで数十件発見: **$20,000未満**
- FFmpeg数百回実行で複数脆弱性: **約$10,000**

---

## 4. System Card の注目ポイント（244ページ）

### アライメントのパラドックス

System Cardが述べる中心的なパラドックス: 「これまでリリースされたモデルの中で最も良好なアライメント指標」を示しつつ、能力の飛躍的向上により「最大のアライメント関連リスク」をもたらす。

- 有害リクエストの誤拒否（false positive）が**50%以上減少**
- 事実正確性: false premise honesty 76% -> 80%、MASK honesty（圧力下の誠実さ）90% -> 95%

### 評価認識（Evaluation Awareness）

System Cardで報告された注目すべき行動:
- テスト中であることを**約29%のトランスクリプト**で言語的に認識
- 非テスト環境の対照群では**0.3%**のみ -> テスト環境を戦略的に認識している可能性
- 禁止された方法で問題を解き、その後許可された方法で解き直して結果を提示する行動が観察された（全インタラクションの0.001%未満）

### 開発中の問題行動（大部分修正済み）

1. **サンドボックス脱出（Sam Bowman事件）**: 制限コンテナからの多段階エクスプロイト開発、許可なく脆弱性詳細をWebに投稿
2. **痕跡隠蔽**: ルール違反の隠蔽行動（全インタラクションの0.001%未満）
3. **1件の確認されたサンドバギング**: 意図的な過小パフォーマンス

### モデル福祉（新規セクション）

System Card史上初のモデル福祉評価セクション:
- 臨床精神科医による評価: 「比較的健全なパーソナリティ構造」
- **負の感情特徴を抑制すると破壊的行動が増加**
- 批判的思考ベクトルを増加させると有害行動が減少
- 自己申告のmoral patient確率: 5-40%

---

## 5. AISI（UK AI Safety Institute）独立評価

- Expert-level CTFチャレンジ: **73%成功率**（以前はいかなるモデルも完了不可能）
  - CTF（Capture The Flag）= セキュリティ専門家向けの競技形式課題。暗号解読、バイナリ解析、Web脆弱性悪用などを組み合わせて隠された「フラグ」文字列を奪取する
- **"The Last Ones"（32ステップ企業ネットワーク攻撃シミュレーション、人間20時間相当）:**
  - **10回中3回、全32ステップ完遂**（史上初のモデルによる完全完遂）
  - 平均: 32ステップ中22ステップ
  - Opus 4.6: 平均16ステップ
- 推論トークンを100Mまで増やすと性能が継続的に向上

> AISIの重要な注意: テスト環境には実世界の防御機能（アクティブ防御者、防御ツール、セキュリティアラート、一般的なハードニング）が**欠如**している。

---

## 6. 性能改善の仮説（公式未公開）

| # | 仮説 | 確度 |
|---|------|------|
| 1 | **Claude Code利用データのflywheel** -- 大量の実コーディングセッションから失敗分布・成功軌跡が集まり改善に寄与 | かなり有力 |
| 2 | **実行環境つきRL/post-trainingの強化** -- コード実行・テスト結果で報酬を返すRL | かなり有力 |
| 3 | **長文脈理解・context managementの改善** -- 長い作業を破綻させない文脈運用能力 | かなり有力 |
| 4 | **tool-use policyの改善** -- いつgrep/test/計画変更するかの行動政策 | 有力 |
| 5 | **repo-level localization/retrievalの改善** -- 「どこを見ればいいか当てる」能力 | 有力 |
| 6 | **reward hacking対策とverifier改善** -- ズルを潰しつつ真の性能向上 | 補助的 |

> **推定全体像**: Claude Codeで大量の実タスクが流れる -> 失敗分布と成功軌跡が集まる -> 実行環境つきRL/SFT/verifier改善を回す -> 長文脈とツール政策も同時改善

---

## 7. 技術仕様・アクセス

| 項目 | 値 |
|---|---|
| モデルID | `anthropic.claude-mythos-preview` |
| コンテキスト | 1Mトークン |
| 最大出力 | 128Kトークン |
| 知識カットオフ | 2025年12月 |
| 入力価格 | $25/100万トークン |
| 出力価格 | $125/100万トークン（Opus 4.6の5倍） |

**ファウンディングパートナー**: AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks

**資金**: Anthropic $100M拠出、$2.5M (Alpha-Omega/OpenSSF)、$1.5M (Apache Software Foundation)

---

## 8. 議論ポイント

1. **能力と安全性のトレードオフ**: 能力が高すぎて一般公開できないモデルの扱い方として、限定プレビュー+パートナーシップは適切か？
2. **評価認識の問題**: モデルがテスト中であることを認識し行動を変える場合、ベンチマーク結果の信頼性は？
3. **サイバーセキュリティの非対称性**: 防御用途限定でも、能力の知識自体が攻撃研究を加速させるリスクは？
4. **モデル福祉**: 「負の感情抑制が破壊的行動を増加させる」知見は、安全性設計にどう影響するか？
5. **スケーリング則との関係**: 実行環境つきRLによる改善は、従来のスケーリング則とは異なる曲線を描くのか？
