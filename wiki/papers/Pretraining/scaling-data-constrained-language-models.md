---
title: "Scaling Data-Constrained Language Models"
aliases: ["Scaling Data-Constrained Language Models", "Data-Constrained Scaling Laws", "データ制約スケーリング則", "datablations"]
created: 2026-06-19
updated: 2026-06-19
tags: [data-constrained, scaling-laws, data-repetition, chinchilla, token-crisis, code-data, data-filtering, pretraining, compute-optimal]
peer_review: accepted
venue: "NeurIPS 2023 (Oral, Outstanding Main Track Paper Runner-Up)"
sources: [src-scaling-data-constrained-language-models]
---

# Scaling Data-Constrained Language Models

> **査読**: ✅ accepted — NeurIPS 2023 (Oral, Outstanding Main Track Paper Runner-Up)

Muennighoff, Rush, Barak, Le Scao, Piktus, Tazi, Pyysalo, Wolf & Raffel (2023) — Hugging Face × Harvard × University of Turku / arXiv 2305.16264 (OpenReview j5BuTrEj35)

## ソースからの事実
- **規模**: 400超の学習run（GPT-2 アーキ、**10M–8.7B パラメータ・最大900Bトークン・最大1500エポック**、C4 サブセット）で data-constrained レジームを実証。モデル・データを公開（huggingface/datablations） [source: §4](../../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **【核心】Data-Constrained Scaling Law**: Chinchilla の L(N,D)=A/N^α+B/D^β+E を、繰り返しで価値が指数減衰する**実効データ D'・実効パラメータ N'** に置換。D'=U_D+U_D·R\*_D·(1−e^(−R_D/R\*_D))。**R\*_D≈15 が繰り返しの「半減期」** [source: §3.1](../../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **Return**: 固定計算量下で**最大~4エポックの繰り返しは新規データとほぼ同等**（8.7Bで4エポックは1エポック比 損失+0.5%）。意味ある改善は**~16エポックまで**、**~40エポックで無価値** [source: §6](../../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **Allocation**: データ制約下では Chinchilla（N・D 等比）と異なり**「パラメータよりエポックを速くスケール」**（過剰パラメータは繰り返しデータより速く減衰、R\*_N<R\*_D）。25Bユニークでは Chinchilla 推奨より**27%少パラメータ**のモデルが上回る [source: §5-6](../../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **補完策**: **コード50%混入で実効トークン2倍**（NL劣化なし、WebNLG/bAbI は向上）。フィルタ（dedup・perplexity）は**ノイズデータでのみ有効** [source: §7](../../../sources/Pretraining/scaling-data-constrained-language-models.md)

→ 詳細: [evidence](../../../evidence/Pretraining/scaling-data-constrained-language-models.md)

## 現時点の解釈

**token-crisis（データ枯渇）に対し「同じデータを何エポックまで繰り返してよいか・余った計算をどう配分するか」を Chinchilla 則の拡張として定量化した、data-constrained scaling の決定版**。本リポジトリのスケーリング則・事前学習クラスタの中核ピース。

- **[To Repeat or Not To Repeat] との対ペア（最重要）**: 同じ NeurIPS 2023 で arXiv 投稿もほぼ同時（2305.13230 vs 2305.16264）の token-crisis 2大論文。[To Repeat or Not To Repeat](to-repeat-or-not-to-repeat.md) は **T5/encoder-decoder** で「多エポック劣化の**機序と緩和策**（dropout・MoE・データ品質は効かない）」を、本論文は **GPT-2/decoder** で「**スケーリング則と計算配分**」を扱う。両者は相補的で結論も整合する:
  - **「数エポックの繰り返しは無害」で一致**（To Repeat: dropout 等で緩和可能 / 本論文: ~4エポックは損失ほぼ不変）。
  - **「大きすぎるモデルはデータ制約下で不利」で一致**: To Repeat の「T5-XL（2²⁷）は4倍データの T5-Large（2²⁹）に負ける」を、本論文は **「過剰パラメータは繰り返しデータより速く価値減衰（R\*_N<R\*_D）→ パラメータよりエポックを優先」**として scaling law で定式化。一方の経験則を他方が理論化した関係。
  - 緩和の方向は別アプローチ: To Repeat=**正則化（dropout）**で劣化を抑える、本論文=**データ拡張（コード）・配分最適化**で枯渇を回避。
- **RL 後学習の data-constrained 版との接続**: [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) は「RL ではデータ制約下で**最適化ステップ総数 > ユニークサンプル数**、高品質データ再利用が有効」と報告。本論文（事前学習の繰り返しは~4エポックまで有効）の**RL 後学習への一般化**であり、両段階で「繰り返し・再利用がどこまで効くか」を測る系譜。
- **knowledge-capacity との繰り返し観の違い**: [Knowledge Capacity Scaling Laws](knowledge-capacity-scaling-laws.md) は「各**知識**を~1000回露出すると2bit/param 高密度保存」と繰り返しを有益視。本論文は「**コーパス全体**を~16エポック超繰り返すと無価値」。粒度（個別知識 vs コーパス全体）の違いで、繰り返しの便益が逆方向に見える点が示唆的。
- **データ拡張・品質路線との補完**: 「コードで実効トークン2倍／フィルタはノイズ用」という知見は、[Rewriting Pre-Training Data](rewriting-pretraining-data.md)（リライト・合成でデータを増やす）・[FineData](huggingface-finedata.md)（大規模フィルタ済みデータ）と直結。token-crisis への正攻法＝「繰り返し・コード混入・合成で実効データ量を増やす」。C4 と著者 Raffel は [T5](t5-text-to-text-transformer.md) 由来。
- **Chinchilla の直系拡張**: [ATLAS](atlas-multilingual-scaling-laws.md)（多言語）・[When Scaling Meets LLM Finetuning](../Post_Training/scaling-llm-finetuning.md)（finetune）と並ぶ「Chinchilla 則を別レジームに拡張する」系譜の、**データ制約レジーム版**。

GPT-2 アーキ・英語 C4・8.7B 規模・2023年の研究で、フロンティア規模やマルチモーダル時代の token-crisis 像へそのまま外挿はできない（提案式は過学習で損失が再上昇する領域をモデル化しない）。だが「**~4エポックはほぼタダ・~16エポックまで有用・エポックをパラメータより優先・コードで実効2倍**」という指針は、データ制約下の事前学習設計の事実上の標準リファレンスとして今も参照される。

## 関連ページ
- [To Repeat or Not To Repeat (Token-Crisis)](to-repeat-or-not-to-repeat.md) — 同 NeurIPS 2023 の対ペア論文（T5 で機序・緩和策、本論文は decoder でスケーリング則・配分）。「大モデルはデータ制約下で不利」を経験則↔理論で対応
- [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) — RL 後学習の data-constrained 版（再利用・ステップ総数の支配）
- [Knowledge Capacity Scaling Laws](knowledge-capacity-scaling-laws.md) — 繰り返し露出を有益とする（粒度＝個別知識 vs コーパス全体の違い）
- [Rewriting Pre-Training Data](rewriting-pretraining-data.md) / [FineData](huggingface-finedata.md) — 実効データ量を増やすデータ拡張・品質路線（コード混入・フィルタの接続先）
- [T5 (text-to-text transformer)](t5-text-to-text-transformer.md) — C4 データセット・著者 Raffel の出自
- [ATLAS](atlas-multilingual-scaling-laws.md) / [When Scaling Meets LLM Finetuning](../Post_Training/scaling-llm-finetuning.md) — Chinchilla 則を別レジームに拡張する系譜（本論文はデータ制約版）

## 未解決の問い
- R\*_D≈15（~16エポックで繰り返しの価値が半減期）は GPT-2/C4 での fit。フロンティア規模 decoder-only や多言語・コード比率の異なるデータで R\*_D・R\*_N はどう変わるか
- 「コードで実効トークン2倍」は合成データ・他モダリティ混入でも成り立つか。合成データの繰り返しは多エポック劣化（[To Repeat or Not To Repeat](to-repeat-or-not-to-repeat.md)）を起こすか
- 提案式は過学習で損失が再上昇する領域をモデル化しない。データ制約下で「繰り返し・パラメータ過多が害に転じる」境界を予測式に組み込めるか
