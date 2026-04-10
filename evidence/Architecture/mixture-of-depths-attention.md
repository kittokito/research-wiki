---
source: src-mixture-of-depths-attention
date_extracted: 2026-04-07
---

# Mixture-of-Depths Attention からの抽出

## 主要な主張
- LLMが深くなるにつれ、浅い層で形成された有益な特徴が繰り返しの残差更新で希薄化される信号劣化問題が発生 [source](../../sources/Architecture/mixture-of-depths-attention.md)
- 各アテンションヘッドがシーケンスKVペア（現在層）と深度KVペア（先行層）の両方に注意できるMoDAメカニズムを提案 [source](../../sources/Architecture/mixture-of-depths-attention.md)
- ハードウェア効率の良いアルゴリズムで非連続メモリアクセスパターンを解決、シーケンス長64KでFlashAttention-2の97.3%の効率を達成 [source](../../sources/Architecture/mixture-of-depths-attention.md)

## 主要な貢献
- MoDA: 深度方向の情報アクセスを可能にする新しいアテンションメカニズム
- ハードウェア効率を維持した実装アルゴリズム

## ベンチマーク

| ベンチマーク | スコア | 備考 |
|---|---|---|
| 平均Perplexity | -0.2改善 | 10検証ベンチマーク |
| 下流タスク平均 | +2.11% | 10下流タスク |
| FLOPsオーバーヘッド | 3.7% | ほぼ無視可能 |

## 制限・注意点
- 1.5Bパラメータモデルでの検証のみ。大規模モデルでの効果は未確認
