---
title: "Qwen3 Technical Report"
aliases: ["Qwen3", "Qwen3-235B-A22B", "Qwen3-30B-A3B", "Qwen3-32B"]
created: 2026-05-11
updated: 2026-05-11
tags: [technical-report, open-weight, dense, MoE, multilingual, thinking-mode, thinking-budget, strong-to-weak-distillation, GRPO, Qwen, QK-Norm, multi-stage-pretraining, instance-level-data-mixture, synthetic-data, Apache-2.0]
peer_review: n/a
venue: ""
sources: [src-qwen3]
---

# Qwen3 Technical Report

> **査読**: — n/a（テクニカルレポート、arXiv 2505.09388 / Apache 2.0）

Qwen Team (2025) — arXiv 2505.09388 / GitHub: QwenLM/Qwen3

## ソースからの事実

### モデル構成
- **6 dense + 2 MoE = 8 モデル、Apache 2.0** で公開 [source: §2](../../../sources/Technical_Report/qwen3.md)
- **Qwen3-235B-A22B** (flagship MoE): 235B total / 22B active、94 layers、Q/KV heads 64/4、128 experts (8 active)、context 128K [source: §2 Table 2](../../../sources/Technical_Report/qwen3.md)
- **Qwen3-30B-A3B** (軽量 MoE): 30B/3B active、48 layers、Q/KV 32/4、128 experts (8 active)、128K [source: §2 Table 2](../../../sources/Technical_Report/qwen3.md)
- Dense: 0.6B/1.7B (32K), 4B/8B/14B/32B (**128K**)、4B 以下は tie embedding [source: §2 Table 1](../../../sources/Technical_Report/qwen3.md)

### アーキテクチャ
- Dense は Qwen2.5 を踏襲: **GQA + SwiGLU + RoPE + pre-RMSNorm** [source: §2](../../../sources/Technical_Report/qwen3.md)
- **QKV-bias 除去**（Qwen2 から）、**QK-Norm**（attention QK の softmax 前 RMSNorm）を導入 → 訓練安定 [source: §2](../../../sources/Technical_Report/qwen3.md)
- MoE は **fine-grained expert segmentation**（128 total / 8 active）、**Qwen2.5-MoE と異なり shared expert を廃止**、**global-batch load balancing loss** で expert 特化を促進 [source: §2](../../../sources/Technical_Report/qwen3.md)
- BBPE tokenizer (vocab 151,669) [source: §2](../../../sources/Technical_Report/qwen3.md)

### Pre-training データ戦略
- **36T tokens / 119 言語**（Qwen2.5 比でトークン数 2×、言語数 4×、Qwen2.5 は 29 言語）[source: §3.1](../../../sources/Technical_Report/qwen3.md)
- **データ拡充パイプライン**: (1) **Qwen2.5-VL** で PDF 様文書から text recognition、(2) **Qwen2.5** で抽出結果を refine、(3) **Qwen2.5-Math / Qwen2.5-Coder** で domain-specific 合成データ生成（textbook / Q&A / instructions / code、数十ドメイン）[source: §3.1](../../../sources/Technical_Report/qwen3.md)
- **多言語データアノテーションシステム**: 30T+ tokens に educational value / fields / domains / safety 等の多次元ラベル付与 [source: §3.1](../../../sources/Technical_Report/qwen3.md)
- **インスタンスレベル data mixture optimization**（従来のソース／ドメインレベルではなく）、small proxy model + fine-grained label で広範な ablation [source: §3.1](../../../sources/Technical_Report/qwen3.md)
- **3-stage pre-training**:
  - **(S1) General**: 30T+ tokens @ seq 4,096、119 言語の一般知識基盤 [source: §3.2](../../../sources/Technical_Report/qwen3.md)
  - **(S2) Reasoning**: 5T 高品質 tokens @ seq 4,096、**STEM/coding/reasoning/synthetic の比率を上げ、learning rate decay を加速** [source: §3.2](../../../sources/Technical_Report/qwen3.md)
  - **(S3) Long-Context**: 数百億 tokens @ seq 32,768（75% が 16K-32K、25% が 4K-16K）、**RoPE base 10K→1M（ABF）+ YARN + Dual Chunk Attention で推論時 4× 拡張 → 実効 128K** [source: §3.2](../../../sources/Technical_Report/qwen3.md)
- 独自の scaling laws で最適 LR scheduler / batch size を予測 [source: §3.2](../../../sources/Technical_Report/qwen3.md)

