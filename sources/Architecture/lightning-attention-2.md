---
id: src-lightning-attention-2
title: "Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths in Large Language Models"
authors: ["Zhen Qin", "Weigao Sun", "Dong Li", "Xuyang Shen", "Weixuan Sun", "Yiran Zhong"]
year: 2024
url: "https://arxiv.org/abs/2401.04658"
type: paper
peer_review: n/a
venue: ""
tags: [lightning-attention, linear-attention, transformer, GPU-kernel, IO-aware, long-context, TransNormerLLM, MiniMax]
date_added: 2026-05-01
status: processed
---

# Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths in Large Language Models

## 概要
Linear attention は理論上 O(N) でも、causal mask 下で必要な **累積和 (cumsum)** が GPU 上で逐次計算となり実装速度が softmax attention に勝てない問題を解決した論文。**tiling 手法** で attention を block 単位に分け、**intra-block は通常の left-product (softmax-like)、inter-block は right-product (linear KV state)** で分離計算する。これにより causal linear attention の理論的 O(N) スケーリングを **GPU 上でも実用速度で達成** し、シーケンス長を 32K-128K まで伸ばしても **TGS (tokens per GPU per second) が一定**（FlashAttention-2 は急減）。Triton で I/O-aware に実装、TransNormerLLM-1B/3B で実証。MiniMax-M1 の lightning attention の元論文。

## メモ
著者: Zhen Qin, Weigao Sun, Dong Li, Xuyang Shen, Weixuan Sun, Yiran Zhong (corresponding) — OpenNLPLab / Shanghai AI Lab。arXiv 2401.04658（v1: 2024-01-09, v2: 2024-01-15）。Comments 欄: **"Technical Report"** と明記、コードは https://github.com/OpenNLPLab/lightning-attention で公開。本リポジトリでは [Linear Transformers (Katharopoulos et al., 2020)](../../wiki/papers/Architecture/linear-transformers.md) の数学的枠組みを **LLM 規模の GPU 実装に落とし込んだ後継** として位置付け。MiniMax-M1 (2025) の "lightning attention" はこの論文の直接の延長。Lightning Attention-1 は前作（TransNormerLLM 内）で提案、本論文の LA2 は前作の累積和ボトルネックを tiling で解消した版。
