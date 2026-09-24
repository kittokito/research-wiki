---
source: src-scaling-data-constrained-language-models
date_extracted: 2026-06-19
---

# Scaling Data-Constrained Language Models からの抽出

## 主要な主張

### 問題設定と規模
- Chinchilla 則を素朴に外挿すると、現在の大規模モデルは近い将来 **web 上のテキスト総量に制約**される。高品質英語データは Chinchilla 則とモデル巨大化の趨勢のもとで **2024年頃に枯渇**しうる（Villalobos et al. 推定）。「データが尽きたらどうするか？」が本研究の問い [source: §1](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **400超の学習run**（GPT-2 アーキ/トークナイザ、**10M–8.7B パラメータ・最大900B総トークン・最大1500エポック**、C4 サブセット）で data-constrained レジームを実証。early stopping を使わず過学習も観察 [source: §4](../../sources/Pretraining/scaling-data-constrained-language-models.md)

### Data-Constrained Scaling Law（中核の数式）
- Chinchilla の **L(N,D) = A/N^α + B/D^β + E** を、繰り返しで価値が減衰する**実効データ D'・実効パラメータ N'** に置き換える [source: §3.1](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **D' = U_D + U_D·R\*_D·(1 − e^(−R_D/R\*_D))**（Eq 5）。U_D=ユニークトークン数=min{D_C, D}、R_D=繰り返し回数=（D/U_D）−1=エポック−1。繰り返しのたびにトークンは価値の **(1 − 1/R\*_D)** 分を失う指数減衰 [source: §3.1](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **N' = U_N + U_N·R\*_N·(1 − e^(−R_N/R\*_N))**（Eq 6）。過剰パラメータも同様に価値が減衰 [source: §3.1](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- R\*_D, R\*_N は学習される「半減期」定数。**R_D = R\*_D のとき、繰り返しトークンは平均 1 − 1/e ≈ 63% の価値**。含意: 何回繰り返しても、**U_D + U_D·R\*_D 個の新鮮なトークンを1エポック学習した損失は超えられない** [source: §3.1](../../sources/Pretraining/scaling-data-constrained-language-models.md)

### Return（繰り返しの価値）
- **【核心】固定計算量下で、最大~4エポックの繰り返しデータは新規データとほぼ同等**（損失の差は無視できる・下流タスク差も非有意）。例: 8.7B モデルを4エポック（D_C=44Bユニーク）学習すると、1エポック（178Bユニーク）比で **検証損失わずか +0.5%** [source: §6, Fig 4-5](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- 意味ある改善は **~16エポック（R\*_D≈15）まで**。それを超えると **リターンは極めて速く減衰**し、**~40エポックで繰り返しは無価値**。過剰な繰り返しでは**計算量を足す価値も最終的にゼロに減衰** [source: §6, Fig 5](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- 計算量・エポックを増やしすぎると損失は下がってから**再び上昇**（過学習・発散）しうる。Fig 4 では 2.8B/55B・4.2B/84B・8.7B/178B の isoFLOP で多エポックほど損失が悪化し、エポック過多で発散 [source: §5, Fig 4](../../sources/Pretraining/scaling-data-constrained-language-models.md)

### Allocation（データ制約下の計算配分）
- **【核心】Chinchilla（N と D を等比スケール）と異なり、データ制約下では「パラメータよりエポックを速くスケール」すべき**。**過剰パラメータは繰り返しデータより速く価値が減衰する（R\*_N < R\*_D）**ため、追加計算の大半はパラメータ増ではなく多エポックに振るのが最適 [source: §5-6, Fig 1, 3](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- 9.3×10²¹ FLOPs・25Bユニークトークンで効率的フロンティアに従うと、**Chinchilla 推奨より27%少ないパラメータ**のモデルが、損失も下流性能も上回る [source: §6](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- 100Mユニークトークンでは、多エポック＋モデル拡大で **損失50%超の削減**が可能。最良損失は **20–60倍のパラメータ・エポック（≈7000倍の FLOPs）**で得られる＝1エポックモデルは学習データを大きく過小利用 [source: §5, Fig 3](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- 含意: Galactica の **120B はデータ制約則からは過大**で、もっと小さくすべきだった。小モデルは推論も安価 [source: §6](../../sources/Pretraining/scaling-data-constrained-language-models.md)

### Complementary Strategies（データ拡張の補完策、D_C=84B・N=4.2B）
- **(a) コード拡張**: 不足する自然言語データを The Stack の Python コードで補う。**最大50%（42Bトークン）をコードに置換しても NL タスク性能は劣化せず＝実効トークンを実質2倍**にできる。さらにコードを増やすと、ベンチ外の **WebNLG（生成）・bAbI（推論）で性能ジャンプ**（コードが long-range state-tracking 能力を与える可能性） [source: §7, Fig 6](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- **(b) フィルタリングの見直し**: perplexity フィルタと重複除去（dedup）を再検証。**perplexity フィルタは有効、dedup はクリーンなデータでは効かない**。データフィルタは**主にノイズの多いデータセットで有効**で、データ制約下ではフィルタを外してデータ量を確保する方が有利なことも [source: §7, Fig 6, Appendix O](../../sources/Pretraining/scaling-data-constrained-language-models.md)
- 組合せ例: **まずコードでデータ2倍 → それを4エポック繰り返す＝8倍の学習トークン**で、最初から8倍ユニークデータがあった場合と同等が期待できる [source: §7](../../sources/Pretraining/scaling-data-constrained-language-models.md)

## 主要な貢献
- **Chinchilla 則のデータ制約版（data-constrained scaling law）** を提案・実証。繰り返しデータ・過剰パラメータの価値減衰を実効量 D'・N' で定式化（R\*_D, R\*_N の半減期定数）
- 「**最大4エポックの繰り返しはほぼ無害／~16エポックまで有用／~40エポックで無価値**」という実務的な繰り返し指針
- データ制約下では「**エポックをパラメータより速くスケール**」という Chinchilla と異なる配分則
- コード拡張で**実効トークン2倍**・フィルタリングは**ノイズ用**という2つの補完的データ拡張策
- 400 run のモデル・データセットを公開（huggingface/datablations）

## 制限・注意点
- GPT-2 アーキ・英語 C4・最大 8.7B パラメータでの実験。フロンティア規模・多言語・マルチモーダルへの直接外挿は保証されない
- 提案式は**過剰なエポック/パラメータが性能を害する可能性をモデル化していない**（単調に飽和する形）。経験的には計算過多で損失が再上昇しうると注記
- コード/フィルタの下流評価は19のNLタスク中心で、コードの一部の便益（long-range タスク）は主ベンチ外

## ベンチマーク結果

### 繰り返しの価値（isoFLOP, Fig 4 / §6）
| 設定 | ユニークデータ D_C | 比較 | 結果 |
|---|---|---|---|
| 8.7B / 178B トークン・1エポック | 178B | 基準 | 単一エポック最良 |
| 8.7B / 178B トークン・4エポック | 44B | vs 1エポック | 検証損失 **+0.5%**（ほぼ同等） |
| 一般則 | — | ~4エポック | 損失・下流とも差が無視できる |
| 一般則 | — | ~16エポック（R\*_D≈15） | ここまで意味ある改善 |
| 一般則 | — | ~40エポック | 繰り返しは無価値 |

### データ拡張・フィルタリング（D_C=84B, N=4.2B, Fig 6 / §7）
| 戦略 | 効果 |
|---|---|
| データ繰り返し | ~4エポック（予算25%）まで下流性能差は非有意、その後低下 |
| コード50%混入（42B） | NL タスクに劣化なし＝**実効トークン2倍**。WebNLG/bAbI は性能ジャンプ |
| perplexity フィルタ | 有効 |
| 重複除去（dedup） | クリーンデータでは効果なし（主にノイズデータで有効） |

## 実装関連
- **データが不足する事前学習では、最大4エポックの繰り返しは「ほぼタダ」**で計算予算を伸ばせる。16エポック超は急速に効かなくなる
- **データ制約下では大きすぎるモデルを避け、小さめモデルを多エポック**回す（パラメータよりエポックを優先配分）。推論も安価になる
- ユニークデータが足りないときは **コード混入（最大50%で実効2倍）** が有効。**フィルタ（dedup）はノイズの多いデータにだけ**適用し、クリーンデータでは外してデータ量を確保
- 公開資産: github.com/huggingface/datablations（400 run のモデル・データ）
