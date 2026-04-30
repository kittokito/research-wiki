---
title: "Dr. GRPO / Understanding R1-Zero-Like Training"
aliases: ["Dr. GRPO", "Understand R1-Zero", "R1-Zero Critical"]
created: 2026-04-23
updated: 2026-04-23
tags: [rl, rlvr, GRPO, dr-grpo, r1-zero, pretraining-bias, optimization-bias, token-efficiency, critical-analysis]
peer_review: accepted
venue: "COLM 2025"
sources: [src-dr-grpo]
---

# Understanding R1-Zero-Like Training: A Critical Perspective (Dr. GRPO)

> **査読**: ✅ accepted — COLM 2025

Liu, Chen, Li, Qi, Pang, Du, Lee, Lin (2025) — Sea AI Lab / sail-sg / NUS / arXiv 2503.20783 / OpenReview 5PAF7PAY2Y

## ソースからの事実
- R1-Zero 流の「SFTなし pure RL で推論向上」を **base model 要因** と **RL要因** に分解して批判的検証 [source](../../../sources/RL/dr-grpo.md)
- **DeepSeek-V3-Base は RL 前から "Aha moment" を示す** → R1-Zero の創発の一部は事前学習バイアス由来 [source](../../../sources/RL/dr-grpo.md)
- **Qwen2.5 base はプロンプトテンプレートなしでも強い推論を示す** → 事前学習段階の instruction-like 能力 [source](../../../sources/RL/dr-grpo.md)
- **GRPO には最適化バイアス**: 不正解出力の応答長を人為的に増加させる方向に偏る [source](../../../sources/RL/dr-grpo.md)
- **Dr. GRPO**（"done right" GRPO）: バイアス除去の unbiased 最適化手法、token 効率を改善しつつ推論性能維持 [source](../../../sources/RL/dr-grpo.md)
- **minimalist R1-Zero recipe**: 7B base で **AIME 2024 43.3%**（当時SOTA）[source](../../../sources/RL/dr-grpo.md)

→ 詳細: [evidence](../../../evidence/RL/dr-grpo.md)

## 現時点の解釈
Dr. GRPO 論文の真の貢献は **「R1-Zero の観察をどこまで RL に帰属させるか」という因果分離の問題提起** にある。DeepSeek-R1-Zero 発表以降、「SFTなし pure RL だけで推論が創発した」という解釈が支配的だったが、本論文は **"Aha moment" 等の現象の相当部分が事前学習由来** であることを示し、**RL の貢献を過大評価しない** 冷静な視点を導入した。これは [RLVR capability boundary debate](../../topics/RL/rlvr-capability-boundary.md) で言う「filtering 派」（[Does RLVR Truly Unlock New Reasoning](./rlvr-does-not-teach-new-reasoning.md), Yue et al.）の「RLは base のカバレッジを狭めるだけ」という主張と呼応するが、Dr. GRPO はより **中立的な立場** で「base の潜在能力 + RL の効率化」という二層説を提示している。

**Dr. GRPO の RL アルゴリズム的貢献** は GRPO の length bias を除去する定式化。この bias は「正解率の低いプロンプト上で不正解出力の応答長が人為的に伸びる」という現象で、**「長い応答は良い推論」という観察が単なる最適化アーティファクト** だった可能性を示す。[ScaleRL](./scale-rl.md) が GRPO を避けて CISPO に乗り換えたのは、本論文が指摘する GRPO の根本的バイアスと整合的（ScaleRL A.16 でも GRPO が 6k GPU-hours 後に truncation で不安定化するのを確認）。[RS-GRPO](./rs-grpo.md) / [MRPO](./mrpo.md) の GRPO 改良系列も、**本論文が指摘した length bias の異なる側面を攻めている** と解釈できる。

**Qwen2.5 の事前学習バイアス** という観察は、[Scaling Behaviors of LLM RL Post-Training](./rl-scaling-math-qwen25.md)（Tan et al., Qwen2.5 0.5B-72B 全系列で RL スケーリング則）の結果解釈に直接影響する: Dr. GRPO の発見が正しければ、Qwen2.5 系列の RL 効率の高さは **事前学習段階の準備度** に起因する可能性があり、他系列（LLaMA, Gemma）では k(N) saturation 式の係数が大きく変わる可能性を示唆する。

**"R1-Zero 流" 全般への一般性**: minimalist recipe + Dr. GRPO で 43.3% AIME 2024 を 7B で達成したことは、**派手な手法なしで SOTA に迫れる** ことの証拠として重要。ただし 2026 時点では [ScaleRL](./scale-rl.md), [MRPO](./mrpo.md), [RS-GRPO](./rs-grpo.md) 等が追い越しており、歴史的ベースラインという位置付け。**COLM 2025 採択** (OpenReview 5PAF7PAY2Y) で、"RLVR の批判的再検討" 領域の代表的論文として今後も長く引用されると予想される。

## 関連ページ
- [RLVRの能力境界論争](../../topics/RL/rlvr-capability-boundary.md) — 「filtering vs 真の能力獲得」の議論に「事前学習バイアス」という第三の軸を追加
- [DeepSeek-R1](./deepseek-r1.md) — 本論文の直接的批判対象
- [Does RLVR Truly Unlock New Reasoning?](./rlvr-does-not-teach-new-reasoning.md) — filtering派、Dr. GRPO の pretraining bias 論と呼応
- [ProRL](./prorl.md) — 長期RLで能力拡張、Dr. GRPO のbias除去と独立軸
- [ScaleRL](./scale-rl.md) — CISPO 採用の背景として Dr. GRPO の指摘する GRPO バイアスが効く
- [MRPO](./mrpo.md) — GRPO 改良、bias 除去の別方向
- [RS-GRPO](./rs-grpo.md) — GRPO 改良、CVaR ベース、本論文の bias 除去と直交
- [Flash-RL / TIS](./flash-rl-tis.md) — rollout/学習ミスマッチ、本論文の pure optimization bias と独立問題
- [Scaling Behaviors of LLM RL Post-Training](./rl-scaling-math-qwen25.md) — Qwen2.5 事前学習バイアスが scaling 則の一般性を損なう可能性

## 未解決の問い
- DeepSeek-V3-Base で観察される "Aha moment" の本質: 訓練データにCoT類似パターンが潜在していたのか、emergence の真の現象か？
- Dr. GRPO のバイアス除去は ScaleRL 分類で「漸近性能」を改善するのか、「効率のみ」を改善するのか？
- Qwen2.5 以外のベースモデル（LLaMA 3, Gemma 2, DeepSeek-V3-Base）で同じ事前学習バイアスが見られるか？
- 「不正解出力の応答長バイアス」は最新の GRPO派生（CISPO, RS-GRPO, MRPO）でどこまで除去されているか？
- Dr. GRPO と CISPO を組み合わせると相加的な改善が得られるか、重複的か？
- 「pretraining bias の有無」を定量化する統一的な指標はあるか？（事前学習段階で推論能力を事前測定する方法）
