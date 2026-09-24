# Recent Additions

最近追加・更新されたページ。新しい順。

---

## 2026-07-01

- [TabFM: A Zero-Shot Foundation Model for Tabular Data](../wiki/papers/Technical_Report/tabfm.md) を追加 — Kong, Das ほか（**Google Research**）、発表ブログ（2026-06-30）。表形式データの分類・回帰を **in-context learning** として定式化し、追加訓練・ハイパラ調整・特徴量エンジニアリング不要で**単一 forward pass** でゼロショット予測する基盤モデル。alternating row/column attention + row compression + ICL の3機構、**構造因果モデル(SCM)由来の数億の合成データのみ**で事前学習し、TabArena（38分類+13回帰）で教師あり定番手法を上回るトップ ELO。TabPFN/TabICL 系譜の統合で、[CLIP](../wiki/papers/Multimodal/clip.md) 的な「基盤モデル＋ゼロショット転移」を表データ領域に持ち込む (Kong, Das et al., 2026 / Google)

## 2026-06-24

- [One Single Hub Text Breaks CLIP](../wiki/papers/Multimodal/hub-text-breaks-clip.md) を追加 — Deguchi, Chousa, Sakai（**NTT × NAIST**）、arXiv 2604.27674、**ACL 2026 Main**。CLIP 系 **cross-modal encoder の hubness 脆弱性**を実証。無関係な多数画像と高類似度になる単一の **hub text** を「hub 埋め込みの閉形式導出→逆変換 decode→beam local search」の3段階で生成する。意味的に無意味な1テキストが多くの画像で人手キャプションの CLIPScore を超え（**Ours 0.842 > Human 0.759**、強モデルで勝率 90%）、image-to-text retrieval は単一挿入でも **Precision@1 −29.3%**。CLIPScore 指標と cross-modal retriever 双方の脆弱性を露呈。[CLIP](../wiki/papers/Multimodal/clip.md) への攻撃面 (Deguchi, Chousa, Sakai, 2026)

## 2026-06-19

- [Scaling Data-Constrained Language Models](../wiki/papers/Pretraining/scaling-data-constrained-language-models.md) を追加 — Muennighoff, Rush, Barak, Raffel ほか（**Hugging Face × Harvard × Turku**）、arXiv 2305.16264、**NeurIPS 2023 Oral / Outstanding Paper Runner-Up**。400超の run（最大8.7B・900Bトークン）で **Chinchilla 則をデータ繰り返しに拡張した data-constrained scaling law** を提案。**最大~4エポックの繰り返しは新規データとほぼ同等・~16エポックまで有用・~40エポックで無価値**（R\*_D≈15 が繰り返しの半減期）、データ制約下では「パラメータよりエポックを速くスケール」、コード50%混入で実効トークン2倍。下記 [To Repeat or Not To Repeat](../wiki/papers/Pretraining/to-repeat-or-not-to-repeat.md) と同 NeurIPS 2023 の token-crisis 対ペア (Muennighoff et al., 2023)
- [To Repeat or Not To Repeat (Token-Crisis)](../wiki/papers/Pretraining/to-repeat-or-not-to-repeat.md) を追加 — Xue, Fu, Zhou, Zheng, You（**NUS × Edinburgh × ETH**）、arXiv 2305.13230、**NeurIPS 2023**。高品質テキストが枯渇する **token-crisis** 下で事前学習データを複数エポック繰り返すと **過学習＝multi-epoch degradation** が起きることを T5/C4 で実証。支配要因はデータサイズ・パラメータ数・目的関数（品質・FLOPs は影響小）、緩和は **dropout が有効**、**MoE が dense の過学習挙動を低コスト予測**。[Knowledge Capacity](../wiki/papers/Pretraining/knowledge-capacity-scaling-laws.md)（繰り返し露出を有益とする）の表裏 (Xue et al., 2023)

## 2026-06-11

- [The Implications of Large-Scale Test-Time Compute](../wiki/papers/Inference_Decoding/implications-of-test-time-compute.md) を追加 — Noam Brown（**OpenAI**）の論説（ICLR 2026 招待講演に対応）。**性能向上に伴いベンチ成績がテスト時計算量(test-time compute)に左右される度合いが増し、現代 LLM の能力上限は未知**と主張、test-time compute を第3のスケーリング軸と位置づける。[Reasoning with Sampling](../wiki/papers/Inference_Decoding/reasoning-with-sampling.md) / [RLVR能力境界論争](../wiki/topics/RL/rlvr-capability-boundary.md) の姉妹論点。※X article 本文未取得・テーゼのみ記録 (Noam Brown, 2026)

## 2026-06-09

