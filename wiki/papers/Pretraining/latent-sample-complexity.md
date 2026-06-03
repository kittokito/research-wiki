---
title: "Learn from your own latents and not from tokens: A sample-complexity theory"
aliases: ["Learn from your own latents", "latent prediction sample complexity", "latent予測のサンプル複雑度"]
created: 2026-06-03
updated: 2026-06-03
tags: [self-supervised-learning, sample-complexity, latent-prediction, PCFG, random-hierarchy-model, data2vec, JEPA, theory]
peer_review: preprint
venue: ""
sources: [src-latent-sample-complexity]
---

# Learn from your own latents and not from tokens: A sample-complexity theory

> **査読**: 📝 preprint

Korchinski, Favero, Wyart (2026) — arXiv 2605.27734 / Random Hierarchy Model (RHM) 系

## ソースからの事実
- **中心結果（指数 vs 定数）**: 深さ L の隠れ木の復元に、token-level/教師あり SSL は **L について指数的サンプル**を要するが、latent prediction は **L について定数（対数因子まで）** で達成 [source](../../../sources/Pretraining/latent-sample-complexity.md)
- **解析設定**: 自然言語・画像の合成構造を捉える **PCFG**（深さ L の隠れ木から可視トークン列を生成）。Favero・Wyart の **Random Hierarchy Model** 系の枠組み [source](../../../sources/Pretraining/latent-sample-complexity.md)
- **data2vec の初サンプル複雑度解析**: data2vec は**暗黙的に階層的 latent 予測を行っている**ことを示す [source](../../../sources/Pretraining/latent-sample-complexity.md)
- **H-JEPA 冗長性**: latent 予測は勾配降下で自然に階層を獲得するため、明示的階層スタック（H-JEPA）は **largely redundant** と示唆 [source](../../../sources/Pretraining/latent-sample-complexity.md)

→ 詳細: [evidence](../../../evidence/Pretraining/latent-sample-complexity.md)

## 現時点の解釈

本論文は **「token を予測するな、自己の latent を予測せよ」という SSL の経験則に、サンプル複雑度の理論的根拠を与えた**点が核心。合成的（階層的）データでは、可視トークンから隠れ木全体を直接復元するのは深さに対して指数的に難しいが、各階層で自己の潜在表現を予測すれば構造が段階的に立ち上がり、深さによらず定数サンプルで済む——という分離（separation）を示す。本リポジトリの議論軸との接続:

- **data2vec の理論的説明**: [data2vec](data2vec.md) が3モダリティで token ではなく文脈化 latent を予測して成功した経験的事実に、「それが暗黙的に階層的 latent 予測になっている」という理論を与える。経験（data2vec, 2022）→ 理論（本論文, 2026）の後付け説明という関係。
- **JEPA 設計への含意**: [V-JEPA 2](../Physical_AI/v-jepa-2.md) / [LeWM](../Physical_AI/leworldmodel.md) は latent 空間での予測を中核に据える。本論文の「H-JEPA の明示的階層は冗長」という示唆は、**単純な latent 予測でも勾配降下が自然に階層を作る**ことを意味し、アーキテクチャを過度に複雑化しない方向を後押しする（[LeWM](../Physical_AI/leworldmodel.md) が「6→1 ハイパラ削減」で示した単純化指向と整合）。
- **合成的データ理論の系譜**: PCFG/RHM を使う点は、Transformer の表現力を形式言語で論じる [Transformers are Inherently Succinct](../Architecture/transformers-are-inherently-succinct.md) と同じ「合成・形式構造で学習を理解する」潮流。前者が表現力（何を表せるか）、本論文が学習効率（何サンプルで学べるか）を扱う相補関係。
- **「表現可能性 ≠ 学習可能性」への一視点**: 多くの理論が表現力を論じるのに対し、本論文は **学習に必要なサンプル数（データ効率）** に踏み込む。LLM のデータ効率が生物学的学習者に劣るという問題意識に、目的関数（token vs latent）の選択で効くという具体的レバーを与える。

留保として、結果は PCFG という理想化モデル上のもので、実データ（自然言語・画像）への定量的転移は未検証。それでも「なぜ latent 予測が効くか」を初めて分離定理として示した意義は大きい。

## 関連ページ
- [data2vec](data2vec.md) — 本論文が解析対象とする統一 SSL フレームワーク（latent 予測の代表例）
- [V-JEPA 2](../Physical_AI/v-jepa-2.md) / [LeWorldModel (LeWM)](../Physical_AI/leworldmodel.md) — latent 予測系 SSL、H-JEPA 冗長性の示唆が直結
- [Transformers are Inherently Succinct](../Architecture/transformers-are-inherently-succinct.md) — 合成・形式構造で学習を理解する潮流（表現力 vs 学習効率の相補）

## 未解決の問い
- PCFG 上の「指数→定数」分離は、実データ（自然言語・画像）でどの程度成り立つか？対数因子は実務的サンプル数にどう効くか？
- 「H-JEPA は冗長」は、深い実モデルでも成立するか？明示的階層が有利になる条件はないか？
- ターゲット層の選び方（data2vec の上位 K 層平均）は、本理論の階層対応として最適化できるか？
