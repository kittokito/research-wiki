---
id: src-data2vec
title: "data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language"
authors: ["Alexei Baevski", "Wei-Ning Hsu", "Qiantong Xu", "Arun Babu", "Jiatao Gu", "Michael Auli"]
year: 2022
url: "https://arxiv.org/abs/2202.03555"
type: paper
peer_review: accepted
venue: "ICML 2022 (Oral)"
tags: [self-supervised-learning, masked-prediction, self-distillation, latent-prediction, multimodal, speech, vision, language, EMA-teacher]
date_added: 2026-06-03
status: processed
---

# data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language

## 概要
音声・画像・言語の3モダリティに**同一の自己教師あり学習レシピ**を適用する統一フレームワーク。各モダリティ固有の離散ターゲット（音声単位・visual token・単語）ではなく、**入力全体の文脈化された潜在表現（contextualized latent representations）を予測対象**にする。マスクした入力から、EMA で更新される teacher（self-distillation）が出力する潜在表現（上位 K 層の平均）を student が回帰予測する。標準 Transformer を用い、モダリティごとの入力前処理だけを差し替える。

## メモ
arXiv 2202.03555、v1 2022-02-07 / v3 2022-10-25。著者は Meta AI（FAIR）。**ICML 2022 Oral 採択**。
後続の data2vec 2.0（"Efficient Self-supervised Learning with Contextualized Target Representations", arXiv 2212.07525, ICML 2023）とは別論文。
予測対象を token ではなく self の latent に置く設計は JEPA 系（[V-JEPA 2](../../wiki/papers/Physical_AI/v-jepa-2.md) / [LeWM](../../wiki/papers/Physical_AI/leworldmodel.md)）と同じ系譜で、[Learn from your own latents（サンプル複雑度理論）](../../wiki/papers/Pretraining/latent-sample-complexity.md) が data2vec を「暗黙的に階層的 latent 予測を行う」と理論解析している。
