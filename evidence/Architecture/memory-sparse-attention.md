---
source: src-memory-sparse-attention
date_extracted: 2026-04-07
---

# MSA: Memory Sparse Attention からの抽出

## 主要な主張
- 16Kから100Mトークンへのスケーリング時に最小限の性能劣化 [source](../../sources/Architecture/memory-sparse-attention.md)
- スパースアテンションとdocument-wise RoPEにより線形計算量を実現 [source](../../sources/Architecture/memory-sparse-attention.md)
- KVキャッシュ圧縮により消費者向けGPUで100Mトークン推論が可能 [source](../../sources/Architecture/memory-sparse-attention.md)
- マルチホップ推論に対応し、既存フロンティアモデルとRAGシステムを長文コンテキストベンチマークで凌駕 [source](../../sources/Architecture/memory-sparse-attention.md)

## 主要な貢献
- MSA: 100Mトークンまでスケーラブルなメモリモデル
- document-wise RoPE

## 制限・注意点
- 具体的なベンチマーク数値の詳細は要確認
