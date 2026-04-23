---
title: "Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights"
aliases: ["Neural Thickets"]
created: 2026-04-07
updated: 2026-04-07
tags: [post-training, pretrained-weights, ensemble]
peer_review: preprint
venue: ""
sources: [src-neural-thickets]
---

# Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

> **査読**: 📝 preprint

Gan, Isola (2026) — arXiv 2603.12228

## ソースからの事実
- 事前学習重みの近傍に多様なタスク固有エキスパートが密集 [source](../../../sources/Post_Training/neural-thickets.md)
- ランダムパラメータ摂動+上位K選択+多数決アンサンブルでPPO・GRPO・ESと競争力ある結果 [source](../../../sources/Post_Training/neural-thickets.md)

→ 詳細: [evidence](../../../evidence/Post_Training/neural-thickets.md)

## 現時点の解釈
勾配ベースの最適化を一切使わずランダム摂動とフィルタリングだけで競争力ある結果を得るという発見は、事前学習モデルの性質に関する深い洞察を提供。ただし実用面ではN個のモデルバリアントの保持コストが課題。

## 関連ページ
- [Simple Self-Distillation](simple-self-distillation-code.md)

## 未解決の問い
- 最適なN（摂動数）とK（選択数）の関係は？
- アンサンブルのメモリ効率化は？
