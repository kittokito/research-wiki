---
id: src-gated-deltanet
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
authors: ["Songlin Yang", "Jan Kautz", "Ali Hatamizadeh"]
year: 2025
url: "https://arxiv.org/abs/2412.06464"
type: paper
peer_review: accepted
venue: "ICLR 2025"
tags: [linear-attention, delta-rule, gated-delta-rule, mamba2, deltanet, recurrent, hybrid-architecture, in-context-retrieval, length-extrapolation, chunkwise-parallel, WY-representation, NVIDIA, MIT-CSAIL]
date_added: 2026-05-11
status: processed
---

# Gated Delta Networks: Improving Mamba2 with Delta Rule

## 概要
Songlin Yang (MIT CSAIL) × Jan Kautz / Ali Hatamizadeh (NVIDIA) による ICLR 2025 採択論文。**linear Transformer 系の retrieval 性能不足** を、(1) **Mamba2 系の gating**（適応的メモリ制御）と (2) **DeltaNet 系の delta rule**（精密なメモリ修正）の **2機構を統合する gated delta rule** で改善する。

提案する **Gated Delta Rule (Eq. 10)**:

```
S_t = S_{t-1} (α_t (I − β_t k_t k_t^T))  +  β_t v_t k_t^T
      └─────── ① 古い情報を消去・整理 ───────┘     └─② 新しい情報を追加─┘
```

- **α_t ∈ (0, 1)** はデータ依存のスカラー gating（Mamba2 由来）。α_t → 0 で **メモリ全消去**、α_t → 1 で **純粋な delta rule**（選択的更新）
- **β_t ∈ (0, 1)** は **書き込み強度**（DeltaNet 由来）。**(I − β_t k_t k_t^T)** は Householder-like な generalized transition matrix で、key 方向の古い情報を選択的に弱める
- **新情報 β_t v_t k_t^T** は古い値と新しい値の線形結合として上書き

**Online learning frame**: gated delta rule は online regression 目的関数 L(S_t) = ½‖S_t k_t − v_t‖² の test-time SGD として再解釈でき、**adaptive weight decay つき SGD update** に等価。

**ハードウェア効率実装**: Yang et al. 2024b の DeltaNet 並列化を **WY representation + chunkwise parallelism** で gating 項に拡張、tensor core matmul で hardware-efficient な訓練を維持。

**Gated DeltaNet** アーキテクチャ: Llama macro の self-attention を gated delta rule token mixer に置換。Hybrid 派生として **GatedDeltaNet-H1**（GDN + SWA）と **GatedDeltaNet-H2**（Mamba2 + GDN + SWA）も提案。

**実験**: FineWeb-Edu 100B tokens、1.3B / 400M で訓練。Mamba2 と DeltaNet を language modeling perplexity、common-sense reasoning、in-context retrieval（S-NIAH、SWDE/SQD/FDA/TQA/NQ/Drop）、length extrapolation（4K-20K の6 long-context bench）、LongBench long-context understanding で **一貫して上回り**、Hybrid 版は Transformer++ や Samba を更に上回る。Throughput は DeltaNet とほぼ同等（Mamba2 比で 2-3K tokens/sec 遅い程度の marginal overhead）。

## メモ
arXiv 2412.06464 / v1: 2024-12-09 / v3: 2025-03-06。**ICLR 2025 採択**。GitHub: https://github.com/NVlabs/GatedDeltaNet 。Equation contribution は Songlin Yang（NVIDIA インターン期間中の作業）。**本リポジトリの efficient attention 系譜** の重要中継点: [Linear Transformers (Katharopoulos 2020)](../Architecture/linear-transformers.md) → DeltaNet (Schlag 2021, Yang 2024b) / Mamba2 (Dao & Gu 2024) → **Gated DeltaNet (本論文)** → [MiniMax-M1 Lightning Attention](../Technical_Report/minimax-m1.md) や [Attention to Mamba 蒸留](./attention-to-mamba-distillation.md) の系譜。**S-NIAH の table 2 で「DeltaNet は memorization 強い／Mamba2 は filtering 強い／両者を統合した Gated DeltaNet が両取り」** という整理が清潔。Hybrid 設計（H1/H2）は Samba (Ren et al. 2024) / Griffin (De et al. 2024) の路線に位置する。Online learning + test-time SGD + adaptive weight decay の re-interpretation は本リポ既存の [On SFT, RL, on-policy distillation (Brown & Claude Opus 4.7)](../RL/willccbb-sft-rl-opd.md) の post-training メタ分析（gradient geometry の3軸）とは別軸だが、test-time fast weight programming としての linear RNN 理解を補強する。
