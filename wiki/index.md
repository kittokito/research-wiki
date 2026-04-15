# Wiki Index

wikiに含まれる全ページのカタログ。カテゴリごとに整理。

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
- [Mixture-of-Depths Attention](papers/Architecture/mixture-of-depths-attention.md) — 深度方向KVペアへのアテンションで信号劣化問題に対処 (Zhu et al., 2026)
- [Attention Residuals](papers/Architecture/attention-residuals.md) — softmaxアテンションで残差接続の選択的集約、Kimi Linearに統合 (Chen et al., 2026)
- [Continuous Autoregressive Language Models](papers/Architecture/continuous-autoregressive-lm.md) — next-vector predictionで生成ステップをK分の1に (Shao et al., 2025)
- [MSA: Memory Sparse Attention](papers/Architecture/memory-sparse-attention.md) — 100Mトークンまでスケーラブルなメモリモデル (Chen et al., 2026)
- [mHC: Manifold-Constrained Hyper-Connections](papers/Architecture/manifold-constrained-hyper-connections.md) — HCの恒等写像特性を復元しスケーラビリティ向上 (Xie et al., 2025)
- [Conditional Memory via Scalable Lookup](papers/Architecture/conditional-memory-scalable-lookup.md) — Engramモジュールによる条件付きメモリスパース性 (Cheng et al., 2026)
- [DeepCrossAttention](papers/Architecture/deep-cross-attention.md) — 入力依存の学習可能重みによる残差接続の改良 (Heddes et al., 2025)

### Pretraining
- [Rewriting Pre-Training Data](papers/Pretraining/rewriting-pretraining-data.md) — SwallowCode/SwallowMathでデータリライティングにより性能向上 (Fujii et al., 2025)
- [FineData (HuggingFaceFW)](papers/Pretraining/huggingface-finedata.md) — 大規模オープン事前学習データセット群 (Hugging Face, 2025)

### Post_Training
- [Neural Thickets](papers/Post_Training/neural-thickets.md) — 事前学習重み近傍の多様なエキスパートをランダム摂動で発見 (Gan & Isola, 2026)
- [Simple Self-Distillation](papers/Post_Training/simple-self-distillation-code.md) — 自身の出力のみでコード生成を改善するSSD (Zhang et al., 2026)
- [Namazu Alpha](papers/Post_Training/namazu-alpha.md) — オープン基盤モデルの日本仕様適応 (Sakana AI, 2026)

### Evaluation
- [SWE-CI](papers/Evaluation/swe-ci.md) — CI環境でのコードベース保守能力評価ベンチマーク (Chen et al., 2026)
- [P-hacking with one prompt](papers/Evaluation/p-hacking-with-one-prompt.md) — たった一つのプロンプトでLLMがp-hackingに加担する危険性を実証 (Kawahara, 2026)
- [SECURE: Benchmarking LLMs for Cybersecurity](papers/Evaluation/secure-cybersecurity-benchmark.md) — ICS特化6データセットでLLMのサイバーセキュリティ能力を評価、OOD検出に大きな性能差 (Bhusal et al., 2024)

### Technical_Report
- [Kimi K2.5](papers/Technical_Report/kimi-k25.md) — オープンソースマルチモーダルエージェントモデル (Kimi Team, 2026)

### Reasoning
- [Mind the Gap](papers/Reasoning/mind-the-gap-self-improvement.md) — 生成よりも検証の方が容易であることを示した自己改善研究 (Song et al., 2024)
- [The Reversal Curse](papers/Reasoning/reversal-curse.md) — 「AはB」で学習しても「BはA」に汎化しない (Berglund et al., 2023)
- [GSM-Symbolic](papers/Reasoning/gsm-symbolic.md) — 数値変更だけでLLM数学推論が大きくばらつく、パターンマッチングの限界 (Mirzadeh et al., 2024)
- [The Geometry of Forgetting](papers/Reasoning/geometry-of-forgetting.md) — 埋め込み空間の幾何学から忘却・偽記憶が必然的に発生、有効次元~16のdimensionality illusion (Barman et al., 2026)
- [Large Language Model Reasoning Failures](papers/Surveys_Overview/llm-reasoning-failures.md) — LLM推論失敗の包括的サーベイ (Song et al., 2026)

### Safety_Alignment
- [Sycophantic Delusional Spiraling](papers/Safety_Alignment/sycophantic-delusional-spiraling.md) — シカンシーが理想的ベイズ推論者にも妄想的スパイラルを引き起こす (Chandra et al., 2026)
- [AI Agent Traps](papers/Safety_Alignment/ssrn-6372438.md) — エージェントトラップ6カテゴリの体系化、攻撃成功率86% (Franklin et al., 2026 / DeepMind)

