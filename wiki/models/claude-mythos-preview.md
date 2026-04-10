---
title: "Claude Mythos Preview"
aliases: ["Mythos", "Project Glasswing"]
created: 2026-04-08
updated: 2026-04-08
tags: [claude, anthropic, mythos, agentic-coding, cybersecurity, benchmark]
sources: [src-claude-mythos-preview]
---

# Claude Mythos Preview

Anthropic が2026年4月に Project Glasswing とともに公表。一般公開はされておらず、防御的サイバーセキュリティ用途向けに限定提供。

→ 詳細: [evidence](../../evidence/Technical_Report/claude-mythos-preview.md)

## ソースからの事実

### ベンチマーク概要（Mythos vs Opus 4.6）
| ベンチマーク | Mythos | Opus 4.6 | 差分 |
|---|---|---|---|
| SWE-bench Pro | 77.8% | 53.4% | +24.4pt |
| SWE-bench Verified | 93.9% | 80.8% | +13.1pt |
| Terminal-Bench 2.0 | 82.0% | 65.4% | +16.6pt |
| CyberGym | 83.1% | 66.6% | +16.5pt |
| GPQA Diamond | 94.6% | 91.3% | +3.3pt |
| HLE (without tools) | 56.8% | 40.0% | +16.8pt |
| HLE (with tools) | 64.7% | 53.1% | +11.6pt |
| OSWorld-Verified | 79.6% | 72.7% | +6.9pt |
| BrowseComp | 86.9% | 83.7% | +3.2pt（トークン4.9倍効率的） |
| SWE-bench Multilingual | 87.3% | 77.8% | +9.5pt |
| SWE-bench Multimodal | 59.0% | 27.1% | +31.9pt |

- 改善幅は Claude 系の通常の版上げよりかなり大きく、「3→3.5 Sonnet」以来の目立つジャンプ [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 特に「実行を伴うタスク」（SWE-bench / Terminal-Bench / CyberGym）で差が大きい [source](../../sources/Technical_Report/claude-mythos-preview.md)

### サイバーセキュリティ
- 主要OS・ブラウザで数千の高重大度脆弱性を発見 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 具体例: OpenBSD 27年間の脆弱性、FFmpeg 16年間の脆弱性（自動ツール500万回テストでも未検出）、Linuxカーネル権限昇格チェーン [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 完全自律（人間のステアリングなし）でexploit開発が可能 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Red Team実験: 181回のworking exploit作成、29回のregister control到達（Opus 4.6はほぼ成功せず） [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 発見済み脆弱性はパッチ済み。未パッチ分は暗号ハッシュのみ公開 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### リリース方針
- 防御用途限定の研究プレビューとして提供 [source](../../sources/Technical_Report/claude-mythos-preview.md)
- 今後: 新しいsafeguardsとともにClaude Opusとして広くテスト予定 [source](../../sources/Technical_Report/claude-mythos-preview.md)

### 評価条件の注意
- ベンチごとにscaffold/harnessの統一度が異なる [source](../../sources/Technical_Report/claude-mythos-preview.md)
- HLE (without tools): ツールなし、素のモデル能力寄り [source](../../sources/Technical_Report/claude-mythos-preview.md)
- SWE-bench Pro / CyberGym: agent/scaffold付き。Mythos公表値が元ベンチと同一条件かは明記なし [source](../../sources/Technical_Report/claude-mythos-preview.md)
- Terminal-Bench 2.0: Terminus-2 harness、1Mトークンbudget等の条件が脚注で明示 [source](../../sources/Technical_Report/claude-mythos-preview.md)

## 現時点の解釈

### 何がすごいか
Mythos のすごさは「単に少し賢い」ではなく、既存の Opus 4.6 をかなり大きく上回る幅で、コード修正・長めの推論・ツール利用・サイバー領域がまとめて伸びていること。特に SWE-bench Pro (+24.4pt)、Terminal-Bench 2.0 (+16.6pt)、CyberGym (+16.5pt) のような実行を伴うベンチで差が二桁に達している。

### 性能改善の仮説（公式未公開）
改善要因は公式に開示されていないが、以下の仮説が有力:

1. **Claude Codeの実運用データflywheel**（かなり有力）: 2025年GA以降の大量の実コーディングセッションから失敗分布・成功軌跡が集まり、直接または間接にモデル改善へ寄与
2. **実行環境つきRL/post-trainingの強化**（かなり有力）: 実際にコードを実行・テストしてその結果で報酬を返すRL。pretrain < post-train/RLの寄与と推定
3. **長文脈理解・context managementの改善**（かなり有力）: 長い作業を破綻させない文脈運用能力が本丸
4. **tool-use policyの改善**（有力）: いつgrep/test/計画変更するかという行動政策
5. **repo-level localization/retrievalの改善**（有力）: 「どこを見ればいいか」を当てる能力
6. **reward hacking対策とverifier改善**（補助的）: テスト書き換え等のズルを潰しつつ真の性能向上

推定される全体像: 「Claude Codeで大量の実タスクが流れる → 失敗分布と成功軌跡が集まる → 実行環境つきRL/SFT/verifier改善を回す → 長文脈とツール政策も同時改善」

### 実行環境つきRLについて
普通のRLが「出力テキストそのもの」を評価するのに対し、実行環境つきRLは「出力を実際に環境で使わせて、その結果」を評価する。コーディング文脈では、テスト通過・コンパイル成功・タスク完了等の実行結果が報酬となる。複数ステップの行動列全体に対して学習でき、「作文の上手さを鍛えるRL」から「実務で成功する行動を鍛えるRL」への移行。ただし計算コスト高、報酬ハック、環境ノイズ、クレジット割り当ての難しさがある。

## 関連ページ
- [SWE-CI](../papers/Evaluation/swe-ci.md) — ソフトウェア工学評価ベンチマーク
- [Agentic RL Training](../papers/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md) — エージェントRL訓練の比較
- [OpenClaw-RL](../papers/RL/openclaw-rl.md) — エージェントRLフレームワーク

## 未解決の問い
- Mythosの性能改善のうち、モデル本体の能力向上分とscaffold/harness最適化分はどの程度分離可能か？
- Claude Code利用データのflywheel仮説はどの程度検証可能か？Anthropicのデータ利用ポリシーの変遷との整合性は？
- 実行環境つきRLのスケーリング則（計算量 vs 改善幅）はどこまで明らかになっているか？
