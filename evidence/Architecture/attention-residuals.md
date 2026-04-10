---
source: src-attention-residuals
date_extracted: 2026-04-07
---

# Attention Residuals からの抽出

## 主要な主張
- PreNormの標準残差接続は層出力を均一に蓄積し、深度に伴う隠れ状態の制御不能な成長を引き起こす [source](../../sources/Architecture/attention-residuals.md)
- softmaxアテンションで先行層表現を学習可能な重みで選択的に集約するAttention Residualsを提案 [source](../../sources/Architecture/attention-residuals.md)
- Block AttnResで大規模モデルの計算オーバーヘッドに対処 [source](../../sources/Architecture/attention-residuals.md)
- Kimi Linearアーキテクチャ（48B total / 3B activated）に統合し1.4兆トークンで学習 [source](../../sources/Architecture/attention-residuals.md)

## 主要な貢献
- Attention Residuals: softmaxベースの選択的層間集約
- Block AttnRes: 大規模モデル向けの効率化バリアント

## 制限・注意点
- Kimi Linearアーキテクチャ固有の評価が中心
