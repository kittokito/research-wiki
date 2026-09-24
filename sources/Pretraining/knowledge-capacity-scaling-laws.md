---
id: src-knowledge-capacity-scaling-laws
title: "Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws"
authors: ["Zeyuan Allen-Zhu", "Yuanzhi Li"]
year: 2024
url: "https://arxiv.org/abs/2404.05405"
type: paper
peer_review: accepted
venue: "ICLR 2025 (Spotlight)"
tags: [knowledge-capacity, scaling-laws, memorization, bits-per-parameter, exposure, quantization, MoE, pretraining]
date_added: 2026-06-09
status: processed
---

# Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws

## 概要
言語モデルが保存する**知識量を情報理論的に bit 数で推定**する研究。事実知識をタプル（例: (USA, capital, Washington D.C.)）で表し、制御されたデータセット群で、LM は **1パラメータあたり最大2 bit の知識を保存できる**（int8 量子化でも維持）ことを確立。さらに **(1) 訓練時間（露出回数）・(2) アーキテクチャ・(3) 量子化・(4) MoE 等のスパース性・(5) データの signal-to-noise 比** が容量に与える影響を12の結果で示す。7B モデルなら 14B bit ＝英語 Wikipedia＋教科書を超える知識を保存できる計算。

## メモ
- arXiv 2404.05405、**ICLR 2025 Spotlight**（OpenReview FxNNiUgtfa）。Zeyuan Allen-Zhu, Yuanzhi Li（Meta FAIR / Mohamed bin Zayed Univ.）。
- **要メモ（核心）**: 訓練時間＝**各知識の露出回数**が容量を支配する。各知識を**約1000回露出**させた十分学習レジームで **2 bits/param のピーク容量**に到達。露出が**約100回**に減ると容量はおよそ**半減（~1 bit/param）**。つまり「**1000回露出すると知識が高密度（2bit/param）に保存される**」。
- 「Physics of Language Models」シリーズの一編（制御実験で LM の挙動を物理学的に解明する方針）。
- ユーザー提示 URL（OpenReview FxNNiUgtfa）はこの論文。
