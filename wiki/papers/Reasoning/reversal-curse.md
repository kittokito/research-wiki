---
title: "The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'"
aliases: ["Reversal Curse"]
created: 2026-04-07
updated: 2026-04-07
tags: [reversal-curse, generalization, reasoning]
sources: [src-reversal-curse]
---

# The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'

Berglund, Tong, Kaufmann, Balesni, Stickland, Korbak, Evans (2023) — arXiv 2309.12288

## ソースからの事実
- 「AはBである」で学習しても「BはAである」に自動汎化しない [source](../../../sources/Reasoning/reversal-curse.md)
- 自己回帰LLMの根本的な汎化の失敗 [source](../../../sources/Reasoning/reversal-curse.md)

→ 詳細: [evidence](../../../evidence/Reasoning/reversal-curse.md)

## 現時点の解釈
2023年の発表以来、LLMの根本的制約として広く認知された重要論文。自己回帰モデルの一方向性が双方向関係の学習を困難にする。データ拡張や双方向学習による対処が必要。

## 関連ページ
- [Mind the Gap](mind-the-gap-self-improvement.md)

## 未解決の問い
- 双方向モデルや検索拡張はReversal Curseを緩和するか？
