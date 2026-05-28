---
id: src-clip
title: "Learning Transferable Visual Models From Natural Language Supervision"
authors: ["Alec Radford", "Jong Wook Kim", "Chris Hallacy", "Aditya Ramesh", "Gabriel Goh", "Sandhini Agarwal", "Girish Sastry", "Amanda Askell", "Pamela Mishkin", "Jack Clark", "Gretchen Krueger", "Ilya Sutskever"]
year: 2021
url: "https://arxiv.org/abs/2103.00020"
type: paper
peer_review: accepted
venue: "ICML 2021 (PMLR v139, pp.8748-8763)"
tags: [CLIP, contrastive-learning, vision-language, zero-shot, multimodal, foundation-model, image-text-pretraining]
date_added: 2026-04-30
status: processed
---

# Learning Transferable Visual Models From Natural Language Supervision (CLIP)

## 概要
インターネットから収集した4億の (image, text) ペアで contrastive 事前学習を行い、画像と自然言語キャプションを共有埋め込み空間で対応付ける。下流タスクは「クラス名を自然言語のテキストプロンプトに変換 → 画像埋め込みとの cosine similarity で最近傍を選ぶ」というゼロショット分類で解け、ImageNet で fully supervised の ResNet-50 と同等の精度を達成。30+ の視覚タスクで競争力を実証し、視覚-言語基盤モデル時代の出発点となった論文。

## メモ
OpenAI。arXiv 2103.00020（v1: 2021-02-26）。ICML 2021採択（PMLR v139, pp.8748-8763 / Radford et al. 2021）。コードと事前学習重みは https://github.com/openai/CLIP で公開。データセット名は WIT (WebImageText) — 4億ペア。後続の DALL-E 2、Stable Diffusion、Flamingo、LLaVA、SigLIP 等の事実上の標準テキストエンコーダ／視覚エンコーダの源流。**Multimodalカテゴリで video-models-zero-shot-learners と並ぶ基盤論文として位置付け**（CLIPは画像-テキスト、Veo 3はビデオの汎用基盤）。
