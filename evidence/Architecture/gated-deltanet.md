---
source: src-gated-deltanet
date_extracted: 2026-05-11
---

# Gated DeltaNet (Yang, Kautz, Hatamizadeh, 2025) からの抽出

## 主要な主張

### 問題設定
- Linear Transformer は **retrieval / long-context タスクで標準 Transformer に劣後**、recent work では gating（Mamba2 系）と delta rule（DeltaNet 系）の2系統が独立に改善を試みていた [source: §1](../../sources/Architecture/gated-deltanet.md)
- **Mamba2 の gated update** S_t = α_t S_{t-1} + v_t k_t^T は **すべての key-value 連想を一様に decay** させる → 特定の連想を targeted に忘れることができず inefficient [source: §1 / §2.1](../../sources/Architecture/gated-deltanet.md)
- **DeltaNet の delta rule** S_t = S_{t-1}(I − β_t k_t k_t^T) + β_t v_t k_t^T は **特定の key-value ペアを置換** するが、**メモリ全消去（context switch）の機構を欠く** [source: §1 / §2.2](../../sources/Architecture/gated-deltanet.md)
- **両者は complementary**: gating で rapid memory erasure、delta rule で targeted updates → 統合で両取りを狙う [source: Abstract / §1](../../sources/Architecture/gated-deltanet.md)

### Gated Delta Rule（コア定式化、Eq. 10）
```
S_t = S_{t-1} (α_t (I − β_t k_t k_t^T))  +  β_t v_t k_t^T
      └─────── ① 古い情報を消去・整理 ───────┘     └─② 新しい情報を追加─┘
```
- **α_t ∈ (0, 1)**: data-dependent scalar gating（Mamba2 由来）、状態 decay を制御 [source: §3.1](../../sources/Architecture/gated-deltanet.md)
- **β_t ∈ (0, 1)**: writing strength（DeltaNet 由来）、Siems et al. 2025 に従い β ∈ (0, 2) で negative eigenvalue を許容し state tracking 能力を unlock することも可能 [source: §2.2 footnote 2](../../sources/Architecture/gated-deltanet.md)
- **α_t → 0 でメモリ全消去**（gating 主導、context switch 対応）、**α_t → 1 で純粋な delta rule**（selective update のみ）、間で両者を連続補間 [source: §1](../../sources/Architecture/gated-deltanet.md)
- 第1項 **(I − β_t k_t k_t^T)** は generalized Householder transition matrix、key 方向の古い情報のみを selectively 抑制 [source: §2.2](../../sources/Architecture/gated-deltanet.md)

### Online Learning Frame（Liu et al. 2024 の枠組み）
- Linear RNN の recurrent state update は online learning problem の **closed-form solution** として導出可能 [source: §3.1 / Table 1](../../sources/Architecture/gated-deltanet.md)
- 各手法の online learning objective（Table 1）:
  - **LA (Linear Attention)**: ‖S_t − S_{t-1}‖²_F − 2⟨S_t k_t, v_t⟩
  - **Mamba2**: ‖S_t − α_t S_{t-1}‖²_F − 2⟨S_t k_t, v_t⟩
  - **Longhorn**: ‖S_t − S_{t-1}‖²_F − β_t ‖S_t k_t − v_t‖²
  - **DeltaNet**: ‖S_t − S_{t-1}‖²_F − 2⟨S_t k_t, β_t (v_t − S_{t-1} k_t)⟩
  - **Gated DeltaNet**: ‖S_t − α_t S_{t-1}‖²_F − 2⟨S_t k_t, β_t (v_t − α_t S_{t-1} k_t)⟩
- **Test-time SGD 解釈**: hidden state S を fast weight matrix と見て、delta rule は ½‖S_t k_t − v_t‖² の SGD ステップ。**gated delta rule = adaptive weight decay つき SGD update**（α_t が weight decay rate）[source: §3.1](../../sources/Architecture/gated-deltanet.md)
- DeltaNet は **explicit one-step gradient descent**、Longhorn は **implicit online learning**（closed-form 大域最適解）。両者は **共通の online regression 目的** を異なる方法で最適化 [source: §3.1 footnote 3](../../sources/Architecture/gated-deltanet.md)

