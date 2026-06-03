# Wiki Index

wikiに含まれる全ページのカタログ。カテゴリごとに整理。

> 📊 [査読・採択状況一覧](../index/peer-review.md) — 全論文の査読ステータスを一覧で確認

## Topics
（トピック別ページ）

### RL
- [RLVRの能力境界論争](topics/RL/rlvr-capability-boundary.md) — filteringか真の能力獲得か、界隈の現在の着地点を整理

## Models
（モデル別ページ）

- [Claude Mythos Preview](models/claude-mythos-preview.md) — Opus 4.6を大幅に上回るagentic coding/cyber性能、防御用途限定 (Anthropic, 2026)

## Papers
（論文別ページ）

### Architecture
- [Linear Transformers: Transformers are RNNs](papers/Architecture/linear-transformers.md) — softmax(QKᵀ)を kernel feature map 内積で置換し計算量を O(N²d)→O(Nd²) に削減、causal 生成は **RNN として等価表現**でき推論を **~4000×高速化**。Performer/RWKV/RetNet/Mamba など現代 efficient attention の数学的祖 (Katharopoulos et al., 2020 / Idiap × EPFL × UW) `✅ ICML 2020`
- [Transformers are Inherently Succinct](papers/Architecture/transformers-are-inherently-succinct.md) — Transformer の表現力を **succinctness（簡潔性）** で測り、固定精度 UHAT が同じ形式言語を **LTL より指数・有限オートマトンより二重指数・固定精度 RNN より指数** 簡潔に表現できる階層を構成的に証明。さらに非空性・等価性判定は **EXPSPACE-complete**（検証は本質的に困難）。前提は unique hard-attention (Bergsträßer, Cotterell, Lin, 2025 / RPTU Kaiserslautern × ETH Zürich) `✅ ICLR 2026 (Oral, Outstanding Paper)`
- [Lightning Attention-2](papers/Architecture/lightning-attention-2.md) — causal linear attention の cumsum ボトルネックを **block tiling** で並列化、Triton I/O-aware 実装で **1K→128K でも throughput が flat**（FlashAttention-2 は急減）。Linear Transformers を LLM 規模 GPU 実装に落とし込んだ後継、MiniMax-M1 の元 (Qin et al., 2024 / OpenNLPLab × Shanghai AI Lab) `— tech report`
- [Gated DeltaNet: Improving Mamba2 with Delta Rule](papers/Architecture/gated-deltanet.md) — Mamba2 の gating（全体decay α）と DeltaNet の delta rule（key方向の targeted update β）を統合した **gated delta rule**、chunkwise parallel で hardware-efficient 訓練。1.3B/100B tokens で Mamba2/DeltaNet を一貫上回り、hybrid 版は Transformer++ も上回り (Yang, Kautz, Hatamizadeh, 2025 / MIT CSAIL × NVIDIA) `✅ ICLR 2025`
- [Attention to Mamba: Cross-Architecture Distillation](papers/Architecture/attention-to-mamba-distillation.md) — Transformer→Mambaクロスアーキ蒸留の二段階レシピ（kernel trick経由で純Mambaへ、hybrid不要）、Pythia-1Bで teacher perplexity 13.86 → 14.11 (Moudgil, Huang, Dhekane et al., 2026) `📝 preprint (ICLR 2026 Rejected)`
- [Mixture-of-Depths Attention](papers/Architecture/mixture-of-depths-attention.md) — 深度方向KVペアへのアテンションで信号劣化問題に対処 (Zhu et al., 2026) `📝 preprint`
- [Attention Residuals](papers/Architecture/attention-residuals.md) — softmaxアテンションで残差接続の選択的集約、Kimi Linearに統合 (Chen et al., 2026) `— tech report`
- [Continuous Autoregressive Language Models](papers/Architecture/continuous-autoregressive-lm.md) — next-vector predictionで生成ステップをK分の1に (Shao et al., 2025) `📝 preprint (ICLR 2026 Rejected)`
- [MSA: Memory Sparse Attention](papers/Architecture/memory-sparse-attention.md) — 100Mトークンまでスケーラブルなメモリモデル (Chen et al., 2026) `📝 preprint`
- [mHC: Manifold-Constrained Hyper-Connections](papers/Architecture/manifold-constrained-hyper-connections.md) — HCの恒等写像特性を復元しスケーラビリティ向上 (Xie et al., 2025) `📝 preprint`
- [Conditional Memory via Scalable Lookup](papers/Architecture/conditional-memory-scalable-lookup.md) — Engramモジュールによる条件付きメモリスパース性 (Cheng et al., 2026) `📝 preprint`
- [DeepCrossAttention](papers/Architecture/deep-cross-attention.md) — 入力依存の学習可能重みによる残差接続の改良 (Heddes et al., 2025) `✅ ICML 2025`

