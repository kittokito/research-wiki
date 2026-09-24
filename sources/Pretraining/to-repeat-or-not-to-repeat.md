---
id: src-to-repeat-or-not-to-repeat
title: "To Repeat or Not To Repeat: Insights from Scaling LLM under Token-Crisis"
authors: ["Fuzhao Xue", "Yao Fu", "Wangchunshu Zhou", "Zangwei Zheng", "Yang You"]
year: 2023
url: "https://arxiv.org/abs/2305.13230"
type: paper
peer_review: accepted
venue: "NeurIPS 2023 (Poster)"
tags: [token-crisis, data-repetition, multi-epoch-degradation, overfitting, dropout, MoE, scaling-laws, pretraining, data-constrained]
date_added: 2026-06-19
status: processed
---

# To Repeat or Not To Repeat: Insights from Scaling LLM under Token-Crisis

## 概要
高品質なweb テキストが LLM のスケーリング上限に近づく「**token-crisis（トークン枯渇）**」下で、事前学習データを**複数エポック繰り返す**とどうなるかを T5/C4 上で体系的に実証した最初の研究。データ繰り返しは**過学習＝multi-epoch degradation（多エポック劣化）**を招き、その**支配要因はデータセットサイズ・モデルパラメータ数・訓練目的関数**、影響が小さいのは**データ品質・モデル FLOPs**。緩和策では大半の正則化が効かない中で **dropout が極めて有効**（ただし大規模化には追加チューニングが必要）。さらに **MoE が同等パラメータの dense モデルの過学習挙動を低コストで予測**でき、ハイパラ探索の安価な代理になることを示す。11の insight にまとめられる。

## メモ
- arXiv 2305.13230（v2 2023-10-05）、**NeurIPS 2023 Poster 採択**（OpenReview Af5GvIj3T5）。Fuzhao Xue・Zangwei Zheng・Yang You（**NUS**）、Yao Fu（**University of Edinburgh**）、Wangchunshu Zhou（**ETH Zurich**）。Correspondence: youy@comp.nus.edu.sg。
- **token-crisis の定量**: compute-optimal な PaLM-540B を学習し切るには **10.8兆トークン**必要だが、高品質テキストの総ストックは **~9兆トークン**、成長率は年 **4-5%**（世界経済並み）。悲観シナリオでは **2023〜2027年に新規データが枯渇**しうる（Fig 1）。非英語データではさらに深刻（英語が web の 56%超）。
- **実験設定**: T5 1.1 をデフォルト構成とし、**C4 データセット**・同一アーキ/目的関数で学習。モデルは **T5-Base/Large/XL**。指標は C4 検証集合の **MLM accuracy** と、**SQuAD ファインチューニング**の EM/F1。
- **核心（メモ）**: 「データを繰り返すと過学習で劣化する（multi-epoch degradation）」。データが**足りない**ほど・モデルが**大きい**ほど劣化が激しい。逆に **dataset を大きくする / dropout を入れる**と緩和。
- knowledge-capacity-scaling-laws（同じ「露出・繰り返し」を扱うが、特定知識の繰り返し露出は**高密度保存に有益**とする）と表裏の関係。[[memory_repetition_two_views]] 的な対比点。
- 用語注: 本論文の「データ品質」は web スケール内の相対品質（C4 vs Wikipedia）に限定。高品質 instruction data は射程外。
