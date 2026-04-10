---
id: src-mrpo
title: "Beyond Alignment: Expanding Reasoning Capacity via Manifold-Reshaping Policy Optimization"
authors: ["Dayu Wang", "Jiaye Yang", "Weikang Li", "Jiahui Liang", "Yang Li"]
year: 2026
url: "https://arxiv.org/abs/2602.02545"
type: paper
tags: [RLVR, MRPO, manifold, reasoning, GRPO, effective-rank, spectral-orthogonal-exploration, math]
date_added: 2026-04-08
status: processed
---

# Beyond Alignment: Expanding Reasoning Capacity via Manifold-Reshaping Policy Optimization (MRPO)

## 概要
標準的なRLVRが事前学習のbias manifold（低ランク多様体）に閉じ込められるという問題に対し、幾何学的介入で直接打破するMRPOを提案。2段階で構成される：(1) Spectral Orthogonal Exploration (SOE)でbias manifoldのnull spaceへ方策を誘導、(2) effective rank正則化でRL最適化中の次元崩壊を防止。4Bモデルで32Bモデルを上回る数学推論性能を達成。

## メモ
- 先行するRLVR能力境界論争（Yue et al.のfiltering主張、Invisible Leash等）を踏まえ、manifold制約を前提として受け入れた上で突破を試みる立場
- Student-Guides-Teacher paradigmとMicro-SVDアルゴリズムが実装の核
- 安全性に関する懸念を著者自身が指摘（bias manifold外の動作が安全ガードレールを迂回するリスク）
- 数学推論以外のドメインへの汎化は未検証
