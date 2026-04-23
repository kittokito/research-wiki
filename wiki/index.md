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
- [Attention to Mamba: Cross-Architecture Distillation](papers/Architecture/attention-to-mamba-distillation.md) — Transformer→Mambaクロスアーキ蒸留の二段階レシピ（kernel trick経由で純Mambaへ、hybrid不要）、Pythia-1Bで teacher perplexity 13.86 → 14.11 (Moudgil, Huang, Dhekane et al., 2026) `📝 preprint`
- [Mixture-of-Depths Attention](papers/Architecture/mixture-of-depths-attention.md) — 深度方向KVペアへのアテンションで信号劣化問題に対処 (Zhu et al., 2026) `📝 preprint`
- [Attention Residuals](papers/Architecture/attention-residuals.md) — softmaxアテンションで残差接続の選択的集約、Kimi Linearに統合 (Chen et al., 2026) `— tech report`
- [Continuous Autoregressive Language Models](papers/Architecture/continuous-autoregressive-lm.md) — next-vector predictionで生成ステップをK分の1に (Shao et al., 2025) `🔄 ICLR 2026（投稿中）`
- [MSA: Memory Sparse Attention](papers/Architecture/memory-sparse-attention.md) — 100Mトークンまでスケーラブルなメモリモデル (Chen et al., 2026) `📝 preprint`
- [mHC: Manifold-Constrained Hyper-Connections](papers/Architecture/manifold-constrained-hyper-connections.md) — HCの恒等写像特性を復元しスケーラビリティ向上 (Xie et al., 2025) `📝 preprint`
- [Conditional Memory via Scalable Lookup](papers/Architecture/conditional-memory-scalable-lookup.md) — Engramモジュールによる条件付きメモリスパース性 (Cheng et al., 2026) `📝 preprint`
- [DeepCrossAttention](papers/Architecture/deep-cross-attention.md) — 入力依存の学習可能重みによる残差接続の改良 (Heddes et al., 2025) `✅ ICML 2025`

### Pretraining
- [Rewriting Pre-Training Data](papers/Pretraining/rewriting-pretraining-data.md) — SwallowCode/SwallowMathでデータリライティングにより性能向上 (Fujii et al., 2025) `✅ ICLR 2026`
- [FineData (HuggingFaceFW)](papers/Pretraining/huggingface-finedata.md) — 大規模オープン事前学習データセット群 (Hugging Face, 2025) `✅ NeurIPS 2024`
- [ATLAS: Multilingual Scaling Laws](papers/Pretraining/atlas-multilingual-scaling-laws.md) — 過去最大規模の多言語スケーリング則（774実験/400+言語）、ATLASが+0.3 R²で既存則を上回り、1444言語ペアの転移行列とscratch vs finetuneのクロスオーバー点を同定 (Longpre, Kudugunta, Muennighoff et al., 2025) `✅ ICLR 2026`

### Post_Training
- [Neural Thickets](papers/Post_Training/neural-thickets.md) — 事前学習重み近傍の多様なエキスパートをランダム摂動で発見 (Gan & Isola, 2026) `📝 preprint`
- [Simple Self-Distillation](papers/Post_Training/simple-self-distillation-code.md) — 自身の出力のみでコード生成を改善するSSD (Zhang et al., 2026) `📝 preprint`
- [Namazu Alpha](papers/Post_Training/namazu-alpha.md) — オープン基盤モデルの日本仕様適応 (Sakana AI, 2026) `— blog`

### Evaluation
- [SWE-CI](papers/Evaluation/swe-ci.md) — CI環境でのコードベース保守能力評価ベンチマーク (Chen et al., 2026) `📝 preprint`
- [P-hacking with one prompt](papers/Evaluation/p-hacking-with-one-prompt.md) — たった一つのプロンプトでLLMがp-hackingに加担する危険性を実証 (Kawahara, 2026) `📝 preprint`
- [SECURE: Benchmarking LLMs for Cybersecurity](papers/Evaluation/secure-cybersecurity-benchmark.md) — ICS特化6データセットでLLMのサイバーセキュリティ能力を評価、OOD検出に大きな性能差 (Bhusal et al., 2024) `✅ ACSAC 2024`
- [LiveBench](papers/Evaluation/livebench.md) — 汚染耐性・客観採点・広範タスク・月次更新を同時達成した初のLLMベンチマーク、0.5B-405B評価でトップ<70% (White, Dooley, Roberts et al., 2024) `✅ ICLR 2025 Spotlight`

