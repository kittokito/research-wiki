---
source: src-qwen3
date_extracted: 2026-05-11
---

# Qwen3 (Qwen Team, 2025) からの抽出

## 主要な主張

### モデル構成
- **6 dense + 2 MoE = 8 モデル**、Apache 2.0 License で公開 [source: §2](../../sources/Technical_Report/qwen3.md)
- **Qwen3-235B-A22B**（flagship MoE）: 235B total / 22B active、94 layers、64/4 Q/KV heads、128 experts (8 active)、128K context [source: §2 Table 2](../../sources/Technical_Report/qwen3.md)
- **Qwen3-30B-A3B**（軽量 MoE）: 30B total / 3B active、48 layers、32/4 Q/KV heads、128 experts (8 active)、128K context [source: §2 Table 2](../../sources/Technical_Report/qwen3.md)
- Dense モデル: 0.6B / 1.7B（28 layers, 16/8 heads, tie embedding, 32K context）、4B（36 layers, 32/8 heads, tie embedding, 128K）、8B（36 layers, 32/8 heads, 128K）、14B（40 layers, 40/8 heads, 128K）、32B（64 layers, 64/8 heads, 128K）[source: §2 Table 1](../../sources/Technical_Report/qwen3.md)

### アーキテクチャ
- Dense モデルは Qwen2.5 を踏襲: **GQA**, **SwiGLU**, **RoPE**, **RMSNorm with pre-normalization** [source: §2](../../sources/Technical_Report/qwen3.md)
- **QKV-bias を除去**（Qwen2 から） [source: §2](../../sources/Technical_Report/qwen3.md)
- **QK-Norm**（attention の QK に softmax 前 RMSNorm 適用）を導入 → 訓練安定性向上 [source: §2](../../sources/Technical_Report/qwen3.md)
- MoE モデルは Dense と同一の fundamental architecture、**fine-grained expert segmentation**（DeepSeekMoE 系列の参照）、**128 total experts のうち 8 active per token** [source: §2](../../sources/Technical_Report/qwen3.md)
- **Qwen2.5-MoE と異なり shared expert を廃止**、**global-batch load balancing loss** で expert 特化を促進 [source: §2](../../sources/Technical_Report/qwen3.md)
- Qwen's tokenizer (BBPE, vocab 151,669) [source: §2](../../sources/Technical_Report/qwen3.md)

### Pre-training データ戦略
- **36 trillion tokens, 119 languages and dialects**（Qwen2.5 比でトークン数 2×、言語数 3×、Qwen2.5 は 29 言語）[source: §3.1](../../sources/Technical_Report/qwen3.md)
- カテゴリ: coding / STEM / reasoning tasks / books / multilingual / synthetic [source: §3.1](../../sources/Technical_Report/qwen3.md)
- **データ拡充パイプライン**: (1) **Qwen2.5-VL で PDF 様の文書から OCR/text recognition**、(2) **Qwen2.5 で抽出テキストを refine**、(3) **Qwen2.5-Math / Qwen2.5-Coder で domain-specific 合成データを生成**（textbooks / Q&A / instructions / code snippets、数十ドメイン）[source: §3.1](../../sources/Technical_Report/qwen3.md)
- **多言語データアノテーションシステム**: 30T+ トークンに **educational value / fields / domains / safety** 等の多次元ラベル付与 [source: §3.1](../../sources/Technical_Report/qwen3.md)
- **インスタンスレベル data mixture optimization**（従来のソース／ドメインレベル最適化ではなく）、small proxy model + fine-grained label で広範な ablation [source: §3.1](../../sources/Technical_Report/qwen3.md)

### Pre-training Stage（3段階）
- **(S1) General Stage**: 30T+ tokens, seq length **4,096**、119 言語の一般知識基盤 [source: §3.2](../../sources/Technical_Report/qwen3.md)
- **(S2) Reasoning Stage**: 5T 高品質 tokens, seq length **4,096**、**STEM / coding / reasoning / synthetic data の比率を増やし、learning rate decay を加速** [source: §3.2](../../sources/Technical_Report/qwen3.md)
- **(S3) Long Context Stage**: 数百億 tokens、seq length **32,768**、75% が 16K-32K / 25% が 4K-16K の長文。**RoPE base frequency を 10,000 → 1,000,000 に拡張（ABF）**、**YARN + Dual Chunk Attention (DCA)** で推論時 **4× sequence length 拡張**（実効 128K）[source: §3.2](../../sources/Technical_Report/qwen3.md)
- Qwen2.5 同様に **scaling laws を独自に開発**、最適 learning rate scheduler / batch size を予測 [source: §3.2](../../sources/Technical_Report/qwen3.md)

