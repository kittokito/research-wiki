---
title: "mHC: Manifold-Constrained Hyper-Connections"
aliases: ["mHC"]
created: 2026-04-07
updated: 2026-04-07
tags: [residual-connection, hyper-connections, manifold, architecture]
peer_review: preprint
venue: ""
sources: [src-manifold-constrained-hyper-connections]
---

# mHC: Manifold-Constrained Hyper-Connections

> **査読**: 📝 preprint

Xie, Wei, Cao et al. (2025) — arXiv 2512.24880

## ソースからの事実
- HCは残差ストリーム幅拡張と接続パターン多様化で性能向上するが恒等写像特性を破壊 [source](../../../sources/Architecture/manifold-constrained-hyper-connections.md)
- mHCはHCの残差接続空間を多様体に射影して恒等写像特性を復元 [source](../../../sources/Architecture/manifold-constrained-hyper-connections.md)
- 大規模学習での有効性と優れたスケーラビリティを実証 [source](../../../sources/Architecture/manifold-constrained-hyper-connections.md)

→ 詳細: [evidence](../../../evidence/Architecture/manifold-constrained-hyper-connections.md)

## 現時点の解釈
DeepSeek関連著者陣による研究。HCの問題点（学習不安定性、スケーラビリティ制限）を理論的に正しい方法で解決。恒等写像特性の復元は学習安定性の観点から理論的に重要。

## 関連ページ
- [DeepCrossAttention](deep-cross-attention.md)
- [Attention Residuals](attention-residuals.md)
- [Conditional Memory](conditional-memory-scalable-lookup.md)

## 未解決の問い
- mHCとDCAの組み合わせは有効か？
- DeepSeekの次世代モデルでの採用は？