### Pretraining
- [Rewriting Pre-Training Data](papers/Pretraining/rewriting-pretraining-data.md) — SwallowCode/SwallowMathでデータリライティングにより性能向上 (Fujii et al., 2025) `✅ ICLR 2026`
- [FineData (HuggingFaceFW)](papers/Pretraining/huggingface-finedata.md) — 大規模オープン事前学習データセット群 (Hugging Face, 2025) `✅ NeurIPS 2024`
- [ATLAS: Multilingual Scaling Laws](papers/Pretraining/atlas-multilingual-scaling-laws.md) — 過去最大規模の多言語スケーリング則（774実験/400+言語）、ATLASが+0.3 R²で既存則を上回り、1444言語ペアの転移行列とscratch vs finetuneのクロスオーバー点を同定 (Longpre, Kudugunta, Muennighoff et al., 2025) `✅ ICLR 2026`

### Post_Training
- [How Abilities in LLMs are Affected by SFT Data Composition (DMT)](papers/Post_Training/sft-data-composition.md) — SFTで数学・コード・一般能力はスケーリング特性が異なる（math/codeは単調向上、一般は**~1000サンプルで頭打ち**）。逐次学習は **catastrophic forgetting**、同時学習は能力 conflict。**DMT**（専門データ→一般データに専門を比率kで少量混合する2段階）で両方を緩和 (Dong et al., 2023 / Alibaba・Qwen) `✅ ACL 2024 Main`
- [Neural Thickets](papers/Post_Training/neural-thickets.md) — 事前学習重み近傍の多様なエキスパートをランダム摂動で発見 (Gan & Isola, 2026 / MIT) `✅ ICML 2026 (Spotlight)`
- [Simple Self-Distillation](papers/Post_Training/simple-self-distillation-code.md) — 自身の出力のみでコード生成を改善するSSD (Zhang et al., 2026) `📝 preprint`
- [Namazu Alpha](papers/Post_Training/namazu-alpha.md) — オープン基盤モデルの日本仕様適応 (Sakana AI, 2026) `— blog`

