---
title: "Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models"
aliases: ["Mind the Gap", "Self-Improvement"]
created: 2026-04-07
updated: 2026-04-07
tags: [self-improvement, verification, generation, reasoning]
sources: [src-mind-the-gap-self-improvement]
---

# Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models

Song, Zhang, Eisenach, Kakade, Foster, Ghai (2024) — arXiv 2412.02674

## ソースからの事実
- LLMの自己改善は事前学習・事後学習・テスト時推論の各段階で機能 [source](../../../sources/Reasoning/mind-the-gap-self-improvement.md)
- モデルが自身の出力を検証→フィルタリング/重み付け→蒸留するフレームワーク [source](../../../sources/Reasoning/mind-the-gap-self-improvement.md)
- **生成よりも検証の方が容易**であることを理論的・実証的に示した [source](../../../sources/Reasoning/mind-the-gap-self-improvement.md)

→ 詳細: [evidence](../../../evidence/Reasoning/mind-the-gap-self-improvement.md)

## 現時点の解釈
「生成は難しいが検証は簡単」というギャップはLLMの自己改善の理論的基盤。このギャップが存在する限り、自己生成データのフィルタリングによる自己改善が原理的に可能。RLHFやテスト時計算スケーリングの理論的裏付けとなる重要な知見。

## 関連ページ
- [Simple Self-Distillation](../Post_Training/simple-self-distillation-code.md)
- [Neural Thickets](../Post_Training/neural-thickets.md)

## 未解決の問い
- 検証が生成より容易でないケース（検証ギャップが閉じるケース）はどのような条件で発生するか？
