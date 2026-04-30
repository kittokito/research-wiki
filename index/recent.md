# Recent Additions

最近追加・更新されたページ。新しい順。

---

## 2026-04-27

- [Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md) を追加 — 共有メモリ並列の Louvain / Leiden / LPA で支配的になる **per-thread hashtable**（100M頂点×64スレッドで **51.2-102.4 GB**）を **weighted Misra-Gries sketch**（~0.5KB/sketch、グラフサイズ非依存）で置換。modularity 劣化は Louvain **≤1%** / Leiden **0.8%** / LPA ほぼゼロ、ランタイムオーバーヘッドは MG8 Louvain **1.48×**（web平均 2.07×）/ MG64 Leiden **3.15×** / MG8 LPA **2.11×**（web/social平均 2.78×）。SuiteSparse 13グラフ（最大3.8Bエッジ）/ dual 16-core Xeon Gold 6226R + 376GB RAM / 64スレッド。著者は [GVE-Leiden](../wiki/papers/Graph_Network/gve-leiden.md) と同一の Subhajit Sahu（IIIT Hyderabad）— 速度SOTA の GVE-Leiden に対し、本論文はメモリ側のSOTAとして相補、コア数×頂点数のスケーリング軸でメモリを切り離す (Sahu, 2024 / IIIT Hyderabad)

## 2026-04-23

- [Dr. GRPO: Understanding R1-Zero-Like Training](../wiki/papers/RL/dr-grpo.md) を追加 — DeepSeek-R1-Zeroの「pure RLで推論創発」を base model / RL に分解して批判的検証。DeepSeek-V3-Base は RL 前から "Aha moment" を示し、Qwen2.5 base もテンプレなしで強い推論能力を示す → **事前学習バイアス説**。さらに **GRPO には不正解出力の応答長を人為的に増やす最適化バイアス** があることを同定し、**Dr. GRPO**（unbiased GRPO）を提案。minimalist R1-Zero recipeで 7B base × **AIME 2024 43.3%**（当時SOTA）。RLVR 能力境界論争に「事前学習バイアス」という第三の軸を追加、ScaleRL の CISPO 採用や各種 GRPO 改良（RS-GRPO, MRPO）の理論的基盤を補強 (Liu, Chen, Li, Qi, Pang, Du, Lee, Lin, 2025 / Sea AI Lab × sail-sg × NUS, COLM 2025)
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
- [SSRN 6372438](../wiki/papers/Press_Releases/ssrn-6372438.md) を追加 — 未処理
- [Karpathy Tweet](../wiki/papers/Press_Releases/karpathy-tweet.md) を追加 — 未処理
- [NRI Report 59421](../wiki/papers/Press_Releases/nri-report-59421.md) を追加 — 未処理
- [GSM-Symbolic](../wiki/papers/Reasoning/gsm-symbolic.md) を追加 — 数値変更だけでLLM数学推論が大きくばらつく (Apple Research)
- NRIレポートを更新 — 「ITロードマップ2026年版 エージェント型AIと汎用人工知能」
- AI Agent Traps を Safety_Alignment に移動
- Karpathy Tweet を更新 — LLMナレッジベース構築ワークフロー
