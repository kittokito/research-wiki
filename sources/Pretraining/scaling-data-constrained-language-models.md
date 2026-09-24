---
id: src-scaling-data-constrained-language-models
title: "Scaling Data-Constrained Language Models"
authors: ["Niklas Muennighoff", "Alexander M. Rush", "Boaz Barak", "Teven Le Scao", "Aleksandra Piktus", "Nouamane Tazi", "Sampo Pyysalo", "Thomas Wolf", "Colin Raffel"]
year: 2023
url: "https://arxiv.org/abs/2305.16264"
type: paper
peer_review: accepted
venue: "NeurIPS 2023 (Oral, Outstanding Main Track Paper Runner-Up)"
tags: [data-constrained, scaling-laws, data-repetition, chinchilla, token-crisis, code-data, data-filtering, deduplication, pretraining, compute-optimal]
date_added: 2026-06-19
status: processed
---

# Scaling Data-Constrained Language Models

## 概要
高品質テキストが枯渇する「データ制約（data-constrained）」レジームで LLM をどうスケールすべきかを、**400超の学習run（10M–8.7B パラメータ・最大900Bトークン・最大1500エポック）**で実証し、**Chinchilla 則をデータ繰り返しに拡張した data-constrained scaling law** を提案・検証した記念碑的研究。中心的知見は **(1) 固定計算量下では最大~4エポックの繰り返しは新規データとほぼ同等（損失変化は無視できる）、意味ある改善は~16エポック（R\*_D≈15）まで、~40エポックで繰り返しの価値はゼロに、(2) データ制約下では Chinchilla（N と D を等比スケール）と異なり「パラメータよりエポックを速くスケール」すべき（過剰パラメータは繰り返しデータより速く価値が減衰、R\*_N < R\*_D）、(3) コードデータ混入で実効トークンを2倍にでき、フィルタリング（重複除去・perplexity）はノイズの多いデータでのみ有効**。

## メモ
- arXiv 2305.16264（v5 2025-06-28）、**NeurIPS 2023 Oral / Outstanding Main Track Paper Runner-Up**（OpenReview j5BuTrEj35）。Muennighoff・Rush・Le Scao・Piktus・Tazi・Wolf・Raffel（**Hugging Face**）、Barak（**Harvard**）、Pyysalo（**University of Turku**）。400 run のモデル・データを公開（github.com/huggingface/datablations）。
- **同時期の対論文**: [[to-repeat-or-not-to-repeat]]（Xue et al., NeurIPS 2023, arXiv 2305.13230）と**ほぼ同時投稿**の token-crisis/データ繰り返し2大論文。あちらは T5/encoder-decoder で「多エポック劣化の機序と緩和策（dropout・MoE）」、本論文は GPT-2/decoder で「データ制約下のスケーリング則と計算配分」。相補的で結論も整合（数エポックの繰り返しは無害）。
- **核心メモ**: Chinchilla の L(N,D)=A/N^α + B/D^β + E を、繰り返しで価値が指数的に減衰する**実効データ D'・実効パラメータ N'** に置き換える。D' = U_D + U_D·R\*_D·(1 − e^(−R_D/R\*_D))（U_D=ユニークトークン、R_D=繰り返し回数=エポック−1）。R\*_D≈15 が繰り返しの「半減期」。
- **実務含意**: 「データを4エポックまで回すのはほぼタダ」「データ制約下では小さめモデルを多エポック」「コードで実効データ2倍」「フィルタは汚いデータにだけ」。Galactica の 120B はデータ制約則からは過大で、もっと小さくすべきだった、と指摘。
- 著者 Raffel は [[t5-text-to-text-transformer]] の筆頭格でもあり、本実験の土台 C4 は T5 由来。
