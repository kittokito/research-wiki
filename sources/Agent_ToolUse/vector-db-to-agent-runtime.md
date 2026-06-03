---
id: src-vector-db-to-agent-runtime
title: "Vector DBを外したら、RAGではなくAgent Runtimeが残った"
authors: ["mofuteq"]
year: 2026
url: "https://zenn.dev/mofuteq/articles/8a2193df98ac05"
type: blog
peer_review: n/a
venue: ""
tags: [RAG, RAR, agent, runtime, LangGraph, typed-artifacts, retrieval, reasoning, design-pattern]
date_added: 2026-05-27
status: processed
---

# Vector DBを外したら、RAGではなくAgent Runtimeが残った

## 概要
著者が当初 RAG（Retrieval Augmented Generation）として構築していたシステムから Vector DB を除去した結果、残ったのは「検索 + 生成」ではなく **推論プロセスを可視化・制御・回復・検査できる Agent Runtime** だったという経験報告。これを **RAR (Retrieval Augmented Reasoning)** と呼び替え、「retrieve → generate」を「retrieve to reason」へ転換する設計パラダイムを提示。LLM を **自律的推論者ではなく、スキーマを埋める変換コンポーネント** として位置付けることで、軽量モデルでも頑健な推論が成立する。

## メモ
Zenn 公開記事。2026-05-21 公開、著者 mofuteq。
ファッション・トレンド分析（trend-to-rule）と契約レビュー（contract-question-agent）の実装経験から抽出された設計原則。
コード片は記事内には含まれず、参照リポジトリ: https://github.com/mofuteq/trend-to-rule
