---
title: "Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws"
aliases: ["Knowledge Capacity Scaling Laws", "2 bits per parameter", "Physics of LM 3.3"]
created: 2026-06-09
updated: 2026-06-09
tags: [knowledge-capacity, scaling-laws, memorization, bits-per-parameter, exposure, quantization, MoE]
peer_review: accepted
venue: "ICLR 2025 (Spotlight)"
sources: [src-knowledge-capacity-scaling-laws]
---

# Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws

> **査読**: ✅ accepted — ICLR 2025 (Spotlight)

Allen-Zhu & Li (2024) — Meta FAIR / arXiv 2404.05405 (OpenReview FxNNiUgtfa)

## ソースからの事実
- LM の保存知識量を**情報理論的に bit で推定**し、**1パラメータあたり最大2 bit**が上限（int8 量子化でも維持）。7B ≒ 14B bit（英語 Wikipedia＋教科書超） [source](../../../sources/Pretraining/knowledge-capacity-scaling-laws.md)
- **【核心】露出回数が容量を支配**: 各知識を**約1000回露出**で **2 bits/param のピーク容量**（高密度保存）。**約100回**だと容量は**およそ半減（~1 bit/param）** [source](../../../sources/Pretraining/knowledge-capacity-scaling-laws.md)
- 容量に効く5因子（訓練時間/露出・アーキテクチャ・量子化・MoE スパース性・データ SNR）を12結果で体系化 [source](../../../sources/Pretraining/knowledge-capacity-scaling-laws.md)

→ 詳細: [evidence](../../../evidence/Pretraining/knowledge-capacity-scaling-laws.md)

## 現時点の解釈

**「モデルは何 bit の知識を、どれだけ密に保存できるか」を実測で定式化した knowledge-side のスケーリング則**。本リポジトリのスケーリング則・事前学習クラスタに、loss/ベンチでなく**情報量(bit)**という軸を加える。

- **メモした核心（露出回数→密度）**: 「各知識 ~1000回露出で 2 bit/param、~100回だと半減」という結果は、**重要事実は学習データ中の出現頻度を確保するほど高密度に保存される**ことを意味する。データ品質・配合を扱う [Rewriting Pre-Training Data](rewriting-pretraining-data.md) / [FineData](huggingface-finedata.md) の「何を・どれだけ見せるか」の議論に、容量の観点から直接の根拠を与える。
- **スケーリング則ファミリーの knowledge 版**: [ATLAS（多言語スケーリング則）](atlas-multilingual-scaling-laws.md)・[言語構造の獲得理論](language-structure-acquisition.md)・[RHM](random-hierarchy-model.md) が「性能・構造」のスケーリングを扱うのに対し、本論文は「**保存知識量**」のスケーリングを扱う相補的ピース。
- **知識の抽出可能性との接続**: 「保存知識は柔軟に抽出可能」という主張は、保存はされても**逆方向には抽出できない**ことを示す [The Reversal Curse](../Reasoning/reversal-curse.md) と対をなす（容量＝保存と、抽出可能性は別問題）。
- **量子化・MoE への含意**: int8 までは 2 bit/param を保つという結果は、[TurboQuant](../Efficiency_Optimization/turboquant.md) 等の圧縮が「どこまで知識を壊さずに済むか」の理論的目安になる。

合成・制御データでの測定のため、雑多な web コーパスの知識へそのまま外挿はできないが、「容量は有限で、露出回数が密度を決める」という描像は事前学習データ設計の指針になる。

## 関連ページ
- [Rewriting Pre-Training Data](rewriting-pretraining-data.md) / [FineData](huggingface-finedata.md) — データ品質・配合（露出回数→容量の実務的含意の接続先）
- [ATLAS: Multilingual Scaling Laws](atlas-multilingual-scaling-laws.md) — 性能側のスケーリング則（本論文は知識量側）
- [言語構造の獲得理論](language-structure-acquisition.md) / [Random Hierarchy Model](random-hierarchy-model.md) — 構造・サンプル複雑度のスケーリング理論
- [The Reversal Curse](../Reasoning/reversal-curse.md) — 保存と抽出可能性は別（容量があっても逆方向抽出は失敗）
- [TurboQuant](../Efficiency_Optimization/turboquant.md) — 量子化圧縮（int8 まで 2bit/param 維持の含意）

## 未解決の問い
- 「~1000回露出で 2bit/param」は合成データの結果。自然コーパスの希少事実はどの露出頻度で高密度保存に達するか
- 容量上限「2 bit/param」は推論・手続き的知識にも当てはまるか、事実知識特有か
- データ SNR（低品質ノイズ混入）が希少知識の保存を阻害する効果は、実 web データでどの規模で効くか
