---
source: src-deepseek-v4
date_extracted: 2026-05-11
---

# DeepSeek-V4 (DeepSeek-AI, 2026) からの抽出

## 主要な主張

### モデル構成
- **DeepSeek-V4-Pro: 1.6T total / 49B activated per token**、43 + 18 = 61 Transformer layers, hidden d=7168 [source: §4.2.1](../../sources/Technical_Report/deepseek-v4.md)
- **DeepSeek-V4-Flash: 284B total / 13B activated per token**、43 layers, hidden d=4096 [source: §4.2.1](../../sources/Technical_Report/deepseek-v4.md)
- 両モデルとも **ネイティブ 1M トークン context** をサポート [source: Abstract](../../sources/Technical_Report/deepseek-v4.md)
- vocab 128K、MTP depth 1、MoEはDeepSeekMoE（fine-grained routed experts + shared experts）継承 [source: §4.2.1](../../sources/Technical_Report/deepseek-v4.md)
- Pro: 1 shared expert + 384 routed experts（うち6 active）、Flash: 1 shared + 256 routed（うち6 active）[source: §4.2.1](../../sources/Technical_Report/deepseek-v4.md)
- 最初の3 MoE層は **Hash routing**（入力token ID→hash関数でexpert決定）、auxiliary-loss-free load balancing は継承 [source: §2.1](../../sources/Technical_Report/deepseek-v4.md)
- routed expert weights は **FP4 precision** で配置（短期的にはFP8と同FLOPsだが将来HW で 1/3 効率改善見込み）[source: Intro](../../sources/Technical_Report/deepseek-v4.md)

### Hybrid Attention (CSA + HCA)
- 最初の2層は **pure sliding window attention**、残りは **CSA と HCA を interleave** 配置 [source: §4.2.1](../../sources/Technical_Report/deepseek-v4.md)
- **CSA (Compressed Sparse Attention)**: m トークンごとのKV cacheを1エントリに圧縮（compression rate m=4）した上で、DeepSeek Sparse Attention (DSA) で top-k に sparse selection [source: §2.3.1](../../sources/Technical_Report/deepseek-v4.md)
- CSA は **DeepSeek-V3.2 の DSA を内包する2段戦略**: compression（m倍）→ DSA top-k 選択 → core MQA。Lightning Indexer による低rank query/keyでindex score算出後top-k [source: §2.3.1](../../sources/Technical_Report/deepseek-v4.md)
- **HCA (Heavily Compressed Attention)**: m' ≫ m トークンごとのKV cacheを1エントリに圧縮（m'=128）、ただし **sparse selection は行わず dense attention を維持** [source: §2.3.2](../../sources/Technical_Report/deepseek-v4.md)
- Shared Key-Value MQA: 圧縮KV entryをkey/valueの双方として使う MQA、grouped output projection で次元削減コスト緩和 [source: §2.3.1-2.3.2](../../sources/Technical_Report/deepseek-v4.md)
- Sliding window attention をsupplementary branch として全層に併用（n_win = 128 tokens）し局所依存を補強 [source: §2.3.3](../../sources/Technical_Report/deepseek-v4.md)
- Partial RoPE（query/KVの last 64 dimensionsにのみ適用）+ **attention sink**（学習可能 sink logit を denominator に追加、attention scoreの総和を1以下に許容）[source: §2.3.3](../../sources/Technical_Report/deepseek-v4.md)
- Lightning indexer の attention 計算は **FP4 precision**、KV entries は RoPE 部分BF16 / その他 FP8 のhybrid storage で KV cache size を半減 [source: §2.3.4](../../sources/Technical_Report/deepseek-v4.md)
- BF16 GQA8 head-dim 128 を baseline とすると、DeepSeek-V4 の 1M-context KV cache は **約2%** にまで圧縮可能 [source: §2.3.4](../../sources/Technical_Report/deepseek-v4.md)

