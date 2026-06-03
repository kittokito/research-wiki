---
source: src-scaling-llm-finetuning
date_extracted: 2026-06-03
---

# When Scaling Meets LLM Finetuning からの抽出

## 調査対象のスケーリング因子
- (1) LLM モデルサイズ、(2) 事前学習データサイズ、(3) ファインチューニングパラメータ数（PET の容量）、(4) ファインチューニングデータサイズ [source](../../sources/Post_Training/scaling-llm-finetuning.md)

## 中心的な結果: multiplicative joint scaling law
- ファインチューニングデータサイズと各スケーリング因子の間に **power-based の乗法的結合スケーリング則**が成立 [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- すなわち、ファインチューニングデータ量の効果は各因子（モデルサイズ等）と**乗法的に結合した冪則**の形で記述できる（L ≈ A · X^{-a} · D_f^{-b} + E 型の joint power-law） [source](../../sources/Post_Training/scaling-llm-finetuning.md)

## 比較する手法
- **Full-Model Tuning (FMT)** — 全パラメータを更新 [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- **Parameter-Efficient Tuning (PET)** — Prompt tuning と LoRA [source](../../sources/Post_Training/scaling-llm-finetuning.md)

## 主要な発見
- **LLM のファインチューニングは、事前学習データのスケーリングよりも LLM モデルサイズのスケーリングからより恩恵を受ける** [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- **PET のパラメータ数スケーリングは概して効きにくい（ineffective）** — PET の容量を増やしても性能はあまり伸びない [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- **最適なファインチューニング手法はタスクとファインチューニングデータ量に強く依存する**（単一のベスト手法はない。低データでは PET が有利になりやすい等） [source](../../sources/Post_Training/scaling-llm-finetuning.md)

## 実験設定
- モデルサイズ **1B〜16B** のバイリンガル LLM [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- タスク: **bilingual 機械翻訳・多言語要約**、**データ制限（data-limited）レジーム** [source](../../sources/Post_Training/scaling-llm-finetuning.md)

## 制限・注意点
- タスクは機械翻訳・要約（生成系・多言語）に限定。分類・推論・コード等への一般化は別途検証が必要 [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- モデル規模は 1B〜16B で、より大規模（数百 B）への外挿は保証されない [source](../../sources/Post_Training/scaling-llm-finetuning.md)
- PET は prompt tuning / LoRA を対象とし、他の PEFT 手法（adapter, IA3 等）の挙動は別途検証が必要 [source](../../sources/Post_Training/scaling-llm-finetuning.md)
