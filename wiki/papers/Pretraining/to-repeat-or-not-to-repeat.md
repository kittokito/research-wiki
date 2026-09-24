---
title: "To Repeat or Not To Repeat: Insights from Scaling LLM under Token-Crisis"
aliases: ["To Repeat or Not To Repeat", "Token-Crisis", "Multi-Epoch Degradation", "多エポック劣化"]
created: 2026-06-19
updated: 2026-06-19
tags: [token-crisis, data-repetition, multi-epoch-degradation, overfitting, dropout, MoE, scaling-laws, pretraining, data-constrained]
peer_review: accepted
venue: "NeurIPS 2023 (Poster)"
sources: [src-to-repeat-or-not-to-repeat]
---

# To Repeat or Not To Repeat: Insights from Scaling LLM under Token-Crisis

> **査読**: ✅ accepted — NeurIPS 2023 (Poster)

Xue, Fu, Zhou, Zheng & You (2023) — NUS × University of Edinburgh × ETH Zurich / arXiv 2305.13230 (OpenReview Af5GvIj3T5)

## ソースからの事実
- **問題設定（token-crisis）**: compute-optimal LLM の必要トークン数が高品質 web テキストの増加速度を上回り、悲観的には **2023〜2027年に枯渇**しうる。素朴な対策は「データを複数エポック繰り返す」こと [source: §1](../../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **【核心】Multi-epoch degradation**: データ繰り返しは**過学習で性能を劣化**させる。**支配要因＝データサイズ・パラメータ数・目的関数**、**影響が小さい＝データ品質・FLOPs**。T5-XL は 4倍データの T5-Large に負ける（2²⁷ vs 2²⁹ トークン） [source: §2-3](../../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **緩和策**: 大半の正則化は無効だが **dropout が極めて有効**（後段投入＝dropstage で学習速度と両立、ただし XL では追加チューニング要）。高品質 Wikipedia でも劣化は緩和されない [source: §3-4](../../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **MoE の二役**: 同等パラメータの dense の過学習挙動を **MoE が低コストで予測**でき（0.32-0.39× FLOPs）、dropout rate 等のハイパラ探索の**安価な代理**になる（コスト 0.48倍）。T5/C4・最大 2.8B 規模 [source: §3.2, §5](../../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

→ 詳細: [evidence](../../../evidence/Pretraining/to-repeat-or-not-to-repeat.md)

## 現時点の解釈

**「データが有限なとき、同じデータを繰り返すと何が起きるか」を T5/C4 で系統的に切り分けた、data-constrained 事前学習の基礎研究**。本リポジトリの事前学習・スケーリング則クラスタに、「**繰り返し（repetition）＝過学習という負の側面**」の軸を与える。

- **knowledge-capacity との表裏関係（最重要）**: [Knowledge Capacity Scaling Laws](knowledge-capacity-scaling-laws.md) は「各知識を **~1000回露出**させると **2 bit/param の高密度保存**に達する」と、繰り返し露出を**有益**と捉える。本論文は「データ（コーパス全体）を繰り返すと**多エポック劣化**で性能が落ちる」と、繰り返しを**有害**と捉える。両者は矛盾でなく、**同じ「繰り返し→記憶（memorization）」現象の表裏**: 十分大きく多様なコーパス内で特定知識を反復露出するのは密な保存に効くが、**限られたコーパス全体を反復**するとコーパスを丸ごと暗記して汎化が崩れる。本論文の「目的関数混合（UL2）は記憶を速め劣化を悪化させる」も、この memorization 軸で読める。
- **データ制約下スケーリングの RL 側との対比**: [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) は、RL 後学習では**データ制約下で「最適化ステップ総数」が「ユニークサンプル数」より支配的**で、高品質データの再利用が有効と報告する。事前学習（本論文＝繰り返しは劣化）と RL 後学習（繰り返しは有効）で**繰り返しの符号が逆転**するのは、両段階の学習信号と過学習リスクの違いを示す好対照。
- **データ品質 vs データ量の議論**: 「高品質（Wikipedia）でも多エポック劣化は緩和されない／品質より量・パラメータ数が効く」という知見は、[Rewriting Pre-Training Data](rewriting-pretraining-data.md) / [FineData](huggingface-finedata.md) の「品質改善・リライト」路線と**競合でなく補完**。本論文の射程は「既存トークンを繰り返す」ことの限界であり、リライト・合成は**高品質トークンの総量を増やす**別レバー＝token-crisis への正攻法。C4 は本実験の土台で [T5](t5-text-to-text-transformer.md) 由来。
- **スケーリング則ファミリーの data-constrained ピース**: Chinchilla 則（パラメータと必要トークンの線形関係）が T5/C4 でも成立することを確認しつつ、その**前提が崩れる「データ不足」レジーム**を扱う。[ATLAS](atlas-multilingual-scaling-laws.md)・[言語構造の獲得理論](language-structure-acquisition.md)・[When Scaling Meets LLM Finetuning](../Post_Training/scaling-llm-finetuning.md) が「データ・モデルを増やすと何が起きるか」を扱うのに対し、本論文は「**増やせないとき**どうなるか」の相補的ピース。
- **MoE を「予測装置」として使う発想**: sparse MoE で高価な dense の挙動を先取りする手法は、MoE を効率化（[Qwen3](../Technical_Report/qwen3.md) / [DeepSeek-V4](../Technical_Report/deepseek-v4.md)）でなく**実験コスト削減のツール**として使う珍しい用途。

T5/C4・2.8B 規模・2023年の研究であり、フロンティア規模 decoder-only やマルチモーダル時代の token-crisis 像へそのまま外挿はできないが、「**有限データの繰り返しは記憶を促し汎化を損なう／dropout と大きなデータが効く**」という描像は、データ制約下の事前学習設計の出発点として今も有効。

## 関連ページ
- [Knowledge Capacity Scaling Laws](knowledge-capacity-scaling-laws.md) — 繰り返し露出を「有益（高密度保存）」と捉える表裏の論文（本論文は「有害（多エポック劣化）」）
- [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) — データ制約下の RL 後学習では繰り返し（再利用）が有効＝符号が逆転する対照
- [Rewriting Pre-Training Data](rewriting-pretraining-data.md) / [FineData](huggingface-finedata.md) — 高品質トークンの総量を増やす token-crisis 正攻法（品質改善で繰り返し劣化を回避できない本論文と補完）
- [T5 (text-to-text transformer)](t5-text-to-text-transformer.md) — 本実験の土台アーキ・C4 データセットの出典
- [ATLAS](atlas-multilingual-scaling-laws.md) / [言語構造の獲得理論](language-structure-acquisition.md) / [When Scaling Meets LLM Finetuning](../Post_Training/scaling-llm-finetuning.md) — スケーリング則ファミリー（本論文は data-constrained ピース）

## 未解決の問い
- T5/C4・2.8B 規模の「多エポック劣化」は、フロンティア規模の decoder-only LLM・マルチモーダル学習でも同じ閾値・支配要因で成立するか
- 「特定知識の反復露出は有益（knowledge-capacity）／コーパス全体の反復は有害（本論文）」の境界はどこか。reuse が有益→有害に転じる繰り返し回数・データ多様性の臨界点は定量化できるか
- データ合成・リライトで「実質的な高品質トークン量」を増やす路線は、token-crisis をどこまで先送りできるか（合成データの繰り返しは多エポック劣化を起こすか）
