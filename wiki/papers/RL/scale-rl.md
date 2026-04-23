---
title: "The Art of Scaling Reinforcement Learning Compute for LLMs (ScaleRL)"
aliases: ["ScaleRL", "RL Scaling Law", "Art of Scaling RL"]
created: 2026-04-21
updated: 2026-04-21
tags: [scaling-law, rl, rlvr, compute-efficiency, scaling-recipe, post-training]
peer_review: accepted
venue: "ICLR 2026 (Oral)"
sources: [src-scale-rl]
---

# The Art of Scaling Reinforcement Learning Compute for LLMs

> **査読**: ✅ accepted — ICLR 2026 (Oral)

Khatri, Madaan, Tiwari et al. (2025) — arXiv 2510.13786 / OpenReview FMjeC9Msws

## ソースからの事実
- 総計 **40万GPU時間以上** を投じた、LLM向けRLスケーリング則の初の大規模体系研究 [source](../../../sources/RL/scale-rl.md)
- 計算-性能曲線を **sigmoid** でフィッティング（pretrainingのpower lawとは異なる形状）[source](../../../sources/RL/scale-rl.md)
- **発見1**: 全てのRLレシピが同じ漸近性能に収束するわけではない（レシピ選択は asymptote を動かす）[source](../../../sources/RL/scale-rl.md)
- **発見2**: loss aggregation / 正則化 / curriculum / off-policy アルゴリズムなどの細部は **計算効率** を調整するだけで、漸近性能を実質的に変えない [source](../../../sources/RL/scale-rl.md)
- **発見3**: 安定・スケーラブルなレシピは **予測可能な軌道** をたどり、小規模実行から外挿できる [source](../../../sources/RL/scale-rl.md)
- ベストプラクティス **ScaleRL** を提案し、10万GPU時間規模の単一RLランで検証性能を事前予測・的中させることで有効性を実証 [source](../../../sources/RL/scale-rl.md)

→ 詳細: [evidence](../../../evidence/RL/scale-rl.md)

## 現時点の解釈
RL訓練に「pretrainingのChinchilla則に相当する予測可能性」をもたらした基礎論文。RLVRの能力境界論争（filtering vs 真の能力獲得）に対して **sigmoid漸近値 vs 計算効率の切り分け** という定量的な分析軸を与えた点が大きい。**「loss aggregation等の細部は漸近値を動かさず効率のみを調整する」** という主張は、GRPO・DAPO・RS-GRPO・GSPO等のRL手法論争の多くが「漸近性能の争いではなく効率の争い」である可能性を示唆し、Yue et al. / ProRL 論争や Flash-RL/TIS のoff-policyミスマッチ議論と合わせて、RL研究の整理軸として重要。**Meta/UT Austin からの ICLR 2026 Oral** で、今後のRLVR論文の比較ベースラインになる。ScaleRL の具体レシピは10万GPU時間レベルで実証されており、実務のRL計画立案に直接的に使える。

## 関連ページ
- [RLVRの能力境界論争](../../topics/RL/rlvr-capability-boundary.md) — asymptote vs efficiency の切り分け軸を提供
- [Does RLVR Truly Unlock New Reasoning?](./rlvr-does-not-teach-new-reasoning.md) — Pass@k分析のfiltering派
- [ProRL](./prorl.md) — 長期RLで能力拡張を主張、予測可能scalingの実証例
- [DeepSeek-R1](./deepseek-r1.md) — Pure RL の大規模実例
- [MRPO](./mrpo.md) — manifold-reshaping による asymptote 突破を狙う
- [RS-GRPO](./rs-grpo.md) — CVaR目的関数、本論文枠組みでは「効率」寄りの修正
- [Flash-RL / TIS](./flash-rl-tis.md) — off-policy ミスマッチで実測scalingが歪む問題
- [The Debate on RLVR Reasoning Capability Boundary](./rlvr-capability-boundary-debate.md)

## 未解決の問い
- ScaleRL の sigmoid漸近値はタスク・モデル規模に応じてどう変化するか？「asymptote を動かす」設計選択のリスト化・体系化は可能か？
- 8B以上の大規模モデル（70B+）でも sigmoid フィッティングが維持されるか、それとも power law に遷移するか？
- 「効率のみ調整する設計選択」は本当に asymptote に影響しないのか、それとも実測計算量が足りず見えていないだけか？
- ScaleRL の外挿能力は agentic RL（環境内行動・長鎖ツール使用）でも成立するか？（CodeScout / OpenClaw-RL との接続）
- Flash-RL/TIS が指摘する rollout/学習ミスマッチは ScaleRL のsigmoid漸近値にどう効くか？（並列化差分を補正しないと scalingが歪む可能性）
