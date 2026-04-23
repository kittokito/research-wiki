---
id: src-rewriting-pretraining-data
title: "Rewriting Pre-Training Data Boosts LLM Performance in Math and Code"
authors: ["Kazuki Fujii", "Yukito Tajima", "Sakae Mizuki", "Masaki Kawamura", "Hinari Shimada", "Taihei Shiotani", "Koshiro Saito", "Masanari Oi", "Taishi Nakamura", "Takumi Okamoto", "Shigeki Ishida", "Kakeru Hattori", "Youmi Ma", "Hiroya Takamura", "Rio Yokota", "Jun Sakuma", "Naoaki Okazaki"]
year: 2025
url: "https://arxiv.org/abs/2505.02881"
type: paper
peer_review: accepted
venue: "ICLR 2026"
tags: [pretraining-data, data-quality, code, math, Swallow, rewriting]
date_added: 2026-04-07
status: processed
---

# Rewriting Pre-Training Data Boosts LLM Performance in Math and Code

## 概要
公開データの体系的な改良によりLLM性能を向上させるSwallowCodeとSwallowMathデータセットを提案。SwallowCode（約16.1Bトークン）は構文検証・スタイルフィルタリング・LLMベースのリライティングでPythonコードを強化。SwallowMath（約2.3Bトークン）はボイラープレート除去と解法の再フォーマットで数学コンテンツを改善。50Bトークン予算内でLlama-3.1-8BのHumanEval pass@1を+17.0改善。

## メモ
cs.LG, cs.AI。日本のチーム（東工大、産総研等）。Swallowシリーズ。
