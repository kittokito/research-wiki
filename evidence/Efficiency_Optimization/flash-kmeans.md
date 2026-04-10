---
source: src-flash-kmeans
date_extracted: 2026-04-07
---

# Flash-KMeans からの抽出

## 主要な主張
- K-meansのGPU実装ボトルネックはアルゴリズム的複雑性ではなくシステムレベル制約に起因 [source](../../sources/Efficiency_Optimization/flash-kmeans.md)
- FlashAssign: 距離計算とオンラインargminを融合し中間メモリ具体化を排除 [source](../../sources/Efficiency_Optimization/flash-kmeans.md)
- sort-inverse update: 高競合アトミック操作をセグメントレベル削減に変換 [source](../../sources/Efficiency_Optimization/flash-kmeans.md)

## 主要な貢献
- Flash-KMeans: GPUに最適化されたK-means実装
- FlashAssign + sort-inverse updateカーネル

## ベンチマーク

| ベンチマーク | スコア | 備考 |
|---|---|---|
| End-to-end speedup | 最大17.9× | vs既存GPU実装 |
| vs cuML/FAISS | 33-200× | NVIDIA H200 |

## 制限・注意点
- NVIDIA H200 GPUでの評価。他のGPUアーキテクチャでの性能は未確認
