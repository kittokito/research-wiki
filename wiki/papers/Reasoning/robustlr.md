---
title: "RobustLR: Evaluating Robustness to Logical Perturbation in Deductive Reasoning"
aliases: ["RobustLR", "logical perturbation robustness", "deductive reasoning robustness"]
created: 2026-06-09
updated: 2026-06-09
tags: [deductive-reasoning, logical-robustness, logical-perturbation, negation, disjunction, diagnostic-benchmark]
peer_review: accepted
venue: "EMNLP 2022"
sources: [src-robustlr]
---

# RobustLR: Evaluating Robustness to Logical Perturbation in Deductive Reasoning

> **査読**: ✅ accepted — EMNLP 2022

Sanyal, Liao, Ren (2022) — USC / arXiv 2205.12598

## ソースからの事実
- Transformer は自然言語ルールベース上で演繹推論を行えるが、**論理意味を真に理解して**いるかは不明——という問いに **RobustLR**（最小論理編集・論理等価変換への頑健性を測る評価スイート）で答える [source](../../../sources/Reasoning/robustlr.md)
- RoBERTa・T5 は RobustLR の各摂動に**一貫した性能を示さず＝論理摂動に頑健でない** [source](../../../sources/Reasoning/robustlr.md)
- 特に**否定(negation)と選言(disjunction)の学習が困難** [source](../../../sources/Reasoning/robustlr.md)

→ 詳細: [evidence](../../../evidence/Reasoning/robustlr.md)

## 現時点の解釈

「論理的に**等価な言い換え・最小編集**で結論が崩れる」ことを示し、モデルが論理意味でなく**表層パターン**に依存していると論証した、[LLMと真の論理的理解の壁](../../topics/Reasoning/llm-logical-understanding-wall.md) ポジションの**演繹論理**側の中核証拠。[Paraphrase and Solve](paraphrase-and-solve-scop.md)（数学・表層形）/ [GSM-Symbolic](gsm-symbolic.md)（数値）が**算術・語彙**の摂動で示した脆弱性を、**形式論理(否定・選言・含意)** の水準で示した点が固有の貢献。

否定・選言という基本演算子の学習困難は、[The Reversal Curse](reversal-curse.md)（"A is B"→"B is A" の非対称）と並ぶ「LLM が論理構造の対称性・結合を内在化できていない」証拠群を成す。2022年・RoBERTa/T5 対象のため現代 LLM での再検証は要るが、論理摂動という診断軸は今も有効。

## 関連ページ
- [[llm-logical-understanding-wall]] — 本論文を含むポジション
- [The Reversal Curse](reversal-curse.md) — 論理的対称性（A is B ↔ B is A）の不成立
- [Paraphrase and Solve (SCoP)](paraphrase-and-solve-scop.md) — 表層形摂動（数学）
- [GSM-Symbolic](gsm-symbolic.md) — 数値摂動（数学）
- [Potemkin Understanding](potemkin-understanding.md) — 脆弱性のメタ評価的一般化

## 未解決の問い
- 現代の大規模 LLM・推論特化モデルは RobustLR の論理摂動にどこまで頑健になったか
- negation/disjunction の学習困難は、データ・目的関数・アーキテクチャのどれで緩和されるか
