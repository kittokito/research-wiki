---
title: "Mixture-of-Depths Attention"
aliases: ["MoDA"]
created: 2026-04-07
updated: 2026-04-07
tags: [attention, depth, signal-degradation, architecture]
sources: [src-mixture-of-depths-attention]
---

# Mixture-of-Depths Attention

Zhu, Fang, Liao, Wang et al. (2026) — arXiv 2603.15619

## ソースからの事実
- 深い層で浅い層の有益な特徴が残差更新で希薄化する信号劣化問題に対処するMoDAを提案 [source](../../../sources/Architecture/mixture-of-depths-attention.md)
- 各ヘッドがシーケンスKVペア（現在層）と深度KVペア（先行層）に注意可能 [source](../../../sources/Architecture/mixture-of-depths-attention.md)
- FlashAttention-2の97.3%の効率で、1.5Bモデルで平均perplexity -0.2、下流タスク+2.11%、FLOPsオーバーヘッドわずか3.7% [source](../../../sources/Architecture/mixture-of-depths-attention.md)

→ 詳細: [evidence](../../../evidence/Architecture/mixture-of-depths-attention.md)

## 現時点の解釈
MoDAはDeepCrossAttentionやAttention Residualsと同じ「深度方向の情報フロー改善」カテゴリに属する。アプローチは異なるが、いずれも標準残差接続の情報希薄化問題に取り組む。MoDAの利点はFlashAttention-2との高い互換性とわずかなFLOPsオーバーヘッド。

## 関連ページ
- [DeepCrossAttention](deep-cross-attention.md)
- [Attention Residuals](attention-residuals.md)
- [mHC](manifold-constrained-hyper-connections.md)

## 未解決の問い
- 大規模モデル（数十B以上）での効果は？
- MoDAとMoEの組み合わせは？
