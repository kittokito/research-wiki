---
title: "MSA: Memory Sparse Attention"
aliases: ["MSA"]
created: 2026-04-07
updated: 2026-04-07
tags: [sparse-attention, long-context, 100M-tokens, architecture]
sources: [src-memory-sparse-attention]
---

# MSA: Memory Sparse Attention

Chen, Chen, Yi et al. (2026) — arXiv 2603.23516

## ソースからの事実
- 16Kから100Mトークンへのスケーリング時に最小限の性能劣化 [source](../../../sources/Architecture/memory-sparse-attention.md)
- スパースアテンションとdocument-wise RoPEにより線形計算量を実現 [source](../../../sources/Architecture/memory-sparse-attention.md)
- 消費者向けGPUで100Mトークン推論が可能 [source](../../../sources/Architecture/memory-sparse-attention.md)

→ 詳細: [evidence](../../../evidence/Architecture/memory-sparse-attention.md)

## 現時点の解釈
100Mトークンコンテキストは現在のフロンティアモデルの1M程度のコンテキスト長を2桁拡張するもの。消費者向けGPUでの推論を可能にするKVキャッシュ圧縮が実用面で重要。

## 関連ページ
- なし

## 未解決の問い
- 100Mトークンでの実用的なユースケースは？
- RAGとの性能比較の詳細は？
