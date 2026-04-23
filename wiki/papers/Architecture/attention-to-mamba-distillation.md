---
title: "Attention to Mamba: A Recipe for Cross-Architecture Distillation"
aliases: ["Attention to Mamba", "Transformer-to-Mamba Distillation"]
created: 2026-04-21
updated: 2026-04-21
tags: [distillation, Mamba, SSM, Transformer, cross-architecture, efficiency, linear-attention]
peer_review: preprint
venue: ""
sources: [src-attention-to-mamba-distillation]
---

# Attention to Mamba: A Recipe for Cross-Architecture Distillation

> **査読**: 📝 preprint

Moudgil, Huang, Dhekane et al. (2026) — arXiv 2604.14191

## ソースからの事実
- 従来のナイーブなTransformer→Mamba蒸留は教師性能を保てず、AttentionとSSMを混在させたhybrid構成に頼るのが通例だった [source](../../../sources/Architecture/attention-to-mamba-distillation.md)
- 本論文は Mambaに **原理的な初期化** を施すことで、hybrid不要の純Mamba蒸留レシピを確立 [source](../../../sources/Architecture/attention-to-mamba-distillation.md)
- 二段階蒸留：(1) Transformerを **kernel trick応用のlinearized Attention** に蒸留 → (2) linearized版を **Attention非使用のadapted Mamba** に蒸留 [source](../../../sources/Architecture/attention-to-mamba-distillation.md)
- Pythia-1B teacher（perplexity 13.86）から蒸留した純Mambaで perplexity **14.11** を達成、downstream性能も保持 [source](../../../sources/Architecture/attention-to-mamba-distillation.md)

→ 詳細: [evidence](../../../evidence/Architecture/attention-to-mamba-distillation.md)

## 現時点の解釈
既存のTransformer資産（事前学習重み・訓練ノウハウ）をMambaへ移行する実務的な橋渡し論文。**hybrid 不要の純Mamba蒸留** という目標を、kernel trick でTransformerをlinear attentionに線形化した上でMambaに橋渡しする二段階設計で達成した点が貢献の本質。SSMの利点（メモリ・スループット）を享受しつつTransformerの事前学習投資を無駄にしない経路を提示しており、**長文処理・エッジ推論用途でのMamba採用加速** を意図した実用路線。ただし実証は1Bスケール止まりで、7B+/70B+スケールでの追試が産業移行判断の焦点になる。また同時期の mHC・MSA 等のアーキテクチャ拡張との併用可能性や、Mamba-2 / 新世代SSMへの手法移植性が今後の検討軸。

## 関連ページ
- [MSA: Memory Sparse Attention](./memory-sparse-attention.md) — 100Mトークンまでスケーラブルなメモリモデル
- [mHC: Manifold-Constrained Hyper-Connections](./manifold-constrained-hyper-connections.md) — HCの恒等写像特性復元
- [Continuous Autoregressive LM](./continuous-autoregressive-lm.md) — next-vector prediction
- [The Lottery Ticket Hypothesis](../Efficiency_Optimization/lottery-ticket-hypothesis.md) — 蒸留/初期化の基礎

## 未解決の問い
- 7B+ 規模以上でも教師性能保持（Δperplexity < 0.5）は維持されるか？
- Mamba-2・Mamba-3 等の新世代SSMバリアントへの移植は追加設計なしで可能か？
- 二段階蒸留のトークン配分最適解はモデルサイズ依存か、あるいは普遍定数に落ち着くか？
- 数学・コード・エージェント等のlong-chain 推論タスクで純Mamba蒸留モデルの限界はどこに現れるか？
