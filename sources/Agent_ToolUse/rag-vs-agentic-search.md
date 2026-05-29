---
id: src-rag-vs-agentic-search
title: "RAGとAgentic Searchの戦争を終わらせに来た!!!"
authors: ["Hirosato Gamo"]
year: 2026
url: "https://zenn.dev/microsoft/articles/d1aa5068b432f9"
type: blog
peer_review: n/a
venue: ""
tags: [RAG, agentic-search, vector-search, CAG, context-augmented-generation, filesystem-search, graph-rag, llm-wiki, retrieval]
date_added: 2026-05-29
status: processed
---

# RAGとAgentic Searchの戦争を終わらせに来た!!!

## 概要
Microsoft の Hirosato Gamo（AI Cloud Solution Architect / Evangelist）による Zenn 記事。「RAG は終わった」という言説が SNS で拡散したことに対し、**用語の背景コンテキストが省略されたことによる誤解**を解きほぐすことを目的とする。RAG は当初「ベクトル検索を前提とする手法」を指していたが、現在は Microsoft / AWS / NVIDIA も含め「外部データを参照して生成を強化する」より広い定義に進化している。一方 Agentic Search は「ファイルシステム探索」と同一視されがちだが、本質は**推論を用いて複数回の検索を反復するアプローチ**であり、検索手段（ベクトル検索 / grep・glob 等）は限定されない。結論として「ベクトル検索 RAG は死んでおらず、対象データの性質・規模・タスクで使い分けることが大事」と整理する。

## メモ
Zenn（Microsoft publication）公開記事。公開 2026-04-08、更新 2026-04-13。
論争の発端として Anthropic の @bcherny 氏（Claude Code の初期は RAG + ローカル Vector DB を使っていたが agentic search の方が一般に有効だと判明）、Karpathy 氏の LLM Wiki 提唱、大規模コンテキスト論（CAG）を挙げて整理している。
査読対象外（個人/企業ブログのオピニオン記事）。本リポジトリ既存の [Vector DBを外したら、RAGではなくAgent Runtimeが残った](../../wiki/papers/Agent_ToolUse/vector-db-to-agent-runtime.md) および [Karpathy Wiki Workflow](../../wiki/papers/Press_Releases/karpathy-tweet.md) と同一論点クラスタ。
