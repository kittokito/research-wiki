---
title: "Flash-KMeans: Fast and Memory-Efficient Exact K-Means"
aliases: ["Flash-KMeans"]
created: 2026-04-07
updated: 2026-04-07
tags: [k-means, GPU, optimization, efficiency]
sources: [src-flash-kmeans]
---

# Flash-KMeans: Fast and Memory-Efficient Exact K-Means

Yang, Xi, Zhao et al. (2026) — arXiv 2603.03329

## ソースからの事実
- GPU実装ボトルネックはシステムレベル制約に起因 [source](../../../sources/Efficiency_Optimization/flash-kmeans.md)
- FlashAssign + sort-inverse updateで最大17.9倍高速化、cuML/FAISSに対し33-200倍 [source](../../../sources/Efficiency_Optimization/flash-kmeans.md)

→ 詳細: [evidence](../../../evidence/Efficiency_Optimization/flash-kmeans.md)

## 現時点の解釈
FlashAttentionと同様のHBM最適化哲学をK-meansに適用。AIシステムにおけるK-meansのオンラインプリミティブ化は、ベクトル量子化やクラスタリングベースの手法の実用性を大幅に向上させる。Song Han labの成果。

## 関連ページ
- [TurboQuant](turboquant.md)

## 未解決の問い
- Flash-KMeansはTurboQuantなどの量子化手法と組み合わせ可能か？