### Hardware-Efficient Chunkwise Algorithm（§3.3）
- DeltaNet の chunkwise 並列化（Yang et al. 2024b）を gating 項に拡張 [source: §3.3](../../sources/Architecture/gated-deltanet.md)
- recurrence を partial expansion して S^r_{[t]} = S_{[t]} F^r + G^r に分解、F^r = γ^r_{[t]} P^r（cumulative Householder の gated 版）、G^r は WY representation で表現 [source: §3.3 / Eq. 3-5](../../sources/Architecture/gated-deltanet.md)
- **UT transform** で W, U を matrix 形にし、強 lower triangular の Γ ⊙ KK^T の逆を取って tensor core matmul で実装可能に [source: §3.3 / Eq. 6-9](../../sources/Architecture/gated-deltanet.md)
- 訓練 throughput は DeltaNet とほぼ同等、Mamba2 比 marginal overhead（2-3K tokens/sec 遅い程度）[source: §4 / Fig. 3](../../sources/Architecture/gated-deltanet.md)

### アーキテクチャ詳細（§3.4、Figure 1）
- **Gated DeltaNet** block: Llama macro architecture を踏襲、self-attention を **gated delta rule token mixer** に置換
- Token mixer block の構成:
  - q, k, v は linear projection + short convolution + SiLU で生成
  - q, k に **L2 normalization** を適用（訓練安定性）
  - α, β は linear projection のみ（Mamba2 の α parameterization を踏襲、α は学習可能 sigmoid）
  - 出力に normalization + gating を適用してから output projection [source: §3.4](../../sources/Architecture/gated-deltanet.md)
- **Hybrid variants**:
  - **GatedDeltaNet-H1**: Gated DeltaNet + Sliding Window Attention (SWA) を交互配置（Griffin / Samba 路線）
  - **GatedDeltaNet-H2**: Mamba2 + Gated DeltaNet + SWA の3層構成 [source: §3.4 / Fig. 1](../../sources/Architecture/gated-deltanet.md)
- Hybrid model は SWA 2K window size を採用 [source: §4](../../sources/Architecture/gated-deltanet.md)

### Single Needle-In-A-Haystack 分析（§3.2 Case Study）
- **S-NIAH-1**（pass-key retrieval, 反復合成 context）: 長期 retention をテスト
  - DeltaNet: 全長で **near-perfect**（97.4-98.8）
  - Mamba2: 2K 超で激減（99.2 → 30.4 at 8K）— **decay が早すぎて履歴を保てない**
  - Gated DeltaNet: 1K-8K で 98.4-91.8 と less severe degradation
- **S-NIAH-2/3**（real-world essay context）: 効率的なメモリ管理をテスト
  - DeltaNet: 長系列で大幅低下（filtering 能力不足、memory collision）
  - Mamba2 / Gated DeltaNet: gating で irrelevant 情報を filter
- 結論: **decay が retention を傷つけ、gating が filtering を facilitate、delta rule が memorization を helps**。Gated DeltaNet が3面とも上位 [source: §3.2 Table 2](../../sources/Architecture/gated-deltanet.md)

## 主要な貢献

1. **Gated Delta Rule の提案**: Mamba2 の gating と DeltaNet の delta rule を統合する単一の recurrent update（Eq. 10）
2. **Hardware-efficient chunkwise parallel training**: WY representation を gated delta rule に拡張、tensor core ベースの GPU 最適化を維持
3. **Online learning / test-time SGD 解釈**: gated delta rule は ½‖S_t k_t − v_t‖² の adaptive weight decay つき SGD update に等価という unified view を提示
4. **Gated DeltaNet アーキテクチャ**: Llama macro + L2 norm + short conv + Mamba2 parameterization の組み合わせで安定訓練
5. **Hybrid 派生 H1/H2**: SWA + Mamba2 と組み合わせて訓練効率と性能の両方を改善
6. **包括的評価**: language modeling / common-sense / in-context retrieval / length extrapolation / long-context understanding の5軸で Mamba2 / DeltaNet を一貫上回り
7. **オープンソース**: github.com/NVlabs/GatedDeltaNet

