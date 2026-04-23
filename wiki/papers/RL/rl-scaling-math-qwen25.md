---
title: "Scaling Behaviors of LLM RL Post-Training (Tan et al., 2025)"
aliases: ["RL Post-Training Scaling", "Qwen2.5 RL Scaling", "k(N) Saturation"]
created: 2026-04-22
updated: 2026-04-22
tags: [scaling-law, rl, rlvr, post-training, mathematical-reasoning, qwen25, grpo, data-efficiency, power-law]
peer_review: accepted
venue: "ACL 2026 (Main Conference)"
sources: [src-rl-scaling-math-qwen25]
---

# Scaling Behaviors of LLM Reinforcement Learning Post-Training

> **査読**: ✅ accepted — ACL 2026 (Main Conference)

Tan, Geng, Yu, Zhang, Wan et al. (2025) — arXiv 2509.25300 / v4 (2026-04-17) / Shanghai AI Lab × Oxford ほか

## ソースからの事実
- Qwen2.5 dense 全系列（**0.5B–72B**）を用いた、数学推論RLポストトレーニングの大規模体系研究 [source](../../../sources/RL/rl-scaling-math-qwen25.md)
- **発見1**: 大モデルほど計算・データ両面で学習効率が一貫して高い [source](../../../sources/RL/rl-scaling-math-qwen25.md)
- **発見2**: test loss と (compute, data) は **log L(N, X) = −k(N)·log X + E(N)** の power-law で記述でき、base / instruct に頑健 [source](../../../sources/RL/rl-scaling-math-qwen25.md)
- **発見3**: 学習効率 k(N) は **k(N) = K_max / (1 + N_0/N)** の形で飽和する（latent saturation）[source](../../../sources/RL/rl-scaling-math-qwen25.md)
- **発見4**: データ制約下では高品質データの繰り返し使用が有効で、最終性能は **ユニークサンプル数ではなく最適化ステップ総数** に支配される [source](../../../sources/RL/rl-scaling-math-qwen25.md)
- GRPO を基軸に、in-domain（訓練分布）＋ OOD（AIME2024, AMC2023, GSM8K, MATH500, HumanEval, Zebra Puzzle, SuperGPQA）で評価 [source](../../../sources/RL/rl-scaling-math-qwen25.md)

→ 詳細: [evidence](../../../evidence/RL/rl-scaling-math-qwen25.md)

## 現時点の解釈
本論文の価値は「RLポストトレーニングにも pretraining と同様の予測可能スケーリングが存在する」ことを示した点にとどまらず、**学習効率 k(N) 自体が飽和する** という保守的な上限を解析的に与えた点にある。**「大モデルほど効率で勝つ」と「効率そのものがサチる」** は表面的には矛盾するが、飽和式 k(N)=K_max/(1+N_0/N) が両者を統合する: 小モデル領域では k(N) が急峻に伸びるが、N ≫ N_0 で K_max に近づくため、単純に「モデルを大きくすれば報酬面のRL効率が常に改善する」わけではない。これは「RLは小モデルには効きにくい / 大モデルほど安価に伸びる」という素朴な直感に、**天井が存在する** という追加制約を与える。

[ScaleRL](./scale-rl.md) が sigmoid（S字）フィットで「漸近値 vs 計算効率」の切り分けを提示したのに対し、本論文は **log-linear power-law + saturated efficiency** を提示しており、両者は関数形を巡って対立するというより、**計算量レンジとタスクに応じた補完的な描像**と解釈するのが妥当。ScaleRLが「全レシピが同じ漸近には行かない」としたのに呼応して、本論文の k(N) saturation は「大モデルの優位性にも上限がある」という、効率側の天井を与える。

発見4（データ再利用）は [ProRL](./prorl.md)（長期RL訓練で境界拡張）と整合的であり、RLVR能力境界論争（`topics/RL/rlvr-capability-boundary.md`）の文脈では「小さく高品質な訓練セット × 十分な最適化ステップ」が効率面のスイートスポットである可能性を示唆する。一方で [Does RLVR Truly Unlock New Reasoning?](./rlvr-does-not-teach-new-reasoning.md) のfiltering派の主張（RLVR は base のカバレッジを狭めるだけ）からすると、「繰り返し最適化が支配的」という結果は **filtering/sharpening の飽和曲線** としても解釈でき、能力境界論争の直接的決着にはならない点に注意。

**ACL 2026 Main 採択** は、RLスケーリング則の研究が NLP 本流コミュニティでの基盤研究として認められたことを意味する。

## 関連ページ
- [ScaleRL: The Art of Scaling RL Compute](./scale-rl.md) — sigmoid フィット・漸近値 vs 効率の切り分け（本論文の power-law + k(N) saturation と相補的）
- [RLVRの能力境界論争](../../topics/RL/rlvr-capability-boundary.md) — 効率飽和は能力境界に追加の上限を与える
- [ProRL](./prorl.md) — 長期RLで境界拡張、本論文の「最適化ステップ総数支配」と整合
- [Does RLVR Truly Unlock New Reasoning?](./rlvr-does-not-teach-new-reasoning.md) — Pass@k filtering 主張、本論文の「繰り返し最適化支配」と接続
- [DeepSeek-R1](./deepseek-r1.md) — Pure RL の大規模実例、スケーリング解析の基礎データ点
- [MRPO](./mrpo.md) — manifold reshaping による asymptote 突破、k(N) saturation を越える手法候補
- [RS-GRPO](./rs-grpo.md) — リスク感応的目的関数、本論文枠組みでは効率側の修正
- [Flash-RL / TIS](./flash-rl-tis.md) — rollout/学習ミスマッチ、本論文の k(N) 推定にも影響する可能性
- [Scaling Laws of Motion Forecasting and Planning](../Physical_AI/scaling-laws-motion-forecasting-planning.md) — LLM外でのスケーリング則
- [ATLAS: Multilingual Scaling Laws](../Pretraining/atlas-multilingual-scaling-laws.md) — pretraining側のスケーリング則

## 未解決の問い
- k(N) saturation の K_max, N_0 はタスク / RLアルゴリズム / 報酬形状でどう変化するか？ 普遍定数は存在するか？
- Qwen2.5 系列以外（MoE / LLaMA / DeepSeek / Kimi）でも同じ power-law + k(N) 飽和式が成立するか？
- 「最適化ステップ総数 vs サンプルユニーク数」の支配関係は、agentic RL / コード実行 / webブラウジング等の環境内RLでも成立するか？
- 本論文の power-law と ScaleRL の sigmoid はどの計算量レンジで切り替わるか？同一データで比較できないか？
- k(N) saturation の物理的（アーキテクチャ的）起源は何か？表現容量と報酬信号の分布のミスマッチが支配因子か？
- データ制約下で「繰り返し最適化が支配的」という結果は、memorization / 報酬ハッキング / pass@k劣化 を伴わずにどこまで延長できるか？
