---
title: "Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning"
aliases: ["SHLPT", "Similarity Heuristic Lifelong Prompt Tuning", "lifelong prompt tuning negative transfer"]
created: 2026-06-09
updated: 2026-06-09
tags: [prompt-tuning, PEFT, lifelong-learning, continual-learning, negative-transfer, catastrophic-forgetting]
peer_review: accepted
venue: "ACL 2024 Findings"
sources: [src-shlpt-lifelong-prompt-tuning]
---

# Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning

> **査読**: ✅ accepted — ACL 2024 Findings

Wu, Jiang, Lian (2024) — ACL 2024 Findings (pp.10944–10959)

## ソースからの事実
- lifelong prompt tuning は効率的だが**転移制約**がある: 全タスクで positive transfer を保証する万能アルゴリズムは現状不能、非類似タスクは **negative transfer** を招く [source](../../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)
- 主因は **アルゴリズム選択とタスク特性のミスアラインメント** [source](../../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)
- **SHLPT**: **学習可能な類似度メトリック**でタスクを類似/非類似の2サブセットに分割し、どちらからも有益な転移を引き出す。**parameter pool** で catastrophic forgetting に対処 [source](../../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)
- lifelong learning ベンチマークで **SOTA を上回り**、negative transfer に頑健 [source](../../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)

→ 詳細: [evidence](../../../evidence/Post_Training/shlpt-lifelong-prompt-tuning.md)

## 現時点の解釈

**prompt tuning（PEFT）を継続学習（lifelong learning）に適用したときの negative transfer と catastrophic forgetting の同時緩和**を狙う論文。本リポジトリの post-training 系の論点と複数の接点を持つ:

- **PEFT スケーリングの限界という文脈**: [When Scaling Meets LLM Finetuning](scaling-llm-finetuning.md) は「PET（prompt tuning/LoRA）のパラメータ scaling は概して効きにくく、最適手法はタスク・データ量依存」と示した。SHLPT は同じ prompt tuning でも、**タスク系列の類似性に応じて転移を出し分ける**という別軸で PEFT の有効活用を図るもので、「PEFT は万能でなくタスク特性次第」という主張の continual 版と読める。
- **catastrophic forgetting / data composition**: [SFT Data Composition (DMT)](sft-data-composition.md) は逐次学習の catastrophic forgetting と能力 conflict を data 混合で緩和した。SHLPT は parameter pool（パラメータ側）で同じ問題に対処し、緩和の手段がデータ側 vs パラメータ側で対照的。
- **タスク順序・選択の設計**: [Curriculum Instruction Tuning](../../topics/Post_Training/curriculum-instruction-tuning.md) が「データの順序・配合・難易度」を設計変数化したのに対し、SHLPT は「**タスク間の類似性**」を設計変数化して転移を制御する。
- **継続学習の別アプローチ**: [Learning, Fast and Slow (FST)](../RL/learning-fast-and-slow.md) は prompt を fast weights として継続適応する。SHLPT も prompt（PEFT）を継続学習の担い手にする点で発想が近く、negative transfer / plasticity をどう扱うかで対比できる。

## 関連ページ
- [When Scaling Meets LLM Finetuning](scaling-llm-finetuning.md) — PET（prompt tuning/LoRA）のスケーリング限界とタスク依存性
- [SFT Data Composition / DMT](sft-data-composition.md) — catastrophic forgetting をデータ混合で緩和（SHLPT はパラメータ pool で対処）
- [Curriculum Instruction Tuning](../../topics/Post_Training/curriculum-instruction-tuning.md) — タスク順序・配合の設計（SHLPT はタスク類似性の設計）
- [Learning, Fast and Slow (FST)](../RL/learning-fast-and-slow.md) — prompt を継続適応の担い手にする近縁アプローチ

## 未解決の問い
- 「学習可能な類似度メトリック」はタスク分割の誤りに対しどれだけ頑健か？ 類似度判定の失敗は転移制御の失敗に直結しないか
- prompt tuning 以外の PEFT（LoRA 等）や full finetuning でも、同じ「類似性ヒューリスティックによる転移出し分け」は有効か
- parameter pool の規模はタスク数に対しどうスケールするか（長いタスク系列でのコスト）