- [Knowledge Capacity Scaling Laws (Physics of LM 3.3)](../wiki/papers/Pretraining/knowledge-capacity-scaling-laws.md) を追加 — Allen-Zhu & Li（**Meta FAIR**）、arXiv 2404.05405、**ICLR 2025 Spotlight**。LM の保存知識量を bit で実測し **1パラメータ＝最大2 bit**（int8 でも維持、7B≒Wikipedia＋教科書超）と確立。**各知識を~1000回露出で 2bit/param の高密度に到達、~100回だと容量半減**。訓練時間・アーキ・量子化・MoE・SNR の5因子×12結果。[Reversal Curse](../wiki/papers/Reasoning/reversal-curse.md) と「保存と抽出可能性は別」で対 (Allen-Zhu & Li, 2024)
- **トピック追加**: [LLMと真の論理的理解の壁](../wiki/topics/Reasoning/llm-logical-understanding-wall.md) — 「ベンチ高得点＝真の論理理解か？」を3水準（表層摂動／論理摂動／評価の妥当性）で整理するポジション。[GSM-Symbolic](../wiki/papers/Reasoning/gsm-symbolic.md)・[Potemkin Understanding](../wiki/papers/Reasoning/potemkin-understanding.md) 等6本を束ね「LLM は意味でなく表層・統計的規則性に依存して正解しうる」と結論。[RLVRの能力境界論争](../wiki/topics/RL/rlvr-capability-boundary.md) の姉妹論点
- [Potemkin Understanding in LLMs](../wiki/papers/Reasoning/potemkin-understanding.md) を追加 — Mancoridis, Weeks, Vafa, Mullainathan、**ICML 2025**。ベンチ正解から能力を推論できるのは「LLM が人間と同じ仕方で概念を取り違える」場合に限り妥当——さもなくば正解は **potemkin understanding（理解の幻想）**。potemkin はモデル・タスク・ドメインに遍在し概念表現の内的非一貫性を反映、評価の前提を崩す (Mancoridis et al., 2025)
- [Paraphrase and Solve (SCoP)](../wiki/papers/Reasoning/paraphrase-and-solve-scop.md) を追加 — Zhou ほか、**NAACL 2024 Long**。数学問題の**表層形のわずかな変更**で solve rate が激変＝表層形への非頑健を露呈。緩和策 Self-Consistency-over-Paraphrases を提案するが根本原因は残る。[GSM-Symbolic](../wiki/papers/Reasoning/gsm-symbolic.md) と同型の脆弱性を言い換え軸で実証 (Zhou et al., 2024)
- [RobustLR](../wiki/papers/Reasoning/robustlr.md) を追加 — Sanyal, Liao, Ren（**USC**）、arXiv 2205.12598、**EMNLP 2022**。自然言語ルールベース上の**演繹推論**が最小論理編集・論理等価変換に頑健でないことを診断。RoBERTa・T5 は特に**否定・選言の学習が困難**で、論理意味でなく表層に依存と論証。[Reversal Curse](../wiki/papers/Reasoning/reversal-curse.md) と並ぶ論理構造の非内在化の証拠 (Sanyal, Liao, Ren, 2022)
- [Exploring the Limits of Transfer Learning (T5)](../wiki/papers/Pretraining/t5-text-to-text-transformer.md) を追加 — Raffel ほか（**Google**）、arXiv 1910.10683、**JMLR 2020**。NLP の全テキストタスクを **text-to-text** に統一し、目的関数・アーキ・データ・転移手法を数十タスクで体系的にアブレーション。新データセット **C4** とスケールで多数ベンチ SOTA。pretrain→finetune transfer の記念碑で、[A Survey on Negative Transfer](../wiki/papers/Surveys_Overview/survey-on-negative-transfer.md) の positive transfer 側の代表 (Raffel et al., 2020)
- [A Survey on Negative Transfer](../wiki/papers/Surveys_Overview/survey-on-negative-transfer.md) を追加 — Zhang, Deng, Zhang, Wu、arXiv 2009.00909、**IEEE/CAA J. Automatica Sinica 2022**。**negative transfer（source 知識の利用が target 性能を下げる現象）**の初の体系的サーベイ。約50手法を secure transfer / domain similarity / distant transfer / NT mitigation の4分類で整理。[SHLPT](../wiki/papers/Post_Training/shlpt-lifelong-prompt-tuning.md) の一般論版で「類似度推定で転移可否を測る」系譜の先祖。2020年提出で LLM 時代の転移は射程外 (Zhang et al., 2022)
- [A Functional Taxonomy of World Models](../wiki/papers/Physical_AI/a-functional-taxonomy-of-world-models.md) を追加 — **Fei-Fei Li**（**World Labs**）、Substack 論説。「world model」を機能で3分類: **renderer**（ピクセル観測）/ **simulator**（幾何・物理・動力学に忠実）/ **planner**（観測＋目標→action）。POMDP の agent loop に位置づけ「LM＝テキストの統計構造／world model＝空間と時間の統計構造」と対比、unified world model への収束を展望。本リポジトリの [V-JEPA 2](../wiki/papers/Physical_AI/v-jepa-2.md) / [LeWM](../wiki/papers/Physical_AI/leworldmodel.md) 等を読む座標系 (Fei-Fei Li, 2026)
- [SHLPT: Similarity Heuristic Lifelong Prompt Tuning](../wiki/papers/Post_Training/shlpt-lifelong-prompt-tuning.md) を追加 — Wu, Jiang, Lian、**ACL 2024 Findings**。**lifelong prompt tuning（PEFT × 継続学習）**の **negative transfer** を緩和。学習可能な類似度メトリックでタスクを類似/非類似に分割し双方から有益な転移を引き出す＋parameter pool で catastrophic forgetting に対処、lifelong ベンチで SOTA 超。[Survey on Negative Transfer](../wiki/papers/Surveys_Overview/survey-on-negative-transfer.md) の具体実装、[DMT](../wiki/papers/Post_Training/sft-data-composition.md) へのパラメータ側からの対 (Wu, Jiang, Lian, 2024)

## 2026-06-03

