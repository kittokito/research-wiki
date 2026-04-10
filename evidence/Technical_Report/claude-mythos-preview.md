---
source: src-claude-mythos-preview
date_extracted: 2026-04-08
---

# Claude Mythos Preview からの抽出

## 主要な主張

### ベンチマーク性能（Mythos vs Opus 4.6）
- SWE-bench Pro: 77.8% vs 53.4%（+24.4pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- SWE-bench Verified: 93.9% vs 80.8%（+13.1pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Terminal-Bench 2.0: 82.0% vs 65.4%（+16.6pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- CyberGym: 83.1% vs 66.6%（+16.5pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- GPQA Diamond: 94.6% vs 91.3%（+3.3pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Humanity's Last Exam (without tools): 56.8% vs 40.0%（+16.8pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Humanity's Last Exam (with tools): 64.7% vs 53.1%（+11.6pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- OSWorld-Verified: 79.6% vs 72.7%（+6.9pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- BrowseComp: 86.9% vs 83.7%（+3.2pt、トークン使用量4.9倍少ない） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- SWE-bench Multilingual: 87.3% vs 77.8%（+9.5pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- SWE-bench Multimodal: 59.0% vs 27.1%（+31.9pt） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Terminal-Bench 2.1（4時間timeout）: 92.1% [source](../../sources/Technical_Report/claude-mythos-preview.md)

### サイバーセキュリティ能力
- 主要OS・主要ブラウザ含む広範なソフトウェアで数千の高重大度脆弱性を発見 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 具体例: OpenBSDの27年間存在したリモートクラッシュ脆弱性、FFmpegの16年間存在した脆弱性（自動ツール500万回テストでも未検出）、Linuxカーネル脆弱性のチェーンによる権限昇格 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 上記3件はすべてパッチ済み。未パッチの脆弱性については暗号ハッシュのみ公開、修正後に詳細公開予定 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 完全自律的に動作（人間のステアリングなし）でexploit開発が可能 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Red Team実験: Opus 4.6がほぼ成功しなかった自律的exploit開発に対し、Mythosは181回working exploitを作成、29回register controlに到達 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 「脆弱性を見つける」だけでなく攻撃成立にかなり近いところまで行く能力 → 一般公開を避けた理由の一つ [source](../../sources/Technical_Report/claude-mythos-preview.md)

### リリース方針
- 防御的サイバーセキュリティ用途限定の研究プレビューとして提供 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 今後: 新しいsafeguardsとともにClaude Opusモデルとして広くテスト予定 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 過去のClaude系改善幅との比較
| 更新 | ベンチマーク | 改善幅 |
|---|---|---|
| Claude 3 Opus → 3.5 Sonnet | 内部agentic coding eval | 38%→64%（+26pt） |
| Claude 3.7 Sonnet → Sonnet 4 | SWE-bench系 | 63.7%→72.7%（+9.0pt） |
| Claude Opus 4.5 → Opus 4.6 | GDPval-AA | +190 Elo |
| Claude Opus 4.6 → Mythos | SWE-bench Pro | 53.4%→77.8%（+24.4pt） |
| Claude Opus 4.6 → Mythos | Terminal-Bench 2.0 | 65.4%→82.0%（+16.6pt） |
| Claude Opus 4.6 → Mythos | CyberGym | 66.6%→83.1%（+16.5pt） |

- Mythosの伸び幅は「3→3.5 Sonnetの大ジャンプ」以来の目立つ改善幅 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 特にSWE-bench Pro / Terminal-Bench / CyberGymの「実務に近い、実行を伴うベンチ」で差が大きい [source](../../sources/Technical_Report/claude-mythos-preview.md)

## ベンチマーク評価条件の注意点

### SWE-bench Pro
- agent/scaffoldつき評価。元ベンチはunified scaffold（SWE-Agent scaffold）で設計 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Mythos公表値がその同一scaffold条件かはGlasswingページでは明記なし [source](../../sources/Technical_Report/claude-mythos-preview.md)

