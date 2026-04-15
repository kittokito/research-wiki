---
id: src-geometry-of-forgetting
title: "The Geometry of Forgetting"
authors: ["Sambartha Ray Barman", "Andrey Starenky", "Sophia Bodnar", "Nikhil Narasimhan", "Ashwin Gopinath"]
year: 2026
url: "https://arxiv.org/abs/2604.06222"
type: paper
tags: [memory, forgetting, embedding, interference, false-memory, geometry, cosine-similarity, dimensionality]
date_added: 2026-04-14
status: processed
---

# The Geometry of Forgetting

## 概要
記憶現象（忘却、偽記憶、間隔効果、TOT現象）が生物学的ハードウェアではなく高次元埋め込み空間の幾何学的性質から生じることを示す。べき乗則忘却（b = 0.460 ± 0.183、人間 b ≈ 0.5）は時間減衰ではなく競合記憶間の干渉から発生。本番用埋め込みモデル（名目384〜1,024次元）は分散を約16有効次元に集中させ、干渉に脆弱な領域に位置する。未修正の事前学習済み埋め込みにcosine類似度を適用するだけでDRM偽記憶パラダイムを再現（偽警報率0.583、人間~0.55）。意味により情報を組織化し近接性で検索するあらゆるシステムに共通する「特徴」であると主張。

## メモ
- q-bio.NC, cs.AI, cs.IR, cs.NE。Sentra + MIT。
- 2026年3月公開。
- 5つの実験領域: 干渉による忘却、偽記憶（DRM）、間隔効果、TOT現象、クロスモーダル検索。
- RAGシステムやベクトルDBへの実用的示唆が大きい（vector averaging fallacyの指摘）。
