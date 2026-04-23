---
source: src-atlas-multilingual-scaling-laws
date_extracted: 2026-04-20
---

# ATLAS: Adaptive Transfer Scaling Laws からの抽出

## 主要な主張
- 多言語スケーリング則研究として過去最大規模：774実験、10M-8Bパラメータ、400+学習言語、48評価言語 [source](../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- 単言語・多言語の両方に適用可能な Adaptive Transfer Scaling Law (ATLAS) を提案 [source](../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- ATLAS は既存スケーリング則を out-of-sample 汎化で **0.3 R² 以上** 上回る [source](../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- 38×38=1444 言語ペアの cross-lingual transfer matrix を経験的に測定、言語間の相互利益スコアを定量化 [source](../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- language-agnostic scaling law を導出、言語追加時にモデルサイズとデータをどう最適スケールすべきかを定式化 [source](../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- scratch学習 vs 多言語チェックポイントからのfinetune の **計算クロスオーバー点** を同定 [source](../../sources/Pretraining/atlas-multilingual-scaling-laws.md)

## 主要な貢献
- 多言語スケーリング則の標準ツール ATLAS
- 言語ペア間転移行列（low-resource 言語への転移設計の基盤データ）
- Curse of Multilinguality の定量化と緩和指針
- 英語中心のスケーリング則研究の民主化・非英語圏への拡張

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| 実験数 | 774 | 多言語事前学習・finetune |
| モデルサイズ範囲 | 10M-8B | パラメータ数 |
| 学習言語数 | 400+ | 多様な低資源言語含む |
| 評価言語数 | 48 | out-of-sample を含む |
| 言語ペア数 | 1444 (38×38) | 転移行列 |
| out-of-sample 汎化改善 | +0.3 R² 以上 | 既存スケーリング則比 |

## 制限・注意点
- 最大モデルが8Bまでで、70B+ 規模での外挿妥当性は未検証
- 評価は48言語 / 転移行列は38言語。400+学習言語のうち大多数は転移スコアが直接測定されていない
- decoder-only LLM中心の結果で、encoder-only / encoder-decoder への一般化は別検証が必要
- 「Curse of Multilinguality」の緩和指針は得られるが根本的な capacity bottleneck 問題を解消するわけではない

## 実装関連
- ATLAS 係数を用いて、対象言語セットと計算予算から最適なモデルサイズ・データ配分・scratch vs finetune を決定する実用ワークフローを示唆
- 多言語モデル開発における言語混合比（sampling ratio）の設計に転移行列が直接利用可能
