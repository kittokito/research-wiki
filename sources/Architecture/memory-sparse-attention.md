---
id: src-memory-sparse-attention
title: "MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens"
authors: ["Yu Chen", "Runkai Chen", "Sheng Yi", "Xinda Zhao", "Xiaohong Li", "Jianjin Zhang", "Jun Sun", "Chuanrui Hu", "Yunyun Han", "Lidong Bing", "Yafeng Deng", "Tianqiao Chen"]
year: 2026
url: "https://arxiv.org/abs/2603.23516"
type: paper
peer_review: preprint
venue: ""
tags: [sparse-attention, long-context, RoPE, KV-cache, 100M-tokens, memory]
date_added: 2026-04-07
status: processed
---

# MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens

## 概要
100MトークンまでスケーラブルなメモリモデルのためのMemory Sparse Attention（MSA）を提案。スパースアテンションとdocument-wise RoPEにより学習・推論時に線形計算量を実現。16Kから100Mトークンへのスケーリング時の性能劣化を最小化し、KVキャッシュ圧縮により消費者向けGPUで100Mトークン推論を可能に。マルチホップ推論にも対応し、既存フロンティアモデルやRAGシステムを凌駕。

## メモ
cs.CL, cs.AI, cs.IR。2026年3月公開。
