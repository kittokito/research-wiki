---
id: src-rl-scaling-math-qwen25
title: "Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning"
authors: ["Zelin Tan", "Hejia Geng", "Xiaohang Yu", "Mulei Zhang", "Guancheng Wan", "Yifan Zhou", "Qiang He", "Xiangyuan Xue", "Heng Zhou", "Yutao Fan", "Zhongzhi Li", "Zaibin Zhang", "Guibin Zhang", "Chen Zhang", "Zhenfei Yin", "Philip Torr", "Lei Bai"]
year: 2025
url: "https://arxiv.org/abs/2509.25300"
type: paper
peer_review: accepted
venue: "ACL 2026 (Main Conference)"
tags: [scaling-law, rl, rlvr, post-training, mathematical-reasoning, qwen25, grpo, data-efficiency, power-law]
date_added: 2026-04-22
status: processed
---

# Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning

## 概要
Qwen2.5 dense系列（0.5B–72B）のフルラインナップを用いて、RLベースのポストトレーニング（GRPO、数学推論特化）におけるモデル規模・データ量・計算量の相互作用を体系的に調べた実証研究。主張は4点: (1) 大モデルほど計算・データ両面で学習効率が高い、(2) test loss と (compute, data) は base/instruct を問わず **log L(N,X) = −k(N)·log X + E(N)** の予測可能な power-law でモデル化できる、(3) しかし学習効率 k(N) は **k(N) = K_max / (1 + N_0/N)** の形で飽和する（モデル規模を大きくしてもいつか上限に近づく）、(4) データ制約下では高品質データを繰り返し使うのが極めて有効で、最終性能は **サンプルのユニーク数ではなく最適化ステップ総数** でほぼ決まる。

## メモ
cs.LG / cs.AI。Shanghai AI Lab、Oxford（Philip Torr）等の国際共同研究。v4で ACL 2026 Main 採択を明記。評価は in-domain（訓練分布）+ OOD（AIME2024, AMC2023, GSM8K, MATH500, HumanEval, Zebra Puzzle, SuperGPQA）。Meta/UT Austinの [ScaleRL](./scale-rl.md)（sigmoidフィット・40万GPU時間）と相補的: 本論文は power-law フィット＋学習効率 k(N) の解析的形を提示し、**k(N)のsaturation** という新しい発見を含む。RLVR能力境界論争（`topics/RL/rlvr-capability-boundary.md`）に対して「大モデルは効率で勝るが、効率そのものがサチる」という追加の定量的制約を与える点が重要。
