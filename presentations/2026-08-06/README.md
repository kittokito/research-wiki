# 勉強会発表資料 (2026-08-06)

## 発表テーマ：ICL は結局、文脈から何を学んでいるのか

## テーマ一覧

| # | タイトル | カテゴリ | 出典 | 役割 |
|---|---------|---------|------|------|
| 0 | [前回のまとめと、今回の3本の位置づけ](00-recap-and-positioning.md) | 導入 | — | 前回の要約・3本の立ち位置・時系列 |
| 1 | [The Structured Task Hypothesis](01-structured-task-hypothesis.md) | ICL / 仮説検証 | ACL 2024 Main | 起点（機構の同定） |
| 2 | [Learning vs Retrieval](02-learning-vs-retrieval.md) | ICL / 回帰・プロンプト設計 | NAACL 2025 Main | 二分法の解体（スペクトル） |
| 3 | [Many-Shot In-Context Learning](03-many-shot-icl.md) | ICL / 長文脈スケーリング | NeurIPS 2024 Spotlight | 体制の転換（スケール） |

## このセッションの主張（1枚で）

> **ICL は「認識か学習か」の二択ではない。**
> 実体は事前学習で獲得したタスクの**合成**であり、認識と学習の比率は**プロンプト設計とショット数**という操作可能な変数で決まる。
> few-shot 時代に得られた「ICL は学習していない」という結論の一部は、**ショット数が足りなかったこと**の帰結でもある。

## 前回からの接続

前回は Mao et al. (2025) のサーベイを使い、ICL を **skill recognition**（既知タスクの特定）と **skill learning**（文脈からの新規学習）の2能力に整理した。そのうえで、講義資料で強調されていた **GD 説**（transformer が順伝播の中で暗黙に勾配降下を実行しているという説明）を「skill learning の内部機構の一候補、しかも線形回帰という限定設定での数学的等価」として位置を下げた。

今回の3本は、この枠組みに次の3つの更新を加える。

1. **第3の軸が要る**（1本目）。2能力の間に「既知タスクの**合成**」がある。ICL は札を1枚引いているのではなく、複数の札を組み合わせている。
2. **2能力は排他的でない**（2本目）。認識と学習は連続量の両端であり、比率はプロンプト設計で動かせる。
3. **同じ実験でもショット数で結論が変わる**（3本目）。ラベルを反転させた感情分析は、少ショットでは事前学習バイアスに負け、ショットを増やすと通常ラベルに追いつく。同じモデル・同じタスクで、測ったショット数だけで「認識が優勢」から「学習が優勢」へ見え方が反転する。

GD 説についても、今回は2回の更新が入る。1本目は GD 説を**直接の検証対象**に据えて「LLaMA2-70B・数十例では勾配降下による線形回帰と相関しない」と示す。一方で3本目は「Gemini 1.5 Pro・数千ショットでは勾配降下に相当する計算をしている」と述べる。**問いは「GD 説は正しいか」から「どの体制で GD 的挙動が現れるか」へ移る。**

## ストーリーの弧

```
1本目  仮説の選択         認識 / 学習 / 合成 のどれか？  →  合成
   ↓   （排他的・離散）        GD説を直撃して棄却
   
2本目  比率の操作         認識と学習の比率は何で決まる？ →  例数↑で学習側 / 特徴量名↑で検索側
   ↓   （連続・操作可能）      1本目を名指しで批判
   
3本目  体制の転換         ショット数を3桁増やすと？     →  事前学習バイアスを上書き
       （スケール依存）          few-shotの否定的結論が崩れる      非言語の高次元関数を学習
                                                                  SFTに並ぶ
```

## 3本のつながり（クロスリンク）

- **2本目 → 1本目の直接批判**：Nafar et al. は Appendix B を丸ごと Li et al. 2024 への反論に充てている。争点は (a) LLaMA 2 のみを使った点（長文脈でタスクを忘れる既知の問題があり、公開時点で LLaMA 3 は既に利用可能だった）、(b) データセットが平易すぎる点、(c) 埋め込み層に依存した実験（線形モデルを80層に合わせて80エポック訓練するなど）の正当化が弱い点。**「出力ラベルは学習に使われているか」で結論が正反対**になる。
- **3本目が部分的に決着をつける**：1本目は数十例、2本目は文脈長の制約から最大100例。3本目は 8192ショット・100万トークンまで開放する。事前学習バイアスの上書きは **few-shot では起きず many-shot で起きる**（Figure 10）。「学習が起きないように見えた」観測の一部は、単にショット数が足りなかっただけだった。
- **early ascent が要石**：3本目が few-shot での性能・確信度の落ち込みを説明する概念として引くのが **Pan et al. 2023（"Disentangling task recognition and task learning"）**——前回の 2能力枠組みの出典そのものである。少数ショットでは**誤ったスキルが検索され**、many-shot でタスク学習が取って代わる。2能力の枠組み自体が、ショット数に依存する現象として使われている。
- **データ汚染という共通の穴**：2本目は「言語的手がかりが一切なくても数値列だけで汚染が起きうる」と示した（Anonymized Features での改善が実際の特徴量重要度と対応しない）。3本目の評価タスク（MATH・GSM8K・BBH）はいずれも汚染の疑いが濃く、伸び幅のどこまでが真の文脈内学習かは切り分けられていない。
- **合成 vs 検索の呼び分け**：2本目は「タスク選択も合成も、まとめて knowledge retrieval の傘に入れる」と明言している。1本目の H1（選択）と H3（合成）の区別を、2本目は意図的に潰している。**同じ現象を違う粒度で切っている**点に注意して読む必要がある。