## ベンチマーク結果

### Language Modeling + Common-sense Reasoning（1.3B, Table 3）
| Model | Wiki ppl ↓ | LMB ppl ↓ | LMB acc ↑ | PIQA | Hella. | Wino. | ARC-e | ARC-c | SIQA | BoolQ | Avg ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Recurrent | | | | | | | | | | | |
| RetNet | 19.08 | 17.27 | 40.52 | 70.07 | 49.16 | 54.14 | 67.34 | 33.78 | **40.78** | 60.39 | 52.02 |
| HGRN2 | 19.10 | 17.69 | 39.54 | 70.45 | 49.53 | 52.80 | 69.40 | 35.32 | 40.63 | 50.66 | 51.79 |
| Mamba | 17.92 | 15.06 | 43.98 | 71.32 | 52.91 | 52.95 | 69.52 | 35.40 | 37.76 | 61.13 | 53.12 |
| Mamba2 | **16.56** | 12.56 | 45.66 | 71.87 | 55.67 | 55.24 | 72.47 | 37.88 | 40.20 | 60.13 | 54.89 |
| DeltaNet | 17.71 | 16.88 | 42.46 | 70.72 | 50.93 | 53.35 | 68.47 | 35.66 | 40.22 | 55.29 | 52.14 |
| **Gated DeltaNet** | 16.42 | 12.17 | **46.65** | **72.25** | **55.76** | **57.45** | 71.21 | **38.39** | 40.63 | 60.24 | **55.32** |
| Attention/Hybrid | | | | | | | | | | | |
| Transformer++ | 18.53 | 18.32 | 42.60 | 70.02 | 50.23 | 53.51 | 68.83 | 35.10 | 40.66 | 57.09 | 52.25 |
| Samba | 16.13 | 13.29 | 44.94 | 70.94 | 53.42 | 55.56 | 68.81 | 36.17 | 39.96 | **62.11** | 54.00 |
| GatedDeltaNet-H1 | 16.07 | 12.12 | 47.73 | 72.57 | 56.53 | 58.40 | 71.75 | 40.10 | 41.40 | 54.00 | 56.40 |
| **GatedDeltaNet-H2** | **15.91** | **12.55** | **48.76** | **72.59** | **56.88** | **57.77** | **71.33** | **39.07** | **41.91** | 61.55 | **56.18** |

### In-context Retrieval（real-world, Table 4）
| Model | SWDE | SQD | FDA | TQA | NQ | Drop | Avg |
|---|---|---|---|---|---|---|---|
| RetNet | 14.0 | 28.5 | 7.0 | 54.4 | 16.2 | 17.3 | 22.9 |
| Mamba2 | 19.1 | 33.6 | 42.5 | 61.0 | 20.8 | 19.2 | 29.8 |
| DeltaNet | 17.9 | 30.9 | 18.4 | 53.9 | 17.3 | 18.6 | 26.2 |
| **Gated DeltaNet** | **25.4** | 34.8 | 23.7 | 60.0 | 20.0 | 19.8 | **30.6** |
| Transformer++ | 29.5 | 38.0 | **52.2** | 58.3 | 22.5 | 21.6 | 37.0 |
| Samba | 33.0 | 39.2 | 50.5 | 57.7 | 23.5 | 14.9 | 36.5 |
| **GatedDeltaNet-H1** | 35.6 | 39.7 | 52.0 | 60.1 | 24.6 | 22.2 | 39.0 |
| **GatedDeltaNet-H2** | **38.2** | **40.4** | 50.7 | **63.3** | **24.8** | 23.3 | **40.1** |