### Manifold-Constrained Hyper-Connections (mHC)
- Residual connection の幅を n_hc 倍に拡張する Hyper-Connections (HC) を **doubly stochastic matrices manifold（Birkhoff polytope）** に射影 [source: §2.2](../../sources/Technical_Report/deepseek-v4.md)
- 制約 B_l ∈ M := {M ∈ R^{n×n} | M·1_n = 1_n, 1_n^T·M = 1_n^T, M ≥ 0} により **spectral norm ‖B_l‖₂ が1で抑制**、residual transformationが non-expansive → 数値安定 [source: §2.2](../../sources/Technical_Report/deepseek-v4.md)
- 入出力射影 A_l, C_l も Sigmoid で非負性・有界性を制約し signal cancellation を回避 [source: §2.2](../../sources/Technical_Report/deepseek-v4.md)
- B_l 制約は **Sinkhorn-Knopp 反復**（t_max=20）で射影実装、Pro/Flash 共に拡張係数 **n_hc = 4** [source: §2.2 / §4.2.1](../../sources/Technical_Report/deepseek-v4.md)
- Dynamic parameterization: A_l, B_l, C_l を input-dependent component（X_l・W^pre/W^res/W^post）と static bias の和で生成、それぞれに learnable gating factor α^pre, α^res, α^post を掛ける [source: §2.2](../../sources/Technical_Report/deepseek-v4.md)

### Muon Optimizer
- Embedding/output head/RMSNorm/mHC modules/static biases/gating factors **以外** にMuonを適用、これらにはAdamW [source: §2.4 / §4.2.2](../../sources/Technical_Report/deepseek-v4.md)
- **Hybrid Newton-Schulz iterations**（10 step、最初8 step (a,b,c)=(3.4445,-4.775,2.0315) で収束、最後2 step (2,-1.5,0.5) で安定化）で orthogonalization [source: §2.4](../../sources/Technical_Report/deepseek-v4.md)
- Nesterov + RMS rescale（√max(n,m)·γ）+ weight decay、attention query/KV entry に RMSNorm 直接適用するため **QK-Clip は不要** [source: §2.4](../../sources/Technical_Report/deepseek-v4.md)

### 効率
- **1M context での single-token inference FLOPs**: V4-Pro **27%** / V4-Flash **10%**（対 DeepSeek-V3.2、equivalent FP8 FLOPs比）[source: Intro](../../sources/Technical_Report/deepseek-v4.md)
- **1M context KV cache size**: V4-Pro **10%** / V4-Flash **7%**（対 DeepSeek-V3.2）[source: Intro](../../sources/Technical_Report/deepseek-v4.md)
- BF16 GQA8 head-dim 128 baseline 比: 1M-context で **約 2%** まで KV cache 圧縮 [source: §2.3.4](../../sources/Technical_Report/deepseek-v4.md)

### Pre-training
- DeepSeek-V4-Flash: **32T tokens**、DeepSeek-V4-Pro: **33T tokens** [source: §4.2.2](../../sources/Technical_Report/deepseek-v4.md)
- 4K → 16K → 64K → **1M** へ段階的に sequence length 拡張 [source: §4.2.2](../../sources/Technical_Report/deepseek-v4.md)
- **Anticipatory Routing**: backbone は θ_t、routing indices は θ_{t-Δt}（履歴パラメータ）で計算 → routing-induced loss spike を抑制、~20% wall-clock overhead [source: §4.2.3](../../sources/Technical_Report/deepseek-v4.md)
- **SwiGLU clamping** 線形成分を [-10, 10] にクランプ、gate 上限 10 → 数値外れ値除去で安定化 [source: §4.2.3](../../sources/Technical_Report/deepseek-v4.md)
- Batch size scheduling、cosine LR decay（peak 2.7e-4 → end 2.7e-5、Pro は 2.0e-4 → 2.0e-5）[source: §4.2.2](../../sources/Technical_Report/deepseek-v4.md)
- Auxiliary-loss-free balancing bias update speed 0.001、sequence-wise balance loss weight 0.0001、MTP loss weight 0.3→0.1 [source: §4.2.2](../../sources/Technical_Report/deepseek-v4.md)

### Post-training
- **Specialist Training**: 各ドメイン（math/coding/agent/instruction-following 等）で個別の SFT + GRPO RL 訓練 → 専門家モデル群 [source: §5.1.1](../../sources/Technical_Report/deepseek-v4.md)
- **On-Policy Distillation (OPD)** で specialist 群を単一 unified model に統合（reverse KL loss）— **DeepSeek-V3.2 の mixed RL を OPD で完全置換** [source: §5.1.2 / Intro](../../sources/Technical_Report/deepseek-v4.md)
- **3つの reasoning effort mode**: **Non-think**（高速・低リスク判断、`</think>` summary）/ **Think High**（複雑問題、`<think>...</think>` summary）/ **Think Max**（推論能力境界探索、特別 system prompt で「shortcuts なし」「全 edge case 検証」を強制）[source: §5.1.1 Table 2-3](../../sources/Technical_Report/deepseek-v4.md)
- **Generative Reward Model (GRM)**: actor network 自体を GRM として共同最適化、ルーブリック誘導 RL データで判断と生成能力を統合 [source: §5.1.1](../../sources/Technical_Report/deepseek-v4.md)
- Tool-call schema を XML-based `<|DSML|tool_calls>` 形式に刷新、escaping failures 削減 [source: §5.1.1 Table 4](../../sources/Technical_Report/deepseek-v4.md)
- **FP4 quantization-aware training** for MoE expert weights + indexer QK path [source: §5.2.1](../../sources/Technical_Report/deepseek-v4.md)

