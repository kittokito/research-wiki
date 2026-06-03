---
source: src-bert-rediscovers-nlp-pipeline
date_extracted: 2026-06-03
---

# BERT Rediscovers the Classical NLP Pipeline からの抽出

## 主要な主張
- BERT は **古典的 NLP パイプラインの各ステップを解釈可能・局在的（localizable）に表現**している [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- 各ステップを担う層は**期待される順序**で現れる: **POS タグ付け → 構文（constituents/dependencies）→ 固有表現認識（NER）→ 意味役割（SRL）→ 照応解析（coreference）** [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- 下位層に表層・統語的タスク、上位層に意味的タスクが集中する（syntactic-then-semantic） [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- BERT は厳密なフィードフォワードではなく、**上位層の文脈で下位の決定を見直す「動的パイプライン」**的挙動を示す（曖昧性解消など） [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)

## 手法
- **edge probing**（Tenney et al. 2019 のスイート）を BERT の各層に拡張し、層ごとに各言語タスクの解ける度合いを測定 [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- 2つの指標:
  - **center-of-gravity / expected layer**: スカラー混合重みから、各タスクの情報がどの層に集中しているかを測る
  - **cumulative scoring**: 各層が新たに加える性能寄与（どの層で情報が立ち上がるか）を測る [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- BERT-base / BERT-large で分析 [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)

## 制限・注意点
- probing は「情報が表現に存在する」ことを示すが、「モデルがそれを実際に使っている」ことの直接証明ではない [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- 層順序の主張は probe の設計・指標に依存しうる（後続の再検証 [Does BERT Rediscover...](../../sources/Pretraining/does-bert-rediscover-nlp-pipeline.md) が指摘） [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
- BERT（encoder, 2019）に関する知見であり、現代の decoder-only LLM への直接の一般化は別途検証が必要 [source](../../sources/Pretraining/bert-rediscovers-nlp-pipeline.md)