### Post-training パイプライン
- **2つの設計目標**: (1) **Thinking Control**（thinking / non-thinking mode 統合 + thinking budget 制御）、(2) **Strong-to-Weak Distillation**（軽量モデル訓練の効率化）[source: §4](../../sources/Technical_Report/qwen3.md)
- フラッグシップは **4 stage**、軽量モデルは Strong-to-Weak Distillation 単独 [source: §4 Figure 1](../../sources/Technical_Report/qwen3.md)

#### 4-Stage（フラッグシップ用）
- **Stage 1: Long-CoT Cold Start**: math/code/logic/STEM の検証可能 reference answer 付き dataset、Qwen2.5-72B-Instruct で2段階フィルタリング（query filtering: easy/multi-subq/general-text 除去、QwQ-32B で N candidate 生成し human annotator が evaluate、誤答・反復・guesswork・think-summary不一致・言語混在・validation類似を除外）。foundational reasoning pattern を植え付ける段階で **訓練サンプル数・ステップを最小化** [source: §4.1](../../sources/Technical_Report/qwen3.md)
- **Stage 2: Reasoning RL**: 3,995 query-verifier pairs（cold-start 未使用・cold-start で学習可能・最大難度・広範サブドメイン）、**GRPO** で update、大 batch + 高 rollout 数 + off-policy training。entropy 制御で exploration-exploitation バランス。**170 RL step で Qwen3-235B-A22B の AIME'24 70.1 → 85.1** [source: §4.2](../../sources/Technical_Report/qwen3.md)
- **Stage 3: Thinking Mode Fusion**: Stage 2 model に continual SFT で non-thinking 能力を統合。**SFT データ構成**: thinking data は Stage 2 model で Stage 1 query に rejection sampling、non-thinking data は coding/math/instruction/multilingual/creative/QA/role-play を多様化、low-resource 言語の翻訳タスクを増加。**Chat template に /think /no_think フラグ**（user/system message 内）、non-thinking 時も `<think></think>` を空で挿入し format consistency。Multi-turn では最後の flag に従う [source: §4.3 Table 9](../../sources/Technical_Report/qwen3.md)
- **Thinking Budget**: thinking length が user 指定 threshold に達すると `"Considering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>.\n\n"` を強制挿入、累積推論で最終回答生成。**明示訓練ではなく Thinking Mode Fusion の自然な副産物** [source: §4.3](../../sources/Technical_Report/qwen3.md)
- **Stage 4: General RL**: **20+ distinct task の reward system** をカスタム scoring criteria で構築。コア能力: Instruction Following / Format Following（/think /no_think flag・think tag 一貫性）/ Preference Alignment / Agent Ability（multi-turn 実環境 feedback）/ Specialized Scenarios（RAG hallucination 抑制等）。**3 種 reward**: (1) Rule-based、(2) Model-based with Reference Answer（Qwen2.5-72B-Instruct で reference 比較スコア）、(3) Model-based without Reference（preference data で訓練した scalar reward model）[source: §4.4](../../sources/Technical_Report/qwen3.md)

#### Strong-to-Weak Distillation（軽量モデル用）
- 5 dense（0.6B/1.7B/4B/8B/14B）+ 1 MoE（30B-A3B）に適用 [source: §4.5](../../sources/Technical_Report/qwen3.md)
- **(1) Off-policy Distillation**: teacher（Qwen3-32B / Qwen3-235B-A22B）の /think + /no_think 両出力を組み合わせて basic reasoning + mode-switching の基礎付与 [source: §4.5](../../sources/Technical_Report/qwen3.md)
- **(2) On-policy Distillation**: 学生が on-policy sequence 生成（/think または /no_think mode）、teacher の logit との **KL divergence 最小化** で fine-tune [source: §4.5](../../sources/Technical_Report/qwen3.md)
- **4 stage 訓練比で GPU 時間 1/10**、higher Pass@1 / improved Pass@64（exploration 改善）[source: §4](../../sources/Technical_Report/qwen3.md)