### RL
- [The Debate on RLVR Reasoning Capability Boundary](papers/RL/rlvr-capability-boundary-debate.md) — shrinkage vs expansionを二段階動態で統一的に再解釈 (arXiv 2510.04028, 2025)
- [Does RLVR Truly Unlock New Reasoning?](papers/RL/rlvr-does-not-teach-new-reasoning.md) — Pass@k分析によりRLVRはfiltering/sharpening主体と主張 (Yue et al., 2025)
- [DeepSeek-R1](papers/RL/deepseek-r1.md) — SFTなしpure RLでself-verification・reflection出現 (DeepSeek-AI, 2025)
- [MRPO](papers/RL/mrpo.md) — Manifold-Reshaping Policy Optimization、SOE+rank正則化で4Bが32Bを上回る (Wang et al., 2026)
- [CodeScout](papers/RL/codescout.md) — Unix端末のみでRL訓練したコード検索エージェント、1.7Bが18倍大きいモデルを上回る (Sutawika et al., 2026)
- [OpenClaw-RL](papers/RL/openclaw-rl.md) — next-state信号を活用したエージェントRLフレームワーク (Wang et al., 2026)

### Agent_ToolUse
- [AutoHarness](papers/Agent_ToolUse/autoharness.md) — LLMエージェントのための自動コードハーネス合成 (Lou et al., 2026)
- [Self-Organizing LLM Agents](papers/Agent_ToolUse/self-organizing-llm-agents.md) — 自己組織化が設計済み階層を14%上回る (Dochkina, 2026)
- [Agentic RL Training](papers/Agent_ToolUse/kimi-cursor-chroma-agentic-rl.md) — Kimi/Cursor/ChromaのエージェントRL訓練比較 (Schmid, 2026)

### Domain_Specific
- [Automated PLC Test Generation](papers/Domain_Specific/automated-plc-test-generation.md) — LLMによるPLC制御ロジックテストケース自動生成 (Koziolek et al., 2024)
- [Sarashina-Embedding-v2](papers/Domain_Specific/sarashina-embedding-v2.md) — 日本語特化テキスト埋め込みモデル (SB Intuitions, 2025)

### Social_Science
- [The AI Layoff Trap](papers/Social_Science/ai-layoff-trap.md) — 需要外部性による自動化軍拡競争、ピグー税のみが解消可能 (Hemenway Falk & Tsoukalas, 2026)

### Physical_AI
- [DreamZero](papers/Physical_AI/dreamzero-world-action-models.md) — ビデオ拡散によるゼロショットロボットポリシー (Ye et al., 2026)
- [V-JEPA 2](papers/Physical_AI/v-jepa-2.md) — 自己教師あり動画モデルによるロボット理解・予測・計画 (Assran et al., 2025)
- [Scaling Laws of Motion Forecasting and Planning](papers/Physical_AI/scaling-laws-motion-forecasting-planning.md) — 自動運転の動作予測・計画でLLM型スケーリング則が成立、閉ループでも有効 (Baniodeh et al., 2025)

### Efficiency_Optimization
- [Flash-KMeans](papers/Efficiency_Optimization/flash-kmeans.md) — GPU最適化K-meansで最大17.9倍高速化 (Yang et al., 2026)
- [TurboQuant](papers/Efficiency_Optimization/turboquant.md) — KVキャッシュ6倍圧縮 (Zandieh & Mirrokni, 2026)
- [The Lottery Ticket Hypothesis](papers/Efficiency_Optimization/lottery-ticket-hypothesis.md) — 密なネットワーク内のスパースなwinning ticketの発見 (Frankle & Carbin, 2018)

### Graph_Network
- [From Louvain to Leiden](papers/Graph_Network/louvain-to-leiden.md) — 精製ステップとキュー管理で連結コミュニティを保証するグラフ分割アルゴリズム (Traag et al., 2019)

### Symbolic_Computation
- [All elementary functions from a single binary operator](papers/Symbolic_Computation/eml-single-operator.md) — eml(x,y)=exp(x)−ln(y)と定数1で全初等関数を生成、連続版NANDゲート (Odrzywołek, 2026)

### Press_Releases
- [Karpathy Wiki Workflow](papers/Press_Releases/karpathy-tweet.md) — LLMでソース文書を構造化wikiにコンパイル (Karpathy, 2026)
- [NRI ITロードマップ2026](papers/Press_Releases/nri-report-59421.md) — エージェント型AIと汎用人工知能 (幸田, 長谷, 権藤, 2026)

## Comparisons
（比較ページ）

*まだページがありません。*

## Benchmarks
（ベンチマーク結果）

*まだページがありません。*

## Engineering
（実装メモ・ノウハウ）

- [AWS上でGPU分散学習・ML開発をする自分向け注意事項まとめ](engineering/aws-gpu-ml-security-practices.md) — IAM/S3/SSH/Secrets/ログ/学習データ/チーム運用/コスト/法務を網羅した実践ルール集
