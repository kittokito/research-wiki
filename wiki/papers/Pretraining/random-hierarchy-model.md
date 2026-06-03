---
title: "How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model"
aliases: ["Random Hierarchy Model", "RHM", "ランダム階層モデル"]
created: 2026-06-03
updated: 2026-06-03
tags: [random-hierarchy-model, compositional-data, sample-complexity, hierarchical-representation, PCFG, feature-learning, curse-of-dimensionality]
peer_review: accepted
venue: "Physical Review X 14, 031001 (2024)"
sources: [src-random-hierarchy-model]
---

# How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model

> **査読**: ✅ accepted — Physical Review X 14, 031001（2024）

Petrini, Cagnetta, Tomasini, Favero, Wyart (2023) — EPFL / arXiv 2307.02129

## ソースからの事実
- **RHM**: 言語・画像の階層構造に着想した合成分類タスク族（PCFG 的）。深さ L、branching factor s、クラス数 n_c、**multiplicity m**（各シンボルの同義表現数）、入力次元 d = s^L [source](../../../sources/Pretraining/random-hierarchy-model.md)
- **中心結果: サンプル複雑度 P\* = n_c · m^L** — 入力次元 d=s^L に対し**多項式**で次元の呪いを回避。浅いネットは指数的 → **深さが本質** [source](../../../sources/Pretraining/random-hierarchy-model.md)
- **メカニズム**: P\* は「**同義（synonyms）の交換に不変な表現**を作るのに必要なサンプル数」と一致。低レベル特徴とクラスの相関がノイズを超えて検出可能になる点が学習閾値 [source](../../../sources/Pretraining/random-hierarchy-model.md)
- 深い CNN で経験的に検証 [source](../../../sources/Pretraining/random-hierarchy-model.md)

→ 詳細: [evidence](../../../evidence/Pretraining/random-hierarchy-model.md)

## 現時点の解釈

RHM は **「なぜ深層ネットは高次元データを少数例で学べるのか」に、合成的に解ける生成モデルで定量的に答えた**基盤論文。鍵は「データが階層的・合成的なら、サンプル複雑度は次元に対し指数でなく多項式（P\* = n_c m^L）になり、深さがその階層を段階的に潰す（synonyms を同定して各パッチを1シンボルに縮約）ために必要」という描像。本リポジトリの議論軸との接続:

- **本リポジトリの RHM クラスタの起点**: [Learn from your own latents（サンプル複雑度理論）](latent-sample-complexity.md) と [言語構造の獲得理論](language-structure-acquisition.md) はいずれも本論文の RHM/PCFG 枠組みを土台にする。前者は「latent 予測が token 予測より指数→定数でデータ効率的」、後者は「LM が相関を通じて文法の深い変数を獲得」を示し、本論文の「階層を段階的に学ぶ」描像の SSL/言語版。
- **data2vec の理論的背景**: [data2vec](data2vec.md) が自己の latent を予測して効くのは、本論文の「同義不変表現を段階構築する」過程を暗黙に行っているため、と [latent-sample-complexity](latent-sample-complexity.md) 経由で接続する。
- **「表現力 vs 学習効率」の学習効率側**: [Transformers are Inherently Succinct](../Architecture/transformers-are-inherently-succinct.md) が「Transformer は形式言語を簡潔に**表現できる**」を論じるのに対し、RHM は「階層データを何サンプルで**学習できる**か」を論じる。同じ合成・形式構造を、表現力と学習効率の両面から照らす関係。
- **構造感受性との対比**: [GSM-Symbolic](../Reasoning/gsm-symbolic.md) が「表面的パターンマッチの脆さ」を経験的に示すのに対し、RHM は「正しく階層を学べば合成構造に汎化する」条件（十分な P\*）を理論的に与える。

統計物理由来の理想化モデル（一様ランダム production rule・分類タスク）であり実データへの転移は定性的だが、**「合成性 + 深さ → 多項式サンプル複雑度」という分離を解析可能な形で確立した**意義は大きい。

## 関連ページ
- [Learn from your own latents（サンプル複雑度理論）](latent-sample-complexity.md) — RHM/PCFG 枠組みで latent 予測のデータ効率を示す（同系譜）
- [言語構造の獲得理論](language-structure-acquisition.md) — RHM を言語/LM に展開、相関と文脈窓・データ量の関係
- [data2vec](data2vec.md) — 同義不変表現の段階構築を暗黙に行う latent 予測 SSL
- [Transformers are Inherently Succinct](../Architecture/transformers-are-inherently-succinct.md) — 合成・形式構造の表現力側（本論文は学習効率側）

## 未解決の問い
- P\* = n_c m^L の多項式スケーリングは、一様ランダムでない現実の文法・画像統計でどこまで保たれるか？
- Transformer（self-attention）でも CNN と同じ「synonyms 同定 → 縮約」の階層学習が起きるか？
- 「相関がノイズを超える点 = 学習閾値」という描像は、SGD の最適化動態（いつ特徴が立ち上がるか）とどう対応するか？