- Gated DeltaNet は recurrent 系で全体最高、Hybrid 版は Transformer++ や Samba を上回り **retrieval ギャップを解消** [source: §4](../../sources/Architecture/gated-deltanet.md)
- 純 recurrent では Transformer++ にまだ及ばないが、Hybrid 化で逆転 [source: §4](../../sources/Architecture/gated-deltanet.md)

### S-NIAH（1.3B, Table 2）
| Model | S-NIAH-1 (1K/2K/4K/8K) | S-NIAH-2 (1K/2K/4K/8K) | S-NIAH-3 (1K/2K/4K/8K) |
|---|---|---|---|
| DeltaNet | 97.4/96.8/**99.0**/98.8 | 98.4/45.6/18.6/14.4 | **85.2**/47.0/22.4/(small) |
| Mamba2 | **99.2**/**98.8**/65.4/30.4 | 99.4/**98.8**/56.2/17.0 | 64.4/47.6/4.6/(small) |
| **Gated DeltaNet** | 98.4/88.4/91.4/91.8 | **100.0**/**99.8**/**92.2**/**29.6** | **86.6**/**84.2**/**27.6**/(small) |

### Length Extrapolation（Figure 2）
- 4K-20K の6 long-context benchmark（GovReport / QMSum / NarrativeQA / Qasper / CodeParrot / PG19）で perplexity 評価
- Gated DeltaNet は **RNN models 中で最低 overall perplexity**、relative robustness を示す
- Hybrid models は attention を local context modeling に使うことで更に改善 [source: §4](../../sources/Architecture/gated-deltanet.md)

### LongBench long-context understanding（Table 5）
- Gated DeltaNet が single-doc QA / few-shot in-context learning / Code tasks で recurrent models 中で consistent advantage [source: §4](../../sources/Architecture/gated-deltanet.md)

## 制限・注意点

- 純 recurrent Gated DeltaNet は **real-world retrieval** で Transformer++ にまだ届かない（30.6 vs 37.0 平均）、Hybrid 化必須
- 評価規模が 1.3B / 100B tokens で、本格的 frontier scale（70B+ / 数 T tokens）での挙動は未検証
- α_t / β_t parameterization の sensitivity・ablation は限定的
- **3つ目の機構（attention sink、partial RoPE 等）** との組み合わせは未探索
- DeltaNet の β ∈ (0, 2) 拡張（negative eigenvalue で state tracking unlock、Siems et al. 2025）は本論文では試していない（footnote のみ）
- S-NIAH 表で DeltaNet が S-NIAH-1 で Mamba2 を上回る理由が **decay の有無** に集約されているが、parameterization 違いによる effect の切り分けは限定的
- Hybrid H2 の Mamba2 + GatedDeltaNet + SWA の3層構成の比率最適化は系統的でない（経験則）

## 実装関連

- **GitHub**: https://github.com/NVlabs/GatedDeltaNet
- 訓練: AdamW, peak LR 4e-4, weight decay 0.1, gradient clipping 1.0, cosine LR with 1B token warmup, batch 0.5M tokens
- 1.3B / 400M、FineWeb-Edu 100B tokens
- Llama2 tokenizer (vocab 32K)、訓練長 4K（Hybrid は SWA window 2K）
- Code: Triton + FLA-style chunkwise kernel
- 関連先行: [Linear Transformers (Katharopoulos 2020)](../Architecture/linear-transformers.md), DeltaNet (Schlag 2021a), Yang et al. 2024a (GLA), Yang et al. 2024b (DeltaNet chunkwise), Mamba2 (Dao & Gu 2024), Longhorn (Liu et al. 2024)
- 後続: Hybrid 路線は [MiniMax-M1 Lightning Attention](../Technical_Report/minimax-m1.md) や [Attention to Mamba Distillation](../Architecture/attention-to-mamba-distillation.md), [Qwen3.5-Omni Hybrid MoE](../Technical_Report/qwen35-omni.md), [DeepSeek-V4 CSA+HCA](../Technical_Report/deepseek-v4.md) と接続