### Multilingual 対応
- 119 言語・方言サポート（Qwen2.5 の 29 言語から大幅拡張）[source: §3.1](../../sources/Technical_Report/qwen3.md)
- 評価ベンチマーク: Multi-IF (8 lang) / INCLUDE (44 lang) / MMMLU (14 lang) / MT-AIME2024 (55 lang) / PolyMath (18 lang) / MLogiQA (10 lang) [source: §4.6 Table 10](../../sources/Technical_Report/qwen3.md)

## 主要な貢献

- **dense + MoE の8モデルフルレンジ Apache 2.0 公開**、0.6B-235B の幅広い deployment 帯
- **Thinking mode と Non-thinking mode を単一モデルに統合** + **Thinking Budget** による reasoning effort 動的制御 — QwQ / DeepSeek-R1 等の separate model 路線を解消
- **Strong-to-Weak Distillation** で軽量モデル post-training を **GPU 時間 1/10** に圧縮、Pass@1/Pass@64 共に上回る
- **インスタンスレベル data mixture optimization** によるデータ品質の体系化
- **Qwen2.5-VL + Qwen2.5-Math + Qwen2.5-Coder の合成データパイプライン** で **36T tokens / 119 言語** のスケーラブルなコーパス構築
- **QK-Norm** 導入と **QKV-bias 除去** による訓練安定性改善
- **MoE での shared expert 廃止 + global-batch load balancing loss** という Qwen2.5-MoE / DeepSeekMoE と異なる expert specialization 設計
- **Reasoning RL の 170 step で AIME'24 70.1 → 85.1** という単一ランの実例公開、ハイパーパラメータの manual intervention なし
- 119 言語向けの **multilingual data annotation system** と instance-level mixture 最適化のレシピ

## ベンチマーク結果

### Base モデル（Qwen3-235B-A22B-Base vs SOTA、Table 3）
| Benchmark | Qwen2.5-72B | Qwen2.5-Plus | Llama-4-Maverick | DeepSeek-V3 | Qwen3-235B-A22B |
|---|---|---|---|---|---|
| Total / Active Params | 72B / 72B | 271B / 37B | 402B / 17B | 671B / 37B | **235B / 22B** |
| MMLU | 86.06 | 85.02 | 85.16 | 87.19 | **87.81** |
| MMLU-Pro | 58.07 | 63.52 | 63.91 | 59.84 | **68.18** |
| GPQA | 45.88 | 41.92 | 43.94 | 41.92 | **47.47** |
| GSM8K | 91.50 | 91.89 | 87.72 | 87.57 | **94.39** |
| MATH | 62.12 | 62.78 | 63.32 | 62.62 | **71.84** |
| EvalPlus | 65.93 | 61.43 | 68.38 | 63.75 | **77.60** |
| MBPP | 76.00 | 74.60 | 75.40 | 74.20 | **81.40** |
| MGSM | 82.40 | 82.21 | 79.69 | 82.68 | **83.53** |

- DeepSeek-V3-Base (671B/37B active) を **15 ベンチ中 14 で上回り、total 約 1/3 / activated 約 2/3 params** [source: §3.3](../../sources/Technical_Report/qwen3.md)
- Llama-4-Maverick (402B/17B) を total 約 1/2 で多くのベンチで上回り [source: §3.3](../../sources/Technical_Report/qwen3.md)
- Qwen2.5-72B-Base と比較し total 1/3 で全 15 ベンチを上回り [source: §3.3](../../sources/Technical_Report/qwen3.md)

### MoE スケーリング観察
- 同じ pre-training data で **Qwen3 MoE は activated params 1/5 で Qwen3 dense と同等性能** [source: §3.3](../../sources/Technical_Report/qwen3.md)
- アーキ + training token + training strategy 改善で **activated params 1/2 未満で Qwen2.5 MoE を超える** [source: §3.3](../../sources/Technical_Report/qwen3.md)
- **activated params 1/10 で Qwen2.5 dense と comparable** [source: §3.3](../../sources/Technical_Report/qwen3.md)

