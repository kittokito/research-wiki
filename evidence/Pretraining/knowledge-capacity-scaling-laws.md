---
source: src-knowledge-capacity-scaling-laws
date_extracted: 2026-06-09
---

# Knowledge Capacity Scaling Laws からの抽出

## 主要な主張
- LM の保存知識量を**情報理論的に bit 数で推定**（loss やベンチでなく）。事実知識はタプル（例: (USA, capital, Washington D.C.)）で表現 [source](../../sources/Pretraining/knowledge-capacity-scaling-laws.md)
- LM は **1パラメータあたり最大「2 bits」の知識**を保存でき、それが上限。**int8 量子化でも 2 bit/param は維持**される [source](../../sources/Pretraining/knowledge-capacity-scaling-laws.md)
- 保存知識は downstream で**柔軟に抽出可能** [source](../../sources/Pretraining/knowledge-capacity-scaling-laws.md)
- **【核心メモ】露出回数（training duration）が容量を支配**: 各知識を**約1000回露出**させると **2 bits/param のピーク容量**に到達（＝高密度に保存）。露出が**約100回**に減ると容量はおよそ**半減し ~1 bit/param** に低下 [source](../../sources/Pretraining/knowledge-capacity-scaling-laws.md)

## 主要な貢献
- 「2 bits/param」という普遍的な知識容量則の確立（制御データセットで実証）
- 容量に影響する5因子を体系化: **(1) 訓練時間/露出回数・(2) アーキテクチャ・(3) 量子化・(4) MoE 等スパース性・(5) データ SNR**、計12の結果
- 系: 7B モデル ≒ 14B bit ＝英語 Wikipedia＋教科書を超える知識量
- 知見例: 露出不足（100回）だと容量半減 / int8 までは無害だが int4 等では劣化 / データに低品質ノイズが混ざると稀少知識の保存が阻害される（SNR の影響）

## 制限・注意点
- 合成・制御データセット（事実タプル）での測定で、自然な web コーパスの雑多な知識へそのまま外挿できるとは限らない
- 「factual knowledge tuple」の保存に焦点で、推論・手続き的知識の容量は対象外

## ベンチマーク結果
| 条件 | 知識容量 |
|---|---|
| 十分な露出（各知識 ~1000回） | **2 bits / parameter**（ピーク・高密度） |
| 露出不足（各知識 ~100回） | およそ半減（**~1 bit / parameter**） |
| int8 量子化 | 2 bits/param を維持 |

## 実装関連
- 「希少知識（露出が少ない事実）は保存効率が落ちる」→ 重要事実は学習データ中の出現頻度（露出回数）を確保することが高密度保存に効く、という実務的含意
