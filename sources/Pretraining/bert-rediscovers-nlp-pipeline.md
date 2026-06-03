---
id: src-bert-rediscovers-nlp-pipeline
title: "BERT Rediscovers the Classical NLP Pipeline"
authors: ["Ian Tenney", "Dipanjan Das", "Ellie Pavlick"]
year: 2019
url: "https://arxiv.org/abs/1905.05950"
type: paper
peer_review: accepted
venue: "ACL 2019"
tags: [BERT, probing, edge-probing, interpretability, NLP-pipeline, layer-analysis, linguistic-structure, representation]
date_added: 2026-06-03
status: processed
---

# BERT Rediscovers the Classical NLP Pipeline

## 概要
BERT の各層が何を計算しているかを **edge probing** で解析し、**古典的 NLP パイプライン（POS タグ付け → 構文解析 → 固有表現認識 → 意味役割 → 照応解析）の各ステップが、期待される順序で層に局在する**ことを示した解釈研究。下位層に表層・統語的タスク、上位層に意味的タスクが現れる。2種類の指標——情報が集中する層を測る **center-of-gravity（expected layer）** と、各層が新たに加える寄与を測る **cumulative scoring**——を用いる。さらに、BERT は厳密なフィードフォワードではなく、**上位層の文脈情報で下位の決定を見直す「動的パイプライン」**的挙動も示す。

## メモ
arXiv 1905.05950、**ACL 2019 採択**（P19-1452, pp.4593-4601）。著者は Google（Tenney, Das）× Brown 大（Pavlick）。
edge probing は Tenney et al. 2019「What do you learn from context?」のスイートを各層に拡張したもの。
再検証論文 [Does BERT Rediscover a Classical NLP Pipeline?](../../wiki/papers/Pretraining/does-bert-rediscover-nlp-pipeline.md)（Niu et al., COLING 2022）と対をなす。深層ネットのどこに言語構造が宿るかという点で [言語構造の獲得理論](../../wiki/papers/Pretraining/language-structure-acquisition.md)（Cagnetta & Wyart）の経験的対応物。
