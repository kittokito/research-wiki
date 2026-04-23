---
title: "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models"
aliases: ["ProRL"]
created: 2026-04-16
updated: 2026-04-16
tags: [RLVR, prolonged-training, reasoning-boundary, KL-divergence, policy-reset, Nemotron, NVIDIA]
peer_review: accepted
venue: "NeurIPS 2025"
sources: [src-prorl]
---

# ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in LLMs

> **査読**: ✅ accepted — NeurIPS 2025

Liu, Diao, Lu, Hu, Dong, Choi, Kautz, Dong (2025) — arXiv 2505.24864 / NVIDIA

## ソースからの事実
- 長期RL訓練（2,000+ステップ）でベースモデルのサンプリングでは到達不可能な新しい推論戦略を発見 [source](../../../sources/RL/prorl.md)
- KLダイバージェンス制御・参照ポリシーリセット・多タスク多様性の3要素で安定した長期訓練を実現 [source](../../../sources/RL/prorl.md)
- 1.5Bモデルで数学+14.7%、コード+13.9%、論理パズル+54.8%、STEM+25.1%改善 [source](../../../sources/RL/prorl.md)
- ベースモデルの出発性能が低いほどRLの効果が大きい逆相関 [source](../../../sources/RL/prorl.md)
- 未知タスク・高難度問題へのOOD汎化を実証 [source](../../../sources/RL/prorl.md)

→ 詳細: [evidence](../../../evidence/RL/prorl.md)

## 現時点の解釈

Yue et al.の「RLVRはfilteringに過ぎない」説への直接反論。標準的なRLVRが短期訓練で止まるためにfilteringに見えるだけで、十分長い訓練を行えば真に新しい推論能力を獲得できると主張。RLVR能力境界論争のexpansion側の主要論文。

## 関連ページ
- [[rlvr-does-not-teach-new-reasoning]] — ProRLが反論する対象（filtering説）
- [[rlvr-capability-boundary-debate]] — RLVR能力境界論争の全体像

## 未解決の問い
- 大規模モデル（70B+）でもProRLの効果は同様に再現されるか？
- 「新しい推論戦略」と「既存戦略の組み合わせ」の区別をどう厳密に定義するか？