## 図表ディレクトリ

`figures/` に各論文の原典 PDF から切り出した図表を配置（Python 生成のグラフは作らない方針）。各 .md 本文に埋め込み済み。

```
figures/
  st-fig1-hypotheses.png             # 1本目 Fig 1: 3仮説の図解（選択 / メタ学習 / 合成）
  st-fig2-ra-pa.png                  # 1本目 Fig 2: RAタスク(応答改変)とPAタスク(プロンプト改変)
  st-fig3-ra-icl-learns.png          # 1本目 Fig 3: RAタスクもLを増やせば80%超（H1の棄却）
  st-fig5-pa-below-chance.png        # 1本目 Fig 5: PA-ICLはチャンス以下、PA-LR(ロジスティック回帰)は約50%
  st-table1-icl-vs-linear.png        # 1本目 Tab 1: 暗記課題でICL 59.8 vs 勾配降下線形回帰 99.9（GD説の直撃）
  st-fig6-composition-correlation.png # 1本目 Fig 6: 部品τ_gの学習性と合成τ_RAの学習性が相関（H3の支持）
  st-table2-natural-vs-random.png    # 1本目 Tab 2: 自然な写像(同義語/対義語/キーワード) vs ランダム写像
  st-fig7-synonym-orders.png         # 1本目 Fig 7: 同義語の次数（positive→tang / negative→or）
  st-fig8-order-decay.png            # 1本目 Fig 8: 次数（＝合成の複雑さ）が上がるほど性能低下
  lvr-fig1-configs.png               # 2本目 Fig 1: 3プロンプト構成（Named / Anonymized / Randomized GT）
  lvr-fig2-direct-qa.png             # 2本目 Fig 2: Direct QAのベースライン。Admission ChanceはMean model以下
  lvr-fig3-config-comparison.png     # 2本目 Fig 3: 全因子での総合比較。Randomized GTが一貫して最悪
  lvr-fig3-insurance-zoom.png        # 2本目 Fig 3拡大: NamedがAnonymizedのほぼ内側＝ほぼ一貫して低誤差
  lvr-fig5-vs-classical-ml.png       # 2本目 Fig 5: 10-30例ではLLMがRidge/RandomForestを上回る
  lvr-fig6-features.png              # 2本目 Fig 6: 特徴量数の効果（Anonymizedは単調、Namedは非単調）
  lvr-fig7-ker.png                   # 2本目 Fig 7: KER(知識の寄与)は10例で最大、100例でほぼ消える
  ms-fig1-few-vs-many.png            # 3本目 Fig 1: 11タスクでのfew-shot vs many-shot（最大+36.4）
  ms-fig3-translation.png            # 3本目 Fig 3: 低資源翻訳でNLLB/Google Translateを超える
  ms-fig4-summarization.png          # 3本目 Fig 4: XSumは50ショットで頭打ち、XLSum(転移)は伸び続ける
  ms-fig7-reinforced-unsupervised.png # 3本目 Fig 7: Reinforced/Unsupervised ICL（MATH500・GSM8K転移）
  ms-fig10-pretraining-bias.png      # 3本目 Fig 10: flipped/abstractラベルがmany-shotでdefaultに接近
  ms-fig11-highdim-classification.png # 3本目 Fig 11: 16/32/64次元の線形分類がkNNに追随
  ms-fig12-parity.png                # 3本目 Fig 12: 20桁系列パリティ。20倍データのGPT-2 Mediumを超える
  ms-fig13-sft-vs-icl.png            # 3本目 Fig 13: 997例でSFT 47.7 vs many-shot ICL 47.2（Bemba）
  ms-fig15-frontier-llms.png         # 3本目 Fig 15: 4モデル比較。few-shotの強さはmany-shotの強さを予測しない
  ms-fig16-distinct-vs-repeated.png  # 3本目 Fig 16: 同じ25例の繰り返しは効かない（情報量が効いている）
  ms-fig17-ordering.png              # 3本目 Fig 17: 50ショットでも順序感度は残る
```

出典：Structured Task Hypothesis arXiv 2406.04216（ACL 2024, pp. 12365–12379）／ Learning vs Retrieval arXiv 2409.04318（NAACL 2025, pp. 8206–8229）／ Many-Shot ICL arXiv 2404.11018（NeurIPS 2024 Spotlight）。
