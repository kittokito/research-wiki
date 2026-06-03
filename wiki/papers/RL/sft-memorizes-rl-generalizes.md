---
title: "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training"
aliases: ["SFTvsRL", "SFT Memorizes RL Generalizes", "Chu et al. 2025"]
created: 2026-05-19
updated: 2026-05-19
tags: [RL, SFT, post-training, generalization, memorization, out-of-distribution, PPO, outcome-based-reward, multimodal, V-IRL, GeneralPoints]
peer_review: accepted
venue: "ICML 2025 (PMLR 267)"
sources: [src-sft-memorizes-rl-generalizes]
---

# SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training

> **査読**: ✅ accepted — **ICML 2025** (PMLR 267, Vancouver)

Chu, Zhai, Yang, Tong, Xie, Schuurmans, Le, Levine, Ma (2025) — UC Berkeley × HKU × Google DeepMind × University of Alberta — [arXiv 2501.17161](https://arxiv.org/abs/2501.17161) / [Project](https://tianzhechu.com/SFTvsRL/) / [Code](https://github.com/LeslieTrue/SFTvsRL)

## ソースからの事実
- **RL（PPO + outcome-based reward）は rule-based textual と visual の両 OOD で汎化**、SFT は ID に過適合し OOD で劇的劣化 [source](../../../sources/RL/sft-memorizes-rl-generalizes.md)
- **SFT は RL の前段として依然必要** ——指示追従できない Llama-3.2-Vision-11B への直接 RL は全て失敗 [source](../../../sources/RL/sft-memorizes-rl-generalizes.md)
- **SFT は recognition token を犠牲に reasoning token に局所過適合**、計算量を増やすほど視覚認識精度が低下（RL は逆に向上） [source](../../../sources/RL/sft-memorizes-rl-generalizes.md)
- **V-IRL-VL の visual OOD で +33.8pt の SOTA 更新**（16.7% → 77.8%）、V-IRL-L Rule OOD で SFT は 80.8% → 1.3% という極端な暗記の証拠 [source](../../../sources/RL/sft-memorizes-rl-generalizes.md)
- **検証反復数 {1, 3, 5, 10} で OOD 改善 {+0.48, +2.15, +2.99, +5.99}pt** の test-time compute scaling [source](../../../sources/RL/sft-memorizes-rl-generalizes.md)
- Compute scaling で **RL のみ ID/OOD 両方で単調増加**、SFT は ID 増加でも OOD は逆効果 [source](../../../sources/RL/sft-memorizes-rl-generalizes.md)

→ 詳細: [evidence](../../../evidence/RL/sft-memorizes-rl-generalizes.md)

## 現時点の解釈
本論文の核心は「SFT vs RL」を単なる手法選択ではなく **memorization vs generalization の根本的軸**として再定義した点にある。本リポジトリの [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](willccbb-sft-rl-opd.md) が後年（2026）に提示した **compounding argument**（SFT は分布固定で天井 ≈ teacher、RL はロールアウトで compounding し天井 = verifier 能力）の **経験的先行事例**として位置付けられる。Brown & Claude Opus 4.7 の理論的整理が本論文の実証結果を一般化する関係。

「SFT 必要」の限定条件（指示追従できない backbone）の明示は [DeepSeek-R1](deepseek-r1.md) の "pure RL で SFT 不要" 主張との見かけの矛盾を解消する道具立てとして重要。[Dr. GRPO](dr-grpo.md) が指摘した「事前学習バイアスが R1 系の "Aha moment" を支えていた」と整合的で、**backbone の事前知識量に応じて SFT 必要性が変動する**という共通理解を補強する。

V-IRL-VL Visual OOD の **+61.1pt** という極端な改善幅は、reasoning token と recognition token の表現学習に対する RL/SFT の **質的に異なる勾配ジオメトリ**を示唆——本リポジトリの [On SFT, RL, and on-policy distillation](willccbb-sft-rl-opd.md) の "gradient geometry の3軸（密度・バイアス・集中度）" 分類の動機にも繋がる。SFT が reasoning token に過適合する仮説は、後年の **OPSD の pivot token concentration による performance collapse** 発見（Brown & Claude Opus 4.7 2026）と同根の現象であり、SFT の局所過適合が token type 間の不均衡から生まれることを示す系譜の起点。

検証反復数による test-time compute scaling は **o1 / DeepSeek-R1 系の inference-time compute scaling** パラダイムの早期実証であり、[Reasoning with Sampling](../Inference_Decoding/reasoning-with-sampling.md) や [MiniMax-M1](../Technical_Report/minimax-m1.md) の thinking budget 戦略の理論的根拠の一部を提供する。

評価面では本リポジトリの [Your Evals Will Break](../Evaluation/your-evals-will-break.md) が問題提起する「accuracy ベンチマークの構造的脆弱性」の対極として、**OOD shift を明示的に評価軸に組み込んだ post-training 比較**の好例。能力レジーム遷移を捕捉する設計の手本となりうる。

## 関連ページ
- [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](willccbb-sft-rl-opd.md) — compounding argument の理論化、本論文の経験事実を一般化
- [DeepSeek-R1](deepseek-r1.md) — "pure RL で reasoning 創発" の主張、本論文の "SFT 必要" の限定条件と接続
- [Dr. GRPO](dr-grpo.md) — 事前学習バイアス説、backbone 依存性の理論基盤
- [ProRL](prorl.md) — RL が真に新しい reasoning 能力を獲得することの主張、本論文の汎化結果と整合
- [Does RLVR Truly Unlock New Reasoning?](rlvr-does-not-teach-new-reasoning.md) — 反対側の立場（RLVR は filtering）、本論文の OOD 改善と論争中
- [ScaleRL](scale-rl.md) — RL の sigmoid scaling 則、本論文の compute scaling 観察の精緻化
- [Scaling Behaviors of LLM RL Post-Training](rl-scaling-math-qwen25.md) — power-law フィット、本論文の compute scaling と相補
- [Flash-RL / TIS](flash-rl-tis.md) — off-policy RL の暗黙化問題、本論文のような長期 on-policy RL の安定性確保技術
- [Your Evals Will Break](../Evaluation/your-evals-will-break.md) — OOD 評価設計の重要性、本論文は実装側の好例

## 未解決の問い
- 指示追従済み backbone（Qwen3 / DeepSeek-V3 等）で本論文のセットアップを再現したら、SFT 前段は本当に不要か？
- "SFT memorizes" の境界は ID/OOD の分布距離でどう数値化できるか？ memorize → generalize の臨界点はあるか？
- Visual OOD で +61.1pt、Rule OOD で +9.3pt という改善幅の差はなぜ生まれるか？ recognition vs reasoning の表現学習の質的差異か、データ多様性の差か？
- outcome-based reward の優位性は PPO 固有か、GRPO / RLOO / VinePPO 等でも再現するか？
- カードゲーム + ナビゲーションの結論は、大規模 reasoning ベンチマーク（AIME / SWE-Bench / GPQA）にどこまで外挿できるか？
- "SFT は reasoning token に過適合する" 仮説の **メカニズム解釈**（attention head・回路レベル）は？ [The Geometry of Forgetting](../Reasoning/geometry-of-forgetting.md) の埋め込み幾何学と接続可能か？
