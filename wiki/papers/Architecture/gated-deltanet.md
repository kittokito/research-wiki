---
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
aliases: ["Gated DeltaNet", "GatedDeltaNet", "GatedDeltaNet-H1", "GatedDeltaNet-H2", "Gated Delta Rule"]
created: 2026-05-11
updated: 2026-05-11
tags: [linear-attention, delta-rule, gated-delta-rule, mamba2, deltanet, recurrent, hybrid-architecture, in-context-retrieval, length-extrapolation, chunkwise-parallel, WY-representation, NVIDIA, MIT-CSAIL]
peer_review: accepted
venue: "ICLR 2025"
sources: [src-gated-deltanet]
---

# Gated Delta Networks: Improving Mamba2 with Delta Rule

> **査読**: ✅ accepted — ICLR 2025

Songlin Yang (MIT CSAIL), Jan Kautz, Ali Hatamizadeh (NVIDIA) — arXiv 2412.06464 / GitHub: NVlabs/GatedDeltaNet

## ソースからの事実

### コア定式化：Gated Delta Rule（Eq. 10）

```
S_t = S_{t-1} (α_t (I − β_t k_t k_t^T))  +  β_t v_t k_t^T
      └─────── ① 古い情報を消去・整理 ───────┘     └─② 新しい情報を追加─┘
```

- 第1項 **① 古い情報を消去・整理**: 状態 S_{t-1} に対し **α_t（gating）と (I − β_t k_t k_t^T)（Householder-like 変換）の合成** を作用。**α_t → 0 でメモリ全消去**、**α_t → 1 で純粋な delta rule**（key 方向のみを selectively 抑制）[source: §3.1](../../../sources/Architecture/gated-deltanet.md)
- 第2項 **② 新しい情報を追加**: writing strength **β_t ∈ (0, 1)** で新しい value v_t を key k_t と outer product として書き込む [source: §3.1](../../../sources/Architecture/gated-deltanet.md)
- α_t（data-dependent scalar gating）と β_t（writing strength）の **2つのデータ依存ノブ** で、context switch（α）と selective update（β）を **独立に制御** [source: §1](../../../sources/Architecture/gated-deltanet.md)

### 統合の動機：Mamba2 と DeltaNet の相補性
- **Mamba2** (S_t = α_t S_{t-1} + v_t k_t^T) は **gating で rapid memory erasure** できるが、すべての連想を一様に decay → targeted forgetting 不可 [source: §2.1](../../../sources/Architecture/gated-deltanet.md)
- **DeltaNet** (S_t = S_{t-1}(I − β_t k_t k_t^T) + β_t v_t k_t^T) は **delta rule で targeted update** できるが、メモリ全消去機構なし → context switch で古い情報を素早く除けない [source: §2.2](../../../sources/Architecture/gated-deltanet.md)
- **両者は相補的**: gating（rapid erasure） + delta rule（targeted update）を **gated delta rule** で統合 [source: Abstract / §1](../../../sources/Architecture/gated-deltanet.md)

### Online Learning / Test-Time SGD 解釈（§3.1, Table 1）
- 各 linear RNN 系手法は **online learning objective の closed-form solution** として整理可能（Liu et al. 2024 の枠組み）
- Gated DeltaNet の online objective: **‖S_t − α_t S_{t-1}‖²_F − 2⟨S_t k_t, β_t (v_t − α_t S_{t-1} k_t)⟩**
- Test-time SGD として: S_{t+1} = S_t − β_t ∇L(S_t) = S_t (I − β_t k_t k_t^T) + β_t v_t k_t^T、**gated delta rule = adaptive weight decay (α_t) つき SGD update**（fast weight programming 視点）[source: §3.1](../../../sources/Architecture/gated-deltanet.md)

### Hardware-Efficient Chunkwise Training（§3.3）
- DeltaNet の chunkwise 並列化（Yang et al. 2024b）を gating に拡張
- **WY representation + UT transform** で cumulative Householder の matrix product を tensor core matmul に分解
- 訓練 throughput は DeltaNet とほぼ同等、Mamba2 比 marginal overhead（2-3K tokens/sec 遅い程度）[source: §4](../../../sources/Architecture/gated-deltanet.md)

### アーキテクチャ（§3.4）
- **Gated DeltaNet block**: Llama macro architecture を踏襲、self-attention を gated delta rule token mixer に置換
- Token mixer: q, k, v は **linear proj + short conv + SiLU**、q, k に **L2 norm**、α, β は linear proj のみ、出力は norm + gate + linear proj [source: §3.4](../../../sources/Architecture/gated-deltanet.md)
- **Hybrid variants**: **GatedDeltaNet-H1** (GDN + SWA) と **GatedDeltaNet-H2** (Mamba2 + GDN + SWA) [source: §3.4](../../../sources/Architecture/gated-deltanet.md)

