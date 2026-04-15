---
id: src-lottery-ticket-hypothesis
title: "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks"
authors: ["Jonathan Frankle", "Michael Carlin"]
year: 2018
url: "https://arxiv.org/abs/1803.03635"
type: paper
tags: [pruning, sparsity, lottery-ticket, initialization, subnetwork]
date_added: 2026-04-10
status: processed
---

# The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

## 概要
密に初期化されたフィードフォワードネットワークには、単独で訓練しても元のネットワークと同等のテスト精度に同程度のイテレーションで到達できるサブネットワーク（"winning tickets"）が含まれるという「宝くじ仮説」を提唱。標準的なプルーニング手法により、訓練を効果的にする初期重みを持つサブネットワークを自然に発見できることを示す。MNIST・CIFAR10の全結合・畳み込みアーキテクチャで、元のサイズの10-20%未満のwinning ticketを一貫して発見。

## メモ
cs.LG / cs.AI / cs.NE。MIT CSAIL。2018年3月公開。ICLR 2019 Best Paper Award。ニューラルネットワークのスパース性・プルーニング研究の転換点となった論文。
