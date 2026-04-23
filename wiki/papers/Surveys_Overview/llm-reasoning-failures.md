---
title: "Large Language Model Reasoning Failures"
aliases: ["LLM Reasoning Failures"]
created: 2026-04-07
updated: 2026-04-07
tags: [LLM, reasoning, robustness, survey, formal-reasoning, informal-reasoning]
peer_review: accepted
venue: "TMLR 2026"
sources: [src-llm-reasoning-failures]
---

# Large Language Model Reasoning Failures

> **査読**: ✅ accepted — TMLR 2026

Song, Han, Goodman (2026) — TMLR 2026

## ソースからの事実
- LLMの推論失敗を二軸で分類する初の包括的サーベイ [source: §1](../../../sources/Surveys_Overview/llm-reasoning-failures.md)
- **推論タイプ軸**: Non-Embodied（Informal / Formal）と Embodied（1D / 2D / 3D） [source: §2](../../../sources/Surveys_Overview/llm-reasoning-failures.md)
- **失敗タイプ軸**: Fundamental（アーキテクチャ固有）/ Application-Specific（ドメイン固有）/ Robustness（入力摂動による不安定） [source: §2](../../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 既存の緩和策（CoT、RAG、データ拡張等）はいずれも失敗を完全排除できず、タスク固有のエンジニアリングが必須 [source: §6](../../../sources/Surveys_Overview/llm-reasoning-failures.md)

→ 詳細な主張・ベンチマーク・緩和策: [evidence](../../../evidence/Surveys_Overview/llm-reasoning-failures.md)

## 現時点の解釈
本論文はLLMの推論限界を体系的に整理した重要なレファレンスである。特に「失敗の3分類」は、LLMを実応用する際のリスク評価フレームワークとして有用。Fundamental Failuresがアーキテクチャに起因するという主張は、プロンプトエンジニアリングだけでは根本解決できない問題領域の存在を示唆しており、アーキテクチャレベルの改善やツール統合の必要性を裏付ける。

ロバストネス問題は、ベンチマーク上の高性能がそのまま実運用での信頼性を意味しないことを強く警告している。

## 関連ページ
- （関連ページが追加され次第リンク）

## 未解決の問い
- Fundamental Failuresのうち、アーキテクチャ変更で解消可能なものと本質的に困難なものの境界はどこか？
- 緩和策の組み合わせ（CoT + RAG + マルチエージェント等）による相乗効果はどの程度か？
