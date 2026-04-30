---
title: "Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches"
aliases: ["Memory-Efficient Community Detection", "Weighted MG Sketches for Community Detection"]
created: 2026-04-27
updated: 2026-04-27
tags: [community-detection, graph-algorithm, Louvain, Leiden, LPA, Misra-Gries, sketch, memory-efficiency, parallel-computing, shared-memory, multicore]
peer_review: preprint
venue: ""
sources: [src-memory-efficient-cd-sketches]
---

# Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches

> **査読**: 📝 preprint — arXiv 2411.02268 (v3 2025-01-30)

Sahu (2024) — IIIT Hyderabad / arXiv 2411.02268

## ソースからの事実
- 共有メモリ並列の Louvain / Leiden / LPA は **per-thread hashtable** が `8T|V|〜16T|V|` バイト規模に膨らみ、100M頂点 × 64スレッドで **51.2〜102.4 GB** に達する（メモリ律速）[source](../../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- 提案: **weighted Misra-Gries sketch** による hashtable 置換 — sketch サイズはグラフサイズに依存せず ~0.5KB 以下/sketch [source](../../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- 品質劣化（modularity）: Louvain **≤1%** / Leiden **0.8%** / LPA ほぼゼロ [source](../../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- ランタイムオーバーヘッド: MG8 Louvain **1.48×**（web平均 2.07×）/ MG64 Leiden **3.15×** / MG8 LPA **2.11×**（web/social平均 2.78×）[source](../../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- 評価: dual 16-core Xeon Gold 6226R（32コア）+ 376GB RAM、64スレッド、SuiteSparse 13グラフ（最大3.8Bエッジ）[source](../../../sources/Graph_Network/memory-efficient-cd-sketches.md)
- Misra-Gries パラメータ: k=8（Louvain/LPA）/ k=64（Leiden）[source](../../../sources/Graph_Network/memory-efficient-cd-sketches.md)

→ 詳細: [evidence](../../../evidence/Graph_Network/memory-efficient-cd-sketches.md)

## 現時点の解釈
**著者は [GVE-Leiden](./gve-leiden.md) と同一の Subhajit Sahu（IIIT Hyderabad）**。GVE-Leiden が「並列ライデン法の **速度SOTA**」だったのに対し、本論文は **「同じ著者が hashtable を sketch に置き換えてメモリ側のスケーラビリティを取りに行った」follow-up** と読むのが妥当。両者は速度⇄メモリのトレードオフ軸の対極を埋める関係。

最も強いポイントは **「メモリ要求がグラフサイズに依存しなくなる」** こと。従来は |V| が増えるほど per-thread hashtable が肥大し、コア数を増やすほどメモリが線形に膨張する設計（実用上の上限を作る）。Misra-Gries スケッチ化により、**コア数 × 頂点数のスケーリング軸でメモリが切り離される**ため、超大規模グラフ（10B+ エッジ）や高並列環境（128+ スレッド）への上限を物理メモリではなく計算予算側で律速できる。

ただしランタイム 1.5〜3.2× の劣化は無視できない。**メモリ制約が真のボトルネックである場面**（メモリ枯渇でスワップが発生、または1ノードに収まらず分散実装の検討が必要）でこそ意味があり、ランタイム最優先なら GVE-Leiden 系の hashtable 実装の方が実用的。「メモリ予算を捨てて速度を取るか、速度を一定譲ってメモリを取るか」の選択肢を提供する位置付けに近い。

Leiden で k=64 と他より大きい sketch を使う点は、**Leiden の精製ステップ（refinement phase）で隣接コミュニティとの結合度比較が密になる**性質と整合的。逆に LPA は最頻ラベルだけ追えればよいので k=8 で済み、k に対する感度がアルゴリズムの内部構造を反映している。

preprint段階（2025-01-30 v3まで）。venue採択が未確認のため、結果の独立検証はまだ薄い。

## 関連ページ
- [GVE-Leiden: Fast Leiden in Shared Memory](./gve-leiden.md) — 同著者の速度SOTA。本論文はメモリ側のSOTAとして相補
- [From Louvain to Leiden](./louvain-to-leiden.md) — ライデン法原論文、本論文の評価対象アルゴリズムの一つ

## 未解決の問い
- ランタイム 1.5〜3.2× の劣化は **アルゴリズム的最適化（ベクトル化、局所性改善）** や **sketch 構造の最適化** でどこまで縮められるか？
- 64スレッドを超える領域（128/256スレッド、NUMAをまたぐ環境）で、メモリ削減とランタイムの両者は同じ傾きを保つか？
- 同じ sketch 化アプローチは **GVE-Leiden の高速実装** に直接組み込んで「速度SOTA かつメモリ非依存」を達成可能か？
- weighted Misra-Gries の **誤差バウンド（ε vs k）** は modularity 損失とどう対応するか？理論保証と実測 1% の関係は？
- 13グラフでの平均的傾向だが、**bipartite graph・citation network・通信ネットワーク** 等の構造特性が異なるグラフでも同じ品質劣化幅で済むか？
- Leiden が k=64 必要な理由は精製ステップの構造に内在するか、実装上のチューニングで k を下げられるか？
- 分散メモリ（複数ノード、MPI）に拡張した場合、ノード間通信での sketch のマージ操作はどの程度効率化可能か？
