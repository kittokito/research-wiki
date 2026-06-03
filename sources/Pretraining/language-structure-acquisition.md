---
id: src-language-structure-acquisition
title: "Towards a theory of how the structure of language is acquired by deep neural networks"
authors: ["Francesco Cagnetta", "Matthieu Wyart"]
year: 2024
url: "https://arxiv.org/abs/2406.00048"
type: paper
peer_review: accepted
venue: "NeurIPS 2024"
tags: [PCFG, language-acquisition, token-correlations, context-window, scaling-law, hierarchical-representation, random-hierarchy-model, EPFL]
date_added: 2026-06-03
status: processed
---

# Towards a theory of how the structure of language is acquired by deep neural networks

## 概要
[Random Hierarchy Model](../../wiki/papers/Pretraining/random-hierarchy-model.md) の枠組みを言語モデルに展開した理論論文。自然言語の階層構造を捉える **PCFG（tree-like 生成モデル）** 上で、**token-token 相関を解析的に導出**し、それが文法の隠れ変数（hidden variables）の表現構築に使えること——**相関の range が長いほど、対応する隠れ変数は深い**——を示す。有限の訓練集合は相関の解像度を **effective range** に制限し、その range は訓練集合サイズとともに伸びる。結果として、**より多くの例で訓練された LM は文法構造のより深い表現を構築できる**。さらに、テスト損失の訓練集合サイズに対するスケーリング則が**文脈窓（context window）長にどう依存するか**を予測し、Shakespeare・Wikipedia で経験的に検証した。

## メモ
arXiv 2406.00048、v1 2024-05。**NeurIPS 2024 採択**（Proceedings of the 38th NeurIPS）。著者は EPFL の Cagnetta & Wyart。
[RHM 原論文](../../wiki/papers/Pretraining/random-hierarchy-model.md)（PRX 2024）の言語/LM 版であり、[Learn from your own latents](../../wiki/papers/Pretraining/latent-sample-complexity.md) と同系譜。スケーリング則を扱う点で [ATLAS](../../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md) や [Scaling Behaviors of LLM RL](../../wiki/papers/RL/rl-scaling-math-qwen25.md) とも接続する。
