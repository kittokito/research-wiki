---
source: src-sft-data-composition
date_extracted: 2026-06-03
---

# How Abilities in LLMs are Affected by SFT Data Composition からの抽出

## 主要な主張
- **3能力はスケーリング特性が異なる**: 数学推論・コード生成はデータ量とともに単調に向上、**一般能力（指示追従）は約1,000サンプルで頭打ち（plateau）** [source](../../sources/Post_Training/sft-data-composition.md)
- **データ量 > 混合比**: 性能はデータ構成比よりもデータ量に強く影響される [source](../../sources/Post_Training/sft-data-composition.md)
- **低リソース vs 高リソースで混合効果が反転**: データ量が少ないときは混合（data composition）が各能力を底上げするが、データ量が多いときは能力間が **競合（conflict）** する [source](../../sources/Post_Training/sft-data-composition.md)
- **逐次学習は catastrophic forgetting を招く**: 複数スキルを順番に学習すると先に獲得した能力を忘却する [source](../../sources/Post_Training/sft-data-composition.md)
- **モデルが大きいほど低リソース設定での gain が大きい**（特に math と general 能力） [source](../../sources/Post_Training/sft-data-composition.md)

## 評価設定
- **数学推論**: ベンチマーク GSM8K
- **コード生成**: ベンチマーク HumanEval
- **一般能力（human alignment）**: ベンチマーク MT-Bench
- **ベースモデル**: LLaMA 系（7B / 13B / 33B）でモデルサイズの影響も検証 [source](../../sources/Post_Training/sft-data-composition.md)

## 提案手法: DMT（Dual-stage Mixed Fine-tuning）
- **動機**: multi-task（同時学習）は能力間 conflict、sequential（逐次学習）は catastrophic forgetting を起こす。両者の良いとこ取りを狙う [source](../../sources/Post_Training/sft-data-composition.md)
- **Stage 1**: 専門データ（数学・コードなどの specialized data）で学習し専門能力を獲得 [source](../../sources/Post_Training/sft-data-composition.md)
- **Stage 2**: 一般データ（general/alignment data）に、**専門データの一部を比率 k で混ぜて**学習。小さな k の専門データ混合が忘却を防ぐ [source](../../sources/Post_Training/sft-data-composition.md)
- **key idea**: スケーリング特性の異なる能力を、専門→（少量混合つき）一般 の順で学習することで、専門能力を保持しつつ一般能力を伸ばす [source](../../sources/Post_Training/sft-data-composition.md)

## 効果
- DMT は SFT フェーズの **性能 conflict と catastrophic forgetting の両方を緩和**し、一般能力と専門能力のバランスを達成 [source](../../sources/Post_Training/sft-data-composition.md)
- 同時学習・逐次学習のいずれの単純戦略よりも、専門能力を保ちながら一般能力を両立できる [source](../../sources/Post_Training/sft-data-composition.md)

## 制限・注意点
- 対象は SFT 段階のみ（RLHF/DPO 等の後続段階は本研究のスコープ外） [source](../../sources/Post_Training/sft-data-composition.md)
- 能力は math / code / general の3軸に限定。他の能力（多言語・長文脈・安全性等）への一般化は別途検証が必要 [source](../../sources/Post_Training/sft-data-composition.md)
- 混合比 k の最適値はデータ量・モデルサイズに依存し、単一の推奨値ではない [source](../../sources/Post_Training/sft-data-composition.md)
