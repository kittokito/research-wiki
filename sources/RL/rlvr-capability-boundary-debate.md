---
id: src-rlvr-capability-boundary-debate
title: "The Debate on RLVR Reasoning Capability Boundary"
authors: ["不明（arXiv 2510.04028）"]
year: 2025
url: "https://arxiv.org/html/2510.04028v1"
type: paper
peer_review: under-review
venue: ""
tags: [RLVR, reasoning, capability-boundary, GRPO, exploration, exploitation]
date_added: 2026-04-08
status: processed
---

# The Debate on RLVR Reasoning Capability Boundary

## 概要
RLVRの能力境界をめぐるshrinkage派とexpansion派の対立を、probability mass dynamicsの二段階モデル（exploitation stage → exploration stage）として統一的に再解釈した論文。GRPO-N/GSPO-Nを提案し、negative gradientsに集中することでprolonged trainingを安定化させ、境界拡張を促進できると主張。

## メモ
- 「事前学習多様体への閉じ込め」を初期段階では認めつつ、永続的上限とは見なさない立場
- Theorem 1で期待logit updateが現在の方策確率に依存することを示し、極小tail行動は有限サンプル下で更新にほぼ寄与しないと明記
- "manifold"という用語は使わず、support / solution space / probability mass allocationの言葉で議論を組み立てている