### Evaluation
- [SWE-CI](papers/Evaluation/swe-ci.md) — CI環境でのコードベース保守能力評価ベンチマーク (Chen et al., 2026) `📝 preprint`
- [P-hacking with one prompt](papers/Evaluation/p-hacking-with-one-prompt.md) — たった一つのプロンプトでLLMがp-hackingに加担する危険性を実証 (Kawahara, 2026) `📝 preprint`
- [SECURE: Benchmarking LLMs for Cybersecurity](papers/Evaluation/secure-cybersecurity-benchmark.md) — ICS特化6データセットでLLMのサイバーセキュリティ能力を評価、OOD検出に大きな性能差 (Bhusal et al., 2024) `✅ ACSAC 2024`
- [LiveBench](papers/Evaluation/livebench.md) — 汚染耐性・客観採点・広範タスク・月次更新を同時達成した初のLLMベンチマーク、0.5B-405B評価でトップ<70% (White, Dooley, Roberts et al., 2024) `✅ ICLR 2025 Spotlight`
- [Your Evals Will Break and You Won't See It Coming](papers/Evaluation/your-evals-will-break.md) — 評価インフラは「次世代モデル=現行の強化版」を暗黙前提に置くため、創発・grokking 的な能力相転移で予測不能に破綻すると警鐘。物理の **秩序パラメータ**概念で能力遷移を捕捉する **自己進化型評価** を提唱、「評価は訓練目標の上流」と指摘 (Wang, 2026 / DeepMind → NVIDIA) `— blog`
- [BlueprintSymVL: A Discriminative Benchmark for VLM Symbol Recognition in Engineering Blueprints](papers/Evaluation/blueprintsymvl.md) — エンジニアリング図面（P&ID）の VLM シンボル認識を評価する**最初のドメイン特化ベンチマーク**。red-circle ハイライト付き **one-shot visual in-context querying**、count+label 両方を要求する strict criterion。**Gemini 2.5 Pro 50.5% > Qwen 40.5% > GPT-4o 30% > InternVL 4.5%** の discriminative power、Dense/Similar シナリオで性能崩壊・全モデル Recall≫Precision。結論: 現状 VLM は autonomous deployment に不適 (Shteriyanov et al., 2025 / McDermott ほか) `✅ Results in Engineering 2025`

### Technical_Report
- [Kimi K2.5](papers/Technical_Report/kimi-k25.md) — オープンソースマルチモーダルエージェントモデル (Kimi Team, 2026) `— tech report`
- [MiniMax-M1](papers/Technical_Report/minimax-m1.md) — 世界初のオープンウェイト大規模 hybrid attention 推論モデル、456B MoE / 45.9B active、ネイティブ1M context。新規RL **CISPO**（IS重みクリップ）で 512 H800 × 3週間 / $534,700 のフルRL訓練、DeepSeek-R1/Qwen3-235B に匹敵（特に SWE・tool use・long context）(MiniMax Team, 2025) `— tech report`
- [Qwen3.5-Omni](papers/Technical_Report/qwen35-omni.md) — 数百億パラメータの Hybrid Attention MoE omni-modal モデル、256k context、1億時間 audio-visual 学習。215 audio/audio-visual benchmark で SOTA・主要 audio で Gemini-3.1 Pro 超え、ARIA による安定ストリーミング TTS、Audio-Visual Vibe Coding 創発 (Qwen Team, 2026) `— tech report`
- [DeepSeek-V4](papers/Technical_Report/deepseek-v4.md) — 1.6T/49B active の Pro と 284B/13B の Flash、ネイティブ1M context の MoE。**CSA/HCA の hybrid attention**、mHC を1.6Tスケールで初実装、Muon optimizer。V3.2比 1M-context FLOPs 27%/10%・KV cache 10%/7% (DeepSeek-AI, 2026) `— tech report`
- [Qwen3](papers/Technical_Report/qwen3.md) — dense+MoE 計8モデル（0.6B-235B）を Apache 2.0 公開、flagship は 128 experts/8 active・128K context。Pre-training 36T tokens/119言語、Post-training は 4-stage で **thinking/non-thinking を統合**、軽量モデルは distillation で GPU 時間 1/10。DeepSeek-R1 を 23ベンチ中17で上回り (Qwen Team, 2025) `— tech report`

### Reasoning
- [Mind the Gap](papers/Reasoning/mind-the-gap-self-improvement.md) — 生成よりも検証の方が容易であることを示した自己改善研究 (Song et al., 2024) `✅ ICLR 2025`
- [The Reversal Curse](papers/Reasoning/reversal-curse.md) — 「AはB」で学習しても「BはA」に汎化しない (Berglund et al., 2023) `✅ ICLR 2024`
- [GSM-Symbolic](papers/Reasoning/gsm-symbolic.md) — 数値変更だけでLLM数学推論が大きくばらつく、パターンマッチングの限界 (Mirzadeh et al., 2024) `✅ ICLR 2025`
- [The Geometry of Forgetting](papers/Reasoning/geometry-of-forgetting.md) — 埋め込み空間の幾何学から忘却・偽記憶が必然的に発生、有効次元~16のdimensionality illusion (Barman et al., 2026) `📝 preprint`
- [Large Language Model Reasoning Failures](papers/Surveys_Overview/llm-reasoning-failures.md) — LLM推論失敗の包括的サーベイ (Song et al., 2026) `✅ TMLR 2026`

### Safety_Alignment
- [Sycophantic Delusional Spiraling](papers/Safety_Alignment/sycophantic-delusional-spiraling.md) — シカンシーが理想的ベイズ推論者にも妄想的スパイラルを引き起こす (Chandra et al., 2026) `📝 preprint`
- [AI Agent Traps](papers/Safety_Alignment/ssrn-6372438.md) — エージェントトラップ6カテゴリの体系化、攻撃成功率86% (Franklin et al., 2026 / DeepMind) `📝 preprint`
- [Scalable Extraction of Training Data from LMs](papers/Safety_Alignment/scalable-training-data-extraction.md) — Divergence attackでChatGPTの学習データを150倍速で抽出、アラインメントはメモリゼーションを隠蔽するだけ (Nasr, Carlini et al., 2023) `✅ ICLR 2025`

### RL
- [Learning, Fast and Slow: Towards LLMs That Adapt Continually](papers/RL/learning-fast-and-slow.md) — **Fast-Slow Training (FST)** = parameter θ を slow weights（GRPO+CISPO）、prompt Φ を fast weights（GEPA = Reflective Prompt Evolution）として interleave 最適化。RL 単独比 **最大3倍のサンプル効率**＋asymptote も上回り、継続学習で RL が stall する設定でも near-peak を維持 (Tiwari et al., 2026 / UC Berkeley × Mila × UT Austin) `📝 preprint`
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](papers/RL/sft-memorizes-rl-generalizes.md) — SFT/RL を **memorization vs generalization** 軸で実証対比。GeneralPoints / V-IRL の rule・visual OOD で RL は汎化・SFT は ID 過適合（極端な暗記）、V-IRL Visual OOD で **+33.8pt SOTA**。ただし指示追従できない backbone への直接 RL は失敗し SFT 前段が必要 (Chu et al., 2025 / UC Berkeley × HKU × Google DeepMind × U Alberta) `✅ ICML 2025`
- [The Debate on RLVR Reasoning Capability Boundary](papers/RL/rlvr-capability-boundary-debate.md) — shrinkage vs expansionを二段階動態で統一的に再解釈 (arXiv 2510.04028, 2025) `📝 preprint (ICLR 2026 Rejected)`
- [Does RLVR Truly Unlock New Reasoning?](papers/RL/rlvr-does-not-teach-new-reasoning.md) — Pass@k分析によりRLVRはfiltering/sharpening主体と主張 (Yue et al., 2025) `✅ NeurIPS 2025 (Oral, Best Paper Runner-up)`
- [Dr. GRPO: Understanding R1-Zero-Like Training](papers/RL/dr-grpo.md) — R1-Zeroの "Aha moment" の一部はDeepSeek-V3-Base時点で既出現、Qwen2.5 base はテンプレなし推論が可能 → 事前学習バイアス説。GRPOには不正解出力の応答長を人為的に増やす最適化バイアスがあることを同定、**Dr. GRPO**（unbiased GRPO）を提案。minimalist recipeで7B base × AIME 2024 43.3%（当時SOTA）(Liu et al., 2025 / Sea AI Lab × NUS) `✅ COLM 2025`
- [ProRL](papers/RL/prorl.md) — 長期RL訓練で推論境界を真に拡張、Yue et al.への反論 (Liu et al., 2025 / NVIDIA) `✅ NeurIPS 2025`
- [DeepSeek-R1](papers/RL/deepseek-r1.md) — SFTなしpure RLでself-verification・reflection出現 (DeepSeek-AI, 2025) `✅ Nature 2025`
- [MRPO](papers/RL/mrpo.md) — Manifold-Reshaping Policy Optimization、SOE+rank正則化で4Bが32Bを上回る (Wang et al., 2026) `📝 preprint`
- [CodeScout](papers/RL/codescout.md) — Unix端末のみでRL訓練したコード検索エージェント、1.7Bが18倍大きいモデルを上回る (Sutawika et al., 2026) `📝 preprint`
- [OpenClaw-RL](papers/RL/openclaw-rl.md) — next-state信号を活用したエージェントRLフレームワーク (Wang et al., 2026) `📝 preprint`
- [RS-GRPO](papers/RL/rs-grpo.md) — リスク感応的目的関数でexploration dilemmaを緩和、pass@1維持+pass@k向上 (Jiang et al., 2025 / 清華大 × ByteDance Seed) `✅ ICLR 2026 (Poster)`
- [Flash-RL / TIS: Off-Policy Framework Mismatch](papers/RL/flash-rl-tis.md) — vLLM rolloutとFSDP学習の分布乖離で効率的RLが暗黙にoff-policy化、Truncated Importance Samplingで数行修正。VeRL等主要フレームワークに統合済み (Yao, Liu et al., 2025 / UCSD × MSR) `— blog`
- [ScaleRL: The Art of Scaling RL Compute](papers/RL/scale-rl.md) — 40万GPU時間超の体系実験でLLM向けRLのsigmoid scaling則を定式化、漸近値 vs 計算効率の切り分けで能力境界論争を再定式化、10万GPU時間単一ランで検証損失を事前予測 (Khatri, Madaan, Tiwari et al., 2025 / Meta × UT Austin) `✅ ICLR 2026 Oral`
- [Scaling Behaviors of LLM RL Post-Training](papers/RL/rl-scaling-math-qwen25.md) — Qwen2.5 0.5B–72B全系列で数学推論RL（GRPO）のスケーリング則を定式化、log L(N,X)=−k(N)·log X+E(N)のpower-law、学習効率k(N)=K_max/(1+N_0/N)の飽和、データ制約下では「最適化ステップ総数」が「ユニークサンプル数」より支配的 (Tan, Geng, Yu et al., 2025 / Shanghai AI Lab × Oxford) `📝 preprint (ICLR 2026 Withdrawn)`
- [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](papers/RL/willccbb-sft-rl-opd.md) — SFT/RL/OPD/SDFT/OPSD を統一 token-level policy gradient（α, λ, π_T の3ダイアル）で整理するメタ分析。**compounding argument** で SFT-then-RL 順序を説明し、各メソッドを Pareto curve 上に配置。AI 共著の技術メタ分析の運用例 (Brown & Claude Opus 4.7, 2026 / X 投稿) `— blog`

