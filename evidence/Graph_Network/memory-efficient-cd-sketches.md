---
source: src-memory-efficient-cd-sketches
date_extracted: 2026-04-27
---

# Memory-Efficient Community Detection (Sahu, 2024) からの抽出

## 主要な主張
- 既存の Louvain / Leiden / LPA の並列実装は、衝突回避のためスレッドごとに巨大な hashtable を確保しており、メモリが律速要因になる [source](../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- スレッドあたりのハッシュテーブルは **8T|V|〜16T|V| バイト規模**（T=スレッド数, |V|=頂点数）。100M 頂点 × 64 スレッドで **51.2〜102.4 GB** に達する [source](../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- 提案: **weighted Misra-Gries sketch** で hashtable を置き換える（per-thread でスケッチ ~0.5KB 以下、グラフサイズに依存しない）[source](../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- Louvain における品質劣化は **modularity で ≤1%**、Leiden で **0.8%**、LPA でほぼ default 同等 [source](../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- ランタイムオーバーヘッド: MG8 Louvain **1.48×**（web平均 2.07×）/ MG64 Leiden **3.15×** / MG8 LPA **2.11×**（web/social平均 2.78×）[source](../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- Misra-Gries の k パラメータ: **k=8**（Louvain / LPA）, **k=64**（Leiden）[source](../../sources/Graph_Network/memory-efficient-cd-sketches.md)

## 主要な貢献
- 重み付き Misra-Gries スケッチによる per-thread hashtable 置換という設計レシピ
- Louvain / Leiden / LPA の3アルゴリズムへの一括適用
- 13グラフ（SuiteSparse Matrix Collection、最大3.80Bエッジ）での実証評価
- メモリ・品質・ランタイムの3軸トレードオフの定量提示

## ベンチマーク結果

### メモリ削減
| 環境 | hashtable | weighted MG sketch |
|---|---|---|
| 100M 頂点 × 64 スレッド | 51.2〜102.4 GB | ~0.5 KB / sketch（実質ゼロ近傍） |
| メモリ依存性 | 8T|V|〜16T|V| | グラフサイズ非依存 |

### 品質と速度（提案 vs 既存実装）
| アルゴリズム | k | modularity 劣化 | ランタイムオーバーヘッド | web/social 平均 |
|---|---|---|---|---|
| Louvain (MG8) | 8 | ≤1% | 1.48× | 2.07× |
| Leiden (MG64) | 64 | 0.8% | 3.15× | — |
| LPA (MG8) | 8 | ほぼゼロ | 2.11× | 2.78× |

### 評価環境
| 項目 | 値 |
|---|---|
| ハードウェア | dual 16-core Intel Xeon Gold 6226R（32コア / 2.90 GHz） |
| メモリ | 376 GB RAM |
| スレッド数 | 64（全実験共通） |
| グラフ数 | 13（SuiteSparse Matrix Collection） |
| グラフサイズ範囲 | 3.07M-214M 頂点 / 25.4M-3.80B エッジ |
| グラフ種別 | web graphs（7）/ social networks（2）/ road networks（2）/ protein k-mer（2） |

## 制限・注意点
- ランタイムオーバーヘッドは無視できない（特に Leiden で 3.15×、web Louvain で 2× 超）。**メモリ制約が律速のときに使うトレードオフ**であって、速度を求める場面では [GVE-Leiden](./gve-leiden.md)（同著者）等の hashtable 実装が依然有利
- Leiden で k=64 が必要なのは、Leiden の精製ステップで多数の隣接コミュニティとの結合度を比較する必要があるためと推察される（k=8 では品質崩壊の可能性、論文内で要確認）
- 品質劣化「≤1%」は modularity 評価値であって、コミュニティ構造の詳細（NMI、ARI、クラスタサイズ分布等）の対等性は別軸
- 64スレッド・単一サーバー設定の結果。**128/256スレッド** や **NUMA をまたぐ高スレッド数領域** で同じ品質・性能トレードオフが成立するかは外挿
- 13グラフでテスト範囲は限定的。**通信ネットワーク・citation graph・bipartite graph** 等の構造で挙動が変わる可能性
- weighted Misra-Gries の理論保証（誤差 ε と sketch サイズ k の関係）はクラシック Misra-Gries の重み付き拡張に依拠するが、本論文での誤差バウンド導出の厳密度は要確認
- venue 採択情報なし（2025-01時点 v3、arXiv のみ）

## 実装関連
- arXiv 2411.02268 / v1 2024-11-04 / v2 2024-11-06 / v3 2025-01-30
- 15ページ / 12図 / 1表 / CC BY-NC-SA 4.0
- IIIT Hyderabad（Professor CR Rao Rd, Gachibowli, Hyderabad, Telangana, India 500032）
- 同著者の関連論文: [GVE-Leiden](./gve-leiden.md)（速度SOTA）、GVE-Louvain（先行実装）
- 評価対象アルゴリズム: Louvain / Leiden / Label Propagation Algorithm（LPA）
- 評価データ: SuiteSparse Matrix Collection 13 graphs
