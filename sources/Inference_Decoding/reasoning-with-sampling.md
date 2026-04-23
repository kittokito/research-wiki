---
id: src-reasoning-with-sampling
title: "Reasoning with Sampling: Your Base Model is Smarter Than You Think"
authors: ["Aayush Karan", "Yilun Du"]
year: 2025
url: "https://arxiv.org/abs/2510.14901"
type: paper
peer_review: under-review
venue: "ICLR 2026（投稿中）"
tags: [MCMC, inference-time-compute, power-distribution, base-model, sampling, training-free, reasoning]
date_added: 2026-04-16
status: processed
---

# Reasoning with Sampling: Your Base Model is Smarter Than You Think

## 概要
追加学習なしにベースLLMから推論能力を引き出す反復サンプリングアルゴリズムを提案。べき分布（p^α）をターゲットとした自己回帰MCMCでトークン部分列を再サンプリングし、MATH500・HumanEval・GPQAでRL訓練モデルに匹敵・上回る性能を達成。サンプル多様性も保持。

## メモ
- 訓練不要・外部検証器不要で推論時計算のみでreasoning改善
- RLVRが必要かという議論に「推論時計算で代替可能」という第三の視点を提供
- ICLR 2026 Conference Submission（OpenReview Vsgq2ldr4K、投稿中）— ICLR 2026 Orals公式リストには含まれず、採択ステータス未確定
