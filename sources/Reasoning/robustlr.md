---
id: src-robustlr
title: "RobustLR: Evaluating Robustness to Logical Perturbation in Deductive Reasoning"
authors: ["Soumya Sanyal", "Zeyi Liao", "Xiang Ren"]
year: 2022
url: "https://arxiv.org/abs/2205.12598"
type: paper
peer_review: accepted
venue: "EMNLP 2022"
tags: [deductive-reasoning, logical-robustness, logical-perturbation, negation, disjunction, diagnostic-benchmark]
date_added: 2026-06-09
status: processed
---

# RobustLR: Evaluating Robustness to Logical Perturbation in Deductive Reasoning

## 概要
自然言語で書かれた論理ルールベース上での Transformer の**演繹推論(deductive reasoning)**が、本当に論理意味を理解して行われているのかを診断する評価スイート **RobustLR** を提案。ルールベースへの**最小限の論理的編集**や**標準的な論理等価変換**に対するモデルの頑健性を測る。RoBERTa・T5 での実験で、先行研究の訓練済みモデルは RobustLR の各種摂動に**一貫した性能を示さず＝論理摂動に頑健でない**ことを確認。特に**否定(negation)と選言(disjunction)演算子の学習が困難**。演繹推論ベース言語モデルの欠点を示し、より良い論理推論モデル設計の指針を与える。データ・コード公開。

## メモ
- arXiv 2205.12598（提出 2022-05-25、v2 2022-11-08）。**EMNLP 2022 採択**。Soumya Sanyal, Zeyi Liao, Xiang Ren（USC 系）。Subjects: cs.CL/cs.LG/cs.LO。
- 「論理的に等価な言い換え・最小編集で推論が崩れる」= 論理意味の真の理解の欠如。本リポジトリの「真の論理的理解の壁」ポジションの中核。
- ユーザー提示の4本目（タイトルは "A Diagnostic Benchmark..." とも称されるが、正式タイトルは上記）。
