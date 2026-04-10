---
title: "OpenClaw-RL: Train Any Agent Simply by Talking"
aliases: ["OpenClaw-RL"]
created: 2026-04-07
updated: 2026-04-07
tags: [RL, agent, next-state-signal]
sources: [src-openclaw-rl]
---

# OpenClaw-RL: Train Any Agent Simply by Talking

Wang, Chen, Jin, Wang, Yang (2026) — arXiv 2604.01193

## ソースからの事実
- next-state信号（ユーザー返答、ツール出力、GUI状態変化）を即時オンライン学習ソースとして活用 [source](../../../sources/RL/openclaw-rl.md)
- ポリシーは全てのnext-state信号から同時に学習可能 [source](../../../sources/RL/openclaw-rl.md)

→ 詳細: [evidence](../../../evidence/RL/openclaw-rl.md)

## 現時点の解釈
エージェントRLにおけるnext-state信号の普遍性に着目した点が新規。既存システムが未活用のシグナルを学習に統合する実用的フレームワーク。

## 関連ページ
- [Agentic RL Training](../Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md)

## 未解決の問い
- next-state信号の品質はタスクにより大きく異なるか？ノイジーなnext-state信号への対処は？
