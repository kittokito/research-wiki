---
id: src-deep-cross-attention
title: "DeepCrossAttention: Supercharging Transformer Residual Connections"
authors: ["Mike Heddes", "Adel Javanmard", "Kyriakos Axiotis", "Gang Fu", "MohammadHossein Bateni", "Vahab Mirrokni"]
year: 2025
url: "https://arxiv.org/abs/2502.06785"
type: paper
tags: [residual-connection, transformer, attention, architecture, training-efficiency]
date_added: 2026-04-07
status: processed
---

# DeepCrossAttention: Supercharging Transformer Residual Connections

## 概要
Transformerの残差接続における情報希薄化問題を指摘し、入力依存の学習可能な重みで各層の出力を動的に結合するDeepCrossAttention（DCA）を提案。GRNの3バリアント（v1: 次元非依存, v2: 次元依存, v3: 入力依存）を設計し、DCAではGRN-v3を3インスタンス（Q, K, V）使用して深さ方向のクロスアテンションを実現。言語モデリングで同品質を最大3倍高速に達成し、パラメータ増加はほぼゼロ。

## メモ
- cs.LG
- 2025年2月10日公開、2025年7月23日v2更新
- Google Research所属の著者陣
- LM1B, C4, ImageNet (ViT) で評価
- CC BY 4.0ライセンス
