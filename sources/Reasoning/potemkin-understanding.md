---
id: src-potemkin-understanding
title: "Potemkin Understanding in Large Language Models"
authors: ["Marina Mancoridis", "Bec Weeks", "Keyon Vafa", "Sendhil Mullainathan"]
year: 2025
url: "https://proceedings.mlr.press/v267/mancoridis25a.html"
type: paper
peer_review: accepted
venue: "ICML 2025"
tags: [understanding, conceptual-coherence, benchmark-validity, evaluation, reasoning, potemkin]
date_added: 2026-06-09
status: processed
---

# Potemkin Understanding in Large Language Models

## 概要
LLM のベンチマーク正解が**真の概念理解**を意味するのかを問う論文。ベンチマーク（AP試験等）は本来「人間の誤解パターン」を前提に妥当性が成立するが、LLM が人間とは**異なる仕方で**概念を取り違える場合、正解は **potemkin understanding（理解の幻想）**——どの人間の解釈とも整合しない答えに駆動された見せかけの理解——に過ぎない。potemkin の存在を定量化する2手続き（3ドメインの専用ベンチ／下限を与える一般手続き）を提示し、**potemkin はモデル・タスク・ドメインを問わず遍在**すると報告。さらにこれらの失敗は単なる誤りではなく、**概念表現の深い内的非一貫性(internal incoherence)** を反映すると示す。

## メモ
- ICML 2025（PMLR v267, mancoridis25a）。Marina Mancoridis, Bec Weeks, Keyon Vafa, Sendhil Mullainathan。
- 「ベンチで解ける＝理解している」という推論の妥当性そのものを揺らす評価論であり、本リポジトリの「LLMと真の論理的理解の壁」ポジションの中核。
- ユーザー提示 URL（PMLR v267 mancoridis25a）はこの論文。
