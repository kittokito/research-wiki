---
title: "MiniMax-M1: Scaling Test-Time Compute with Lightning Attention"
aliases: ["MiniMax-M1", "M1", "Lightning Attention Reasoning Model"]
created: 2026-04-23
updated: 2026-04-23
tags: [technical-report, open-weight, reasoning, MoE, lightning-attention, long-context, rl, CISPO, test-time-compute, MiniMax]
peer_review: n/a
venue: ""
sources: [src-minimax-m1]
---

# MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention

> **査読**: — n/a（テクニカルレポート）

MiniMax Team (2025) — arXiv 2506.13585 / GitHub: MiniMax-AI/MiniMax-M1

## ソースからの事実
- **世界初のオープンウェイト・大規模ハイブリッドアテンション推論モデル** [source](../../../sources/Technical_Report/minimax-m1.md)
- アーキテクチャ: **hybrid MoE + lightning attention**（MiniMax-Text-01 ベース）、**456B total / 45.9B active per token** [source](../../../sources/Technical_Report/minimax-m1.md)
- **ネイティブ 1M context**（DeepSeek R1 の8倍）、lightning attention で test-time compute を効率的にスケール [source](../../../sources/Technical_Report/minimax-m1.md)
- RL訓練: **sandbox ベースの実ソフトウェアエンジニアリング環境** を含む多様タスク [source](../../../sources/Technical_Report/minimax-m1.md)
- **CISPO**（新規RLアルゴリズム）: **importance sampling weights を clip**（token updates ではなく）し、競合RL派生を上回る [source](../../../sources/Technical_Report/minimax-m1.md)
- hybrid attention + CISPO で **512 H800 GPU × 3週間 / $534,700** のフルRL訓練 [source](../../../sources/Technical_Report/minimax-m1.md)
- **thinking budget 40K / 80K の2版を公開**（40Kは80K訓練の途中段階）[source](../../../sources/Technical_Report/minimax-m1.md)
- DeepSeek-R1 / Qwen3-235B に匹敵・上回る、特に **complex software engineering / tool use / long-context** で強み [source](../../../sources/Technical_Report/minimax-m1.md)

→ 詳細: [evidence](../../../evidence/Technical_Report/minimax-m1.md)

## 現時点の解釈
MiniMax-M1 の位置付けは **「オープンウェイト推論モデル競争」×「hybrid attention による test-time compute scaling」×「RLアルゴリズム改良（CISPO）」** の3軸が交差する点にある。DeepSeek-R1 がpure transformer + GRPO、Qwen3-235B が標準MoE+推論、に対し、**M1は attention 機構そのものを効率化** して長い思考系列（thinking budget 40K/80K）を現実的なコストで訓練・推論可能にした点で differentiate している。

**CISPO** は本wikiの RL 論争とも直結: 「importance sampling weights を clip する（token updates ではなく）」という設計は、[Flash-RL / TIS](../RL/flash-rl-tis.md) の Truncated Importance Sampling（rollout/学習ミスマッチを IS 比の上限クランプで緩和）と同系統の発想であり、clip 対象を「トークン更新」から「IS 重み」へずらすことでRL効率を改善する。この方向性は [ScaleRL](../RL/scale-rl.md) の枠組みでは **「効率を動かす設計選択」** に分類され、漸近性能より計算効率側の最適化に寄っている（ScaleRL の結論に沿う）。一方 [RS-GRPO](../RL/rs-grpo.md) の CVaR ベース目的関数とは独立した軸の修正で、本質的に直交（組み合わせ可能）。

**コスト公開（$534,700 / 3週間 / 512 H800）** は推論モデルのRL訓練コストを透明化した点で意義深く、[Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) の k(N) saturation 議論の追加データ点として有用。Qwen2.5 72B 系列外での power-law / saturation フィットの検証材料にもなる（ただし本論文は scaling 論文ではないので直接のフィット提供はない）。

1M context は **DeepSeek-R1 の 8倍** という数字だけだと実効性能は未保証。[Memory Sparse Attention](../Architecture/memory-sparse-attention.md)・[TurboQuant](../Efficiency_Optimization/turboquant.md) など KV cache 最適化論文との関連で、lightning attention の実効 long-range 性能は独立評価が望まれる。

テクニカルレポート（査読 n/a）であり、CISPO の一般性・hybrid attention の long-context 実効性能・ベンチマーク比較の公平性は **第三者による再現・独立評価待ち**。ただし **オープンウェイト + GitHubコード公開** のため、検証のハードルは低い。

## 関連ページ
- [Kimi K2.5](./kimi-k25.md) — 同じオープンウェイト技術レポート枠（マルチモーダル側）
- [Flash-RL / TIS](../RL/flash-rl-tis.md) — importance sampling 側のRL効率修正、CISPO と同系統
- [RS-GRPO](../RL/rs-grpo.md) — CVaR ベース目的関数、CISPO と直交
- [ScaleRL](../RL/scale-rl.md) — CISPO は「効率を動かす設計選択」に該当する可能性
- [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) — RL訓練コストのデータ点
- [Memory Sparse Attention](../Architecture/memory-sparse-attention.md) — 1M context の実効性能評価軸
- [Attention Residuals](../Architecture/attention-residuals.md) — Kimi Linear 系の注意機構改良、lightning attention と並列する系譜

## 未解決の問い
- CISPO の利点は MiniMax-M1 の hybrid attention と密結合か、標準 Transformer + GRPO でも同等効果が出るか？
- 1M context の needle-in-haystack / long-range dependency の実効性能は、lightning attention で実際にどこまで保たれるか？
- thinking budget 40K → 80K で得られる追加性能の内訳（何のタスクで伸び、何は頭打ちか）は？
- $534,700 / 3週間というコストは、[Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) の k(N) saturation フィットのどの点にあたるか？
- CISPO はなぜ token-level clipping ではなく IS-weight clipping が優位か（理論的根拠）？
- MiniMax-M1 の hybrid attention における lightning / softmax の比率（何層ごと）と、その比率が推論能力・long context 性能にどう効いているか？
