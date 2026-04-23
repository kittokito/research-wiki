---
id: src-scalable-training-data-extraction
title: "Scalable Extraction of Training Data from (Production) Language Models"
authors: ["Milad Nasr", "Nicholas Carlini", "Jonathan Hayase", "Matthew Jagielski", "A. Feder Cooper", "Daphne Ippolito", "Christopher A. Choquette-Choo", "Eric Wallace", "Florian Tramèr", "Katherine Lee"]
year: 2023
url: "https://arxiv.org/abs/2311.17035"
type: paper
peer_review: accepted
venue: "ICLR 2025"
tags: [privacy, memorization, data-extraction, divergence-attack, ChatGPT, alignment-bypass]
date_added: 2026-04-15
status: processed
---

# Scalable Extraction of Training Data from (Production) Language Models

## 概要
学習データを持たない攻撃者がLLMに対してクエリを投げるだけで、学習データを逐語的に抽出できる「extractable memorization」を大規模に実証。ChatGPTに対する「divergence attack」（単一トークン単語の反復指示）により、通常時の150倍の速度で学習データが漏洩することを発見。アラインメントはメモリゼーションを除去するのではなく隠蔽するに過ぎないことを示した。

## メモ
- arXiv 2311.17035、2023年11月28日
- カテゴリ: cs.LG, cs.CL, cs.CR
- Google DeepMind、UC Berkeley、ETH Zürich等の共同研究
- Nicholas Carliniはメモリゼーション・プライバシー研究の第一人者
- 責任ある開示プロセスを経て公開（2023年8月30日にOpenAIに通知、90日後公開）