### Agent_ToolUse
- [AutoHarness](papers/Agent_ToolUse/autoharness.md) — LLMエージェントのための自動コードハーネス合成 (Lou et al., 2026) `📋 workshop`
- [Self-Organizing LLM Agents](papers/Agent_ToolUse/self-organizing-llm-agents.md) — 自己組織化が設計済み階層を14%上回る (Dochkina, 2026) `🔄 IEEE Access（投稿中）`
- [Agentic RL Training](papers/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md) — Kimi/Cursor/ChromaのエージェントRL訓練比較 (Schmid, 2026) `— blog`
- [LLM-as-a-Verifier](papers/Agent_ToolUse/llm-as-a-verifier.md) — 3軸（granularity/repetition/decomposition）スケール検証、trajectory reward modelでTerminal-Bench 2 86.4% (SOTA) / SWE-Bench Verified 77.8%、Claude Opus 4.6 / GPT 5.4 / Geminiを上回る (Kwok, Li, Atreya et al., 2026 / Stanford × UC Berkeley × NVIDIA) `— blog`
- [Vector DBを外したら、RAGではなくAgent Runtimeが残った](papers/Agent_ToolUse/vector-db-to-agent-runtime.md) — RAG（retrieve→generate）を **RAR (Retrieval Augmented Reasoning)**（retrieve to reason）に再定義する経験報告。Typed Artifacts と LangGraph+SQLite 状態機械で「推論構造を runtime に外出し」、LLM を「自律的推論者」から「スキーマを埋める変換コンポーネント」に再配置 (mofuteq, 2026 / Zenn) `— blog`
- [RAGとAgentic Searchの戦争を終わらせに来た!!!](papers/Agent_ToolUse/rag-vs-agentic-search.md) — 「RAG は終わった」言説を**用語の定義ズレに起因する疑似論争**として整理。RAG は広義化（外部データ参照で生成強化）、**Agentic Search の本質は手段でなく「推論で複数回検索を反復する戦略」**。ベクトル検索 RAG は死んでおらず、CAG / ファイルシステム探索 / LLM Wiki を含め「対象データの性質・規模・タスクで使い分ける」が結論 (Hirosato Gamo, 2026 / Microsoft・Zenn) `— blog`

