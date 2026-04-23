---
title: "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks"
aliases: ["Lottery Ticket Hypothesis", "LTH"]
created: 2026-04-10
updated: 2026-04-10
tags: [pruning, sparsity, lottery-ticket, initialization]
peer_review: accepted
venue: "ICLR 2019"
sources: [src-lottery-ticket-hypothesis]
---

# The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

> **査読**: ✅ accepted — ICLR 2019 (Best Paper)

Frankle & Carbin (2018) — arXiv 1803.03635 — ICLR 2019 Best Paper

## ソースからの事実
- 密なネットワークにはスクラッチから訓練可能なスパースサブネットワーク（winning tickets）が存在する [source](../../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)
- 標準的なiterative magnitude pruningでwinning ticketを発見可能 [source](../../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)
- MNIST・CIFAR10で元のサイズの10-20%未満のwinning ticketを一貫して発見、元ネットワーク以上の精度・速度 [source](../../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)

→ 詳細: [evidence](../../../evidence/Efficiency_Optimization/lottery-ticket-hypothesis.md)

## 現時点の解釈
ニューラルネットワークのスパース性研究における転換点。「大きなネットワークが学習しやすいのは初期化時に"当たりくじ"のサブネットワークを含む確率が高いから」という直観を与え、プルーニング・効率化研究に新たな方向性をもたらした。後続研究（Stabilizing the Lottery Ticket Hypothesis, Linear Mode Connectivity等）で大規模モデルへの拡張が進み、現在のスパース学習・構造化プルーニング研究の基盤となっている。

## 関連ページ
- [Flash-KMeans](flash-kmeans.md)
- [TurboQuant](turboquant.md)

## 未解決の問い
- LLM規模でのLTHの成立条件は？大規模Transformerでのwinning ticketの性質はCNN時代と異なるか？
