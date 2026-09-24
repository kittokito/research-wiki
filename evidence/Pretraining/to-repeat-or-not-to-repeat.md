---
source: src-to-repeat-or-not-to-repeat
date_extracted: 2026-06-19
---

# To Repeat or Not To Repeat からの抽出

## 主要な主張

### 背景：token-crisis（トークン枯渇）
- compute-optimal LLM を学習し切るのに必要なトークン数は、web 上の高品質テキストの増加速度を**大きく上回る**。PaLM-540B を完全学習するには **10.8兆トークン**必要だが、高品質テキストの総ストックは **~9兆トークン**、成長率は年 **4-5%** [source: §1](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- 悲観シナリオでは **2023〜2027年に新規高品質データが枯渇**しうる。**データはハードウェアよりも深刻なボトルネック**になりうる [source: §1](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- 緩和の最も素朴な手段が「**事前学習データを複数エポック繰り返す**」こと。本研究はその効果を体系的に検証する最初の研究 [source: §1](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

### 繰り返しの帰結（Sec 2）
- **【核心】Multi-epoch degradation（多エポック劣化）**: 事前学習データを繰り返すと**過学習に陥り性能が劣化**する。**大きいモデルほど token-crisis 下で過学習しやすい** [source: §2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- 十分なデータがないと、**T5-XL は計算資源をより多く消費しても、4倍のデータ（2²⁹ vs 2²⁷ トークン）を持つ T5-Large に負ける** [source: §2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **下流タスクにも波及**: SQuAD ファインチューニングでも劣化。2²⁷ トークン学習は事前学習 val acc が 2.9pt 下がるだけでなく、**下流 F1 が 1.9pt 低下** [source: §2, Table 1](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- Encoder-Decoder（T5）は Chinchilla scaling law 同様にデータ飢餓的で、必要トークン数とパラメータ数は**線形関係**（Fig 2）。Encoder-Decoder と Decoder-only は本質的に大きく違わない（Appendix F で確認） [source: §2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

### 劣化の支配要因（Sec 3）
- **【データ】データセットサイズ（重要）**: 大きいデータセットは多エポック劣化を緩和。2²⁷ トークンを 2⁸ エポック回すと顕著に過学習するが、2²⁹ トークンを同ステップ数なら劣化しない（バッチサイズ固定の追加 ablation でも確認、Appendix G） [source: §3.1](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **【データ】データ品質（影響小）**: 高品質とされる **Wikipedia でも多エポック劣化は緩和されない**。Wikipedia 2²⁷ トークンの SQuAD EM は **-3.0**（C4 2²⁷ の -2.5 と同程度）に劣化。ただし「品質」は相対概念で、極端な低品質データはクリーニングで品質が効く余地あり [source: §3.1, Table 2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **【モデル】パラメータ数（重要）**: 計算予算固定でも**パラメータ数が劣化に決定的**。MoE で増やす / ParamShare で減らす（FLOPs 同等）と切り分け、**パラメータが少ないほど繰り返しの悪影響が小さく、学習可能パラメータが多いほど限られたデータで過学習しやすい** [source: §3.2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **【モデル】FLOPs（影響小）**: 学習可能パラメータを固定し FLOPs を 1×/2×/4× に変えても、劣化の明確な増加は観測されない（FLOPs の影響は無視できる） [source: §3.2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **【目的関数】目的関数の混合（UL2）**: UL2（next-token prediction と MLM を混合）は学習を加速するが**記憶（memorization）も速め、多エポック劣化を悪化**させる。UL2 w/ repeat の SQuAD F1 は **-2.5**（vanilla MLM の -1.9 より大きい劣化） [source: §3.3, Table 3](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

### MoE による dense 挙動の予測（Sec 3.2）
- **MoE は同等の学習可能パラメータを持つ dense モデルの過学習挙動をほぼ再現**する。Dense Large 784M vs MoE Base 701M（MoE は **0.39× FLOPs・2.1× throughput**）、Dense XL 2.8B vs MoE Large 2.4B（**0.32× FLOPs・3.8× throughput**）でほぼ同一の過学習トレンド [source: §3.2, Fig 6](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- 含意: GPT-4 が小モデルで大モデル挙動を予測したように、**安価な sparse MoE で高価な大規模 dense モデルの挙動を低炭素・低コストで予測**できる [source: §3.2](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

### 正則化による緩和（Sec 4）
- **【dropout が極めて有効】**: ほとんどの正則化（DropPath・label-smoothing・weight decay）は効かない中、**dropout だけが多エポック劣化を顕著に緩和**。限られたデータで dropout あり val acc **63.0** vs なし **61.7**。weight decay は学習を不安定化（**NaN**）させうる [source: §4, Table 4](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **dropout は LLM で過小利用**: GPT-3・PaLM・LLaMA・Chinchilla・Gopher など 10B 超の主要 LLM は dropout を使わない（データ潤沢だと dropout は学習を遅らせるため）。**Galactica は例外**で dropout を使い 120B を過学習なく学習できた可能性 [source: §4](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **【dropstage：後段から dropout 投入】**: 事前学習の**前半は dropout なし**で速く学習し、数エポック後に dropout を入れる方式（dropstage）でも、最初から dropout を入れた場合と同等の最終性能。前半の学習はむしろ速い [source: §4, Insight 9, Fig 8](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- **大規模では追加チューニングが必要**: dropout は完全な解ではなく、**XL スケールでは dropout を入れても後半に検証精度がやや低下**しうる [source: §4, Insight 10, Fig 9](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

### MoE をハイパラ探索の代理に（Sec 5）
- **MoE Hyper-Parameter Tuning**: 大規模 dense モデルのハイパラ（例: dropout rate）探索は高価（T5-XL を5回学習 ≈ **$37,000**）。**安価な MoE で dropout rate を sweep（0.1〜0.5）→ 最適 0.2〜0.3 を特定し、Dense XL で検証するとほぼ同一曲線** [source: §5, Insight 11, Fig 10](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- コスト比較: MoE Large の sweep が **10.6K USD**、Dense XL 単発が 7.4K USD、開発全体で 18K USD ＝ **Dense XL を直接チューニングする費用の 0.48倍** [source: §5](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)
- 最終結果: 適切な dropout を MoE 経由で導入すると、Chinchilla 則では 16M モデル分しかない 2²⁷ トークンでも、**1700倍超大きい 2.8B パラメータまでスケールして改善**できる [source: §5](../../sources/Pretraining/to-repeat-or-not-to-repeat.md)

## 主要な貢献
- token-crisis 下で「データ繰り返し」を体系的に研究した**最初の実証研究**。11の insight に集約
- 多エポック劣化の支配要因を **(重要) データサイズ・パラメータ数・目的関数 / (影響小) データ品質・FLOPs** に整理
- 緩和策として **dropout の有効性**（特に後段投入＝dropstage）と限界（大規模での追加チューニング）を特定
- **MoE を dense 挙動予測・ハイパラ探索の安価な代理**として使う手法を提案（コスト 0.48倍）

## 制限・注意点
- T5（encoder-decoder）/ C4 / 最大 2.8B パラメータ規模での実験。フロンティア規模の decoder-only LLM へ直接外挿はできない（ただし encoder-decoder ≈ decoder-only を Appendix F で確認）
- 「データ品質」の結論は web スケール内の相対品質（C4 vs Wikipedia）に限定。高品質 instruction data やデータ合成・リライトによる**高品質トークンの拡張**は射程外
- 2023年の研究で、当時の token-crisis 予測（2023-2027 枯渇）はその後のデータ合成・多モーダル化で前提が変わりうる

## ベンチマーク結果

### Multi-epoch degradation（SQuAD ファインチューニング, Table 1 / 2）
| 事前学習設定 | C4 Val Acc | SQuAD EM | SQuAD F1 |
|---|---|---|---|
| T5-Base C4 2³⁵ トークン（1 epoch） | 64.6 | 82.4 | 90.0 |
| T5-Base C4 2²⁷ トークン（2⁸ epochs） | 61.7 (-2.9) | 79.9 (-2.5) | 88.1 (-1.9) |
| Wikipedia 2³⁵ トークン | — | 82.4 | 89.9 |
| Wikipedia 2²⁷ トークン | — | 79.4 (-3.0) | 87.6 (-2.3) |

### 目的関数（MLM vs UL2, Table 3）
| 設定 | SQuAD EM | SQuAD F1 |
|---|---|---|
| MLM w/o repeat | 82.4 | 90.0 |
| MLM w/ repeat | 79.9 (-2.5) | 88.1 (-1.9) |
| UL2 w/o repeat | 82.5 | 90.1 |
| UL2 w/ repeat | 79.6 (-2.9) | 87.6 (-2.5) |

### 正則化 ablation（限られたデータ, Table 4）
| 設定 | Val Acc |
|---|---|
| 限られたデータ・正則化なし | 61.7 |
| + dropout | 63.0 |
| + DropPath | 62.9 |
| + label-smoothing | 62.6 |
| + weight decay | NaN（不安定化） |

### MoE による dense 予測（Fig 6）
| 比較 | パラメータ | MoE の相対 FLOPs | MoE の throughput | 過学習トレンド |
|---|---|---|---|---|
| Dense Large vs MoE Base | 784M vs 701M | 0.39× | 2.1× | ほぼ同一 |
| Dense XL vs MoE Large | 2.8B vs 2.4B | 0.32× | 3.8× | ほぼ同一 |

## 実装関連
- **データが潤沢でない事前学習では dropout を入れる**（特に前半なし→後半投入の dropstage が学習速度と正則化を両立）
- 大規模 dense のハイパラ探索は **MoE で安価に代理探索**してから本番に移すとコスト 0.48倍
- 限られたデータでは**モデルを大きくしすぎない**／**データセット自体を大きくする（合成・収集）**ことが、品質改善より直接的に効く
