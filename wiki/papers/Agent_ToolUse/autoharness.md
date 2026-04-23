---
title: "AutoHarness: improving LLM agents by automatically synthesizing a code harness"
aliases: ["AutoHarness"]
created: 2026-04-07
updated: 2026-04-07
tags: [agent, code-synthesis, harness]
peer_review: workshop
venue: "ICLR 2026 Workshop on Recursive Self-Improvement"
sources: [src-autoharness]
---

# AutoHarness: improving LLM agents by automatically synthesizing a code harness

> **査読**: 📋 workshop — ICLR 2026 Workshop on Recursive Self-Improvement

Lou, Lázaro-Gredilla, Dedieu, Wendelken, Lehrach, Murphy (2026) — arXiv 2603.09229

## ソースからの事実
- Gemini-2.5-Flashが反復改良でLLM周りの保護コード構造を自動合成 [source](../../../sources/Agent_ToolUse/autoharness.md)
- 小さなモデルがGemini-2.5-Proを凌駕可能 [source](../../../sources/Agent_ToolUse/autoharness.md)
- ランタイムLLM呼び出し排除の完全コードポリシー生成を実現 [source](../../../sources/Agent_ToolUse/autoharness.md)

→ 詳細: [evidence](../../../evidence/Agent_ToolUse/autoharness.md)

## 現時点の解釈
「コードとしてのポリシー」は推論コストの根本的削減を実現する興味深いアプローチ。小さなモデルが大きなモデルを超えるという結果は、エージェント性能がモデルサイズだけでなく実行環境の構造化に大きく依存することを示唆。

## 関連ページ
- [Self-Organizing LLM Agents](self-organizing-llm-agents.md)
- [OpenClaw-RL](../RL/openclaw-rl.md)

## 未解決の問い
- TextArena以外の環境でのcode-as-policyの汎用性は？
