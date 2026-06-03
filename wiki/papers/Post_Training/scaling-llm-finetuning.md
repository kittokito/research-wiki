---
title: "When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method"
aliases: ["Scaling LLM Finetuning", "finetuning scaling law", "FMT vs PET scaling"]
created: 2026-06-03
updated: 2026-06-03
tags: [scaling-law, finetuning, PEFT, LoRA, prompt-tuning, full-model-tuning, data-efficiency]
peer_review: accepted
venue: "ICLR 2024"
sources: [src-scaling-llm-finetuning]
---

# When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method

> **査読**: ✅ accepted — ICLR 2024

Zhang, Liu, Cherry, Firat (2024) — Google DeepMind / arXiv 2402.17193

## ソースからの事実
- ファインチューニング性能を **LLMモデルサイズ・事前学習データ・ファインチューニングパラメータ数・ファインチューニングデータ**の4因子で分析 [source](../../../sources/Post_Training/scaling-llm-finetuning.md)
- ファインチューニングデータ量と各因子の間に **power-based の乗法的結合スケーリング則（multiplicative joint scaling law）** が成立 [source](../../../sources/Post_Training/scaling-llm-finetuning.md)
- **LLM ファインチューニングは事前学習データのスケーリングより LLM モデルサイズのスケーリングから恩恵を受ける** [source](../../../sources/Post_Training/scaling-llm-finetuning.md)
- **PET（prompt tuning / LoRA）のパラメータ数スケーリングは概して効きにくい** [source](../../../sources/Post_Training/scaling-llm-finetuning.md)
- **最適なファインチューニング手法はタスク・データ量依存**（低データでは PET 有利等）。FMT と PET を比較 [source](../../../sources/Post_Training/scaling-llm-finetuning.md)
- 1B〜16B、bilingual 機械翻訳・多言語要約、データ制限レジームで検証 [source](../../../sources/Post_Training/scaling-llm-finetuning.md)

→ 詳細: [evidence](../../../evidence/Post_Training/scaling-llm-finetuning.md)

## 現時点の解釈

本論文は **ファインチューニングを「予測可能なスケーリング則の対象」として定式化**し、設計判断（どの因子に投資するか、どの手法を選ぶか）に経験則を与えた点が核心。特に「**finetune データ × 各因子の乗法的結合**」という形は、「モデルが大きいほど少ない finetune データで足りる」「PET 容量を増やすより素のモデルを大きくする方が効く」といった実務判断に直結する。本リポジトリの議論軸との接続:

- **SFT データ設計クラスタの定量側**: [SFT Data Composition / DMT](sft-data-composition.md) が「能力ごとに finetune データの飽和点が違う」を定性的に示したのに対し、本論文は **finetune データ量の効果を冪則で定量化**する。両者を合わせると「finetune データは効くが、その限界効用はモデルサイズと乗法的に絡む」という像になり、[Curriculum Instruction Tuning](../../topics/Post_Training/curriculum-instruction-tuning.md) の「データの順序・配合・量」設計空間に**量の軸**の理論を加える。
- **スケーリング則ファミリーの finetune 版**: [言語構造の獲得理論](../Pretraining/language-structure-acquisition.md)（データ量↔文法深さ）、[ATLAS](../Pretraining/atlas-multilingual-scaling-laws.md)（多言語事前学習スケーリング）、[Scaling Behaviors of LLM RL](../RL/rl-scaling-math-qwen25.md)（RL ポストトレ）と並ぶ「**各学習段階のスケーリング則**」の一角。事前学習→ファインチューニング→RL の各段でスケーリングの効き方が違う、という全体像の finetune ピースを埋める。
- **PEFT の限界の明示**: 「PET のパラメータ scaling は効きにくい」は、LoRA/prompt を「大容量化して FMT に迫る」発想への警鐘。[Curriculum Instruction Tuning](../../topics/Post_Training/curriculum-instruction-tuning.md) で触れた D-MoLE（層ごとに LoRA を動的配置）のような**配置の工夫**が、単純な容量増より重要だという含意とも整合。

実務的には「**低データ × 小～中モデルなら PET、十分なデータなら FMT、そして finetune 性能を上げたいならまず素のモデルを大きく**」という指針として読める。タスクが機械翻訳・要約（多言語生成）に限られ、規模も 16B までである点は留保。

## 関連ページ
- [SFT Data Composition / DMT](sft-data-composition.md) — finetune データが能力に与える効果（本論文の定量スケーリングの定性版）
- [Curriculum Instruction Tuning](../../topics/Post_Training/curriculum-instruction-tuning.md) — finetune データの順序・配合（本論文は「量」の軸を定量化）
- [言語構造の獲得理論](../Pretraining/language-structure-acquisition.md) / [ATLAS](../Pretraining/atlas-multilingual-scaling-laws.md) / [Scaling Behaviors of LLM RL](../RL/rl-scaling-math-qwen25.md) — 各学習段階のスケーリング則ファミリー

## 未解決の問い
- 乗法的結合スケーリング則は、機械翻訳・要約以外（推論・コード・指示追従）や数百Bモデルでも保たれるか？
- 「PET パラメータ scaling が効かない」は配置の工夫（D-MoLE 型の動的 LoRA）でどこまで覆るか？
- 「モデルサイズ > 事前学習データ」という finetune 側の結論は、事前学習側の Chinchilla 的最適配分とどう両立するか？
