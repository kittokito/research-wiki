---
id: src-sft-data-composition
title: "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition"
authors: ["Guanting Dong", "Hongyi Yuan", "Keming Lu", "Chengpeng Li", "Mingfeng Xue", "Dayiheng Liu", "Wei Wang", "Zheng Yuan", "Chang Zhou", "Jingren Zhou"]
year: 2023
url: "https://arxiv.org/abs/2310.05492"
type: paper
peer_review: accepted
venue: "ACL 2024 (Main)"
tags: [SFT, data-composition, catastrophic-forgetting, multi-task, math-reasoning, code-generation, instruction-following, DMT, scaling]
date_added: 2026-06-03
status: processed
---

# How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition

## 概要
SFT（教師ありファインチューニング）時に **数学推論・コード生成・一般的な指示追従（human-alignment）** の3能力がデータ量・混合比・モデルサイズ・SFT戦略にどう影響されるかを体系的に調査した論文。3能力は **スケーリング特性が異なる**（数学・コードはデータ量とともに単調向上、一般能力は約1,000サンプルで頭打ち）。複数能力を同時/逐次に学習させると、低リソースでは混合が各能力を底上げするが、高リソースでは能力間が競合（conflict）し、逐次学習では **catastrophic forgetting** が起きる。これに対し **DMT（Dual-stage Mixed Fine-tuning）**——まず専門データ（数学・コード）で学習し、次に一般データに専門データの一部（比率 k）を混ぜて学習する2段階法——を提案し、competition と forgetting の両方を緩和して専門能力と一般能力のバランスを達成する。

## メモ
arXiv 2310.05492、v1 2023-10-09 / v4 2024-06-07。**ACL 2024 Main Conference 採択**。
著者は Alibaba（Qwen チームを含む: Keming Lu, Dayiheng Liu, Chang Zhou, Jingren Zhou ら）。評価は GSM8K（数学）/ HumanEval（コード）/ MT-Bench（一般）、ベースモデルは LLaMA 系（7B/13B/33B）。
[Qwen3](../../wiki/papers/Technical_Report/qwen3.md) の多段 post-training（thinking/non-thinking 統合）や継続学習の議論（[Learning, Fast and Slow](../../wiki/papers/RL/learning-fast-and-slow.md)）の先行研究として読める。
