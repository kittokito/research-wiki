---
id: src-gve-leiden
title: "GVE-Leiden: Fast Leiden Algorithm for Community Detection in Shared Memory Setting"
authors: ["Subhajit Sahu", "Kishore Kothapalli", "Dip Sankar Banerjee"]
year: 2024
url: "https://arxiv.org/abs/2312.13936"
type: paper
peer_review: workshop
venue: "ICPP 2024 Workshops"
tags: [community-detection, graph-algorithm, Leiden, parallel-computing, shared-memory, HPC, multicore]
date_added: 2026-04-23
status: processed
---

# GVE-Leiden: Fast Leiden Algorithm for Community Detection in Shared Memory Setting

## 概要
ライデン法（Leiden algorithm）の共有メモリ並列計算向け高速実装 **GVE-Leiden** を提案したテクニカルレポート。dual 16-core Intel Xeon Gold 6226R（計32コア）の単一サーバー上で、既存実装に対し大差で勝利:
- オリジナル Leiden 実装比 **436倍**
- igraph Leiden 比 **104倍**
- NetworKit Leiden 比 **8.2倍**
- **cuGraph Leiden（NVIDIA A100 GPU）比 3.0倍**
3.8Bエッジのグラフで **403M edges/s** の処理速度。スレッド数を倍増するごとに平均1.6倍のスケーリング。CPU実装がGPU実装（A100）を上回る稀な事例。

## メモ
cs.DC / cs.PF。DOI: 10.1145/3673038.3673146（ACM Proceedings of the 53rd ICPP Workshops 2024）。IIIT Hyderabad 系。GVE-* シリーズ（GVE-Louvain, GVE-Leiden 等）の一部。既存の [louvain-to-leiden](./louvain-to-leiden.md)（アルゴリズム原論文）に対し、本論文は **実装側の最前線** を示す。arXiv v1: 2023-12-21、v8: 2024-07-06。arXiv メタデータは著者を Sahu 1名表記だが、ACM proceedings では Sahu / Kothapalli / Banerjee の3名（Semantic Scholar確認）— published版の著者リストを採用。arXiv admin note: 2312.04876 と大幅テキスト重複（おそらく先行GVE-Louvainとの統合説明）。
