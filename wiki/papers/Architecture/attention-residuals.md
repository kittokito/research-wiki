---
title: "Attention Residuals"
aliases: ["AttnRes", "Block AttnRes"]
created: 2026-04-07
updated: 2026-04-07
tags: [residual-connection, attention, architecture, Kimi]
sources: [src-attention-residuals]
---

# Attention Residuals

Chen, Zhang, Su et al. (2026) — arXiv 2603.15031

## ソースからの事実
- PreNormの標準残差接続が深度に伴う隠れ状態の制御不能な成長を引き起こす問題を指摘 [source](../../../sources/Architecture/attention-residuals.md)
- softmaxアテンションで先行層表現を学習可能重みで選択的に集約するAttention Residualsを提案 [source](../../../sources/Architecture/attention-residuals.md)
- Kimi Linear（48B total / 3B activated）に統合し1.4Tトークンで学習、出力マグニチュードと勾配分布のバランス改善 [source](../../../sources/Architecture/attention-residuals.md)

→ 詳細: [evidence](../../../evidence/Architecture/attention-residuals.md)

## 現時点の解釈
Moonshot AI / Kimi関連チームからの研究で、DeepCrossAttentionやmHCと同様の残差接続改良。実際にKimi Linearという実プロダクションモデルに統合されている点が他の研究との差別化要因。

## 関連ページ
- [DeepCrossAttention](deep-cross-attention.md)
- [mHC](manifold-constrained-hyper-connections.md)
- [MoDA](mixture-of-depths-attention.md)

## 未解決の問い
- Block AttnResの効率性と性能のトレードオフは？