### Technical_Report
- [Kimi K2.5](papers/Technical_Report/kimi-k25.md) — オープンソースマルチモーダルエージェントモデル (Kimi Team, 2026) `— tech report`

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
- [The Debate on RLVR Reasoning Capability Boundary](papers/RL/rlvr-capability-boundary-debate.md) — shrinkage vs expansionを二段階動態で統一的に再解釈 (arXiv 2510.04028, 2025) `🔄 under-review`
- [Does RLVR Truly Unlock New Reasoning?](papers/RL/rlvr-does-not-teach-new-reasoning.md) — Pass@k分析によりRLVRはfiltering/sharpening主体と主張 (Yue et al., 2025) `✅ NeurIPS 2025 (Oral, Best Paper Runner-up)`
- [ProRL](papers/RL/prorl.md) — 長期RL訓練で推論境界を真に拡張、Yue et al.への反論 (Liu et al., 2025 / NVIDIA) `✅ NeurIPS 2025`
- [DeepSeek-R1](papers/RL/deepseek-r1.md) — SFTなしpure RLでself-verification・reflection出現 (DeepSeek-AI, 2025) `✅ Nature 2025`
- [MRPO](papers/RL/mrpo.md) — Manifold-Reshaping Policy Optimization、SOE+rank正則化で4Bが32Bを上回る (Wang et al., 2026) `📝 preprint`
- [CodeScout](papers/RL/codescout.md) — Unix端末のみでRL訓練したコード検索エージェント、1.7Bが18倍大きいモデルを上回る (Sutawika et al., 2026) `📝 preprint`
- [OpenClaw-RL](papers/RL/openclaw-rl.md) — next-state信号を活用したエージェントRLフレームワーク (Wang et al., 2026) `📝 preprint`
- [RS-GRPO](papers/RL/rs-grpo.md) — リスク感応的目的関数でexploration dilemmaを緩和、pass@1維持+pass@k向上 (Jiang et al., 2025 / 清華大 × ByteDance Seed) `🔄 ICLR 2026（投稿中）`
- [Flash-RL / TIS: Off-Policy Framework Mismatch](papers/RL/flash-rl-tis.md) — vLLM rolloutとFSDP学習の分布乖離で効率的RLが暗黙にoff-policy化、Truncated Importance Samplingで数行修正。VeRL等主要フレームワークに統合済み (Yao, Liu et al., 2025 / UCSD × MSR) `— blog`
- [ScaleRL: The Art of Scaling RL Compute](papers/RL/scale-rl.md) — 40万GPU時間超の体系実験でLLM向けRLのsigmoid scaling則を定式化、漸近値 vs 計算効率の切り分けで能力境界論争を再定式化、10万GPU時間単一ランで検証損失を事前予測 (Khatri, Madaan, Tiwari et al., 2025 / Meta × UT Austin) `✅ ICLR 2026 Oral`
- [Scaling Behaviors of LLM RL Post-Training](papers/RL/rl-scaling-math-qwen25.md) — Qwen2.5 0.5B–72B全系列で数学推論RL（GRPO）のスケーリング則を定式化、log L(N,X)=−k(N)·log X+E(N)のpower-law、学習効率k(N)=K_max/(1+N_0/N)の飽和、データ制約下では「最適化ステップ総数」が「ユニークサンプル数」より支配的 (Tan, Geng, Yu et al., 2025 / Shanghai AI Lab × Oxford) `✅ ACL 2026 Main`

### Agent_ToolUse
- [AutoHarness](papers/Agent_ToolUse/autoharness.md) — LLMエージェントのための自動コードハーネス合成 (Lou et al., 2026) `📋 workshop`
- [Self-Organizing LLM Agents](papers/Agent_ToolUse/self-organizing-llm-agents.md) — 自己組織化が設計済み階層を14%上回る (Dochkina, 2026) `🔄 IEEE Access（投稿中）`
- [Agentic RL Training](papers/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md) — Kimi/Cursor/ChromaのエージェントRL訓練比較 (Schmid, 2026) `— blog`
- [LLM-as-a-Verifier](papers/Agent_ToolUse/llm-as-a-verifier.md) — 3軸（granularity/repetition/decomposition）スケール検証、trajectory reward modelでTerminal-Bench 2 86.4% (SOTA) / SWE-Bench Verified 77.8%、Claude Opus 4.6 / GPT 5.4 / Geminiを上回る (Kwok, Li, Atreya et al., 2026 / Stanford × UC Berkeley × NVIDIA) `— blog`

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
- [Video models are zero-shot learners and reasoners](papers/Multimodal/video-models-zero-shot-learners.md) — Veo 3が明示訓練外のタスク（segmentation/edge detection/editing/物理理解/affordance/道具使用）をゼロショットで解く現象を体系実証、迷路・対称性など初期visual reasoning発現 (Wiedemer, Li, Vicol et al., 2025 / Google DeepMind) `📝 preprint`

### Inference_Decoding
- [Reasoning with Sampling](papers/Inference_Decoding/reasoning-with-sampling.md) — MCMCベースの推論時サンプリングでRL訓練なしにreasoning改善 (Karan & Du, 2025 / Harvard) `🔄 ICLR 2026（投稿中）`

### Efficiency_Optimization
- [Flash-KMeans](papers/Efficiency_Optimization/flash-kmeans.md) — GPU最適化K-meansで最大17.9倍高速化 (Yang et al., 2026) `📝 preprint`
- [TurboQuant](papers/Efficiency_Optimization/turboquant.md) — KVキャッシュ6倍圧縮 (Zandieh & Mirrokni, 2026) `✅ ICLR 2026 (Poster)`
- [The Lottery Ticket Hypothesis](papers/Efficiency_Optimization/lottery-ticket-hypothesis.md) — 密なネットワーク内のスパースなwinning ticketの発見 (Frankle & Carbin, 2018) `✅ ICLR 2019`

### Graph_Network
- [From Louvain to Leiden](papers/Graph_Network/louvain-to-leiden.md) — 精製ステップとキュー管理で連結コミュニティを保証するグラフ分割アルゴリズム (Traag et al., 2019) `✅ Scientific Reports 2019`

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
