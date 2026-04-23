---
title: "ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining"
aliases: ["ATLAS", "Adaptive Transfer Scaling Law", "Multilingual Scaling Laws"]
created: 2026-04-20
updated: 2026-04-20
tags: [scaling-law, multilingual, pretraining, transfer-learning, curse-of-multilinguality]
peer_review: accepted
venue: "ICLR 2026"
sources: [src-atlas-multilingual-scaling-laws]
---

# ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality

> **査読**: ✅ accepted — ICLR 2026

Longpre, Kudugunta, Muennighoff et al. (2025) — arXiv 2510.22037

## ソースからの事実
- 多言語スケーリング則研究として過去最大規模：774実験、10M-8Bパラメータ、400+学習言語、48評価言語 [source](../../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- Adaptive Transfer Scaling Law (ATLAS) は既存スケーリング則を out-of-sample 汎化で **+0.3 R² 以上** 上回る [source](../../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- 38×38=1444 言語ペアの cross-lingual transfer matrix を経験的に測定 [source](../../../sources/Pretraining/atlas-multilingual-scaling-laws.md)
- language-agnostic scaling law により言語追加時の最適モデルサイズ・データ配分を定式化、scratch vs 多言語チェックポイントからの finetune の計算クロスオーバー点を同定 [source](../../../sources/Pretraining/atlas-multilingual-scaling-laws.md)

→ 詳細: [evidence](../../../evidence/Pretraining/atlas-multilingual-scaling-laws.md)

## 現時点の解釈
Chinchilla 系スケーリング則の「英語中心」という致命的な偏りを、過去最大規模の多言語実験で拡張した重要な論文。特に (i) ATLAS による **+0.3 R² 以上の汎化改善**、(ii) 1444 言語ペアの転移行列、(iii) scratch vs finetune のクロスオーバー点、の3つは多言語モデル開発のリソース配分を経験則から定量原則へと引き上げる実用的ツールになる。Curse of Multilinguality の根本解消ではないが、その定量的分解と緩和指針を初めて提供した点が意義深い。日本語・他非英語言語中心のLLM開発（Swallow, Sarashina, Namazu 等）における学習戦略決定に直結するため、関連ページと横串で参照されるべき。

## 関連ページ
- [Rewriting Pre-Training Data (Swallow)](./rewriting-pretraining-data.md) — 日本語中心LLMのデータ品質向上
- [FineData (HuggingFaceFW)](./huggingface-finedata.md) — 大規模オープン事前学習データ
- [Namazu Alpha](../Post_Training/namazu-alpha.md) — オープン基盤モデルの日本語事後学習適応
- [Sarashina-Embedding-v2](../Domain_Specific/sarashina-embedding-v2.md) — 日本語特化埋め込み
- [Scaling Laws of Motion Forecasting and Planning](../Physical_AI/scaling-laws-motion-forecasting-planning.md) — ドメイン横断のスケーリング則研究

## 未解決の問い
- 8B以上（70B+ 規模）でATLASの外挿は成立するか？
- 400+学習言語のうち転移行列に含まれない大多数の言語について、ATLAS係数からの外挿はどの程度信頼できるか？
- Curse of Multilinguality はモデル容量拡大（MoE等のsparsity活用）で本質的に解消可能か、それともcapacity-agnosticな情報論的限界か？
- ATLAS はencoder-only / encoder-decoder アーキテクチャでも同等に成立するか？
