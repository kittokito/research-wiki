---
title: "Potemkin Understanding in Large Language Models"
aliases: ["Potemkin Understanding", "potemkins", "illusion of understanding"]
created: 2026-06-09
updated: 2026-06-09
tags: [understanding, conceptual-coherence, benchmark-validity, evaluation, reasoning]
peer_review: accepted
venue: "ICML 2025"
sources: [src-potemkin-understanding]
---

# Potemkin Understanding in Large Language Models

> **査読**: ✅ accepted — ICML 2025

Mancoridis, Weeks, Vafa, Mullainathan (2025) — PMLR v267

## ソースからの事実
- ベンチマークから能力を推論できるのは、LLM が**人間と同じ仕方で**概念を取り違える場合に限り妥当。さもなくば正解は **potemkin understanding（理解の幻想）** [source](../../../sources/Reasoning/potemkin-understanding.md)
- potemkin を定量化する2手続き（3ドメインの専用ベンチ／下限を与える一般手続き）を提示 [source](../../../sources/Reasoning/potemkin-understanding.md)
- **potemkin はモデル・タスク・ドメインを問わず遍在**し、失敗は**概念表現の深い内的非一貫性(internal incoherence)** を反映 [source](../../../sources/Reasoning/potemkin-understanding.md)

→ 詳細: [evidence](../../../evidence/Reasoning/potemkin-understanding.md)

## 現時点の解釈

「ベンチで解ける＝理解している」という**評価の前提そのもの**を崩す論文で、本リポジトリの [LLMと真の論理的理解の壁](../../topics/Reasoning/llm-logical-understanding-wall.md) ポジションの中核。表層的に正解しても概念表現が内的に非一貫——という主張は、[GSM-Symbolic](gsm-symbolic.md)（数値変更で崩れる）・[Paraphrase and Solve](paraphrase-and-solve-scop.md)（表層形で崩れる）・[RobustLR](robustlr.md)（論理摂動で崩れる）が示す「脆弱性」の、**メタ評価レベルでの一般化**として読める。

また「尺度がモデルの実態を捉え損なう」という点で [Your Evals Will Break](../Evaluation/your-evals-will-break.md) と問題意識を共有し、[LLM Reasoning Failures](../Surveys_Overview/llm-reasoning-failures.md) サーベイの失敗類型に「理解の幻想」という診断軸を加える。

## 関連ページ
- [[llm-logical-understanding-wall]] — 本論文を含むポジション
- [GSM-Symbolic](gsm-symbolic.md) / [Paraphrase and Solve (SCoP)](paraphrase-and-solve-scop.md) / [RobustLR](robustlr.md) — 摂動への脆弱性の具体例
- [Your Evals Will Break](../Evaluation/your-evals-will-break.md) — 評価尺度がモデルの実態を捉え損なう問題
- [LLM Reasoning Failures](../Surveys_Overview/llm-reasoning-failures.md) — 推論失敗の包括サーベイ

## 未解決の問い
- 「人間の誤解パターンと一致するか」を妥当性基準とする枠組みは、どこまで一般化できるか
- internal incoherence は学習・スケールで縮減するのか、それとも質的な壁か
