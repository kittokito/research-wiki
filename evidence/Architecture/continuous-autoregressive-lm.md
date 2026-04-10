---
source: src-continuous-autoregressive-lm
date_extracted: 2026-04-07
---

# Continuous Autoregressive Language Models からの抽出

## 主要な主張
- 高忠実度オートエンコーダでK個のトークンを99.9%以上の再構成精度で1つの連続ベクトルに圧縮 [source](../../sources/Architecture/continuous-autoregressive-lm.md)
- 生成ステップをK分の1に削減可能 [source](../../sources/Architecture/continuous-autoregressive-lm.md)
- 尤度フリーの学習・評価・サンプリングフレームワークを開発 [source](../../sources/Architecture/continuous-autoregressive-lm.md)
- 離散トークンベースラインと比較して性能-計算効率が向上 [source](../../sources/Architecture/continuous-autoregressive-lm.md)

## 主要な貢献
- next-vector predictionパラダイム
- 尤度フリーフレームワーク

## 制限・注意点
- 実用的な生成品質と離散モデルとの詳細比較は限定的
