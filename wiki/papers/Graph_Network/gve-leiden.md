---
title: "GVE-Leiden: Fast Leiden Algorithm for Community Detection"
aliases: ["GVE-Leiden", "Fast Leiden Shared Memory"]
created: 2026-04-23
updated: 2026-04-23
tags: [community-detection, graph-algorithm, Leiden, parallel-computing, shared-memory, HPC, multicore]
peer_review: workshop
venue: "ICPP 2024 Workshops"
sources: [src-gve-leiden]
---

# GVE-Leiden: Fast Leiden Algorithm for Community Detection in Shared Memory Setting

> **査読**: 📋 workshop — ICPP 2024 Workshops

Sahu, Kothapalli, Banerjee (2024) — IIIT Hyderabad / DOI 10.1145/3673038.3673146 / arXiv 2312.13936

## ソースからの事実
- dual 16-core Intel Xeon Gold 6226R（計32コア）単一サーバー上で、既存Leiden実装に対し大差で勝利 [source](../../../sources/Graph_Network/gve-leiden.md):
  - オリジナル Leiden 比 **436×**
  - igraph Leiden 比 **104×**
  - NetworKit Leiden 比 **8.2×**
  - **cuGraph Leiden（NVIDIA A100 GPU）比 3.0×**
- **403M edges/s** @ 3.8B エッジグラフ [source](../../../sources/Graph_Network/gve-leiden.md)
- スレッド数倍増ごと平均 **1.6×** のスケーリング [source](../../../sources/Graph_Network/gve-leiden.md)

→ 詳細: [evidence](../../../evidence/Graph_Network/gve-leiden.md)

## 現時点の解釈
[louvain-to-leiden](./louvain-to-leiden.md)（Traag et al., 2019）がライデン法というアルゴリズムの原論文であるのに対し、本論文は **「同じアルゴリズムを並列実行したときに実装でどこまで速くなるか」** の実装側SOTAを示す位置付け。両論文は直交する価値（アルゴリズム vs エンジニアリング）を持つ。

最も強い主張は **「32コアCPU実装が NVIDIA A100 GPU 実装（cuGraph Leiden）を3.0倍上回る」** という結果。GPU優位が自明視されがちな並列グラフアルゴリズムで、共有メモリ・CPU最適化が依然として十分な余地を持つことを示唆する。ただしこれは「CPUが本質的に有利」ではなく **cuGraph実装の成熟度が低かった可能性** を含むため、結論としては「ライデン法のGPU最適化はまだ十分ではない」と読むのが妥当。

**igraph/NetworKit 比 8〜100倍** の差は、日常的にPython/Rでライデン法を使うユーザーに実用的インパクトが大きい。30億エッジ規模の解析が単一サーバーで現実的になる（数分〜数十分オーダー）ことで、LLM 応用（[karpathy-tweet](../Press_Releases/karpathy-tweet.md) の wiki構築ワークフロー等でのドキュメントクラスタリング）やログ解析・ソーシャルネットワーク解析でのLeiden法の採用障壁が下がる。

ICPP 2024 **Workshops** 採択（メインプロシーディングではなく併設ワークショップ）。ベンチマーク中心のテクニカルレポート色が強く、アルゴリズム的新規性よりエンジニアリング貢献が主。

## 関連ページ
- [From Louvain to Leiden](./louvain-to-leiden.md) — ライデン法の原論文、本論文はその並列実装SOTA
- [Karpathy Wiki Workflow](../Press_Releases/karpathy-tweet.md) — ドキュメントクラスタリングとしてのコミュニティ検出応用文脈

## 未解決の問い
- cuGraph Leiden（A100）の3.0倍差は cuGraph 実装の最適化で縮まるか、それともアルゴリズム構造上GPUに不利なのか？
- 1.6×/倍化 のスケーリングは 64/128/256コアでも維持されるか？メモリ帯域・cache coherence のボトルネック位置は？
- 分散メモリ（複数ノード、MPI）実装へ拡張したとき、3.8Bエッジ超の規模でも同じ実装原理が効くか？
- グラフ構造（スケールフリー性、コミュニティサイズ分布、直径）で相対高速化倍率はどう変わるか？
- 同じ高速化アプローチは Louvain / Label Propagation / InfoMap / Spectral 等の他のコミュニティ検出アルゴリズムに移植可能か？
