---
id: src-fromage
title: "Grounding Language Models to Images for Multimodal Inputs and Outputs (FROMAGe)"
authors: ["Jing Yu Koh", "Ruslan Salakhutdinov", "Daniel Fried"]
year: 2023
url: "https://arxiv.org/abs/2301.13823"
type: paper
peer_review: accepted
venue: "ICML 2023 (PMLR v202)"
tags: [FROMAGe, frozen-LLM, multimodal, image-retrieval, vision-language, in-context-learning, OPT, CLIP]
date_added: 2026-04-30
status: processed
---

# Grounding Language Models to Images for Multimodal Inputs and Outputs (FROMAGe)

## 概要
凍結された text-only LLM（OPT-6.7B）と凍結された画像エンコーダ（CLIP ViT-L/14）を **線形マッピング層のみで結合** し、interleaved な image-and-text 入力を処理して、テキストと **検索された画像** を交互に生成できるモデル FROMAGe（Frozen Retrieval Over Multimodal data for Autoregressive Generation）を提案。学習可能なパラメータは数百万（全体の0.1%未満）、Conceptual Captions のみで訓練。LLMの in-context learning 能力をそのまま継承し、zero-shot で contextual image retrieval、multi-turn dialogue with images、visual storytelling を実現。

## メモ
著者: Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried — Carnegie Mellon University。arXiv 2301.13823（v1: 2023-01-31, v4: 2023-06-13）。**ICML 2023採択**（arXiv Comments に明記、PMLR v202）。プロジェクトページ: https://jykoh.com/fromage 、コード: https://github.com/kohjingyu/fromage 。後の vision-language 研究（GILL, Emu, Anole 等）で「凍結LLM + 軽量結合層」レシピの参照点。CLIPの後継として「事前学習済み視覚-言語モデルを **生成** 側に拡張する」流れを切り開いた論文の一つ。
