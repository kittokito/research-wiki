---
id: src-paraphrase-and-solve-scop
title: "Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models"
authors: ["Yue Zhou", "Yada Zhu", "Diego Antognini", "Yoon Kim", "Yang Zhang"]
year: 2024
url: "https://aclanthology.org/2024.naacl-long.153/"
type: paper
peer_review: accepted
venue: "NAACL 2024"
tags: [mathematical-reasoning, surface-form, robustness, self-consistency, paraphrase, SCoP]
date_added: 2026-06-09
status: processed
---

# Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models

## 概要
数学問題の**表層形(surface form)**と LLM の可解性の関係を調べた論文。**表層形のわずかな変更**が答えの分布と solve rate を大きく変えることを示し、LLM の推論が表層形に敏感で**頑健性を欠く**ことを露呈。改善策として、問題の特定表層形から推論経路を多様化する **Self-Consistency-over-Paraphrases (SCoP)** を提案。4つの数学推論ベンチ×3 LLM で、vanilla self-consistency を上回り（特に当初「解けない」とされた問題で）。問題難易度と表層形の追加分析（cross-model difficulty agreement、paraphrasing transferability、Variance of Variations (VOV)）も提示。

## メモ
- NAACL 2024 Long（2024.naacl-long.153, pp.2793–2804）。Yue Zhou, Yada Zhu, Diego Antognini, Yoon Kim, Yang Zhang（IBM × MIT 系）。
- 「数値や文言を変えるだけで推論が崩れる」= GSM-Symbolic と同型の脆弱性。本リポジトリの「真の論理的理解の壁」ポジションの一角。
- ユーザー提示 URL（2024.naacl-long.153）はこの論文。