### Infrastructure
- **Fine-Grained EP** scheme: experts を waves に分割し dispatch/combine/L1/L2 を fused kernel に統合、Comet比 **1.42×→1.92× 理論 speedup** [source: §3.1](../../sources/Technical_Report/deepseek-v4.md)
- **TileLang DSL**（Wang et al., 2026）で kernel 開発生産性と効率を両立 [source: §3.2](../../sources/Technical_Report/deepseek-v4.md)
- **Batch-invariant deterministic kernels**: 訓練と推論で bitwise reproducibility 保証 [source: §3.3](../../sources/Technical_Report/deepseek-v4.md)
- Hybrid ZeRO for Muon、cost-effective mHC via recomputation+fused kernels、two-stage contextual parallelism for compressed attention [source: §3.4](../../sources/Technical_Report/deepseek-v4.md)
- Heterogeneous KV cache structure + **on-disk KV cache storage** で shared-prefix reuse [source: §3.5](../../sources/Technical_Report/deepseek-v4.md)

## 主要な貢献

- DeepSeek-V3系列に対する **アーキテクチャ大改革**: hybrid CSA+HCA attention、mHC residual、Muon optimizer の3点同時導入
- 1M token context を **実用的なコスト** で支持する最初の open MoE モデル群（V3.2 比 single-token FLOPs 27%/10%、KV cache 10%/7%）
- CSA は **「compression + sparsity」の2段戦略** を確立（既存手法は片方のみ）、DSA (DeepSeek-V3.2) を内包する後継
- HCA は **「heavy compression + dense attention」** という独立軸を提示、sparse selection を捨てる代わりに圧縮率 m' を 32×（=128/4）強化
- **mHC** を 1.6T-scale MoE で **大規模実証**（Xie et al. 2025 の理論を Production scale で初実装）
- Post-training で **mixed RL → On-Policy Distillation** への移行という方法論的シフト（willccbb メタ分析の OPD ダイアル整理を実プロダクションで検証）
- **Think Max mode** で reasoning effort を system prompt 注入で制御する具体的レシピを公開
- Anticipatory Routing / SwiGLU clamping / FP4 QAT / TileLang / batch-invariant deterministic kernels 等、大規模 MoE 訓練の安定化・効率化ノウハウを多数公開
- **GitHub** に inference 実装公開: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/tree/main/inference

## ベンチマーク結果

### Base モデル比較（Table 1, evaluated under unified internal framework）
| Benchmark (Metric) | # Shots | V3.2-Base | V4-Flash-Base | V4-Pro-Base |
|---|---|---|---|---|
| # Activated Params | — | 37B | 13B | 49B |
| # Total Params | — | 671B | 284B | 1.6T |
| **World Knowledge** | | | | |
| AGIEval (EM) | 0-shot | 80.1 | 82.6 | **83.1** |
| MMLU (EM) | 5-shot | 87.8 | 88.7 | **90.1** |
| MMLU-Redux (EM) | 5-shot | 87.5 | 89.4 | **90.8** |
| MMLU-Pro (EM) | 5-shot | 65.5 | 68.3 | **73.5** |
| MMMLU (EM) | 5-shot | 87.9 | 88.8 | **90.3** |
| C-Eval (EM) | 5-shot | 90.4 | 92.1 | **93.1** |
| MultiLoKo (EM) | 5-shot | 38.7 | 42.2 | **51.1** |
| Simple-QA verified (EM) | 25-shot | 28.3 | 30.1 | **55.2** |
| FACTS Parametric (EM) | 25-shot | 27.1 | 33.9 | **62.6** |
| **Lang. & Reasoning** | | | | |
| BBH (EM) | 3-shot | **87.6** | 86.9 | 87.5 |
| DROP (F1) | 1-shot | 88.2 | 88.6 | **88.7** |
| HellaSwag (EM) | 0-shot | 86.4 | 85.7 | **88.0** |
| WinoGrande (EM) | 0-shot | 78.9 | 79.5 | **81.5** |
| **Code & Math** | | | | |
| HumanEval (Pass@1) | 0-shot | 62.8 | 69.5 | **76.8** |
| GSM8K (EM) | 8-shot | 91.1 | 90.8 | **92.6** |
| MATH (EM) | 4-shot | **60.5** | 57.4 | 64.5 |
| **Long Context** | | | | |
| LongBench-V2 (EM) | 1-shot | 40.2 | 44.7 | **51.5** |

