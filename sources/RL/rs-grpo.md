---
id: src-rs-grpo
title: "Risk-Sensitive RL for Alleviating Exploration Dilemmas in Large Language Models"
authors: ["Yuhua Jiang", "Jiawei Huang", "Yufeng Yuan", "Xin Mao", "Yu Yue", "Qianchuan Zhao", "Lin Yan"]
year: 2025
url: "https://arxiv.org/abs/2509.24261"
type: paper
peer_review: under-review
venue: "ICLR 2026（投稿中）"
tags: [RLVR, GRPO, pass-at-k, exploration-exploitation, risk-sensitive-RL, CVaR, Tsinghua, ByteDance-Seed]
date_added: 2026-04-17
status: processed
---

# Risk-Sensitive RL for Alleviating Exploration Dilemmas in Large Language Models

## 概要
事前学習済みLLMの初期方針が鋭く尖鋭化している（sharpened initial policy）ため、標準的なRL手法は狭い解集合に閉じ込められ、pass@1は向上するがpass@k（解の多様性）が低下する「exploration dilemma」を指摘。平均報酬と最大報酬を補間するリスク感応的な目的関数（CVaRベース）を導入し、困難なプロンプトからの学習を増幅するRS-GRPOを提案。6つの数学推論ベンチマークと5つのLLMでpass@1を維持しつつpass@kを継続的に向上させることを実証。

## メモ
- 著者所属: 清華大学（Jiang, Huang, Zhao）+ ByteDance Seed（Yuan, Yue, Yan）
- GRPOへの最小限の修正（few lines of code）で実装可能
- RLVR能力境界論争における「pass@kが下がる問題」への実装面からのアプローチ
- Yue et al. (filtering説)・ProRL (expansion説)・MRPO (manifold-reshaping)とは別系統で、目的関数のリスク感応性を調整する方向性