- [When Scaling Meets LLM Finetuning](../wiki/papers/Post_Training/scaling-llm-finetuning.md) を追加 — Zhang, Liu, Cherry, Firat（**Google DeepMind**）、arXiv 2402.17193、**ICLR 2024**。ファインチューニング性能を **LLMサイズ・事前学習データ・finetuneパラメータ数・finetuneデータ** の4因子で分析し **乗法的結合スケーリング則**を発見。**(a) LLMサイズのスケールが事前学習データより効く、(b) PET（LoRA等）のパラメータscalingは効きにくい、(c) 最適手法はタスク・データ量依存**。[DMT](../wiki/papers/Post_Training/sft-data-composition.md) の定量スケーリング版。機械翻訳・要約・16Bまでに限定 (Zhang et al., 2024)
- [BERT Rediscovers the Classical NLP Pipeline](../wiki/papers/Pretraining/bert-rediscovers-nlp-pipeline.md) を追加 — Tenney, Das, Pavlick（**Google × Brown**）、arXiv 1905.05950、**ACL 2019**。**edge probing** で BERT 各層を解析し、古典 NLP パイプライン（POS→構文→NER→意味役割→照応）が期待順に層に局在＝**下位層に統語・上位層に意味**を実証。[言語構造の獲得理論](../wiki/papers/Pretraining/language-structure-acquisition.md) の経験的対応物。BERT（encoder）対象で decoder-only への一般化は別途検証要 (Tenney, Das, Pavlick, 2019)
- [Does BERT Rediscover a Classical NLP Pipeline?](../wiki/papers/Pretraining/does-bert-rediscover-nlp-pipeline.md) を追加 — Niu, Lu, Penn（**Toronto大**）、**COLING 2022**。上記 Tenney et al. の層分離説を**批判的に再検証**し、**決定的な経験的支持は乏しく probe の方法論・指標に敏感**と結論。新プローブ **GridLoc** で層深さに頼らない規則性を検出。「BERT の言語構造は実在するが層深さは最良の説明軸でない」。原説と「主張↔再検証」のペア (Niu, Lu, Penn, 2022)
- [Random Hierarchy Model (RHM)](../wiki/papers/Pretraining/random-hierarchy-model.md) を追加 — Petrini, Cagnetta ほか（**EPFL**）、arXiv 2307.02129、**Physical Review X 2024**。「なぜ深層ネットは高次元データを少数例で学べるか」を合成 PCFG タスク **RHM** で解析。深い CNN のサンプル複雑度は **P\*=n_c·m^L** で入力次元に対し多項式＝次元の呪いを回避（浅いネットは指数的＝深さが本質）。本リポジトリの RHM 系（[latent-sample-complexity](../wiki/papers/Pretraining/latent-sample-complexity.md) / [言語構造の獲得理論](../wiki/papers/Pretraining/language-structure-acquisition.md)）の起点。実データ転移は定性的 (Petrini et al., 2023)
- [言語構造の獲得理論](../wiki/papers/Pretraining/language-structure-acquisition.md) を追加 — Cagnetta & Wyart（**EPFL**）、arXiv 2406.00048、**NeurIPS 2024**。[RHM](../wiki/papers/Pretraining/random-hierarchy-model.md) を LM に展開。PCFG 上で token-token 相関を解析的に導出し、**データを増やすほど LM は文法構造のより深い表現を構築**することを示す。テスト損失のスケーリング則が文脈窓長に依存することを予測し Shakespeare/Wikipedia で検証。経験的スケーリング則に機序的説明を与える。PCFG 理想化・小規模検証の留保あり (Cagnetta & Wyart, 2024)
- [Curriculum Instruction Tuning](../wiki/topics/Post_Training/curriculum-instruction-tuning.md)（トピック）を追加 — EmergentMind のトピック概観（~11論文の二次ソース）。**SFTデータを難易度（易→難）で順序づけ・適応スケジュールする手法群**を整理（CAMPUS/TAPIR/Data-CUBE/D-MoLE/CITING 等）。収束加速・一般化強化が一貫報告される一方、静的カリキュラムの硬直性・難易度の主観性・負の転移が共通の弱点。[DMT](../wiki/papers/Post_Training/sft-data-composition.md) の動的・多段一般化 (EmergentMind, 2026)
- [data2vec](../wiki/papers/Pretraining/data2vec.md) を追加 — Baevski ほか（**Meta AI / FAIR**）、arXiv 2202.03555、**ICML 2022 Oral**。音声・画像・言語に**同一の自己教師ありレシピ**を適用する統一フレームワーク。離散トークンでなく **EMA teacher が出す文脈化潜在表現（上位K層平均）をマスク入力から回帰予測**。3モダリティで competitive〜SOTA。「token を捨てて自己の latent を予測する」JEPA 系設計の起点で、[V-JEPA 2](../wiki/papers/Physical_AI/v-jepa-2.md) / [LeWM](../wiki/papers/Physical_AI/leworldmodel.md) と同系譜 (Baevski et al., 2022)
- [Learn from your own latents（サンプル複雑度理論）](../wiki/papers/Pretraining/latent-sample-complexity.md) を追加 — Korchinski, Favero, Wyart、arXiv 2605.27734、preprint。**なぜ latent 予測 SSL が token 予測よりデータ効率が良いか**を理論証明。PCFG 上で **token/教師あり学習は隠れ木復元に L について指数的サンプル**を要するが **latent 予測は定数（対数因子まで）**。[data2vec](../wiki/papers/Pretraining/data2vec.md) の初サンプル複雑度解析を与え「暗黙的に階層的 latent 予測を行う」と示し、H-JEPA の明示的階層は冗長と示唆。実データ転移は未検証 (Korchinski, Favero, Wyart, 2026)

- **査読ステータス一斉再検証**（全60件の preprint/under-review/accepted/workshop を OpenReview・arXiv Comments・学会採択リストで再確認）— **ステータス変更8件**:
  - **昇格（→ accepted）**: [Reasoning with Sampling](../wiki/papers/Inference_Decoding/reasoning-with-sampling.md) **ICLR 2026 Oral**、[RS-GRPO](../wiki/papers/RL/rs-grpo.md) **ICLR 2026 Poster**、[Neural Thickets](../wiki/papers/Post_Training/neural-thickets.md) **ICML 2026 Spotlight**
  - **venue 訂正**: [GVE-Leiden](../wiki/papers/Graph_Network/gve-leiden.md) は「ICPP 2024 Workshops」ではなく **ICPP 2024 本会議**（workshop→accepted）
  - **降格（reject/withdraw 判明）**: [RLVR Capability Boundary Debate](../wiki/papers/RL/rlvr-capability-boundary-debate.md)・[Continuous Autoregressive LM (CALM)](../wiki/papers/Architecture/continuous-autoregressive-lm.md) は **ICLR 2026 Rejected**（under-review→preprint）、[Attention to Mamba](../wiki/papers/Architecture/attention-to-mamba-distillation.md) も ICLR 2026 Rejected（preprint のまま注記追加）
  - **⚠️ 偽陽性の修正**: [Scaling Behaviors of LLM RL Post-Training](../wiki/papers/RL/rl-scaling-math-qwen25.md) は **「ACL 2026 Main 採択」が誤り**で、実態は ICLR 2026 取り下げ（Withdrawn）→ preprint に訂正 —— **【2026-06-11 追記・再訂正】** その後 arXiv v4 (2026-04-17) の Comments で **ACL 2026 Main 採択が確認**された（ICLR 取り下げ後に改訂・再投稿して採択）。本「偽陽性の修正」自体が誤りで、accepted (ACL 2026 Main) に再訂正済み
  - 件数: accepted 29→32、workshop 3→2、under-review 5→1、preprint 23→25。track 精緻化（FineWeb=Spotlight, DeepCrossAttention/ProRL/Rewriting/ATLAS=Poster, LLM Reasoning Failures=Survey Certification）も反映

- [How Abilities in LLMs are Affected by SFT Data Composition (DMT)](../wiki/papers/Post_Training/sft-data-composition.md) を追加 — Dong ほか（**Alibaba / Qwen team**）、arXiv 2310.05492、**ACL 2024 Main**。SFT 時に数学・コード・一般能力がデータ量・混合比・モデルサイズにどう影響されるかを体系調査。**math/code はデータ量で単調向上・一般能力は約1,000サンプルで頭打ち**、混合は低リソースで各能力を底上げ・高リソースで能力 conflict、逐次学習は catastrophic forgetting。提案手法 **DMT**（Stage1 で専門データ→Stage2 で一般データに専門を比率 k で少量混合）で conflict と forgetting を両立緩和。[willccbb OPD メタ分析](../wiki/papers/RL/willccbb-sft-rl-opd.md) の compounding argument の SFT 内版 (Dong, Yuan, Lu et al., 2023)

## 2026-05-29

- [Transformers are Inherently Succinct](../wiki/papers/Architecture/transformers-are-inherently-succinct.md) を追加 — Bergsträßer, Cotterell, Lin（**RPTU × ETH Zürich**）、arXiv 2510.19315、**ICLR 2026 Oral (Outstanding Paper)**。Transformer の表現力を **succinctness（簡潔性）** で測り、固定精度 UHAT が同じ形式言語を **LTL より指数・有限オートマトンより二重指数・固定精度 RNN より指数**に簡潔に表現できる階層を構成的に証明。さらに非空性・等価性判定は **EXPSPACE-complete** で形式的検証は本質的に困難。並列 attention が簡潔性優位の源泉で、[Linear Transformers](../wiki/papers/Architecture/linear-transformers.md)（Transformer⇄RNN 等価）と対をなす。前提は unique hard-attention・固定精度 (Bergsträßer, Cotterell, Lin, 2025)

