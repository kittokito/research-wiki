---
title: "Continuous Autoregressive Language Models"
aliases: ["next-vector prediction"]
created: 2026-04-07
updated: 2026-04-07
tags: [autoregressive, continuous, efficiency, architecture]
sources: [src-continuous-autoregressive-lm]
---

# Continuous Autoregressive Language Models

Shao, Li, Meng, Zhou (2025) — arXiv 2510.27688

## ソースからの事実
- K個のトークンを99.9%以上の再構成精度で1連続ベクトルに圧縮し生成ステップをK分の1に [source](../../../sources/Architecture/continuous-autoregressive-lm.md)
- 尤度フリーの学習・評価・サンプリングフレームワークを開発 [source](../../../sources/Architecture/continuous-autoregressive-lm.md)
- 離散トークンベースラインと比較して性能-計算効率が向上 [source](../../../sources/Architecture/continuous-autoregressive-lm.md)

→ 詳細: [evidence](../../../evidence/Architecture/continuous-autoregressive-lm.md)

## 現時点の解釈
「next-token prediction」から「next-vector prediction」への転換は、推論効率の根本的改善を目指す重要な方向性。ただし連続空間でのサンプリング品質と離散トークンの表現力の比較は慎重に見る必要がある。

## 関連ページ
- なし（新しいパラダイム）

## 未解決の問い
- 連続ベクトル予測の品質は離散トークン予測と同等か？
- 大規模モデルでのスケーリング特性は？
