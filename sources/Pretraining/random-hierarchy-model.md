---
id: src-random-hierarchy-model
title: "How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model"
authors: ["Leonardo Petrini", "Francesco Cagnetta", "Umberto M. Tomasini", "Alessandro Favero", "Matthieu Wyart"]
year: 2023
url: "https://arxiv.org/abs/2307.02129"
type: paper
peer_review: accepted
venue: "Physical Review X 14, 031001 (2024)"
tags: [random-hierarchy-model, compositional-data, sample-complexity, hierarchical-representation, PCFG, feature-learning, curse-of-dimensionality, EPFL]
date_added: 2026-06-03
status: processed
---

# How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model

## 概要
深層ネットが高次元タスクを少数例から学べるのはなぜか、を解析するための合成タスク族 **Random Hierarchy Model (RHM)** を提案した理論論文。RHM は言語・画像の階層構造に着想した PCFG 的生成モデルで、各クラスが高レベル特徴のグループに対応し、各特徴がさらに下位特徴のグループに（深さ L にわたり再帰的に）対応する。各シンボルは **multiplicity m** 個の同義（synonymic）な下位表現を持つ。中心的結果は、深い CNN がこのタスクを学ぶのに必要な**サンプル複雑度が P\* = n_c · m^L**（n_c=クラス数）であり、これは入力次元 d = s^L（s=branching factor）に対して**多項式**で、次元の呪いを回避すること。学習は「同義グループの交換に対して不変な内部表現」を段階的に構築することで進み、その閾値は低レベル特徴とクラスの相関がサンプリングノイズを超えて検出可能になる点と一致する。

## メモ
arXiv 2307.02129、v1 2023-07 / **Physical Review X 14, 031001 (2024) に掲載**。著者は EPFL（Wyart 研、統計物理 × 深層学習理論の系譜）。
[Learn from your own latents（サンプル複雑度理論）](../../wiki/papers/Pretraining/latent-sample-complexity.md) や [言語構造の獲得理論](../../wiki/papers/Pretraining/language-structure-acquisition.md) の基盤となる RHM の原論文。[data2vec](../../wiki/papers/Pretraining/data2vec.md) の latent 予測がなぜ効くかの理論的背景でもある。