- [RAGとAgentic Searchの戦争を終わらせに来た!!!](../wiki/papers/Agent_ToolUse/rag-vs-agentic-search.md) を追加 — Hirosato Gamo（**Microsoft**）の Zenn 記事（2026-04）。「RAG は終わった」言説を、各手法の評価前提の省略に起因する疑似論争として整理。RAG は「外部データ参照で生成を強化」へ広義化し、**Agentic Search の本質は手段でなく「推論で複数回検索を反復する戦略」**。ベクトル検索 RAG は死んでおらず、CAG / ファイルシステム探索 / LLM Wiki を含め「対象データの性質・規模・タスクで使い分ける」が結論。[Vector DBを外したら](../wiki/papers/Agent_ToolUse/vector-db-to-agent-runtime.md) と同一論点クラスタ。査読対象外オピニオン (Hirosato Gamo, 2026 / Microsoft・Zenn)

## 2026-05-28

- [BlueprintSymVL](../wiki/papers/Evaluation/blueprintsymvl.md) を追加 — Shteriyanov ほか（**McDermott × Eindhoven ほか**）、**Results in Engineering 2025**。エンジニアリング図面（P&ID）の **VLM シンボル認識**を評価する初のドメイン特化ベンチマーク。red-circle ハイライト付き one-shot visual in-context querying で、シンボル数＋text label 両方を要求。**Gemini 2.5 Pro 50.5% 〜 InternVL 4.5%** と discriminative で、Dense/Similar で性能崩壊・全モデル Recall≫Precision。結論: 現状 VLM は autonomous deployment に不適。[SECURE](../wiki/papers/Evaluation/secure-cybersecurity-benchmark.md) と並ぶ domain-specialized reliability benchmark (Shteriyanov et al., 2025)

## 2026-05-27

- [Vector DBを外したら、RAGではなくAgent Runtimeが残った](../wiki/papers/Agent_ToolUse/vector-db-to-agent-runtime.md) を追加 — mofuteq の Zenn 記事（2026-05-21）。RAG から Vector DB を外したら残ったのは「検索+生成」でなく Agent Runtime だった、という経験報告を **RAR (Retrieval Augmented Reasoning)** として整理。**推論構造を runtime に外出し**し、LLM を「自律的推論者」から「スキーマを埋める変換コンポーネント」へ再配置（Typed Artifacts、canonical/emerging query の分離）。実装は LangGraph + SQLite 状態機械。[LLM-as-a-Verifier](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md) と同じ「能力をモデル内でなく外部構造に分配する」哲学。特定ドメイン検証のみ (mofuteq, 2026 / Zenn)

## 2026-05-19