### Post-training（4 stage + Strong-to-Weak Distillation）
- **2つの設計目標**: (1) Thinking Control（thinking + non-thinking を単一モデルに統合 + thinking budget）、(2) Strong-to-Weak Distillation（軽量モデル訓練を効率化）[source: §4](../../../sources/Technical_Report/qwen3.md)
- フラッグシップ 4 stage:
  - **Stage 1 Long-CoT Cold Start**: 検証可能な math/code/logic/STEM の query-answer dataset、Qwen2.5-72B-Instruct で2段階フィルタリング + QwQ-32B で N candidates 生成 [source: §4.1](../../../sources/Technical_Report/qwen3.md)
  - **Stage 2 Reasoning RL**: 3,995 query-verifier pairs、**GRPO**、large batch + 高 rollout + off-policy training、entropy 制御。**170 RL step で Qwen3-235B-A22B の AIME'24 70.1 → 85.1** [source: §4.2](../../../sources/Technical_Report/qwen3.md)
  - **Stage 3 Thinking Mode Fusion**: continual SFT で /think /no_think フラグを統合、chat template に組み込み [source: §4.3](../../../sources/Technical_Report/qwen3.md)
  - **Stage 4 General RL**: **20+ task の reward system**（rule-based / model-based with reference / model-based without reference の3種）、Agent Ability で multi-turn 実環境 RL [source: §4.4](../../../sources/Technical_Report/qwen3.md)
- **Thinking Budget**: thinking length が threshold 超で強制終了命令を挿入、自然発現（明示訓練ではない）[source: §4.3](../../../sources/Technical_Report/qwen3.md)
- **Strong-to-Weak Distillation**（5 dense + 1 MoE）: (1) off-policy distillation で /think + /no_think 両出力で基礎付与、(2) **on-policy distillation で学生生成 + teacher logit との KL** minimize。**4 stage 訓練比で GPU 時間 1/10**、higher Pass@1 + improved Pass@64 [source: §4.5](../../../sources/Technical_Report/qwen3.md)

### 主要ベンチマーク（抜粋）
- **Base**: Qwen3-235B-A22B-Base が **DeepSeek-V3-Base を 15 ベンチ中 14 で上回り**（total ~1/3, activated ~2/3）、MMLU-Pro **68.2**（DSV3 59.8）、MATH **71.8**（DSV3 62.6）、EvalPlus **77.6**（DSV3 63.8）[source: §3.3 Table 3](../../../sources/Technical_Report/qwen3.md)
- **Thinking**: Qwen3-235B-A22B が **DeepSeek-R1 を 23 ベンチ中 17 で上回り**（activated 60%, total 35%）、AIME'24 **85.7** / AIME'25 **81.5** / LiveCodeBench v5 **70.7** / CodeForces 2056 / BFCL v3 **70.8** [source: §4.6 Table 11](../../../sources/Technical_Report/qwen3.md)
- **Non-thinking**: GPT-4o-2024-11-20 を **18/23 ベンチで上回り**、Arena-Hard **96.1**、CodeForces percentile **75.7%** [source: §4.6 Table 12](../../../sources/Technical_Report/qwen3.md)
- Qwen3-32B (Thinking) が QwQ-32B を **23/17 ベンチで上回り** 32B reasoning SOTA に [source: §4.6 Table 13](../../../sources/Technical_Report/qwen3.md)

### MoE スケーリングの観察
- **activated params 1/5 で Qwen3 dense 相当** / **1/2 未満で Qwen2.5 MoE を超える** / **1/10 で Qwen2.5 dense と comparable** [source: §3.3](../../../sources/Technical_Report/qwen3.md)

→ 詳細: [evidence](../../../evidence/Technical_Report/qwen3.md)

## 主要な図表

![Figure 1: Qwen3 シリーズの post-training pipeline。Flagship（Qwen3-235B-A22B / Qwen3-32B）は 4 stage: Long-CoT Cold Start → Reasoning RL → Thinking Mode Fusion → General RL。Lightweight モデル（30B-A3B / 14B / 8B / 4B / 1.7B / 0.6B）は flagship を teacher として Strong-to-Weak Distillation 単独で訓練。](../../../figures/Technical_Report/qwen3/fig-1-post-training-pipeline.png)
*出典: 論文 Figure 1 — フラッグシップとライトウェイトの2系統 post-training アプローチを示す。Strong-to-Weak Distillation は 4 stage 訓練比 GPU 時間 1/10。*

## 現時点の解釈

