---
title: "data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language"
aliases: ["data2vec", "統一自己教師あり学習", "latent prediction SSL"]
created: 2026-06-03
updated: 2026-06-03
tags: [self-supervised-learning, masked-prediction, self-distillation, latent-prediction, multimodal, EMA-teacher]
peer_review: accepted
venue: "ICML 2022 (Oral)"
sources: [src-data2vec]
---

# data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language

> **査読**: ✅ accepted — ICML 2022（Oral）

Baevski, Hsu, Xu, Babu, Gu, Auli (2022) — Meta AI (FAIR) / arXiv 2202.03555

## ソースからの事実
- **モダリティ非依存の統一 SSL レシピ**: 音声・画像・言語に同一の方法を適用（違いは入力前処理とマスク戦略のみ） [source](../../../sources/Pretraining/data2vec.md)
- **予測対象 = 自己の文脈化潜在表現**: 離散トークンではなく、入力全体に基づく contextualized latent representations を回帰予測 [source](../../../sources/Pretraining/data2vec.md)
- **self-distillation**: teacher = student 重みの EMA。マスク入力の student 表現から、マスクなしを見た teacher の表現（上位 K 層平均）を予測 [source](../../../sources/Pretraining/data2vec.md)
- **結果**: ImageNet-1K で同規模 ViT の masked prediction を上回り、LibriSpeech で wav2vec 2.0/HuBERT を上回り、GLUE で RoBERTa に匹敵 [source](../../../sources/Pretraining/data2vec.md)

→ 詳細: [evidence](../../../evidence/Pretraining/data2vec.md)

## 現時点の解釈

data2vec の本質は **「何を予測するか」を離散トークンから自己の連続潜在表現へ移したこと**。これにより、モダリティ固有の語彙設計（音声単位・visual codebook・サブワード）を捨てて単一レシピで3領域を統一できた。本リポジトリの議論軸との接続:

- **JEPA 系譜の中核**: 「自己の latent を予測する」設計は [V-JEPA 2](../Physical_AI/v-jepa-2.md) や [LeWM](../Physical_AI/leworldmodel.md) と同じ predictive SSL の系譜。data2vec はこの系譜を speech/vision/language で先行実証した位置づけ。
- **理論的裏付け**: [Learn from your own latents（サンプル複雑度理論）](latent-sample-complexity.md) は、data2vec が **暗黙的に階層的 latent 予測を行っている**ことを示し、token 予測が深さ L に対して指数的サンプルを要するのに対し latent 予測は（対数因子まで）定数で済むと証明。data2vec の経験的成功に理論的説明を与える論文。
- **対照: contrastive/対照学習との違い**: [CLIP](../Multimodal/clip.md) が (image,text) ペアの contrastive で表現を学ぶのに対し、data2vec は単一モダリティ内の masked latent regression。教師信号の作り方（対照 vs 自己蒸留回帰）の対比として読める。

実務的には、後続の **data2vec 2.0（ICML 2023, arXiv 2212.07525）で計算効率が大幅改善**されているため、効率面ではそちらを参照すべき。本論文は「token を捨てて latent を予測する」という設計原理を確立した起点として重要。

## 関連ページ
- [Learn from your own latents（サンプル複雑度理論）](latent-sample-complexity.md) — data2vec を理論解析し、latent 予測の指数→定数のサンプル効率を証明
- [V-JEPA 2](../Physical_AI/v-jepa-2.md) — 動画での predictive SSL（同じ「latent を予測」系譜）
- [LeWorldModel (LeWM)](../Physical_AI/leworldmodel.md) — raw pixels からの JEPA、next-embedding prediction
- [CLIP](../Multimodal/clip.md) — 対照学習による表現学習との対比

## 未解決の問い
- 「上位 K 層平均の文脈化ターゲット」が効く理由は何か？層選択は理論的に最適化できるか（[サンプル複雑度理論](latent-sample-complexity.md) の階層対応と接続するか）？
- self-distillation（EMA teacher）の collapse 回避は、どの程度がアーキ依存・ハイパラ依存か？
- cross-modal（モダリティ横断）への拡張は、統一レシピの利点を保ったまま可能か？