- V4-Flash-Base（13B active / 284B total）が **V3.2-Base（37B active / 671B total）を大半のベンチで上回る**（パラメータ効率の劇的改善）
- V4-Pro-Base が全カテゴリで決定的な飛躍、特に **FACTS Parametric +35.5pt / Simple-QA +26.9pt / MultiLoKo +12.4pt** で世界知識ベンチ大幅伸長
- LongBench-V2: V3.2 40.2 → V4-Pro **51.5** で +11.3pt、1M context architecture の効果

### Post-training（DeepSeek-V4-Pro-Max, Figure 1 left）
- **SimpleQA Verified (Pass@1): 57.9%** (Claude Opus 4.6: 46.2, GPT-5.4 xHigh: 45.3, Gemini-3.1-Pro: 75.6)
- **HLE (Pass@1): 37.7%** (Claude: 40.0, GPT: 39.8, Gemini: 44.4)
- **Apex Shortlist (Pass@1): 90.2%** (Claude: 85.9, GPT: 78.1, Gemini: 89.1)
- **Codeforces (Rating): 3206** (Claude: 3168, GPT: 3052)
- **SWE Verified (Resolved): 80.6%** (Claude: 80.8, GPT: 80.6)
- **Terminal Bench 2.0 (Acc): 67.9%** (Claude: 65.4, GPT: 75.1, Gemini: 68.5)
- **Toolathlon (Pass@1): 51.8%** (Claude: 47.2, GPT: 54.6, Gemini: 48.8)
- 主張: V4-Pro-Max は open model SOTA を更新、reasoning では GPT-5.4 / Gemini-3.1-Pro に approximately 3-6 months 遅れ、世界知識ベンチでは Gemini-3.1-Pro に劣後

### 効率（Figure 1 right）
- 1M tokens 推論時 single-token FLOPs: V3.2 比 V4-Pro **3.7× lower** / V4-Flash **9.8× lower**
- Accumulated KV cache (1M sequence): V3.2 比 V4-Pro **9.5× smaller** / V4-Flash **13.7× smaller**

## 制限・注意点

- **テクニカルレポート（査読 n/a）**、HuggingFace 公開のみ。第三者再現・独立評価未完
- **"preview version"** と明記、最終版での仕様変動可能性あり
- 自己評価フレームワークでの比較が中心、公平性は要検証（特に SimpleQA・Apex Shortlist 等の知識系で Gemini-3.1 Pro に劣る部分の根拠は限定的）
- "DeepSeek-V4-Pro-Max" は post-training の Think Max effort mode の呼称、追加のモデルウェイトではない
- mHC の有効性は **本論文の規模（1.6T）でのみ実証**、Xie et al. 2025 原論文のみが小規模での先行実験で、中規模スケーリングのデータポイント不足
- FP4 expert weights の **実 HW での 1/3 効率改善は theoretical**、現行 GPU では FP8 と同 FLOPs
- Reasoning（GPT-5.4 / Gemini-3.1-Pro 比）で "approximately 3 to 6 months" のギャップを自認
- Hybrid attention の long-range dependency 実効性能（needle-in-haystack 等）は本論文では LongBench-V2 のみで評価、他の long-context benchmark での独立検証要

## 実装関連

- HuggingFace: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- Inference 実装: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/tree/main/inference
- License: MIT
- 関連: [DeepSeek-V3.2](https://github.com/deepseek-ai/DeepSeek-V3.2)（DSA の元論文）、[DeepSeekMoE Dai et al. 2024](https://arxiv.org/abs/2401.06066)、[Multi-Token Prediction](https://arxiv.org/abs/2404.19737)、[mHC Xie et al. 2025](https://arxiv.org/abs/2512.24880)、[Muon Jordan et al. 2024](https://arxiv.org/abs/2404.13196) / [Liu et al. 2025](https://arxiv.org/abs/2502.16982)
- TileLang DSL: Wang et al., 2026（kernel 開発 DSL）
- Tool-call format: 独自 `<|DSML|>` XML-based schema
