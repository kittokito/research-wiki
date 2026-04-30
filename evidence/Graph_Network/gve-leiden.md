---
source: src-gve-leiden
date_extracted: 2026-04-23
---

# GVE-Leiden (Sahu, Kothapalli, Banerjee, 2024) からの抽出

## 主要な主張
- ライデン法（Leiden）は高品質なコミュニティ検出アルゴリズムだが、大規模グラフでの並列実装の効率は依然として課題 [source](../../sources/Graph_Network/gve-leiden.md)
- **GVE-Leiden** は共有メモリ設定でのライデン法の **最も効率的な実装の1つ** として提案された [source](../../sources/Graph_Network/gve-leiden.md)
- 計測環境: dual 16-core Intel Xeon Gold 6226R（計32コア）の単一サーバー [source](../../sources/Graph_Network/gve-leiden.md)
- **オリジナル Leiden 実装に対し 436倍高速** [source](../../sources/Graph_Network/gve-leiden.md)
- **igraph Leiden に対し 104倍高速** [source](../../sources/Graph_Network/gve-leiden.md)
- **NetworKit Leiden に対し 8.2倍高速** [source](../../sources/Graph_Network/gve-leiden.md)
- **cuGraph Leiden（NVIDIA A100 GPU上）に対し 3.0倍高速** — CPU実装が最新GPU実装を上回る [source](../../sources/Graph_Network/gve-leiden.md)
- 3.8Bエッジのグラフで **403M edges/s** の処理速度を達成 [source](../../sources/Graph_Network/gve-leiden.md)
- スレッド数を倍増するごとに **平均1.6倍** のスケーリング（スレッドスケーラビリティ）[source](../../sources/Graph_Network/gve-leiden.md)

## 主要な貢献
- ライデン法の共有メモリ並列化における SOTA 実装
- GPU実装（cuGraph on A100）を超える性能を CPU（32コア）で達成したという事実
- スレッド倍化ごとに ~1.6倍の継続的スケーリング（実用的な multi-core scaling）
- 30億エッジ級の実グラフでの運用品質データ

## ベンチマーク結果
| 比較対象 | 高速化倍率 | 備考 |
|---|---|---|
| オリジナル Leiden | 436× | リファレンス実装 |
| igraph Leiden | 104× | R/Python 人気実装 |
| NetworKit Leiden | 8.2× | 並列化志向の実装 |
| cuGraph Leiden | 3.0× | NVIDIA A100 GPU上で実行 |

| 項目 | 値 |
|---|---|
| 処理速度 | 403M edges/s |
| 対象グラフ | 3.8B edges |
| スレッドスケーリング | 平均 1.6×/倍化 |
| ハードウェア | dual 16-core Intel Xeon Gold 6226R（32コア） |

## 制限・注意点
- 比較対象の実装バージョン・パラメータ依存性あり（特に cuGraph Leiden のバージョンで結果が変わりうる）
- 単一マシン・共有メモリ設定の結果で、分散メモリ・大規模クラスタへの直接外挿は不可
- 403M edges/s という単一数値は個別グラフ（3.8B edges 特定データセット）のもの。グラフ構造（スケールフリー性、直径、コミュニティサイズ分布）で性能が変動する可能性
- 「コミュニティ検出の品質（modularity等）」の対等性検証は論文内で言及されるが、"同品質での速度比較" の強度は原文要確認
- 「CPU vs GPU」比較はアルゴリズム実装の最適化度合いに大きく依存し、「CPUが本質的に有利」という結論は早計（cuGraph が実装として未成熟だった可能性）
- 1.6×/倍化 は superlinear ではないが、32コアで実用的なスケーリング。256コア以上で同じ傾きが維持されるかは外挿

## 実装関連
- DOI: 10.1145/3673038.3673146
- arXiv 2312.13936 / v1: 2023-12-21 / v8: 2024-07-06
- arXiv admin note: 2312.04876（おそらく GVE-Louvain 系列の先行論文）と大幅テキスト重複
- Proceedings of the 53rd ICPP Workshops (2024)
- IIIT Hyderabad（推定）