- [Learning, Fast and Slow: Towards LLMs That Adapt Continually](../wiki/papers/RL/learning-fast-and-slow.md) を追加 — Tiwari ほか（**UC Berkeley × Mila × UT Austin**）、preprint。**Fast-Slow Training (FST)**: パラメータ θ を slow weights（GRPO+CISPO）、prompt Φ を fast weights（GEPA）として interleave 最適化。**RL 単独比 最大3倍のサンプル効率**＋asymptote も上回り、KL drift を最大70%削減して catastrophic forgetting を回避、継続学習で RL が stall する設定でも near-peak を維持。[On SFT, RL, and OPD](../wiki/papers/RL/willccbb-sft-rl-opd.md) が予告した「学習可能 hint writer」系の具体実装 (Tiwari et al., 2026)
- [SFT Memorizes, RL Generalizes](../wiki/papers/RL/sft-memorizes-rl-generalizes.md) を追加 — Chu, Zhai, Yang ほか（**UC Berkeley × HKU × Google DeepMind × UA**）、**ICML 2025**。SFT vs RL を **memorization vs generalization** 軸で実証対比。GeneralPoints / V-IRL の rule・visual OOD で **RL は汎化・SFT は ID 過適合**（Visual OOD で RL +33.8pt SOTA、Rule OOD で SFT −79.5pt の極端な暗記）。ただし指示追従できない backbone への直接 RL は失敗し、フォーマット安定化に **SFT 前段が必要**。[willccbb compounding argument](../wiki/papers/RL/willccbb-sft-rl-opd.md) の経験的先行事例、[Does RLVR Unlock New Reasoning?](../wiki/papers/RL/rlvr-does-not-teach-new-reasoning.md) の filtering 主張と論争中 (Chu et al., 2025)
- [Your Evals Will Break and You Won't See It Coming](../wiki/papers/Evaluation/your-evals-will-break.md) を追加 — Lun Wang（**Google DeepMind → NVIDIA**）のポジションエッセイ（2026-05-17）。既存 LLM 評価インフラは「次世代モデル＝現行の強化版」を暗黙前提に置くため、能力レジーム遷移（emergence/grokking）で**予測不可能に破綻**すると警鐘。提案2点: 物理の **秩序パラメータ**で能力遷移を捉える／メタシグナルを継続監視する **自己進化型評価**。accuracy ベンチでは原理的に検出できない能力クラス（戦略的情報隠匿）を例示。[LiveBench](../wiki/papers/Evaluation/livebench.md) / [GSM-Symbolic](../wiki/papers/Reasoning/gsm-symbolic.md)（accuracy ベンチの脆弱性）の上位レイヤ（観測装置の構造的不在）(Wang, 2026 / DeepMind → NVIDIA)

## 2026-05-11

- [Gated Delta Networks: Improving Mamba2 with Delta Rule](../wiki/papers/Architecture/gated-deltanet.md) を追加 — Yang（MIT CSAIL）× Kautz / Hatamizadeh（NVIDIA）、**ICLR 2025**。linear Transformer の retrieval/long-context 不足を、**Mamba2 の gating（適応的メモリ消去 α_t）と DeltaNet の delta rule（key 方向の精密更新 β_t）を統合した gated delta rule** で解消、chunkwise parallel で hardware-efficient に訓練。1.3B/100B tokens で Mamba2・DeltaNet を一貫上回り、hybrid 版は Transformer++ も上回り。efficient attention 系譜（[Linear Transformers](../wiki/papers/Architecture/linear-transformers.md)→DeltaNet/Mamba2→本論文）の設計空間統合 (Yang et al., 2025 / MIT CSAIL × NVIDIA)
- [Qwen3 Technical Report](../wiki/papers/Technical_Report/qwen3.md) を追加 — Alibaba Qwen Team（arXiv 2505.09388, Apache 2.0）。**dense 6 + MoE 2 の8モデル（0.6B〜235B-A22B）**をフルレンジ公開、context 128K。pre-training 36T tokens / 119 言語、QK-Norm 導入・MoE は shared expert 廃止。post-training は **thinking/non-thinking を chat template で統合**（thinking budget は自然発現）し、軽量モデルは distillation で GPU 時間 1/10。フラッグシップは DeepSeek-R1 を 23 ベンチ中 17 で上回り（AIME'24 85.7 等）。[willccbb OPD メタ分析](../wiki/papers/RL/willccbb-sft-rl-opd.md) の主要参照点で、[DeepSeek-V4](../wiki/papers/Technical_Report/deepseek-v4.md) より早い OPD 大規模採用例 (Qwen Team, 2025 / Alibaba)
- [DeepSeek-V4](../wiki/papers/Technical_Report/deepseek-v4.md) を追加 — DeepSeek-AI（HF preview, MIT）。**Pro（1.6T/49B active）と Flash（284B/13B）** の MoE、ネイティブ 1M context。3革新: **Hybrid Attention（CSA + HCA を interleave）**・**mHC を 1.6T-scale で初の production 実装**・**Muon optimizer**。1M context で V3.2 比 FLOPs 27%/10%・KV cache 10%/7%、post-training は Specialist Training → **On-Policy Distillation で統合**。Pro-Max は Codeforces 3206 / SWE Verified 80.6% で open SOTA も reasoning は GPT-5.4/Gemini-3.1-Pro に 3-6ヶ月遅れと自認。[mHC](../wiki/papers/Architecture/manifold-constrained-hyper-connections.md) の大規模実装事例 (DeepSeek-AI, 2026)

## 2026-05-07

- [On SFT, RL, and on-policy distillation](../wiki/papers/RL/willccbb-sft-rl-opd.md) を追加 — Will Brown × Claude Opus 4.7 の post-training メタ分析エッセイ（X 投稿, 2026-04-30）。SFT/RL/OPD/SDFT/OPSD を **単一の token-level policy gradient**（α: on-policy 度 / λ: teacher KL vs reward / π_T: teacher の3ダイアル）で統一表現。核心は **compounding argument**——SFT は分布固定で天井≈teacher、RL はロールアウトで compounding し天井=verifier 能力——で SFT-then-RL 順序を説明し、各手法を Pareto curve 上に配置。GRPO variants / RLVR 能力境界 / off-policy RL クラスタのメタ整理。AI 共著形式自体も注目例 (Will Brown & Claude Opus 4.7, 2026)

## 2026-05-01

- [Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths](../wiki/papers/Architecture/lightning-attention-2.md) を追加 — causal linear attention の **cumsum ボトルネック**を **block tiling**（intra-block は並列、inter-block は recurrent 累積）で解消、Triton I/O-aware 実装で **1K→128K でも throughput が flat**（FlashAttention-2 は急減・OOM）、性能劣化なし。[Linear Transformers](../wiki/papers/Architecture/linear-transformers.md) の理論 O(N) を LLM 規模 GPU で初めて実速度化し、[MiniMax-M1](../wiki/papers/Technical_Report/minimax-m1.md) の lightning attention の直接の元論文。arXiv Comments が Technical Report 自称のため peer_review n/a で保守的に扱う (Qin et al., 2024 / OpenNLPLab × Shanghai AI Lab)
- [Linear Transformers: Transformers are RNNs](../wiki/papers/Architecture/linear-transformers.md) を追加 — softmax(QKᵀ) を **kernel feature map 内積**で置換し計算量を **O(N²d)→O(Nd²)** に削減。重要洞察: **causal 自己回帰生成は隠れ状態を持つ RNN として等価表現**でき、推論を **softmax 比 ~4000×高速化**——「Transformer は softmax がなければ RNN」。Performer/RWKV/RetNet/Mamba/Lightning Attention など現代 efficient attention 系全般の数学的祖 (Katharopoulos, Vyas, Pappas, Fleuret, 2020 / Idiap × EPFL × UW, ICML 2020)

## 2026-04-30

- [FROMAGe: Grounding Language Models to Images for Multimodal Inputs and Outputs](../wiki/papers/Multimodal/fromage.md) を追加 — **凍結 OPT-6.7B + 凍結 CLIP** を線形射影層と `[RET]` token のみ（trainable 0.1%未満）で結合、CC3M のみで訓練して interleaved image-text 入出力を実現。VIST 文脈付き retrieval **R@1 20.8 vs CLIP 5.9**、文脈が長いほど差が拡大。「凍結バックボーン + 軽量 projection」設計の祖型で、後の LLaVA / BLIP-2 / Idefics3 の参照点 (Koh, Salakhutdinov, Fried, 2023 / CMU, ICML 2023)
- [CLIP: Learning Transferable Visual Models From Natural Language Supervision](../wiki/papers/Multimodal/clip.md) を追加 — 4億 (image, text) ペアの contrastive 事前学習で **zero-shot ImageNet 76.2%**（fully supervised ResNet-50 同等）、30+ タスクへ転移・distribution shift に頑健。contrastive (InfoNCE) は captioning 目的より zero-shot 効率4倍。DALL-E 2 / Stable Diffusion / LLaVA / Flamingo の標準 vision tower の源流 (Radford et al., 2021 / OpenAI, ICML 2021)
- **SCHEMA更新**: 図表挿入の運用規約を追加
  - `figures/{Category}/{slug}/` ディレクトリ構造を導入（sources/evidence/wiki/papers と同じカテゴリ分割）
  - ファイル命名規則に図表ファイル（`fig-1.png` 等、論文の Figure 番号と対応推奨）を追加
  - Wikiページ粒度ガイドラインに「`wiki/papers/` には可能であれば主要な図表を **1-3点** 挿入する」を追加
  - Wikiページ形式テンプレートに「主要な図表」セクションを追加
  - リンク規約に図表参照パス例を追加
  - 取り込み手順（Ingest）に図表保存ステップを step 3 として挿入

## 2026-04-27

- [Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md) を追加 — Sahu（**IIIT Hyderabad**）、preprint。共有メモリ並列の Louvain / Leiden / LPA で支配的な **per-thread hashtable**（100M頂点×64スレッドで **51.2-102.4 GB**）を **weighted Misra-Gries sketch**（~0.5KB/sketch、グラフサイズ非依存）で置換。modularity 劣化は Louvain ≤1% / Leiden 0.8% / LPA ほぼゼロ、ランタイムは 1.48–3.15×（最大3.8Bエッジで検証）。[GVE-Leiden](../wiki/papers/Graph_Network/gve-leiden.md) と同著者で、速度SOTA に対しメモリ側SOTAとして相補 (Sahu, 2024 / IIIT Hyderabad)

## 2026-04-23

- [Dr. GRPO: Understanding R1-Zero-Like Training](../wiki/papers/RL/dr-grpo.md) を追加 — DeepSeek-R1-Zeroの「pure RLで推論創発」を base model / RL に分解して批判的検証。DeepSeek-V3-Base は RL 前から "Aha moment" を示し、Qwen2.5 base もテンプレなしで強い推論能力を示す → **事前学習バイアス説**。さらに **GRPO には不正解出力の応答長を人為的に増やす最適化バイアス** があることを同定し、**Dr. GRPO**（unbiased GRPO）を提案。minimalist R1-Zero recipeで 7B base × **AIME 2024 43.3%**（当時SOTA）。RLVR 能力境界論争に「事前学習バイアス」という第三の軸を追加、各種 GRPO 改良（RS-GRPO, MRPO）の理論的基盤を補強 (Liu et al., 2025 / Sea AI Lab × NUS, COLM 2025)
- [Qwen3.5-Omni Technical Report](../wiki/papers/Technical_Report/qwen35-omni.md) を追加 — 数百億パラメータ Hybrid Attention MoE omni-modal モデル、256k context、1億時間超の audio-visual 学習。Thinker / Talker 双方に hybrid attention MoE、10時間 audio / 400秒 720P動画（1 FPS）、**215 audio/audio-visual benchmark で SOTA**、主要 audio タスクで **Gemini-3.1 Pro を上回り** audio-visual総合で同等。**ARIA**（text-speech tokenizer 符号化ミスマッチを動的整列）で安定ストリーミングTTS、10言語感情表現音声、script-level 構造化キャプション。**Audio-Visual Vibe Coding**（音声・映像指示→直接コード生成）の創発能力を観測 (Qwen Team, 2026 / Alibaba)
- [MiniMax-M1: Scaling Test-Time Compute with Lightning Attention](../wiki/papers/Technical_Report/minimax-m1.md) を追加 — 世界初のオープンウェイト大規模ハイブリッドアテンション推論モデル。456B total / 45.9B active MoE + lightning attention、ネイティブ1M context（DeepSeek R1の8倍）、新規RLアルゴリズム **CISPO**（token updatesではなくimportance sampling weightsをクリップ）、hybrid attention + CISPO で 512 H800 × 3週間 / $534,700 のフルRL訓練を実現。thinking budget 40K/80K を2モデル公開、DeepSeek-R1/Qwen3-235Bに匹敵し特に complex SWE・tool use・long context で強み。CISPO は Flash-RL/TIS と同系統の IS-weight クリッピング系 (MiniMax Team, 2025)
- [GVE-Leiden: Fast Leiden in Shared Memory](../wiki/papers/Graph_Network/gve-leiden.md) を追加 — ライデン法の共有メモリ並列実装SOTA、dual 16-core Xeon（32コア）で オリジナル比436× / igraph 104× / NetworKit 8.2× / **cuGraph (A100 GPU) 3.0×** の高速化を達成、3.8Bエッジで403M edges/s、スレッド倍化ごと1.6×スケール。CPU実装が最新GPU実装を上回る稀な事例 (Sahu, Kothapalli, Banerjee, 2024 / IIIT Hyderabad, ICPP 2024 Workshops)
- [LeWorldModel (LeWM): Stable End-to-End JEPA from Pixels](../wiki/papers/Physical_AI/leworldmodel.md) を追加 — raw pixelsからend-to-end安定学習する最初のJEPA、next-embedding prediction + Gaussian正則化の2損失項・1ハイパラ（既存end-to-end代替の6→1）、~15Mパラメータ・単GPU・数時間で学習、foundation-model-based world model比 最大48倍高速な計画を2D/3D制御で実現、潜在空間に物理量がprobingで保持・surprise評価で物理的非現実事象を検出。JEPA系world modelの普及閾値を大きく下げた (Maes, Le Lidec, Scieur, LeCun, Balestriero, 2026 / Meta FAIR)

## 2026-04-22

- [Scaling Behaviors of LLM RL Post-Training](../wiki/papers/RL/rl-scaling-math-qwen25.md) を追加 — Qwen2.5 dense全系列（0.5B–72B）で数学推論RL（GRPO）のスケーリング則を体系化、log L(N,X)=−k(N)·log X+E(N) のpower-lawと学習効率飽和 k(N)=K_max/(1+N_0/N) を定式化、データ制約下では「最適化ステップ総数」が「ユニークサンプル数」より支配的。ScaleRL の sigmoid フィットと相補的に、効率側の天井と高品質データ再利用の有効性を追加 (Tan, Geng, Yu et al., 2025 / Shanghai AI Lab × Oxford, ACL 2026 Main)

## 2026-04-21

- [LLM-as-a-Verifier: A General-Purpose Verification Framework](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md) を追加 — scoring granularity / repeated verification / criteria decomposition の3軸でLLM検証をスケール、agent trajectoryの軌跡reward modelとしてtest-time scalingし Terminal-Bench 2 で86.4% (SOTA)・SWE-Bench Verified 77.8%、Claude Opus 4.6 / GPT 5.4 / Geminiを上回る。小型verifier (Gemini 2.5 Flash) で大型generator出力プールを再ランキング (Kwok, Li, Atreya et al., 2026 / Stanford × UC Berkeley × NVIDIA)
- [Attention to Mamba: A Recipe for Cross-Architecture Distillation](../wiki/papers/Architecture/attention-to-mamba-distillation.md) を追加 — Transformer→Mambaクロスアーキ蒸留の二段階レシピ（kernel trick適用linearized Attention経由で純Mambaへ、hybrid不要）、Pythia-1B teacher perplexity 13.86 → 蒸留後Mamba 14.11 (Moudgil, Huang, Dhekane et al., 2026 / Apple推定)
- [Video models are zero-shot learners and reasoners](../wiki/papers/Multimodal/video-models-zero-shot-learners.md) を追加 — Veo 3が明示訓練外のタスク（segmentation / edge detection / editing / 物理理解 / affordance / 道具使用）をゼロショットで解ける現象を体系実証、迷路・対称性など初期visual reasoning発現、video modelが汎用視覚基盤モデルへ向かう軌道を主張（Multimodalカテゴリ初エントリ, ICLR 2026投稿 → Rejected）(Wiedemer, Li, Vicol et al., 2025 / Google DeepMind)
- [ScaleRL: The Art of Scaling Reinforcement Learning Compute for LLMs](../wiki/papers/RL/scale-rl.md) を追加 — 40万GPU時間超の体系実験でLLM向けRLのsigmoid計算-性能曲線を定式化、「漸近性能を動かす設計選択」と「計算効率のみを動かす設計選択（loss aggregation / 正則化 / curriculum / off-policy等）」を切り分け。安定レシピは予測可能scalingを示し、10万GPU時間規模の単一ランで検証損失を事前予測。ベストプラクティス ScaleRL を提案。RLVR能力境界論争を「asymptote vs efficiency」の軸で再定式化する道具立てとして、topics/RL/rlvr-capability-boundary を更新 (Khatri, Madaan, Tiwari et al., 2025 / Meta × UT Austin, ICLR 2026 Oral)
- [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](../wiki/papers/Evaluation/livebench.md) を追加 — 汚染耐性 + 客観自動採点 + 広範タスク（math/coding/reasoning/language/instruction-following/data analysis）+ 月次更新を同時達成した初のベンチマーク、arXiv・math competitions・news・datasetsから問題構築、Big-Bench Hard / AMPS / IFEval 困難化版を含み、0.5B-405Bのモデル評価でトップでも70%未満。全問題・コード・回答公開 (White, Dooley, Roberts et al., 2024 / Abacus.AI × Meta × NYU × UMD × USC, ICLR 2025 Spotlight)

## 2026-04-20

- [ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining](../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md) を追加 — 過去最大規模の多言語スケーリング則研究（774実験 / 10M-8B / 400+学習言語 / 48評価言語）、ATLASが既存スケーリング則を out-of-sample で +0.3 R² 以上上回る、1444言語ペアの転移行列、scratch学習 vs 多言語checkpointからのfinetuneの計算クロスオーバー点を同定 (Longpre, Kudugunta, Muennighoff et al., 2025 / MIT × Google × Stanford, ICLR 2026)

## 2026-04-17

- [Flash-RL / TIS: Your Efficient RL Framework Secretly Brings You Off-Policy RL Training](../wiki/papers/RL/flash-rl-tis.md) を追加 — vLLM/SGLangなrolloutとFSDP/Megatronな学習の実装差分が、同一θでもトークン確率を大きくずらし on-policy RL を暗黙に off-policy 化。Truncated Importance Sampling（`min(π_learner/π_sampler, C)`）による数行の勾配修正で、Qwen2.5-32B+DAPO・INT8 rolloutでも性能回復、entropy collapse／応答長暴走／負のKL推定を解消。VeRL・slime・OAT・SkyRL・OpenRLHF・REINFORCE++ に統合済み (Yao, Liu et al., 2025 / UCSD × MSR)
- [RS-GRPO: Risk-Sensitive RL for Alleviating Exploration Dilemmas](../wiki/papers/RL/rs-grpo.md) を追加 — sharpened prior × 標準RL目的関数がpass@k低下を招く「exploration dilemma」を定式化、CVaRベースのリスク感応的目的関数でGRPO数行修正、6数学ベンチ×5LLMでpass@1維持+pass@k向上 (Jiang et al., 2025 / 清華大 × ByteDance Seed)

## 2026-04-15

- [SECURE: Benchmarking LLMs for Cybersecurity](../wiki/papers/Evaluation/secure-cybersecurity-benchmark.md) を追加 — ICS特化6データセット（MAET, CWET, KCV, VOOD, RERT, CPST）で7モデルを評価、ChatGPT-4が4/6タスクで最高、OOD検出（VOOD）でChatGPT-3.5が8.4%に壊滅的劣化 (Bhusal et al., 2024)
- [Scalable Extraction of Training Data from LMs](../wiki/papers/Safety_Alignment/scalable-training-data-extraction.md) を追加 — 単一トークン反復のdivergence attackでChatGPTの学習データを150倍速で抽出、約$200で10,000+系列、アラインメントはメモリゼーションを隠蔽するだけで除去しない (Nasr, Carlini et al., 2023)

## 2026-04-14

- **エンジニアリングノート新設**: [AWS上でGPU分散学習・ML開発をする自分向け注意事項まとめ](../wiki/engineering/aws-gpu-ml-security-practices.md) を追加 — IAM/S3/SSH/Secrets/ログ/学習データ/チーム運用/監査/コスト/法務の15章構成の実践ルール集（engineering初エントリ）
- [All elementary functions from a single binary operator](../wiki/papers/Symbolic_Computation/eml-single-operator.md) を追加 — eml(x,y)=exp(x)−ln(y)と定数1で全初等関数を生成する連続版NANDゲートの発見、EMLツリーによる勾配ベース記号回帰を実証 (Odrzywołek, 2026)
- [The Geometry of Forgetting](../wiki/papers/Reasoning/geometry-of-forgetting.md) を追加 — 高次元埋め込み空間の幾何学から忘却・偽記憶が必然的に発生、干渉がべき乗則忘却の支配的ドライバー（b=0.460 vs 人間b≈0.5）、本番モデルの有効次元~16（dimensionality illusion）、DRM偽記憶のパラメータフリー再現 (Barman et al., 2026)
- [The AI Layoff Trap](../wiki/papers/Social_Science/ai-layoff-trap.md) を追加 — 需要外部性が合理的企業を自動化軍拡競争に閉じ込め、7つの主要政策を棄却しピグー税のみが有効と理論的に導出 (Hemenway Falk & Tsoukalas, 2026)

## 2026-04-13

- [P-hacking with one prompt](../wiki/papers/Evaluation/p-hacking-with-one-prompt.md) を追加 — LLMに「有意差を見つけて」と依頼するだけでp-hackingを実行、主要3システム全てで再現 (Kawahara, 2026)

## 2026-04-10

- [The Lottery Ticket Hypothesis](../wiki/papers/Efficiency_Optimization/lottery-ticket-hypothesis.md) を追加 — 密なネットワーク内にスクラッチから訓練可能なスパースサブネットワーク（winning tickets）が存在することを実証 (Frankle & Carbin, 2018)
- [From Louvain to Leiden](../wiki/papers/Graph_Network/louvain-to-leiden.md) を追加 — ライデン法の原論文、精製ステップとキュー管理による高速・高品質コミュニティ検出 (Traag et al., 2019)

## 2026-04-08

- [Claude Mythos Preview](../wiki/models/claude-mythos-preview.md) を追加 — Opus 4.6を大幅に上回るagentic coding/cyber性能、ベンチマーク評価条件の分析、性能改善仮説（Claude Code flywheel、実行環境つきRL等）、実行環境つきRLの解説を含む
- [Scaling Laws of Motion Forecasting and Planning](../wiki/papers/Physical_AI/scaling-laws-motion-forecasting-planning.md) を追加 — 50万時間走行データ・84モデルで自動運転のスケーリング則を実証、閉ループでも成立
- **トピック新設**: [RLVRの能力境界論争](../wiki/topics/RL/rlvr-capability-boundary.md) — filtering vs 真の能力獲得、界隈の中間的着地を整理（topics初エントリ）
- [The Debate on RLVR Reasoning Capability Boundary](../wiki/papers/RL/rlvr-capability-boundary-debate.md) を追加 — 二段階動態モデル（exploitation → exploration）でshrinkage/expansion論争を統合
- [Does RLVR Truly Unlock New Reasoning?](../wiki/papers/RL/rlvr-does-not-teach-new-reasoning.md) を追加 — Pass@k分析によるfiltering主張
- [DeepSeek-R1](../wiki/papers/RL/deepseek-r1.md) を追加 — Pure RLでのself-verification/reflection出現
- [MRPO](../wiki/papers/RL/mrpo.md) を追加 — SOE+effective rank正則化でbias manifoldを幾何学的に突破、4Bが32Bを上回る
- [CodeScout](../wiki/papers/RL/codescout.md) を追加 — Unix端末のみでRL訓練したコード検索エージェント、File F1 2.4%→55.46%（1.7B）、SWE-Bench評価

## 2026-04-07

- research-wiki 初期構築
- [Large Language Model Reasoning Failures](../wiki/papers/Surveys_Overview/llm-reasoning-failures.md) を追加 — source, evidence, wiki/papers
- [Conditional Memory via Scalable Lookup](../wiki/papers/Architecture/conditional-memory-scalable-lookup.md) を追加 — Engram: N-gramベースO(1)ルックアップによる新スパース性軸
- [DeepCrossAttention](../wiki/papers/Architecture/deep-cross-attention.md) を追加 — 入力依存重みで残差接続を動的結合、同品質を最大3倍高速に達成
- [Mixture-of-Depths Attention](../wiki/papers/Architecture/mixture-of-depths-attention.md) を追加 — 深度方向KVペアへのアテンションで信号劣化を解消、FLOPsオーバーヘッド3.7%
- [Attention Residuals](../wiki/papers/Architecture/attention-residuals.md) を追加 — softmaxベースの選択的残差集約、Kimi Linearに統合
- [Continuous Autoregressive LM](../wiki/papers/Architecture/continuous-autoregressive-lm.md) を追加 — next-vector predictionで生成ステップ1/K
- [MSA: Memory Sparse Attention](../wiki/papers/Architecture/memory-sparse-attention.md) を追加 — 100Mトークンまでスケーラブルなメモリモデル
- [mHC: Manifold-Constrained Hyper-Connections](../wiki/papers/Architecture/manifold-constrained-hyper-connections.md) を追加 — HCの恒等写像特性復元
- [Rewriting Pre-Training Data](../wiki/papers/Pretraining/rewriting-pretraining-data.md) を追加 — SwallowCode/MathでHumanEval +17.0
- [FineData (HuggingFaceFW)](../wiki/papers/Pretraining/huggingface-finedata.md) を追加 — 15T+トークンのオープン事前学習データセット群
- [Neural Thickets](../wiki/papers/Post_Training/neural-thickets.md) を追加 — ランダム摂動+アンサンブルでPPO/GRPO競争力
- [Simple Self-Distillation](../wiki/papers/Post_Training/simple-self-distillation-code.md) を追加 — 自身の出力のみでコード生成改善
- [Namazu Alpha](../wiki/papers/Post_Training/namazu-alpha.md) を追加 — Sakana AIの日本仕様適応事後学習
- [SWE-CI](../wiki/papers/Evaluation/swe-ci.md) を追加 — CI環境でのエージェント評価ベンチマーク
- [Kimi K2.5](../wiki/papers/Technical_Report/kimi-k25.md) を追加 — オープンソースマルチモーダルエージェントモデル
- [Mind the Gap](../wiki/papers/Reasoning/mind-the-gap-self-improvement.md) を追加 — 生成より検証が容易であることの実証
- [The Reversal Curse](../wiki/papers/Reasoning/reversal-curse.md) を追加 — 「AはB」→「BはA」に汎化しない根本的制約
- [Sycophantic Delusional Spiraling](../wiki/papers/Safety_Alignment/sycophantic-delusional-spiraling.md) を追加 — シカンシーによる妄想的スパイラルの理論的証明
- [OpenClaw-RL](../wiki/papers/RL/openclaw-rl.md) を追加 — next-state信号活用のエージェントRL
- [AutoHarness](../wiki/papers/Agent_ToolUse/autoharness.md) を追加 — 自動コードハーネス合成でエージェント改善
- [Self-Organizing LLM Agents](../wiki/papers/Agent_ToolUse/self-organizing-llm-agents.md) を追加 — 自己組織化が設計済み構造を上回る
- [Agentic RL Training](../wiki/papers/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md) を追加 — Kimi/Cursor/Chromaの訓練比較
- [Automated PLC Test Generation](../wiki/papers/Domain_Specific/automated-plc-test-generation.md) を追加 — LLMによるPLCテストケース自動生成
- [Sarashina-Embedding-v2](../wiki/papers/Domain_Specific/sarashina-embedding-v2.md) を追加 — 日本語特化埋め込みモデル（JMTEBトップティア）
- [DreamZero](../wiki/papers/Physical_AI/dreamzero-world-action-models.md) を追加 — ビデオ拡散ゼロショットロボットポリシー
- [V-JEPA 2](../wiki/papers/Physical_AI/v-jepa-2.md) を追加 — 自己教師あり動画モデル+ロボット展開
- [Flash-KMeans](../wiki/papers/Efficiency_Optimization/flash-kmeans.md) を追加 — GPU K-means最大17.9倍高速化
- [TurboQuant](../wiki/papers/Efficiency_Optimization/turboquant.md) を追加 — KVキャッシュ6倍圧縮
- [SSRN 6372438](../wiki/papers/Safety_Alignment/ssrn-6372438.md) を追加 — 未処理（後に AI Agent Traps として Safety_Alignment に移動）
- [Karpathy Tweet](../wiki/papers/Press_Releases/karpathy-tweet.md) を追加 — 未処理
- [NRI Report 59421](../wiki/papers/Press_Releases/nri-report-59421.md) を追加 — 未処理
- [GSM-Symbolic](../wiki/papers/Reasoning/gsm-symbolic.md) を追加 — 数値変更だけでLLM数学推論が大きくばらつく (Apple Research)
- NRIレポートを更新 — 「ITロードマップ2026年版 エージェント型AIと汎用人工知能」
- AI Agent Traps を Safety_Alignment に移動
- Karpathy Tweet を更新 — LLMナレッジベース構築ワークフロー
