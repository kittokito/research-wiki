---
id: src-dr-grpo
title: "Understanding R1-Zero-Like Training: A Critical Perspective"
authors: ["Zichen Liu", "Changyu Chen", "Wenjun Li", "Penghui Qi", "Tianyu Pang", "Chao Du", "Wee Sun Lee", "Min Lin"]
year: 2025
url: "https://arxiv.org/abs/2503.20783"
type: paper
peer_review: accepted
venue: "COLM 2025"
tags: [rl, rlvr, GRPO, dr-grpo, r1-zero, pretraining-bias, optimization-bias, token-efficiency, critical-analysis]
date_added: 2026-04-23
status: processed
---

# Understanding R1-Zero-Like Training: A Critical Perspective

## 概要
DeepSeek-R1-Zero の「SFTなしpure RLで推論能力向上」という主張を **ベースモデル** と **RL** の2要素に分解して批判的に検証した論文。**Dr. GRPO**（"done right" GRPO）を提案。主要な発見:
1. **DeepSeek-V3-Base は RL 前から "Aha moment" を示す** — R1-Zero で観察された "Aha moment" の一部は事前学習由来のバイアスであり、pure RL による創発ではない可能性
2. **Qwen2.5 base models はプロンプトテンプレートなしでも強い推論能力を示す** — 事前学習段階で既に instruction-like 能力が組み込まれている
3. **GRPO には最適化バイアスがある** — 特に **不正解出力の応答長を人為的に増加させる** 方向に偏り、「長く書けば効率が上がる」のではなく単なるバイアスの副産物
4. **Dr. GRPO**: 上記バイアスを除去した unbiased な最適化手法 → token 効率を改善しつつ推論性能を維持
5. **minimalist R1-Zero recipe**: 7B base model で **AIME 2024 43.3% accuracy** (SOTA at time)

## メモ
cs.LG / cs.AI / cs.CL。**COLM 2025 採択** (OpenReview 5PAF7PAY2Y, decision: Accepted, published 2025-07-08)。Sea AI Lab / sail-sg / NUS（Wee Sun Lee ら）。v1: 2025-03-26、v2: 2025-10-06。GitHub: sail-sg/understand-r1-zero。**RLVR 能力境界論争に対する中立的検証論文** として位置付けられる: 「RLで能力が真に拡張されるか」の議論において、**観測された能力の一部を事前学習へ帰属** させる第三の視点を提供。[DeepSeek-R1](./deepseek-r1.md) の直接的批判であり、[Does RLVR Truly Unlock New Reasoning](./rlvr-does-not-teach-new-reasoning.md)（filtering派）の事前学習バイアス議論と呼応する。Dr. GRPO は [ScaleRL](./scale-rl.md) のレシピ選定における「GRPO系列のバイアス問題」を裏付ける材料でもあり、CISPO / RS-GRPO 等の GRPO改良系列の理論的基盤を補強。
