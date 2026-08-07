# 前回のまとめと、今回の3本の位置づけ

## 1. 前回のまとめ

講義資料（Fred Sala, CS839, UW-Madison, 2023）の後半だけを読むと「**ICL = 文脈内で勾配降下（GD）している**」に落ち着く。誤りではないが狭い、というのが前回の話だった。

Mao et al. のサーベイを読み直すと、ICL は2つの能力に分かれる。

| 能力 | 中身 | 理論枠組み |
|---|---|---|
| **skill recognition** | 事前学習で得た関数から最適な1つを**選ぶ** | Bayesian inference (Xie et al. 2021) |
| **skill learning** | 事前学習で見ていない**新しい関数を学ぶ** | Function learning (Garg et al. 2022) |

**GD説の位置**：skill learning の**内部メカニズムの一候補**にすぎない。前提は「データ生成関数が線形」「transformer を線形化」という限定設定で、示されたのは数学的等価である。skill recognition 側では GD は関与しない。

前回の結論は「GD説は ICL 全体の統一理論ではなく、skill learning 側の一部を説明する部分理論」だった。

---

## 2. 今回の3本の立ち位置

前回は「2能力がある」という**分類**を作るところまで。今回はその分類が実測でどこまで持つかを3方向から詰める。

| # | 論文 | 前回の枠組みに対して何をするか |
|---|---|---|
| 1 | [Structured Task Hypothesis](01-structured-task-hypothesis.md) | 2能力の**どちらでもない第3の軸**を足す。task selection も meta-learning も反証し「事前学習タスクの**合成**」を支持。**GD説を直接の検証対象に据えて棄却** |
| 2 | [Learning vs Retrieval](02-learning-vs-retrieval.md) | 2能力を**排他的な分類から連続量へ**組み替える。比率はプロンプト設計（例数・特徴量名）で操作できる。1本目を名指しで批判 |
| 3 | [Many-Shot ICL](03-many-shot-icl.md) | 2能力の**観測値がショット数に依存する**ことを示す。少ショットでは誤ったスキルが検索され（early ascent）、many-shot でタスク学習が取って代わる |

**今回の結論**：ICL は「認識か学習か」の二択ではない。モデルは、事前学習済みタスクや類似例の**選択・検索**、既知スキルの**合成**、文脈からの規則の**帰納・適合**を条件に応じて併用する。どれが支配的になるかは、ショット数やプロンプト設計だけでなく、事前学習タスクの多様性・モデル・タスク・デモの品質にも依存する。

<small>※3本はいずれも「そういう体制が存在する」ことを示す存在命題であり、一般則ではない。2025–2026 の後続研究を踏まえた留保は [README](README.md#その後の研究を踏まえた留保20252026) にまとめた。</small>

GD説にも更新が入る。1本目は「数十例では勾配降下による線形回帰と相関しない」、3本目は「数千ショットでは勾配降下に相当する計算をしている」。問いは**「GD説は正しいか」から「どの体制で GD 的挙動が現れるか」へ移る**。ただし GD は「**選ばれた予測器をどう適合させるか**」の問いで、認識・検索・合成・学習は「**その予測器がどこから来たか**」の問いである。軸が違うので両立しうる。

---

## 3. 時系列

| 時期 | 論文 | 学会 | 位置づけ |
|---|---|---|---|
| **2020-05** | **Brown et al., Language Models are Few-Shot Learners（GPT-3）** | NeurIPS 2020 | **ICL の提唱**。重み更新なしに文脈中の例だけでタスクを学ぶ現象を in-context learning と名付けた。今回の3本すべてがここを引く |
| 2021-11 | Xie et al., Implicit Bayesian Inference | ICLR 2022 | skill recognition の理論枠組み |
| 2022-02 | Min et al., Rethinking the Role of Demonstrations | EMNLP 2022 | ラベルを壊しても性能が落ちない＝recognition 寄りの証拠 |
| 2022-08 | Garg et al., What Can Transformers Learn In-Context? | NeurIPS 2022 | skill learning の理論枠組み |
| 2022-11 | Akyürek et al., What learning algorithm is ICL? | ICLR 2023 | GD説 |
| 2022-12 | Von Oswald et al., Transformers learn in-context by GD | ICML 2023 | GD説 |
| 2022-12 | Dai et al., Why Can GPT Learn In-Context? | Findings of ACL 2023 | GD説 |
| 2023-05 | Pan et al., Disentangling Task Recognition and Task Learning | Findings of ACL 2023 | 2能力の切り分けの原典 |
| 2023-10 | （Fred Sala 講義 `lecture9-icl.pdf`） | CS839, UW-Madison | 出発点。後半が GD説に振り切る |
| **2024-02** | **Mao et al., A Survey to Recent Progress Towards Understanding In-Context Learning** | Findings of NAACL 2025 | **前回のマスター**。2能力への再整理 |
| 2024-04 | Agarwal et al., Many-Shot In-Context Learning | NeurIPS 2024 Spotlight | **今回の3本目** |
| 2024-06 | Li et al., The Structured Task Hypothesis | ACL 2024 Main | **今回の1本目** |
| 2024-09 | Nafar et al., Learning vs Retrieval | NAACL 2025 Main | **今回の2本目** |

> **サーベイの日付に注意**：学会は NAACL 2025 だが arXiv v1 は **2024-02**。引用文献の山は2023年（68件）で、2024年は15件、2025年は0件。**中身は実質2024年初頭までの整理**であり、学会の年は実際の新しさを1年以上過大に見せる。

### 今回の3本について読み方のメモ

- **1本目 → 2本目は直接の論争**。Nafar et al. は Appendix B を丸ごと Li et al. への反論に充て、「出力ラベルは学習に使われているか」で結論が正反対になる。
- **3本目が両者に共通の穴を開ける**。1本目は数十例、2本目は最大100例。3本目は8192ショットまで開放し、「few-shot での否定的結論の一部は単にショット数不足だった」と示す。
