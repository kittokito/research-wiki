---
id: src-memory-efficient-cd-sketches
title: "Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches"
authors: ["Subhajit Sahu"]
year: 2024
url: "https://arxiv.org/abs/2411.02268"
type: paper
peer_review: preprint
venue: ""
tags: [community-detection, graph-algorithm, Louvain, Leiden, LPA, Misra-Gries, sketch, memory-efficiency, parallel-computing, shared-memory, multicore]
date_added: 2026-04-27
status: processed
---

# Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches

## 概要
コミュニティ検出（Louvain / Leiden / Label Propagation Algorithm: LPA）の共有メモリ並列実装で支配的になる **per-thread hashtable** を、**weighted Misra-Gries sketch**（重み付き頻度近似データ構造）で置き換える提案。Louvain では衝突回避のため `8T|V|〜16T|V|` バイト規模のハッシュテーブルが必要だが、これをスレッドあたり ~0.5KB 以下のスケッチに置換する。**100M頂点 × 64スレッドで 51.2〜102.4 GB のメモリが事実上ゼロ近傍まで削減**。品質劣化は ≤1%（Louvain）/ 0.8%（Leiden）/ ほぼゼロ（LPA）に抑え、ランタイムは Louvain 1.48×（avg 2.07× on web）、Leiden 3.15×、LPA 2.11×（avg 2.78× on web/social）。

## メモ
cs.SI / cs.DC。IIIT Hyderabad（Professor CR Rao Rd, Gachibowli, Hyderabad）。著者は [GVE-Leiden](./gve-leiden.md) と同一の Subhajit Sahu。GVE-Leiden が **速度SOTA** を示したのに対し、本論文は **メモリスケーラビリティ** に攻め所を移した follow-up に当たる位置付け。13グラフ（SuiteSparse Matrix Collection）/ 3.07M-214M 頂点 / 25.4M-3.80B エッジ / dual 16-core Xeon Gold 6226R（32コア）+ 376GB RAM。Misra-Gries 重み付き拡張で k=8（Louvain/LPA）/ k=64（Leiden）。arXiv v1: 2024-11-04 / v2: 2024-11-06 / v3: 2025-01-30。preprint（venue採択は未確認、2025-01時点で arXiv のみ）。
