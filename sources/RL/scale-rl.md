---
id: src-scale-rl
title: "The Art of Scaling Reinforcement Learning Compute for LLMs"
authors: ["Devvrit Khatri", "Lovish Madaan", "Rishabh Tiwari", "Rachit Bansal", "Sai Surya Duvvuri", "Manzil Zaheer", "Inderjit S. Dhillon", "David Brandfonbrener", "Rishabh Agarwal"]
year: 2025
url: "https://arxiv.org/abs/2510.13786"
type: paper
peer_review: accepted
venue: "ICLR 2026 (Oral)"
tags: [scaling-law, rl, rlvr, compute-efficiency, scaling-recipe, post-training]
date_added: 2026-04-21
status: processed
---

# The Art of Scaling Reinforcement Learning Compute for LLMs

## 概要
LLM向けRLの「スケーリング則」を大規模に定式化した初の体系研究（総計40万GPU時間以上）。pretrainingで確立されたpredictable scalingに相当する枠組みがRL訓練に欠けていた状況を受け、計算-性能曲線をsigmoid関数でフィッティングし、設計選択（loss aggregation、正則化、curriculum、off-policyアルゴリズム）を幅広くablation。主な発見は (1) 全てのレシピが同じ漸近性能に収束するわけではない、(2) loss aggregation等の細部は漸近値をほぼ動かさず計算効率を調整する、(3) 安定的なレシピは予測可能な軌道をたどり小規模実行からの外挿が可能、の3点。ベストプラクティス「ScaleRL」を提案し、10万GPU時間規模の単一ランで検証損失を事前予測して実証。

## メモ
cs.LG / cs.AI。著者はMeta AI（Rishabh Agarwal、Brandfonbrener、Zaheer、Dhillon）、UT Austin（Khatri、Duvvuri、Dhillon）等。OpenReview FMjeC9Msws。**ICLR 2026 Oral** 採択。RLVRの能力境界論争（asymptote vs efficiency の切り分け）に直結する定量的基礎を提供する論文で、本wikiの `topics/RL/rlvr-capability-boundary.md` と強く関連。