### Domain_Specific
- [Automated PLC Test Generation](papers/Domain_Specific/automated-plc-test-generation.md) — LLMによるPLC制御ロジックテストケース自動生成 (Koziolek et al., 2024) `✅ IEEE ETFA 2024`
- [Sarashina-Embedding-v2](papers/Domain_Specific/sarashina-embedding-v2.md) — 日本語特化テキスト埋め込みモデル (SB Intuitions, 2025) `— blog`

### Social_Science
- [The AI Layoff Trap](papers/Social_Science/ai-layoff-trap.md) — 需要外部性による自動化軍拡競争、ピグー税のみが解消可能 (Hemenway Falk & Tsoukalas, 2026) `📝 preprint`

### Physical_AI
- [DreamZero](papers/Physical_AI/dreamzero-world-action-models.md) — ビデオ拡散によるゼロショットロボットポリシー (Ye et al., 2026) `📋 workshop`
- [V-JEPA 2](papers/Physical_AI/v-jepa-2.md) — 自己教師あり動画モデルによるロボット理解・予測・計画 (Assran et al., 2025) `📝 preprint`
- [LeWorldModel (LeWM)](papers/Physical_AI/leworldmodel.md) — raw pixelsからend-to-end安定学習できる最初のJEPA、next-embedding prediction + Gaussian正則化の2損失項・1ハイパラ、15M×単GPUで foundation world model比 最大48倍高速な計画、潜在空間が物理量をprobingで保持 (Maes, Le Lidec, Scieur, LeCun, Balestriero, 2026 / Meta FAIR) `📝 preprint`
- [Scaling Laws of Motion Forecasting and Planning](papers/Physical_AI/scaling-laws-motion-forecasting-planning.md) — 自動運転の動作予測・計画でLLM型スケーリング則が成立、閉ループでも有効 (Baniodeh et al., 2025) `— tech report`

