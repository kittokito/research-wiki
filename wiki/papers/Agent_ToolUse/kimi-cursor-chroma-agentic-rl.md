---
title: "How Kimi, Cursor, and Chroma Train Agentic Models with RL"
aliases: ["Agentic RL Training"]
created: 2026-04-07
updated: 2026-04-07
tags: [RL, agent, training, production]
peer_review: n/a
venue: ""
sources: [src-kimi-cursor-chroma-agentic-rl]
---

# How Kimi, Cursor, and Chroma Train Agentic Models with RL

> **査読**: — n/a（ブログ記事）

Schmid (2026) — philschmid.de Blog

## ソースからの事実
- Kimi K2.5: 並列エージェントオーケストレーション [source](../../../sources/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md)
- Cursor Composer 2: 自己要約+本番データからのリアルタイムRL [source](../../../sources/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md)
- Chroma Context-1: 文書プルーニングによる能動的コンテキスト管理学習 [source](../../../sources/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md)
- 3システムとも本番環境学習・成果ベース報酬・大規模非同期ロールアウトを共有 [source](../../../sources/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md)

→ 詳細: [evidence](../../../evidence/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md)

## 現時点の解釈
エージェントRLの実用化が進んでいることを示す良い概観記事。本番環境での学習と成果ベース報酬という共通パターンは、エージェントRL設計のベストプラクティスとして注目に値する。

## 関連ページ
- [Kimi K2.5](../Technical_Report/kimi-k25.md)
- [OpenClaw-RL](../RL/openclaw-rl.md)

## 未解決の問い
- 本番環境での学習のリスク管理は？
