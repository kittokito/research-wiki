---
id: src-louvain-to-leiden
title: "From Louvain to Leiden: guaranteeing well-connected communities"
authors: ["Vincent A. Traag", "Ludo Waltman", "Nees Jan van Eck"]
year: 2019
url: "https://arxiv.org/abs/1810.08473"
type: paper
tags: [community-detection, graph-algorithm, Leiden, Louvain, modularity, network-analysis]
date_added: 2026-04-10
status: processed
---

# From Louvain to Leiden: guaranteeing well-connected communities

## 概要
ルーヴァン法（Louvain algorithm）によるコミュニティ検出には、コミュニティが疎結合や非連結になりうるという重大な欠陥がある（実験では最大25%が疎結合、16%が完全非連結）。ライデン法（Leiden algorithm）を提案し、連結コミュニティを保証し、反復適用により局所最適パーティションに収束することを証明。ルーヴァン法より高速に動作しつつ、ベンチマーク・実データともに優れたパーティション品質を達成する。

## メモ
cs.SI / physics.soc-ph。Leiden University / CWTS。Scientific Reports 9, 5233 (2019)。ライデン法の原論文。
