---
id: src-linear-transformers
title: "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention"
authors: ["Angelos Katharopoulos", "Apoorv Vyas", "Nikolaos Pappas", "François Fleuret"]
year: 2020
url: "https://arxiv.org/abs/2006.16236"
type: paper
peer_review: accepted
venue: "ICML 2020 (PMLR v119, pp.5156-5165)"
tags: [linear-attention, transformer, RNN, kernel-method, efficient-attention, autoregressive, architecture]
date_added: 2026-05-01
status: processed
---

# Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention

## 概要
self-attention の softmax(QKᵀ) を **kernel feature map の内積 φ(Q)φ(K)ᵀ** で近似することで、行列積の結合性 (φ(Q)·(φ(K)ᵀV)) を活用し計算量を **O(N²d) → O(Nd²)** に削減。さらに causal マスク付き自己回帰生成は **RNN として等価に再定式化** でき、推論を再帰的に行うことで autoregressive 推論を最大 **4000倍高速化**。Linear Attention の祖となる論文で、後続の Performer / RWKV / RetNet / Mamba / Lightning Attention / Kimi Linear など linear attention 系全般の数学的基礎。

## メモ
著者: Angelos Katharopoulos, François Fleuret (Idiap Research Institute & EPFL), Apoorv Vyas (Idiap Research Institute), Nikolaos Pappas (University of Washington)。arXiv 2006.16236（v1: 2020-06-29, v3: 2020-08-31）。**ICML 2020 採択**（PMLR v119, pp.5156-5165）。プロジェクトページ: https://linear-transformers.com/ 、コード: https://github.com/idiap/fast-transformers 。本リポジトリの linear/hybrid attention 系（Attention to Mamba, Attention Residuals / Kimi Linear, MiniMax-M1 lightning attention, Qwen3.5-Omni hybrid attention MoE）の **共通祖先**。「kernel-based linear attention は softmax より厳密には弱いが、causal mask + RNN 化で推論コストが定数オーダーになる」という設計トレードオフを最初に明示した論文。