### アーキテクチャ：「Qwen2.5 + QK-Norm + shared-expert 廃止」という保守的改良
Qwen3 のアーキテクチャ変更点は **小粒だが訓練安定性に直結する3点**: (1) **QKV-bias 除去**（Qwen2 から、Qwen2.5 以降は外していた流れの追認）、(2) **QK-Norm 導入**（attention の QK に softmax 前 RMSNorm、Dehghani et al. 2023 ベース）、(3) **Qwen2.5-MoE の shared expert を廃止 + global-batch load balancing loss** で expert 特化を促進。

これらは [DeepSeek-V4](./deepseek-v4.md) の **CSA+HCA / mHC / Muon** のような大幅な構造刷新とは対照的で、**「既存路線の安定化に投資」する保守的アップグレード**として読める。長 context は CSA+HCA のような sparse attention ではなく **RoPE ABF (10K→1M) + YARN + Dual Chunk Attention の inference-time scaling** で対応する古典的路線を維持しているのも特徴。

MoE 設計で **shared expert を廃止** したのは [DeepSeekMoE](https://arxiv.org/abs/2401.06066) や本リポジトリの [DeepSeek-V4](./deepseek-v4.md) が shared expert を採用しているのと対照的で、global-batch load balancing で expert specialization を強制する設計判断。**両者は MoE design space の異なる極**を試している。

### データ戦略：「自社モデルで自社の次世代を作る」合成データ循環
Qwen3 のデータ戦略の核心は **既存 Qwen2.5 系列（VL / Math / Coder）を生成・抽出ツールとして使い、次世代モデルの pre-training corpus を構成** する点にある。具体的には:
- **Qwen2.5-VL** が PDF/scan 画像から text を OCR → trillions of tokens 追加
- **Qwen2.5-Math / Qwen2.5-Coder** が domain-specific 合成データ生成（textbook / Q&A / code）
- **Qwen2.5** 本体が抽出データを refine

この **「自社の現行モデルで次世代の学習データを作る」flywheel** は、本リポジトリの [Rewriting Pre-Training Data (SwallowCode/SwallowMath)](../Pretraining/rewriting-pretraining-data.md) や [FineData](../Pretraining/huggingface-finedata.md) の **データリライティング・キュレーション** の流れと整合的で、特に「LLM-as-data-curator」の最大級事例。

**インスタンスレベル data mixture optimization**（従来のソース／ドメインレベルではなく individual sample レベルで mix を最適化）は、データ品質研究で先端的なアプローチ。具体アルゴリズムは本文非公開だが、small proxy model + multi-dimensional label の組み合わせと推測される。**119 言語の多言語データに対する educational value / fields / domains / safety の多次元ラベル付与** は [ATLAS multilingual scaling laws](../Pretraining/atlas-multilingual-scaling-laws.md) の 400+ 言語スケーリング則研究の **実装側カウンターパート** として位置付けられる。

**3-stage pre-training**（General 30T@4K → Reasoning 5T@4K → Long-Context @32K）は、Reasoning Stage で STEM/coding 比率を上げ learning rate decay を加速する **「データ品質を時間軸で前傾配分」** する設計。これは [Scaling Behaviors of LLM RL Post-Training (Qwen2.5)](../RL/rl-scaling-math-qwen25.md) の "k(N) saturation under data-limited regime" や [RL Scaling Laws](../RL/rl-scaling-math-qwen25.md) で示された **「ユニークサンプル数より最適化ステップ総数」** の議論とも整合する（高品質データを後段で集中投入することで効率改善）。

### Thinking Mode unification と Strong-to-Weak Distillation
**Thinking と Non-thinking を単一モデルに統合**（chat template の /think /no_think フラグ）した点は、本リポ既存の [DeepSeek-V4](./deepseek-v4.md) の **3 reasoning effort modes (Non-think / Think High / Think Max)** や OpenAI o-series の reasoning effort 制御の **オープンウェイト先行事例**（2025-05、DeepSeek-V4 より先）。**Thinking Budget が明示訓練ではなく Thinking Mode Fusion の自然発現** という観察は、reasoning effort 制御が emergence 現象として獲得可能であることを示唆する。

**Strong-to-Weak Distillation** は本リポ既存の [willccbb & Claude Opus 4.7 OPD メタ分析](../RL/willccbb-sft-rl-opd.md) で整理されている **「off-policy distillation → on-policy distillation」の2段構成** をそのまま採用しており、**5 dense + 1 MoE の軽量モデル全体に Production scale で適用** した最初の主要事例。**4 stage 訓練比 GPU 時間 1/10** は OPD の効率優位性の代表的データポイント。

注目点として **Qwen3 (2025-05) → DeepSeek-V4 (2026)** という時系列で、Qwen3 で軽量モデルに OPD を適用 → DeepSeek-V4 で specialist 統合に OPD を適用、と **OPD の use case が "軽量化" から "specialist 統合" に拡張** されていく流れが読める。[Will Brown & Claude Opus 4.7 のメタ分析](../RL/willccbb-sft-rl-opd.md) が future work で予告した「DeepSeek-V4 系 Expert RL+OPD」の **直前段階** として Qwen3 が位置付けられる。

### 立ち位置：オープン Frontier の 2025 年中盤の到達点
Qwen3-235B-A22B (Thinking) が **DeepSeek-R1 を 23 ベンチ中 17 で上回り、activated 60% / total 35%** という効率優位は、open-weight reasoning model としての SOTA を 2025-05 時点で更新。OpenAI-o1 / Gemini2.5-Pro と互角の reasoning（特に LiveCodeBench v5 70.7 / CodeForces 2056 / BFCL v3 70.8）は agent / coding 用途で frontier に肉薄したことを示す。一方 **GPQA-Diamond 71.1（DSR1 71.5, Gemini2.5-Pro 84.0）** など high-end reasoning ベンチでは差があり、**「general task SOTA + high-end reasoning でやや劣後」** という profile。

[MiniMax-M1](./minimax-m1.md) / [Kimi K2.5](./kimi-k25.md) / [DeepSeek-R1](../RL/deepseek-r1.md) の同時期 open-weight 推論モデル群と並べると、Qwen3 は **「標準アーキテクチャ + 大量データ + 4-stage post-training + 全モデル系列の Apache 2.0」** という **deployable な open frontier** を志向した設計で、hybrid attention 系の [DeepSeek-V4](./deepseek-v4.md) / [MiniMax-M1](./minimax-m1.md) や lightning attention 系の [MiniMax-M1](./minimax-m1.md) とは差別化されている。

## 関連ページ

- [Qwen3.5-Omni](./qwen35-omni.md) — Qwen3 の omni-modal 後継、Hybrid Attention MoE 化
- [DeepSeek-V4](./deepseek-v4.md) — 同枠の最新 open-weight MoE、CSA+HCA hybrid attention で異なる路線
- [MiniMax-M1](./minimax-m1.md) — 同時期 open-weight reasoning model、lightning attention 採用
- [Kimi K2.5](./kimi-k25.md) — 同枠 open-weight tech report
- [DeepSeek-R1](../RL/deepseek-r1.md) — Qwen3 Thinking が直接対比される reasoning baseline
- [On SFT, RL, on-policy distillation (Brown & Claude Opus 4.7)](../RL/willccbb-sft-rl-opd.md) — Qwen3 の Strong-to-Weak Distillation を OPD ダイアル整理で解析する道具
- [Dr. GRPO](../RL/dr-grpo.md) — Reasoning RL stage の GRPO 改良候補
- [Rewriting Pre-Training Data](../Pretraining/rewriting-pretraining-data.md) — データキュレーション系譜
- [FineData (HuggingFaceFW)](../Pretraining/huggingface-finedata.md) — オープン pre-training データの参照点
- [ATLAS: Multilingual Scaling Laws](../Pretraining/atlas-multilingual-scaling-laws.md) — 119 言語多言語学習の理論側
- [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) — Qwen2.5 系列の RL scaling 法則、Reasoning RL の解析道具

## 未解決の問い

- **インスタンスレベル data mixture optimization** の具体的アルゴリズム / proxy model 詳細は何か？ablation の幅は？
- **Qwen2.5-VL で PDF から抽出した text の license** は明確化されているか（pre-training data の出自）？
- **Thinking budget が "自然発現"** とされる現象は他のモデル（DeepSeek-V4 Think Max 等）でも再現するか？
- **Strong-to-Weak Distillation の 4 stage 比 1/10 GPU 時間** は absolute 時間で何時間か？scaling は？
- **shared expert 廃止 + global-batch load balancing** は DeepSeek-V4 の shared expert + auxiliary-loss-free 設計とどちらが優位か（control 実験未公開）
- **Reasoning RL の 3,995 query-verifier pairs** は scale で何倍まで効くか、過学習はどこで起きるか？
- 119 言語の **多言語データアノテーションシステム**（多次元ラベル）は他組織の pre-training data 拡張に転用できる reproducibility があるか？
- QK-Norm の効果は **ablation 数値が論文内で明示** されていない（QKV-bias 除去とのコントリビューション分離）
- Thinking mode unification は **mode 間の干渉**（thinking 時の non-thinking 性能劣化／逆）をどう測定したか？
