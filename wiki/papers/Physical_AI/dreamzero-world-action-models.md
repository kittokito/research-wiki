---
title: "World Action Models are Zero-shot Policies (DreamZero)"
aliases: ["DreamZero"]
created: 2026-04-07
updated: 2026-04-07
tags: [world-model, robotics, zero-shot, video-diffusion]
sources: [src-dreamzero-world-action-models]
---

# World Action Models are Zero-shot Policies (DreamZero)

Ye, Ge, Zheng et al. (2026) — arXiv 2602.15922

## ソースからの事実
- ビデオ拡散で将来の世界状態とアクションを予測するDreamZeroを提案 [source](../../../sources/Physical_AI/dreamzero-world-action-models.md)
- SOTA VLAに対して2倍以上の汎化改善、7Hzリアルタイム制御 [source](../../../sources/Physical_AI/dreamzero-world-action-models.md)
- クロスエンボディメント転移で42%以上の相対改善 [source](../../../sources/Physical_AI/dreamzero-world-action-models.md)

→ 詳細: [evidence](../../../evidence/Physical_AI/dreamzero-world-action-models.md)

## 現時点の解釈
世界モデルをゼロショットポリシーとして使うアプローチは、ロボティクスにおける大規模基盤モデルの活用方向として有望。ビデオ拡散の計算コストが課題だが、7Hzのリアルタイム制御達成は実用的。

## 関連ページ
- [V-JEPA 2](v-jepa-2.md)

## 未解決の問い
- より高い制御周波数（30Hz+）の達成は可能か？
