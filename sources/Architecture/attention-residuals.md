---
id: src-attention-residuals
title: "Attention Residuals"
authors: ["Guangyu Chen", "Yu Zhang", "Jianlin Su", "Weixin Xu", "Siyuan Pan", "Yaoyu Wang", "Yucheng Wang", "Guanduo Chen", "Bohong Yin", "Yutian Chen", "Junjie Yan", "Ming Wei"]
year: 2026
url: "https://arxiv.org/abs/2603.15031"
type: paper
tags: [residual-connection, attention, PreNorm, architecture, Kimi]
date_added: 2026-04-07
status: processed
---

# Attention Residuals

## 概要
標準的なPreNorm残差接続が層出力を均一に蓄積し深度に伴う隠れ状態の制御不能な成長を引き起こす問題を指摘。softmaxアテンションで先行層の表現を学習可能な重みで選択的に集約するAttention Residualsを提案。Kimi Linearアーキテクチャ（48B total / 3B activated）に統合し1.4兆トークンで学習、出力マグニチュードと勾配分布のバランスを改善。

## メモ
cs.CL。Moonshot AI / Kimi関連。Block AttnResで大規模モデルの計算オーバーヘッドに対処。