### Multimodal
- [CLIP: Learning Transferable Visual Models From Natural Language Supervision](papers/Multimodal/clip.md) — 4億 (image, text) ペアの contrastive 事前学習で **zero-shot ImageNet 76.2%**（ResNet-50 supervised 同等）、30+ タスクへ転移・distribution shift に頑健。視覚-言語基盤モデルの出発点、現 MLLM/diffusion の事実上標準 vision tower (Radford et al., 2021 / OpenAI) `✅ ICML 2021`
- [FROMAGe: Grounding Language Models to Images for Multimodal Inputs and Outputs](papers/Multimodal/fromage.md) — 凍結 OPT-6.7B + 凍結 CLIP を **線形射影層と `[RET]` token のみ**（trainable 0.1%未満）で結合。VIST 文脈 retrieval R@1 20.8 vs CLIP 5.9。「凍結バックボーン + 軽量 projection」レシピの祖型、後の LLaVA/BLIP-2/GILL の参照点 (Koh, Salakhutdinov, Fried, 2023 / CMU) `✅ ICML 2023`
- [Video models are zero-shot learners and reasoners](papers/Multimodal/video-models-zero-shot-learners.md) — Veo 3が明示訓練外のタスク（segmentation/edge detection/editing/物理理解/affordance/道具使用）をゼロショットで解く現象を体系実証、迷路・対称性など初期visual reasoning発現 (Wiedemer, Li, Vicol et al., 2025 / Google DeepMind) `📝 preprint`

