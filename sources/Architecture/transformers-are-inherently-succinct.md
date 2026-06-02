---
id: src-transformers-are-inherently-succinct
title: "Transformers are Inherently Succinct"
authors: ["Pascal Bergsträßer", "Ryan Cotterell", "Anthony W. Lin"]
year: 2025
url: "https://arxiv.org/abs/2510.19315"
type: paper
peer_review: accepted
venue: "ICLR 2026 (Oral, Outstanding Paper)"
tags: [transformer-expressivity, succinctness, formal-language-theory, LTL, finite-automata, RNN, UHAT, EXPSPACE, circuit-complexity, theory]
date_added: 2026-05-29
status: processed
---

# Transformers are Inherently Succinct

## 概要
Transformer の表現力を **succinctness（簡潔性）** という尺度で形式言語理論的に分析した理論論文。固定精度の **UHAT（Masked Unique Hard-Attention Transformer）** が、同じ形式言語を表現するのに **LTL（線形時相論理）より指数関数的に**、**有限オートマトンより二重指数関数的に** 簡潔であることを証明する。さらに UHAT の非空性（emptiness）・等価性（equivalence）判定問題が **EXPSPACE-complete** であることを示し、Transformer の検証が本質的に困難であることを明らかにする。ICLR 2026 Oral / Outstanding Paper。

## メモ
arXiv 2510.19315、v1 2025-10-22 / v3 2026-05-15。著者: Pascal Bergsträßer × Anthony W. Lin（RPTU Kaiserslautern-Landau / Max Planck Institute for Software Systems）× Ryan Cotterell（ETH Zürich）。
ICLR 2026 採択（Oral）、**ICLR 2026 Outstanding Paper** に選出。OpenReview id=Yxz92UuPLQ。
理論計算機科学（オートマタ・時相論理・計算量）と深層学習の橋渡し。対象は UHAT（unique hard-attention）であり、softmax / 浮動小数点の実務的挙動は対象外という前提に注意。
