---
title: "Your Efficient RL Framework Secretly Brings You Off-Policy RL Training (Flash-RL / TIS)"
aliases: ["Flash-RL", "TIS", "Truncated Importance Sampling", "Rollout-Training Mismatch"]
created: 2026-04-17
updated: 2026-04-17
tags: [RLHF, RLVR, off-policy, importance-sampling, TIS, vLLM, FSDP, VeRL, PPO, GRPO, DAPO, MoE, rollout-training-mismatch, Flash-RL]
peer_review: n/a
venue: ""
sources: [src-flash-rl-tis]
---

# Your Efficient RL Framework Secretly Brings You Off-Policy RL Training

> **査読**: — n/a（ブログ記事 / Feng Yao's Notion）
>
> **採用状況**: VeRL · slime · OAT · SkyRL · OpenRLHF · REINFORCE++ がTISを実装／統合済み

Feng Yao\*, Liyuan Liu\*, Dinghuai Zhang, Chengyu Dong, Jingbo Shang, Jianfeng Gao (2025) — UCSD × Microsoft Research
*初公開 2025-08-05 / 最終更新 2025-10-13*

## ソースからの事実
- hybrid RLフレームワーク（rollout=vLLM/SGLang、train=FSDP/Megatron）では、同一パラメータθでも `π_sampler` と `π_learner` のトークン確率が大きく乖離し、RL訓練を暗黙のうちに off-policy 化する [source](../../../sources/RL/flash-rl-tis.md)
- vLLM側のシステムレベル修正（真のサンプリング確率返却、lm_head fp32化）だけでは乖離は解消しない [source](../../../sources/RL/flash-rl-tis.md)
- 著者らは Truncated Importance Sampling (TIS) を提案: 勾配を `min(π_learner/π_sampler, C) * R * ∇log π_learner` に置き換える数行修正で、REINFORCE/PPO いずれにも適用可能 [source](../../../sources/RL/flash-rl-tis.md)
- Qwen2.5-32B + DAPO、Qwen2.5-0.5B + GSM8K（INT8 rollout）で、TISが entropy collapse・応答長暴走・負のKL推定といった失敗モードを解消し、通常PPOを大きく上回る [source](../../../sources/RL/flash-rl-tis.md)
- ミスマッチの主因は並列化差分（TP/SP の sampler–learner 不一致）と長文応答の累積、sampler backend（vLLM vs SGLang）単独の寄与は小さい [source](../../../sources/RL/flash-rl-tis.md)
- MoEモデルは動的ルーティングと専用カーネルによりミスマッチが増幅される見込み、TISの重要性はさらに高い [source](../../../sources/RL/flash-rl-tis.md)
- GSPO／GMPOが重要度比の計算方式を改良するのに対し、TISは **システム由来のミスマッチ** に対処するため直交して併用可能 [source](../../../sources/RL/flash-rl-tis.md)

→ 詳細: [evidence](../../../evidence/RL/flash-rl-tis.md)

## 現時点の解釈

LLM向けRLフレームワークが「スループット最適化のため生成と学習を別バックエンドで走らせる」という当然の設計判断を採用した結果、標準的な PPO/GRPO/DAPO レシピが **気づかれずに off-policy RL 化していた** ことを突き止めた仕事。問題は数値誤差の蓄積ではなく、TP/SPの並列化設定差や長文生成に沿って内部状態が発散していく「システムレベルの分布乖離」で、vLLM側の精度向上だけでは消えない。

修正は importance-sampling という教科書的な道具立てだが、実装の軽さ（数行）と効果の大きさ（INT8 rolloutでも bf16 相当まで回復、entropy collapse解消）、そして VeRL/slime/OAT/SkyRL/OpenRLHF/REINFORCE++ が素早く採用したことで、事実上コミュニティの標準 patch になっている。ブログゆえ peer review は n/a だが、実用上の影響力は査読付き論文に劣らない。

**RLVR能力境界論争への接続**: Yue et al. 系の「RLVR は filtering に過ぎない」説・ProRL 系の「長期訓練で真に拡張できる」説のどちらの測定も、本ブログが指摘する off-policy バイアスの上に乗っていた可能性が高い。特に entropy collapse や応答長暴走は shrinkage 派の「多様性が失われる」観察と表面的に似ているが、一部はミスマッチ由来のアーティファクトで TIS で解消される。今後の pass@k 計測やスケーリング則検証は、TIS 等で学習–生成ギャップを吸収した上で比較すべき。

**示唆**: 新規RL手法を評価するベースラインは、フレームワークの暗黙バイアスを踏まえて較正すべき。特にMoE RLではTIS類が必須になる可能性が高い。

## 関連ページ
- [[rlvr-capability-boundary]] — RLVR能力境界論争の全体像（off-policy バイアスが測定に与える影響の示唆を追加検討すべき）
- [[prorl]] — 長期RL訓練、KL制御・ポリシーリセットで safetyを担保、TISと併用可能
- [[mrpo]] — 幾何学的介入（SOE + rank正則化）、TISと直交
- [[rs-grpo]] — 目的関数のリスク感応性、TISと直交
- [[rlvr-does-not-teach-new-reasoning]] — pass@k低下の主張、測定条件にoff-policyバイアスが混入していた可能性
- [[reasoning-with-sampling]] — 推論時サンプリング改善、訓練側のTISとは相補的

## 未解決の問い
- クランプ定数 C の最適設定（TIS-2 vs TIS-8）の体系的な指針は？
- MoE RLにおけるTIS効果の定量化（dynamic routingの影響分離）は？
- 長文応答でミスマッチが累積する現象の根本原因（attention累積誤差、KV cache離散化、等）は？
- TIS導入後も残る偏りは、`k3` KL 推定以外のどの診断指標で可視化すべきか？
- sampler／learner の並列化を完全に揃えたときの training throughput ペナルティとのトレードオフ設計は？
