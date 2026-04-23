---
title: "Reasoning with Sampling: Your Base Model is Smarter Than You Think"
aliases: ["Reasoning with Sampling", "MCMC Reasoning"]
created: 2026-04-16
updated: 2026-04-16
tags: [MCMC, inference-time-compute, power-distribution, base-model, sampling, training-free, reasoning]
peer_review: under-review
venue: "ICLR 2026（投稿中）"
sources: [src-reasoning-with-sampling]
---

# Reasoning with Sampling: Your Base Model is Smarter Than You Think

> **査読**: 🔄 under-review — ICLR 2026 Conference Submission（OpenReview [Vsgq2ldr4K](https://openreview.net/forum?id=Vsgq2ldr4K)）

Karan & Du (2025) — arXiv 2510.14901 / Harvard

## ソースからの事実
- べき分布（p^α）をターゲットとした自己回帰MCMCでベースモデルから推論能力を引き出す [source](../../../sources/Inference_Decoding/reasoning-with-sampling.md)
- 追加学習・外部検証器なし、推論時計算のみでMATH500でGRPO相当の性能 [source](../../../sources/Inference_Decoding/reasoning-with-sampling.md)
- HumanEval・AlpacaEval 2.0ではGRPOをOODで上回る [source](../../../sources/Inference_Decoding/reasoning-with-sampling.md)
- RLと異なりサンプル多様性を維持、pass@kでも優れた性能 [source](../../../sources/Inference_Decoding/reasoning-with-sampling.md)

→ 詳細: [evidence](../../../evidence/Inference_Decoding/reasoning-with-sampling.md)

## 現時点の解釈

RLVR論争（filtering vs expansion）に対し、「そもそも推論時のサンプリングだけでRL相当の性能が出る」という第三の視点を提供。ベースモデルの潜在能力がRLなしでも引き出せるという意味で、Yue et al.の「ベースモデルに能力はすでにある」説を推論時アルゴリズムの側面から補強している。

## 関連ページ
- [[rlvr-does-not-teach-new-reasoning]] — ベースモデルに能力が既に存在するという主張
- [[prorl]] — 長期RLは真に境界を拡張すると主張（対立的視点）
- [[rlvr-capability-boundary-debate]] — RLVR能力境界論争の全体像

## 未解決の問い
- MCMCの推論時コストはRL訓練コストと比較してどちらが効率的か？
- α値やサンプリングステップ数のタスク依存性はどの程度か？
