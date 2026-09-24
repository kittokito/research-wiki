---
id: src-t5-text-to-text-transformer
title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "Katherine Lee", "Sharan Narang", "Michael Matena", "Yanqi Zhou", "Wei Li", "Peter J. Liu"]
year: 2020
url: "https://arxiv.org/abs/1910.10683"
type: paper
peer_review: accepted
venue: "JMLR 2020"
tags: [T5, transfer-learning, text-to-text, pretraining, C4, encoder-decoder, denoising-objective]
date_added: 2026-06-09
status: processed
---

# Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

## 概要
**T5** の原論文。NLP のあらゆるテキストタスクを **text-to-text**（入力テキスト→出力テキスト）の統一フォーマットに変換する枠組みを導入し、**pre-training objective・モデルアーキテクチャ・unlabeled データセット・転移手法**などの要因を数十タスクで**体系的に比較**した大規模実証研究。新規データセット **C4 (Colossal Clean Crawled Corpus)** とスケールを組み合わせ、要約・QA・テキスト分類など多数のベンチマークで当時の SOTA を達成。データセット・事前学習済みモデル・コードを公開。

## メモ
- arXiv 1910.10683（提出 2019-10-23、最終改訂 2023-09-19）。**JMLR 2020** 掲載（査読付きジャーナル, vol.21）。Google。
- text-to-text 統一・C4・**denoising（span-corruption）系の事前学習目的**が望ましいという体系的知見が代表的貢献。
- 大規模 pretraining による **positive transfer** の代表例。直近追加の [A Survey on Negative Transfer](../../wiki/papers/Surveys_Overview/survey-on-negative-transfer.md) とは「転移が効く/害になる」の両面で対をなす。
- ユーザー提示 URL（arxiv 1910.10683）はこの論文。