### Inference_Decoding
- [Reasoning with Sampling](papers/Inference_Decoding/reasoning-with-sampling.md) — MCMCベースの推論時サンプリングでRL訓練なしにreasoning改善 (Karan & Du, 2025 / Harvard) `✅ ICLR 2026 (Oral)`

### Efficiency_Optimization
- [Flash-KMeans](papers/Efficiency_Optimization/flash-kmeans.md) — GPU最適化K-meansで最大17.9倍高速化 (Yang et al., 2026) `📝 preprint`
- [TurboQuant](papers/Efficiency_Optimization/turboquant.md) — KVキャッシュ6倍圧縮 (Zandieh & Mirrokni, 2026) `✅ ICLR 2026 (Poster)`
- [The Lottery Ticket Hypothesis](papers/Efficiency_Optimization/lottery-ticket-hypothesis.md) — 密なネットワーク内のスパースなwinning ticketの発見 (Frankle & Carbin, 2018) `✅ ICLR 2019`

### Graph_Network
- [From Louvain to Leiden](papers/Graph_Network/louvain-to-leiden.md) — 精製ステップとキュー管理で連結コミュニティを保証するグラフ分割アルゴリズム (Traag et al., 2019) `✅ Scientific Reports 2019`
- [GVE-Leiden: Fast Leiden in Shared Memory](papers/Graph_Network/gve-leiden.md) — ライデン法の共有メモリ並列SOTA実装、32コアCPUでオリジナル比436×・igraph 104×・NetworKit 8.2×・cuGraph (A100) 3.0×、403M edges/s @ 3.8B edges、スレッド倍化で1.6×スケール (Sahu, Kothapalli, Banerjee, 2024 / IIIT Hyderabad) `✅ ICPP 2024`
- [Memory-Efficient Community Detection via Weighted Sketches](papers/Graph_Network/memory-efficient-cd-sketches.md) — Louvain/Leiden/LPAのper-thread hashtable（100M頂点×64スレッドで51.2-102.4GB）をweighted Misra-Gries sketchで~0.5KB/sketchに置換、グラフサイズ非依存。modularity劣化Louvain≤1%/Leiden 0.8%/LPAほぼゼロ、ランタイム1.48-3.15×。GVE-Leidenと同著者によるメモリ側SOTA (Sahu, 2024 / IIIT Hyderabad) `📝 preprint`

### Symbolic_Computation
- [All elementary functions from a single binary operator](papers/Symbolic_Computation/eml-single-operator.md) — eml(x,y)=exp(x)−ln(y)と定数1で全初等関数を生成、連続版NANDゲート (Odrzywołek, 2026) `📝 preprint`

### Press_Releases
- [Karpathy Wiki Workflow](papers/Press_Releases/karpathy-tweet.md) — LLMでソース文書を構造化wikiにコンパイル (Karpathy, 2026) `— tweet`
- [NRI ITロードマップ2026](papers/Press_Releases/nri-report-59421.md) — エージェント型AIと汎用人工知能 (幸田, 長谷, 権藤, 2026) `— report`

## Comparisons
（比較ページ）

*まだページがありません。*

## Benchmarks
（ベンチマーク結果）

*まだページがありません。*

## Engineering
（実装メモ・ノウハウ）

- [AWS上でGPU分散学習・ML開発をする自分向け注意事項まとめ](engineering/aws-gpu-ml-security-practices.md) — IAM/S3/SSH/Secrets/ログ/学習データ/チーム運用/コスト/法務を網羅した実践ルール集