### Single-NIAH 分析（Table 2、1.3B）
- **S-NIAH-1** (passkey, 反復合成): DeltaNet 全長で **near-perfect**（delta rule の memorization が効く）、Mamba2 は 2K 超で激減、Gated DeltaNet は両者の中間で robust
- **S-NIAH-2/3** (実エッセイ context): DeltaNet は filtering 不足で長系列で激減、Mamba2 / Gated DeltaNet は gating で irrelevant 除去 → 後者が一貫上位
- **「decay が retention を傷つけ、gating が filtering を facilitate、delta rule が memorization を helps」** [source: §3.2](../../../sources/Architecture/gated-deltanet.md)

### ベンチマーク（1.3B, FineWeb-Edu 100B tokens）
- **Language modeling + common-sense**: Gated DeltaNet が recurrent 系で **Wiki ppl 16.42 / LMB acc 46.65 / Avg 55.32** を達成、Mamba2 (54.89) / DeltaNet (52.14) を上回り [source: Table 3](../../../sources/Architecture/gated-deltanet.md)
- **GatedDeltaNet-H2**: Wiki ppl **15.91**、Hybrid 全体で Avg **56.18**（Samba 54.00、Transformer++ 52.25）[source: Table 3](../../../sources/Architecture/gated-deltanet.md)
- **In-context retrieval (real-world)**: GatedDeltaNet-H2 が SWDE 38.2 / SQD 40.4 / TQA 63.3 / Avg **40.1** で全モデル最高（Transformer++ 37.0、Samba 36.5）[source: Table 4](../../../sources/Architecture/gated-deltanet.md)
- **Length extrapolation (4K-20K)**: 6 long-context bench で **RNN 系の最低 perplexity**、Hybrid が更に改善 [source: §4 Fig. 2](../../../sources/Architecture/gated-deltanet.md)

→ 詳細: [evidence](../../../evidence/Architecture/gated-deltanet.md)

## 主要な図表

![Figure 1: Gated DeltaNet の (hybrid) アーキテクチャと block design。左が GatedDeltaNet-H1（GDN + SWA）、中央が H2（Mamba2 + GDN + SWA）、右が Gated DeltaNet token mixer の block 詳細。q/k path は linear proj + shortconv + SiLU + L2 norm、v path は linear proj + shortconv + SiLU、α/β は linear proj のみ、出力は norm + gate + linear proj。](../../../figures/Architecture/gated-deltanet/fig-1-block-design.png)
*出典: 論文 Figure 1 — Gated DeltaNet の token mixer block と2つの hybrid variants (H1, H2) の構成図。*

## 現時点の解釈

### 「gating × delta rule」という設計軸の整理
本論文の中心的洞察は、**linear RNN の状態更新を「全体 decay」と「key 方向の targeted update」の2軸に分解** し、両者を独立に制御するという **設計空間の分節化** にある。Mamba2 は前者のみ、DeltaNet は後者のみを持っていた。Gated DeltaNet は

```
S_t = S_{t-1} (α_t (I − β_t k_t k_t^T)) + β_t v_t k_t^T
```

で **α_t（context decay）と β_t（write strength）** を独立に学習させ、α=1 で DeltaNet、β→0 で Mamba2 様に縮退する **連続パラメトリックなスイートスポット** を確保した。これは [Linear Transformers (Katharopoulos 2020)](./linear-transformers.md) の純粋 outer-product 連想記憶 → DeltaNet の Householder transition → Mamba2 の selective scan という系譜の **明示的 unification** であり、本リポの efficient attention 系譜の中で最も「設計空間を可視化した」論文の1つ。

### Online Learning / Test-Time SGD 視点の重要性
本論文のもう1つの寄与は、**linear RNN の hidden state を fast weight matrix と見て、状態更新を online regression の SGD ステップとして再解釈** する Liu et al. 2024 の枠組みを gated delta rule に拡張した点。具体的には gated delta rule = **adaptive weight decay (α_t) つき SGD update** に等価で、これは concurrent work の Titans (Behrouz et al. 2024) が RNN test-time SGD update に weight decay を導入したことと **独立に同じ結論に到達**。

この視点は本リポ既存の [Attention to Mamba Distillation](./attention-to-mamba-distillation.md)（Transformer → Mamba の蒸留）や [Lightning Attention-2](./lightning-attention-2.md) の linear attention 系論文を **「test-time fast weight learning」** として統一する理論枠組みを与え、後続の [MiniMax-M1 Lightning Attention](../Technical_Report/minimax-m1.md) や [Qwen3.5-Omni Hybrid MoE](../Technical_Report/qwen35-omni.md) の hybrid attention 設計判断の理論的下敷きになっている。

