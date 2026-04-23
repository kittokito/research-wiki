---
id: src-mixture-of-depths-attention
title: "Mixture-of-Depths Attention"
authors: ["Lianghui Zhu", "Yuxin Fang", "Bencheng Liao", "Shijie Wang", "Tianheng Cheng", "Zilong Huang", "Chen Chen", "Lai Wei", "Yutao Zeng", "Ya Wang", "Yi Lin", "Yu Li", "Xinggang Wang"]
year: 2026
url: "https://arxiv.org/abs/2603.15619"
type: paper
peer_review: preprint
venue: ""
tags: [attention, depth, signal-degradation, residual, FlashAttention, architecture]
date_added: 2026-04-07
status: processed
---

# Mixture-of-Depths Attention

## 概要
LLMの深層化に伴う信号劣化問題に対処するMixture-of-Depths Attention（MoDA）を提案。各アテンションヘッドが現在層のシーケンスKVペアと先行層の深度KVペアの両方に注意できるメカニズム。FlashAttention-2の97.3%の効率を達成しつつ、1.5Bパラメータモデルで平均perplexityを0.2改善、下流タスクで2.11%向上。

## メモ
cs.CL, cs.AI。2026年3月公開。FLOPsオーバーヘッドはわずか3.7%。