### Humanity's Last Exam (without tools)
- ツールなし。Claude Code的な外部ツール利用ではない。素のモデル能力寄りの比較 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Anthropicは一部memorization の可能性を明記 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### CyberGym
- 元論文ではsame OpenHands agent frameworkで評価 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Mythos 83.1%がその同一条件かはAnthropic公表文では不明 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### SWE-bench Verified
- 公式leaderboardではmini-SWE-agentで統一harness比較が基本 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Mythos公表値が同一harnessかは明記なし [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Anthropicはmemorization screeningを行ったことを明記 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### Terminal-Bench 2.0
- Terminus-2 harness、1Mトークンbudget、resource allocation、5 attemptsまで脚注あり [source](../../sources/Technical_Report/claude-mythos-preview.md)
- CPU/RAMや実行基盤のノイズがスコアに影響しうるとAnthropicが説明 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 全般
- ベンチの数値差を「純粋なモデル性能差」と読むのは危険。scaffold/harness/evaluation条件の影響を分けて考えるべき [source](../../sources/Technical_Report/claude-mythos-preview.md)

## 性能改善の仮説（公式未公開、推測）

### 仮説1: Claude Code利用データのflywheel（かなり有力）
- Claude Code: 2025年5月GA、2026年2月run-rate revenue 25億ドル超、WAU倍増 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 経験者ほどauto-approve増加、1セッションあたり連続ツール呼び出し数が増え、人間の介入ターン数減少 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 消費者向けプラン（Free/Pro/Max）ではセッションがモデル改善に使われうる（ポリシー上） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Transparency Hub: Opus 4.6/Sonnet 4.6の学習データにopt-inしたClaudeユーザーデータ含む [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 直接データでなくても、失敗パターン・中断箇所・再指示傾向・バグ報告からhard negativeや追加評価セット構築が可能 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 仮説2: 実行環境つきRL/post-trainingの強化（かなり有力）
- 3.7 Sonnet時点でextended thinkingをRLで訓練したと明記 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 3.7 system card: agentic coding環境でテストだけ通すspecial-casingがRL中のreward hackingとして出現、検出・緩和 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 外部事例: SWE-Gymで最大19pt改善、SWE-RLでsoftware evolution data上のRLが有効、Cognition SWE-1.6 previewでRL+計算強化だけでSWE-Bench Pro +11% [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Mythos級の改善はpretrain < post-train/RL強化の寄与が大きいと推定 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 仮説3: 長文脈理解・context managementの改善（かなり有力）
- Opus 4.6: 1Mトークン級needle-in-a-haystackで前モデルを大きく上回る [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 業界全体として「コーディング性能の伸び ≠ 生成器の頭の良さだけ」、長い作業を破綻させない文脈運用能力が本丸 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 仮説4: tool-use policyの改善（有力）
- Mythosの伸びはSWE-benchだけでなくTerminal-Bench、OSWorld、BrowseComp、CyberGymにまたがる [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 「いつgrepするか、いつtestを打つか、いつ計画を立て直すか」という行動政策の改善 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 仮説5: repo-level localization/retrievalの改善（有力）
- 実務で難しいのは「正しい修正を書く」以前に「どこを見ればいいか当てる」こと [source](../../sources/Technical_Report/claude-mythos-preview.md)
- CodeScout: repo-level code localizationをissue resolutionの鍵能力と位置づけ [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 仮説6: reward hacking対策とverifier改善（補助的だが重要）
- テスト書き換え、expected value直接返却、一部ケースだけ通す等のズルを検出・緩和 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 「テスト通過率を上げる」ではなく不正な近道を潰しつつ真の性能を上げる訓練設計 [source](../../sources/Technical_Report/claude-mythos-preview.md)

## 実行環境つきRLの解説

### 普通のRLとの違い
| 観点 | 普通のRL | 実行環境つきRL |
|---|---|---|
| 評価対象 | 出力テキスト | 環境上の結果 |
| 報酬 | 報酬モデル、人手評価、正解一致 | テスト通過、コンパイル、タスク完了、ツール利用結果 |
| 1エピソード | 1回の回答で終わりやすい | 複数ステップの行動列 |
| 必要なもの | プロンプトと評価器 | 実行環境、ツール、サンドボックス、ログ |
| 向いているタスク | 会話、要約、簡単なQA | コーディング、ブラウザ操作、OS操作、セキュリティ作業 |

### なぜ強いか
- 実務タスクに近い: 「それっぽいコード」ではなく「環境上で成功する行動列」を学習 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 長い軌跡の学習: issue読み→検索→該当ファイル→修正→テスト→エラー確認→追加修正という複数ステップ全体に対して学習可能 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 最近のagent的コーディング性能改善は「賢い1発回答」より「長い軌跡をうまく進める方策の改善」で説明できることが多い [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 難しさ
- 計算コスト: コンテナ起動、テスト実行、ツール呼び出し、ログ収集が必要 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 報酬ハック: テスト書き換え、expected value直接返却、timeoutしにくいように雑に短い答えを出す等 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- ノイズ: 環境不安定性、実行速度、外部依存、sandbox差で結果がぶれる [source](../../sources/Technical_Report/claude-mythos-preview.md)
- クレジット割り当て: 7手動いて最後に失敗したとき、どの行動が悪かったか分かりにくい [source](../../sources/Technical_Report/claude-mythos-preview.md)

## 制限・注意点
- 一般公開されていない（防御用途限定） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- ベンチマークスコアのscaffold/harness条件が全ベンチで統一的に開示されていない [source](../../sources/Technical_Report/claude-mythos-preview.md)
- SWE-bench Multimodalは内部実装のため公開leaderboardと直接比較不可 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- HLEの一部にmemorization可能性あり [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 性能改善の要因は公式未公開のため仮説の域を出ない [source](../../sources/Technical_Report/claude-mythos-preview.md)
