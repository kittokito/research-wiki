---
id: src-atlas-multilingual-scaling-laws
title: "ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality"
authors: ["Shayne Longpre", "Sneha Kudugunta", "Niklas Muennighoff", "I-Hung Hsu", "Isaac Caswell", "Alex Pentland", "Sercan Arik", "Chen-Yu Lee", "Sayna Ebrahimi"]
year: 2025
url: "https://arxiv.org/abs/2510.22037"
type: paper
peer_review: accepted
venue: "ICLR 2026"
tags: [scaling-law, multilingual, pretraining, transfer-learning, curse-of-multilinguality, low-resource]
date_added: 2026-04-20
status: processed
---

# ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality

## 概要
多言語事前学習に関する過去最大規模のスケーリング則研究（10M-8Bパラメータ × 400+学習言語 × 48評価言語、計774実験）。単言語・多言語双方に適用可能なAdaptive Transfer Scaling Law (ATLAS) を提案し、既存スケーリング則を out-of-sample 汎化で0.3 R²以上上回ることを実証。38×38=1444言語ペアの転移行列、言語追加時の最適スケーリング則、scratch学習 vs 多言語チェックポイントからのfinetune の計算的クロスオーバー点を導出。

## メモ
cs.CL / cs.LG。著者はMIT Media Lab (Longpre, Pentland)、Google Research/DeepMind (Kudugunta, Caswell, Arik, Lee, Ebrahimi, Hsu)、Stanford (Muennighoff) 系の国際共同。Chinchilla系スケーリング則の多言語版に相当。"Curse of Multilinguality"（言語を増やすほど個別言語の性能が劣化する現象）の定量的分解がコア。
