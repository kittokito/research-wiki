---
id: src-scaling-llm-finetuning
title: "When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method"
authors: ["Biao Zhang", "Zhongtao Liu", "Colin Cherry", "Orhan Firat"]
year: 2024
url: "https://arxiv.org/abs/2402.17193"
type: paper
peer_review: accepted
venue: "ICLR 2024"
tags: [scaling-law, finetuning, PEFT, LoRA, prompt-tuning, full-model-tuning, data-efficiency, machine-translation, summarization]
date_added: 2026-06-03
status: processed
---

# When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method

## 概要
LLM のファインチューニング性能が、**(1) LLM モデルサイズ・(2) 事前学習データサイズ・(3) ファインチューニングパラメータ数・(4) ファインチューニングデータサイズ**の各スケーリング因子にどう依存するかを体系的に調べ、**ファインチューニングデータサイズと各因子の間に power-based の乗法的結合スケーリング則（multiplicative joint scaling law）**が成立することを示した論文。Full-Model Tuning (FMT) と Parameter-Efficient Tuning (PET = prompt tuning / LoRA) を比較。主要知見は、(a) **LLM のファインチューニングは事前学習データのスケーリングより LLM モデルサイズのスケーリングから恩恵を受ける**、(b) **PET のパラメータ数スケーリングは概して効きにくい**、(c) **最適なファインチューニング手法はタスクとファインチューニングデータ量に強く依存する**（低データでは PET 有利等）。

## メモ
arXiv 2402.17193、v1 2024-02-27。**ICLR 2024 採択**。著者は Google DeepMind（Biao Zhang, Colin Cherry, Orhan Firat ら）。
実験は 1B〜16B のバイリンガル LLM、bilingual 機械翻訳・多言語要約、データ制限レジームで実施。
ファインチューニングのデータ・手法の選択を扱う点で [SFT Data Composition / DMT](../../wiki/papers/Post_Training/sft-data-composition.md) や [Curriculum Instruction Tuning](../../wiki/topics/Post_Training/curriculum-instruction-tuning.md) と直結し、スケーリング則を扱う点で [言語構造の獲得理論](../../wiki/papers/Pretraining/language-structure-acquisition.md) / [ATLAS](../../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md) と接続する。