### S-NIAH ケーススタディの教育的価値
Table 2 の S-NIAH-1/2/3 の解釈は **「decay hurts retention / gating facilitates filtering / delta rule helps memorization」** という3つの観察を分離して提示しており、linear RNN 系の design choice trade-off を**最も簡潔に説明する図** になっている。これは後続の hybrid attention 系論文（[DeepSeek-V4](../Technical_Report/deepseek-v4.md) の CSA+HCA や Qwen3.5-Omni の Hybrid Attention MoE）が「sparse + dense」「compression + attention」を組み合わせる動機の前哨として位置付けられる。

### Hybrid 設計が retrieval ギャップを解消
純 recurrent Gated DeltaNet は real-world retrieval で Transformer++ にまだ 6.4pt 劣る（30.6 vs 37.0 Avg）が、**H2（Mamba2 + GDN + SWA）で 40.1 と Transformer++ を上回り**、attention の local context modeling を残しつつ大半の token mixing を sub-quadratic に押し下げる Samba / Griffin 路線の有効性を再確認。これは [DeepSeek-V4](../Technical_Report/deepseek-v4.md) の **「最初の2層は sliding window のみ、残りは CSA/HCA を interleave」** や [Qwen3.5-Omni](../Technical_Report/qwen35-omni.md) の Hybrid Attention MoE の根拠と整合的。

### 立ち位置と後続への影響
本論文は **2024-12 投稿 / ICLR 2025 採択** で、その後の大規模 open-weight モデルの hybrid attention 設計の **理論的足場** を提供した。本リポ系譜での位置付け:

- 前作: [Linear Transformers](./linear-transformers.md) → DeltaNet (Schlag 2021, Yang 2024b) / Mamba2 (Dao & Gu 2024) / Longhorn (Liu 2024)
- 本論文: **gating × delta rule の unification + chunkwise hardware-efficient training + hybrid 派生**
- 後続: [Lightning Attention-2](./lightning-attention-2.md) (GPU 実装側), [MiniMax-M1 Lightning Attention](../Technical_Report/minimax-m1.md), [Attention to Mamba Distillation](./attention-to-mamba-distillation.md), [Qwen3.5-Omni Hybrid Attention MoE](../Technical_Report/qwen35-omni.md), [DeepSeek-V4 CSA+HCA](../Technical_Report/deepseek-v4.md)

特に **「α_t（decay）と β_t（write strength）を独立に学習する」** という設計原則は、後続の hybrid attention 系論文に共通する **「2つの軸を独立に制御」** という抽象パターンの祖型として読める。

## 関連ページ

- [Linear Transformers: Transformers are RNNs](./linear-transformers.md) — linear attention の理論的祖、本論文の出発点
- [Lightning Attention-2](./lightning-attention-2.md) — linear attention の GPU 実装側 SOTA、本論文と相補
- [Attention to Mamba Distillation](./attention-to-mamba-distillation.md) — Transformer → Mamba 蒸留、本論文の Gated DeltaNet も蒸留候補
- [Mixture-of-Depths Attention](./mixture-of-depths-attention.md) — 深度方向 KV attention、別軸の効率化
- [Attention Residuals](./attention-residuals.md) — Kimi Linear の attention residual、関連系譜
- [MiniMax-M1](../Technical_Report/minimax-m1.md) — lightning attention の大規模適用、Gated DeltaNet の後継的位置
- [Qwen3.5-Omni](../Technical_Report/qwen35-omni.md) — Hybrid Attention MoE、本論文の Hybrid 路線を omni-modal で実装
- [DeepSeek-V4](../Technical_Report/deepseek-v4.md) — CSA+HCA hybrid attention、別ベクトルの hybrid 系譜
- [TurboQuant](../Efficiency_Optimization/turboquant.md) — KV cache 量子化、Gated DeltaNet とは独立の効率化軸

## 未解決の問い

- β ∈ (0, 2) 拡張（negative eigenvalue で state tracking unlock、Siems et al. 2025）を Gated DeltaNet に適用した時の性能変化は？
- α_t / β_t の parameterization sensitivity の系統的 ablation
- Hybrid H2 の **Mamba2 / GatedDeltaNet / SWA の3層比率** の最適化は経験則のみ
- 70B+ frontier scale での挙動（本論文は 1.3B / 100B tokens まで）
- attention sink、partial RoPE 等の **第3の機構** との組み合わせ
- LongBench 以外の **needle-in-haystack バリエーション**（multi-hop、distractor 含む）での性能
- gated delta rule の **online learning 解釈** が他の RNN 系（RWKV, RetNet, xLSTM）にどう拡張できるか
- **chunkwise parallel form** の chunk size と性能・throughput の trade-off の系統的検証
