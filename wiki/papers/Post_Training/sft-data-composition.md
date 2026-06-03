---
title: "How Abilities in LLMs are Affected by SFT Data Composition (DMT)"
aliases: ["SFT Data Composition", "DMT: Dual-stage Mixed Fine-tuning", "SFTデータ構成と能力"]
created: 2026-06-03
updated: 2026-06-03
tags: [SFT, data-composition, catastrophic-forgetting, multi-task, DMT, math-reasoning, code-generation, instruction-following]
peer_review: accepted
venue: "ACL 2024 (Main)"
sources: [src-sft-data-composition]
---

# How Abilities in LLMs are Affected by SFT Data Composition (DMT)

> **査読**: ✅ accepted — ACL 2024（Main Conference）

Dong, Yuan, Lu, Li, Xue, Liu, Wang, Yuan, Zhou, Zhou（Alibaba / Qwen team）— arXiv 2310.05492（v1 2023-10）

## ソースからの事実
- **3能力のスケーリング特性が異なる**: 数学（GSM8K）・コード（HumanEval）はデータ量とともに単調向上、**一般能力（MT-Bench）は約1,000サンプルで頭打ち** [source](../../../sources/Post_Training/sft-data-composition.md)
- **混合効果の反転**: 低リソースでは混合が各能力を底上げ、高リソースでは能力間が **競合（conflict）** [source](../../../sources/Post_Training/sft-data-composition.md)
- **逐次学習 → catastrophic forgetting**、同時学習 → conflict というジレンマ [source](../../../sources/Post_Training/sft-data-composition.md)
- **DMT（Dual-stage Mixed Fine-tuning）**: Stage1 で専門データ（math/code）→ Stage2 で一般データに専門データを **比率 k で少量混合**。conflict と forgetting の両方を緩和し専門/一般能力を両立 [source](../../../sources/Post_Training/sft-data-composition.md)
- **モデルサイズ**: 大きいほど低リソース設定での gain が大きい（LLaMA 7B/13B/33B で検証） [source](../../../sources/Post_Training/sft-data-composition.md)

→ 詳細: [evidence](../../../evidence/Post_Training/sft-data-composition.md)

## 現時点の解釈

本論文の核心は **「能力ごとにデータ・スケーリング特性が違う」ことを前提に、学習の順序と混合比で多能力を両立させる**という post-training の設計原理。本リポジトリの議論軸との接続:

- **学習順序（ordering）の系譜**: DMT の「専門 → （少量混合つき）一般」という2段は、[On SFT, RL, and on-policy distillation](../RL/willccbb-sft-rl-opd.md) の **compounding argument**（SFT で土台を作ってから次段で伸ばす順序の正当化）の SFT 内版とみなせる。「順序それ自体が性能を決める」という同じ直観を、能力間 conflict / forgetting の観点から実証している。
- **継続学習との対応**: 「先に得た専門能力を一般データ学習中に忘れる」という catastrophic forgetting の問題と、少量の専門データ混合で抑える発想は、[Learning, Fast and Slow (FST)](../RL/learning-fast-and-slow.md) の継続学習（タスクを跨ぐと RL が stall する設定で near-peak を維持）と同じ問題構造に対する、より単純なデータ側の対処。FST が「fast/slow weights の分離」で解くのに対し、DMT は「学習段階と混合比」で解く。
- **memorization vs generalization との関係**: [SFT Memorizes, RL Generalizes](../RL/sft-memorizes-rl-generalizes.md) は「SFT は ID に過適合しやすい」と指摘するが、本論文は SFT 内でも **能力ごとに飽和点が違い（general は ~1000 で頭打ち）**、過剰データが他能力を押しのける構造を示す。両者を合わせると「general alignment は少データで足り、専門能力こそデータ量が効く」という post-training の資源配分指針が見えてくる。
- **Qwen 系 post-training の先行研究**: 著者が Alibaba/Qwen チームであり、[Qwen3](../Technical_Report/qwen3.md) の多段 post-training（Long-CoT → Reasoning RL → Thinking Mode Fusion → General RL で thinking/non-thinking を統合）に通じる「段階を分けて能力を統合する」設計思想の源流の一つ。

実務的含意は明快で、**「全部混ぜて一気に SFT」は高リソースでは能力を競合させるため、専門能力を先に入れ、一般 alignment は少データ＋専門データの少量混合で仕上げる**のが安全、という指針。古め（2023）の論文だが、multi-skill SFT のデータ配合を考えるときの基準点として今も有効。

## 関連ページ
- [On SFT, RL, and on-policy distillation](../RL/willccbb-sft-rl-opd.md) — 学習順序（SFT-then-RL）の正当化と接続する compounding argument
- [Learning, Fast and Slow (FST)](../RL/learning-fast-and-slow.md) — catastrophic forgetting / 継続学習への別アプローチ
- [SFT Memorizes, RL Generalizes](../RL/sft-memorizes-rl-generalizes.md) — SFT の過適合特性、能力別データ効率の補完的視点
- [Qwen3](../Technical_Report/qwen3.md) — 同チーム系の多段 post-training への発展

## 未解決の問い
- 混合比 k の最適値はデータ量・モデルサイズの関数として予測できるか？スケーリング則化できるか？
- 3能力（math/code/general）以外（多言語・長文脈・安全性・ツール使用）にも同じ「能力ごとに飽和点が違う」構造は当てはまるか？
- DMT の2段構成は、後続の RLHF/DPO/RLVR 段階とどう組み合わさるか？SFT 内 forgetting 対策が RL 段階の能力保持にも効くか？