### Post-training Thinking モード（Qwen3-235B-A22B Thinking、Table 11）
| Benchmark | OpenAI-o1 | DeepSeek-R1 | Gemini2.5-Pro | Qwen3-235B-A22B |
|---|---|---|---|---|
| MMLU-Redux | 92.8 | 92.9 | **93.7** | 92.7 |
| GPQA-Diamond | 78.0 | 71.5 | **84.0** | 71.1 |
| AIME'24 | 74.3 | 79.8 | **92.0** | 85.7 |
| AIME'25 | 79.2 | 70.0 | **86.7** | 81.5 |
| LiveCodeBench v5 | 63.9 | 64.3 | 70.4 | **70.7** |
| CodeForces (Rating) | 1891 | **2029** | 2001 | 2056 |
| BFCL v3 | 67.8 | 56.9 | 62.9 | **70.8** |

- Qwen3-235B-A22B (Thinking) は **DeepSeek-R1 を 23 ベンチ中 17 で上回り**（activated 60% / total 35% params）[source: §4.6](../../sources/Technical_Report/qwen3.md)
- OpenAI-o1 / Gemini2.5-Pro と互角、closed-source モデルとのギャップ縮小 [source: §4.6](../../sources/Technical_Report/qwen3.md)

### Post-training Non-thinking モード（Qwen3-235B-A22B Non-thinking、Table 12）
- DeepSeek-V3 / LLaMA-4-Maverick / Qwen2.5-72B-Instruct を上回り、GPT-4o-2024-11-20 を **18/23 ベンチで上回る** [source: §4.6](../../sources/Technical_Report/qwen3.md)
- IFEval 86.1（DeepSeek-V3 86.1 と並ぶ）、Arena-Hard **96.1**、CodeForces percentile **75.7%** [source: §4.6 Table 12](../../sources/Technical_Report/qwen3.md)

### Qwen3-32B (Thinking) vs QwQ-32B (Table 13)
- Qwen3-32B Thinking は QwQ-32B を **23 ベンチ中 17 で上回り** SOTA 32B reasoning model に [source: §4.6](../../sources/Technical_Report/qwen3.md)
- AIME'24 81.4 (QwQ 79.5)、MATH-500 97.2 (QwQ 98.0)、CodeForces 1977/97.7% (QwQ 1982/97.7%) [source: §4.6 Table 13](../../sources/Technical_Report/qwen3.md)

## 制限・注意点

- テクニカルレポート（**査読 n/a**）、Apache 2.0 License で公開だが第三者再現は今後
- Qwen3-235B-A22B (Thinking) は GPQA-Diamond で **DeepSeek-R1 を下回る**（71.1 vs 71.5）、specific reasoning benchmark でばらつき
- Multilingual benchmark の "INCLUDE" や "MMMLU" では DeepSeek-R1 / Gemini2.5-Pro に劣後する場面あり
- **Pre-training data の出自**（特に Qwen2.5-VL で抽出した PDF 由来）の licensing は本文中で明確化されていない
- **Instance-level data mixture optimization** の具体的アルゴリズム / proxy model 詳細は公開限定的
- **Strong-to-Weak Distillation の GPU 時間 1/10** は absolute cost 公開ではなく相対比のみ
- Thinking budget が **明示訓練でなく自然発現** と述べるが、threshold 設計と性能影響の系統的 ablation は限定的
- Reasoning RL stage の query-verifier pairs **3,995 件** は小規模、scaling 余地と generalizability は要検証

## 実装関連

- arXiv: https://arxiv.org/abs/2505.09388
- GitHub: https://github.com/QwenLM/Qwen3
- HuggingFace: https://huggingface.co/Qwen
- License: **Apache 2.0**
- Chat template: tokenizer に `enable_thinking=False` パラメータで non-thinking mode 切替可能、`/think` / `/no_think` フラグを user/system message 内で混在可能
- 関連: [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115)（pre-training data 拡張の基盤）、[Qwen2.5-VL](https://arxiv.org/abs/2502.13923)（PDF text extraction）、[DeepSeekMoE Dai et al. 2024](https://arxiv.org/abs/2401.06066)（fine-grained expert reference）、[GRPO Shao et al. 2024](https://arxiv.org/abs/2402.03300)、[YARN Peng et al. 2023](https://arxiv.org/abs/2309.00071)、[DCA An et al. 2024](https://arxiv.org/abs/2402.17463)
