---
title: "Embarrassingly Simple Self-Distillation Improves Code Generation"
aliases: ["SSD", "Simple Self-Distillation"]
created: 2026-04-07
updated: 2026-04-07
tags: [self-distillation, code-generation, post-training]
peer_review: preprint
venue: ""
sources: [src-simple-self-distillation-code]
---

# Embarrassingly Simple Self-Distillation Improves Code Generation

> **査読**: 📝 preprint

Zhang, Bai, Zheng, Jaitly, Collobert, Zhang (2026) — arXiv 2603.03823

## ソースからの事実
- 検証器・教師モデル・RLなしにLLM自身の出力のみでコード生成改善が可能 [source](../../../sources/Post_Training/simple-self-distillation-code.md)
- SSD: 特定の温度・トランケーション設定でサンプリング→標準SFTでファインチューニング [source](../../../sources/Post_Training/simple-self-distillation-code.md)

→ 詳細: [evidence](../../../evidence/Post_Training/simple-self-distillation-code.md)

## 現時点の解釈
Mind the Gapの「生成>検証ギャップ」を利用した実用的手法。温度とトランケーションの設定が鍵で、サンプリング分布の調整により高品質データを自動的にフィルタリング。

## 関連ページ
- [Mind the Gap](../Reasoning/mind-the-gap-self-improvement.md)
- [Neural Thickets](neural-thickets.md)

## 未解決の問い
- SSDの最適温度・トランケーション設定はタスク依存か？コード以外のドメインでの効果は？
