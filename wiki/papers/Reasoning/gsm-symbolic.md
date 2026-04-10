---
title: "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models"
aliases: ["GSM-Symbolic"]
created: 2026-04-07
updated: 2026-04-07
tags: [reasoning, math, benchmark, limitations]
sources: [src-gsm-symbolic]
---

# GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

Mirzadeh, Alizadeh, Shahrokhi, Tuzel, Bengio, Farajtabar (2024) — arXiv 2410.05229 / Apple Research

## ソースからの事実
- 同一構造の問題で数値を変えるだけでLLMの性能に大きなばらつき [source](../../../sources/Reasoning/gsm-symbolic.md)
- 無関係な節を追加すると一部モデルで65%以上の性能低下 [source](../../../sources/Reasoning/gsm-symbolic.md)
- 「現在のLLMは真の論理的推論を実行できず、学習データの推論ステップを複製している」と結論 [source](../../../sources/Reasoning/gsm-symbolic.md)

→ 詳細: [evidence](../../../evidence/Reasoning/gsm-symbolic.md)

## 現時点の解釈
GSM8Kの高スコアがLLMの数学的推論能力を過大評価している可能性を示す重要な論文。数値を変えただけで性能がばらつくという結果は、モデルがパターンマッチングに依存し真の数学的理解に至っていないことを強く示唆。ただし2024年時点の評価であり、o1/o3等の推論特化モデルやテスト時計算スケーリングがこの問題をどの程度緩和するかは要検証。

Reversal Curseと合わせて、LLMの汎化能力の根本的限界を理解する上で重要。

## 関連ページ
- [The Reversal Curse](reversal-curse.md) — LLMの汎化の根本的失敗
- [Mind the Gap](mind-the-gap-self-improvement.md) — 生成より検証が容易（自己改善の前提）
- [LLM Reasoning Failures](../Surveys_Overview/llm-reasoning-failures.md) — LLM推論失敗のサーベイ

## 未解決の問い
- o1/o3等の推論特化モデルはGSM-Symbolicでどの程度改善するか？
- テスト時計算スケーリングはパターンマッチングの限界を超えるか？
