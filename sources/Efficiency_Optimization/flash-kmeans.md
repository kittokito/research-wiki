---
id: src-flash-kmeans
title: "Flash-KMeans: Fast and Memory-Efficient Exact K-Means"
authors: ["Shuo Yang", "Haocheng Xi", "Yilong Zhao", "Muyang Li", "Xiaoze Fan", "Jintao Zhang", "Han Cai", "Yujun Lin", "Xiuyu Li", "Kurt Keutzer", "Song Han", "Chenfeng Xu", "Ion Stoica"]
year: 2026
url: "https://arxiv.org/abs/2603.03329"
type: paper
peer_review: preprint
venue: ""
tags: [k-means, GPU, optimization, FlashAssign, HBM, CUDA]
date_added: 2026-04-07
status: processed
---

# Flash-KMeans: Fast and Memory-Efficient Exact K-Means

## 概要
K-meansをオフライン処理ツールからオンラインプリミティブとして再考。GPU実装のボトルネックがアルゴリズム的複雑性ではなくシステムレベルの制約に起因することを特定。FlashAssignで距離計算とオンラインargminを融合し中間メモリ具体化を排除、sort-inverse updateで高競合のアトミック操作を効率的なセグメントレベル削減に変換。NVIDIA H200で最大17.9倍のエンドツーエンド高速化、cuML/FAISSに対し33-200倍の改善。

## メモ
cs.DC。MIT / UC Berkeley / NVIDIA。2026年3月公開。Song Han lab。
