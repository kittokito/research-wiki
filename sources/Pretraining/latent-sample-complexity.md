---
id: src-latent-sample-complexity
title: "Learn from your own latents and not from tokens: A sample-complexity theory"
authors: ["Daniel J. Korchinski", "Alessandro Favero", "Matthieu Wyart"]
year: 2026
url: "https://arxiv.org/abs/2605.27734"
type: paper
peer_review: preprint
venue: ""
tags: [self-supervised-learning, sample-complexity, latent-prediction, PCFG, random-hierarchy-model, data2vec, JEPA, theory, compositional-data]
date_added: 2026-06-03
status: processed
---

# Learn from your own latents and not from tokens: A sample-complexity theory

## 概要
「なぜ自己の潜在表現を予測する SSL は、トークンを予測する学習よりデータ効率が良いのか」を理論的に解明した論文。自然言語・画像の合成的（compositional）構造を捉える **probabilistic context-free grammar (PCFG)**（深さ L の隠れシンボル木から可視トークン列を生成）を解析対象とし、**教師あり/トークンレベル SSL が隠れ木の復元に L について指数的なサンプルを要する**のに対し、**latent prediction は（対数因子を除き）L について定数のサンプルで達成できる**ことを証明する。さらに data2vec の初のサンプル複雑度解析を与え、data2vec が**暗黙的に階層的 latent 予測を行っている**ことを示し、H-JEPA のような明示的階層スタックは**ほぼ冗長**だと示唆する。

## メモ
arXiv 2605.27734、v1 2026-05-26。本文10ページ + appendix（計28ページ）。著者の Favero・Wyart は compositional data の **Random Hierarchy Model (RHM)** 系の研究系譜。
検証は (i) 階層的クラスタリングアルゴリズム、(ii) 各レベルで勾配降下により自己の latent を予測する predictor-clusterer ネットワーク、(iii) data2vec のサンプル複雑度解析、の3実装で行う。
[data2vec](../../wiki/papers/Pretraining/data2vec.md) の理論的説明であり、[V-JEPA 2](../../wiki/papers/Physical_AI/v-jepa-2.md) / [LeWM](../../wiki/papers/Physical_AI/leworldmodel.md) など JEPA 系の predictive SSL とも直結。
