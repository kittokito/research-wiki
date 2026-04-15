# Recent Additions

最近追加・更新されたページ。新しい順。

---

## 2026-04-15

- [SECURE: Benchmarking LLMs for Cybersecurity](../wiki/papers/Evaluation/secure-cybersecurity-benchmark.md) を追加 — ICS特化6データセット（MAET, CWET, KCV, VOOD, RERT, CPST）で7モデルを評価、ChatGPT-4が4/6タスクで最高、OOD検出（VOOD）でChatGPT-3.5が8.4%に壊滅的劣化 (Bhusal et al., 2024)

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
