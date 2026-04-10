---
title: "DeepSeek-R1"
aliases: ["DeepSeek-R1-Zero"]
created: 2026-04-08
updated: 2026-04-08
tags: [RLVR, reasoning, DeepSeek, pure-RL, self-verification, reflection]
sources: [src-deepseek-r1]
---

# DeepSeek-R1

## ソースからの事実
- DeepSeek-V3-Baseに対しSFTなしのpure RLでreasoning capabilityが大幅に向上 [source](../../../sources/RL/deepseek-r1.md)
- R1-Zeroでself-verification・reflectionが自然に出現 [source](../../../sources/RL/deepseek-r1.md)
- 人間が書いたCoTをなぞっただけでは説明しにくい挙動が報告 [source](../../../sources/RL/deepseek-r1.md)

→ 詳細: [evidence](../../../evidence/RL/deepseek-r1.md)

## 現時点の解釈

Pure RLで高度な推論能力が獲得可能であることを示した重要な実例。「人間データを全く超えない」とは言えない証拠を提供するが、「base modelの外側への脱出」なのか「base modelのtailの活性化」なのかは厳密には未決。RLVRの能力境界論争において、expansion側の最も強い実証例の一つ。

## 関連ページ
- [[rlvr-capability-boundary]] — RLVRの能力境界に関するトピック総合

## 未解決の問い
- R1-Zeroの新しい推論パターンはbase modelのtailに完全に帰属できるか？
