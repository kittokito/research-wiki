---
id: src-prorl
title: "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models"
authors: ["Mingjie Liu", "Shizhe Diao", "Ximing Lu", "Jian Hu", "Xin Dong", "Yejin Choi", "Jan Kautz", "Yi Dong"]
year: 2025
url: "https://arxiv.org/abs/2505.24864"
type: paper
peer_review: accepted
venue: "NeurIPS 2025"
tags: [RLVR, prolonged-training, reasoning-boundary, KL-divergence, policy-reset, Nemotron, NVIDIA]
date_added: 2026-04-16
status: processed
---

# ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models

## 概要
長期間のRL訓練（2,000ステップ以上）がLLMの推論能力境界を真に拡張しうることを示した研究。KLダイバージェンス制御・参照ポリシーリセット・多様なタスク訓練からなるProRL手法を提案。Nemotron-Research-Reasoning-Qwen-1.5Bで数学+14.7%、コード+13.9%、論理パズル+54.8%、STEM+25.1%の改善を達成。

## メモ
- Yue et al.の「RLVRはfilteringに過ぎない」説への直接反論
- ベースモデルの出発性能が低いほどRLの効果が大きいという逆相関を報告
- 未知タスク・高難度問題へのOOD汎化を実証
