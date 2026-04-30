# Change Log

時系列の変更ログ。新しいエントリを末尾に追記する（append-only）。

---

## 2026-04-07

- **初期構築**: research-wiki ディレクトリ構造・SCHEMA・テンプレート・インデックスを作成
- **論文追加**: Large Language Model Reasoning Failures (Song et al., 2026)
  - `sources/llm-reasoning-failures.md` 作成
  - `evidence/llm-reasoning-failures.md` 作成
  - `wiki/papers/llm-reasoning-failures.md` 作成
  - SCHEMA.md にセクション参照リンク規約を追加
  - 各インデックスを更新
- **論文追加**: Conditional Memory via Scalable Lookup (Cheng et al., 2026)
  - `sources/Architecture/conditional-memory-scalable-lookup.md` 作成
  - `evidence/Architecture/conditional-memory-scalable-lookup.md` 作成
  - `wiki/papers/Architecture/conditional-memory-scalable-lookup.md` 作成
  - 各インデックスを更新
- **論文追加**: DeepCrossAttention: Supercharging Transformer Residual Connections (Heddes et al., 2025)
  - `sources/Architecture/deep-cross-attention.md` 作成
  - `evidence/Architecture/deep-cross-attention.md` 作成
  - `wiki/papers/Architecture/deep-cross-attention.md` 作成
  - 各インデックスを更新
- **28ソース一括追加**: 以下のソースを追加（sources, evidence, wiki/papers の3ファイルをそれぞれ作成）
  - Architecture (5件): Mixture-of-Depths Attention, Attention Residuals, Continuous Autoregressive LM, MSA: Memory Sparse Attention, mHC: Manifold-Constrained Hyper-Connections
  - Pretraining (2件): Rewriting Pre-Training Data (SwallowCode/Math), FineData (HuggingFaceFW)
  - Post_Training (3件): Neural Thickets, Simple Self-Distillation, Namazu Alpha
  - Evaluation (1件): SWE-CI
  - Technical_Report (1件): Kimi K2.5
  - Reasoning (2件): Mind the Gap (Self-Improvement), The Reversal Curse
  - Safety_Alignment (1件): Sycophantic Delusional Spiraling
  - RL (1件): OpenClaw-RL
  - Agent_ToolUse (3件): AutoHarness, Self-Organizing LLM Agents, Agentic RL Training (blog)
  - Domain_Specific (2件): Automated PLC Test Generation, Sarashina-Embedding-v2
  - Physical_AI (2件): DreamZero, V-JEPA 2
  - Efficiency_Optimization (2件): Flash-KMeans, TurboQuant
  - Press_Releases (3件, unprocessed): SSRN 6372438, Karpathy Tweet, NRI Report 59421
  - 各インデックス（wiki/index.md, index/topics.md, index/models.md, index/recent.md, index/open-questions.md）を更新
- **更新**: NRIレポート — 「ITロードマップ2026年版 エージェント型AIと汎用人工知能」(幸田, 長谷, 権藤)としてURL・内容を更新
- **更新**: AI Agent Traps (SSRN 6372438) — Press_Releases → Safety_Alignment に移動
- **更新**: Karpathy Tweet — LLMナレッジベース構築ワークフローとして内容を更新
- **論文追加**: GSM-Symbolic (Mirzadeh et al., 2024)
  - `sources/Reasoning/gsm-symbolic.md` 作成
  - `evidence/Reasoning/gsm-symbolic.md` 作成
  - `wiki/papers/Reasoning/gsm-symbolic.md` 作成
  - 各インデックスを更新

## 2026-04-08

- **モデル追加**: Claude Mythos Preview (Anthropic, 2026 / Project Glasswing)
  - `sources/Technical_Report/claude-mythos-preview.md` 作成
  - `evidence/Technical_Report/claude-mythos-preview.md` 作成
  - `wiki/models/claude-mythos-preview.md` 作成（modelsカテゴリ初エントリ）
  - 内容: ベンチマーク性能比較（vs Opus 4.6）、過去Claude系改善幅との比較、評価条件（scaffold/harness統一度）の分析、性能改善仮説6つ（Claude Code flywheel、実行環境つきRL等）、実行環境つきRLの解説
  - 各インデックスを更新
- **論文追加**: Scaling Laws of Motion Forecasting and Planning (Baniodeh et al., 2025 / Waymo)
  - `sources/Physical_AI/scaling-laws-motion-forecasting-planning.md` 作成
  - `evidence/Physical_AI/scaling-laws-motion-forecasting-planning.md` 作成
  - `wiki/papers/Physical_AI/scaling-laws-motion-forecasting-planning.md` 作成
  - 各インデックスを更新
- **トピック新設**: RLVRの能力境界論争（topics初エントリ）
  - `wiki/topics/RL/rlvr-capability-boundary.md` 作成 — filtering vs 真の能力獲得、界隈の中間的着地を整理
  - 内容: shrinkage派（Yue et al., Invisible Leash）とexpansion派（DeepSeek-R1, Reasoning Gym）の論点整理、二段階動態モデル、pretraining manifoldへの閉じ込め問題、コーディング領域への示唆、次世代手法（MRPO等）
- **論文追加** (3件): RLVRの能力境界関連
  - `sources/RL/rlvr-capability-boundary-debate.md` 作成 — The Debate on RLVR Reasoning Capability Boundary (arXiv 2510.04028)
  - `sources/RL/rlvr-does-not-teach-new-reasoning.md` 作成 — Does RLVR Truly Unlock New Reasoning? (Yue et al., 2025)
  - `sources/RL/deepseek-r1.md` 作成 — DeepSeek-R1 (DeepSeek-AI, 2025)
  - 各 evidence, wiki/papers も作成
  - 各インデックスを更新
- **論文追加**: MRPO — Beyond Alignment: Expanding Reasoning Capacity via Manifold-Reshaping Policy Optimization (Wang et al., 2026)
  - `sources/RL/mrpo.md` 作成
  - `evidence/RL/mrpo.md` 作成
  - `wiki/papers/RL/mrpo.md` 作成
  - `wiki/topics/RL/rlvr-capability-boundary.md` を更新（MRPO詳細を追記）
  - 各インデックスを更新
- **論文追加**: CodeScout — An Effective Recipe for Reinforcement Learning of Code Search Agents (Sutawika et al., 2026 / CMU)
  - `sources/RL/codescout.md` 作成
  - `evidence/RL/codescout.md` 作成
  - `wiki/papers/RL/codescout.md` 作成
  - `wiki/topics/RL/rlvr-capability-boundary.md` を更新（コーディング領域の具体例として追記）
  - 各インデックスを更新

## 2026-04-10

- **論文追加**: From Louvain to Leiden: guaranteeing well-connected communities (Traag, Waltman & van Eck, 2019)
  - `sources/Graph_Network/louvain-to-leiden.md` 作成
  - `evidence/Graph_Network/louvain-to-leiden.md` 作成
  - `wiki/papers/Graph_Network/louvain-to-leiden.md` 作成
  - 内容: ルーヴァン法 vs ライデン法の比較、隣接ノードキュー管理による高速化、精製（refinement）ステップによる品質保証、アルゴリズム詳細
- **カテゴリ追加**: `Graph_Network`（グラフ・ネットワーク科学）を SCHEMA.md に追加
  - `sources/Graph_Network/`, `evidence/Graph_Network/`, `wiki/papers/Graph_Network/`, `wiki/topics/Graph_Network/` を作成
  - 各インデックスを更新
- **論文追加**: The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks (Frankle & Carbin, 2018)
  - `sources/Efficiency_Optimization/lottery-ticket-hypothesis.md` 作成
  - `evidence/Efficiency_Optimization/lottery-ticket-hypothesis.md` 作成
  - `wiki/papers/Efficiency_Optimization/lottery-ticket-hypothesis.md` 作成
  - 各インデックスを更新

## 2026-04-13

- **論文追加**: P-hacking with one prompt (Kawahara, 2026)
  - `sources/Evaluation/p-hacking-with-one-prompt.md` 作成
  - `evidence/Evaluation/p-hacking-with-one-prompt.md` 作成
  - `wiki/papers/Evaluation/p-hacking-with-one-prompt.md` 作成
  - 各インデックスを更新

## 2026-04-14

- **カテゴリ追加**: `Social_Science`（社会科学・経済学・政策・労働）を SCHEMA.md に追加
  - `sources/Social_Science/`, `evidence/Social_Science/`, `wiki/papers/Social_Science/`, `wiki/topics/Social_Science/` を作成
- **論文追加**: The AI Layoff Trap (Hemenway Falk & Tsoukalas, 2026)
  - `sources/Social_Science/ai-layoff-trap.md` 作成
  - `evidence/Social_Science/ai-layoff-trap.md` 作成
  - `wiki/papers/Social_Science/ai-layoff-trap.md` 作成
  - 各インデックスを更新
  - ※ 当初 `Domain_Specific` に配置されていたが、`Social_Science` カテゴリ新設に伴い移動
- **論文追加**: The Geometry of Forgetting (Barman, Starenky, Bodnar, Narasimhan & Gopinath, 2026)
  - `sources/Reasoning/geometry-of-forgetting.md` 作成
  - `evidence/Reasoning/geometry-of-forgetting.md` 作成
  - `wiki/papers/Reasoning/geometry-of-forgetting.md` 作成
  - 内容: 高次元埋め込み空間の幾何学的性質から忘却・偽記憶が発生、干渉がべき乗則忘却の支配的ドライバー、dimensionality illusion（有効次元~16）、DRM偽記憶のパラメータフリー再現、vector averaging fallacyの指摘
  - 各インデックスを更新
- **エンジニアリングノート新設**: AWS上でGPU分散学習・ML開発をする自分向け注意事項まとめ（engineering初エントリ）
  - `wiki/engineering/aws-gpu-ml-security-practices.md` 作成
  - 内容: IAM/S3/SSH/Secrets/ログ・実験管理/学習データ利用/チェックポイント/チーム開発/監査/コスト/法務・倫理の15章構成
  - 各インデックスを更新
## 2026-04-15

- **論文追加**: SECURE: Benchmarking Large Language Models for Cybersecurity (Bhusal et al., 2024)
  - `sources/Evaluation/secure-cybersecurity-benchmark.md` 作成
  - `evidence/Evaluation/secure-cybersecurity-benchmark.md` 作成
  - `wiki/papers/Evaluation/secure-cybersecurity-benchmark.md` 作成
  - 内容: ICSセクター特化6データセットで7モデルを3軸（知識抽出・理解・推論）評価、VOODでの壊滅的性能差（ChatGPT-4: 87.9% vs ChatGPT-3.5: 8.4%）、セキュリティ領域でのLLM信頼性課題
  - 各インデックスを更新
- **論文追加**: Scalable Extraction of Training Data from (Production) Language Models (Nasr, Carlini et al., 2023)
  - `sources/Safety_Alignment/scalable-training-data-extraction.md` 作成
  - `evidence/Safety_Alignment/scalable-training-data-extraction.md` 作成
  - `wiki/papers/Safety_Alignment/scalable-training-data-extraction.md` 作成
  - 内容: Divergence attack（単一トークン反復）でChatGPTの学習データを150倍速抽出、約$200で10,000+系列、PII含有率16.9%、アラインメントはメモリゼーション隠蔽に過ぎない
  - 各インデックスを更新

- **カテゴリ追加**: `Symbolic_Computation`（記号計算・数式処理・数学的基礎）を SCHEMA.md に追加
  - `sources/Symbolic_Computation/`, `evidence/Symbolic_Computation/`, `wiki/papers/Symbolic_Computation/`, `wiki/topics/Symbolic_Computation/` を作成
- **論文追加**: All elementary functions from a single binary operator (Odrzywołek, 2026)
  - `sources/Symbolic_Computation/eml-single-operator.md` 作成
  - `evidence/Symbolic_Computation/eml-single-operator.md` 作成
  - `wiki/papers/Symbolic_Computation/eml-single-operator.md` 作成
  - 内容: 単一二項演算子 eml(x,y)=exp(x)−ln(y) と定数1で全初等関数を生成（連続版NANDゲート）、EMLツリーによる勾配ベース記号回帰、NNアーキテクチャとの接点
  - 各インデックスを更新

## 2026-04-16

- **スキーマ更新**: `peer_review` / `venue` フィールドを SCHEMA.md に追加
  - 全 sources/ ファイル（47件）および全 wiki/papers/ ファイル（46件）にラベル付与
  - wiki/papers/ 各ページのタイトル直下に査読バッジを追加（プレビュー表示対応）
  - `index/peer-review.md` 新規作成（査読状況別一覧）
  - `wiki/index.md` の各エントリにインラインステータスタグを追加
- **論文追加**: ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in LLMs (Liu et al., 2025 / NVIDIA)
  - `sources/RL/prorl.md` 作成
  - `evidence/RL/prorl.md` 作成
  - `wiki/papers/RL/prorl.md` 作成
  - 内容: KL制御・ポリシーリセット・多タスク多様性による長期RL訓練、1.5Bモデルで数学+14.7%/コード+13.9%/論理パズル+54.8%、Yue et al.のfiltering説への反論
  - 査読: ✅ NeurIPS 2025
- **論文追加**: Reasoning with Sampling: Your Base Model is Smarter Than You Think (Karan & Du, 2025 / Harvard)
  - `sources/Inference_Decoding/reasoning-with-sampling.md` 作成
  - `evidence/Inference_Decoding/reasoning-with-sampling.md` 作成
  - `wiki/papers/Inference_Decoding/reasoning-with-sampling.md` 作成（Inference_Decodingカテゴリ初エントリ）
  - 内容: べき分布＋MCMCサンプリングで訓練なしにベースモデルからreasoning引き出し、MATH500でGRPO相当
  - 査読: 当初 ✅ ICLR 2026 (Oral) と記載 → 2026-04-17 に 🔄 under-review（ICLR 2026 Conference Submission）に訂正（ICLR 2026 Orals公式リストに不在、OpenReview Vsgq2ldr4K）
- **論文更新**: Does RLVR Truly Unlock New Reasoning? (Yue et al., 2025)
  - 正式タイトル・著者リスト・arXiv URL (2504.13837) を追加
  - NeurIPS 2025 Oral / Best Paper Runner-up を明記

## 2026-04-17

- **査読状況一括見直し**: 既存preprint 20件・accepted 17件についてarXiv Comments・OpenReview・会議公式サイト横断で再確認
  - `sources/Architecture/continuous-autoregressive-lm.md` (CALM): preprint → under-review (ICLR 2026 Conference Submission, OpenReview Ce6Mep9oie)
  - `sources/Agent_ToolUse/self-organizing-llm-agents.md`: preprint → under-review (IEEE Access, arXiv Commentsで明記)
  - `sources/Inference_Decoding/reasoning-with-sampling.md`: ✅ ICLR 2026 (Oral) → 🔄 under-review に訂正（Orals公式リスト不在）
  - `sources/Efficiency_Optimization/turboquant.md`: venue に (Poster) 明記（iclr.cc/virtual/2026/poster/10006985 で確認）
  - 残り18件preprintは現時点でステータス変更なし（OpenReview・会議採択リストでヒットなし）
  - 各wiki/papers/ページ冒頭の査読バッジ、`wiki/index.md`、`index/peer-review.md` を更新
  - SCHEMA.md に「venue調査時の注意」節を追加（arXivのみに依存せずOpenReview・会議公式サイトを必ず確認する指針）
- **論文追加**: RS-GRPO — Risk-Sensitive RL for Alleviating Exploration Dilemmas in LLMs (Jiang et al., 2025 / 清華大 × ByteDance Seed)
  - `sources/RL/rs-grpo.md` 作成
  - `evidence/RL/rs-grpo.md` 作成
  - `wiki/papers/RL/rs-grpo.md` 作成
  - 内容: sharpened prior × 標準RL目的関数が招くexploration dilemma、CVaRベースの平均-最大補間目的関数、GRPOへの数行修正で困難プロンプトからの学習を増幅、6数学ベンチ×5LLMでpass@1維持+pass@k継続向上
  - 査読: 🔄 under-review (ICLR 2026 Conference Submission / OpenReview 7kC8ORye4l / arXiv 2509.24261)
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md）を更新
- **ブログ記事追加**: Flash-RL / TIS — "Your Efficient RL Framework Secretly Brings You Off-Policy RL Training" (Yao, Liu et al., 2025 / UCSD × Microsoft Research, Notionブログ)
  - `sources/RL/flash-rl-tis.md` 作成
  - `evidence/RL/flash-rl-tis.md` 作成
  - `wiki/papers/RL/flash-rl-tis.md` 作成
  - 内容: rollout生成（vLLM/SGLang）と学習バックエンド（FSDP/Megatron）の実装差分により、同一パラメータθでも `π_sampler` と `π_learner` のトークン確率が乖離し on-policy RL が暗黙に off-policy 化する問題を提起。重要度比に上限Cのクランプを入れた Truncated Importance Sampling (TIS) による数行の勾配修正を提案。Qwen2.5-32B+DAPO・GSM8K+INT8 rollout で性能回復と entropy collapse／応答長暴走／負のKL推定の解消を確認。並列化差分（TP/SP）・長文応答がミスマッチの主因、sampler backend 単独の影響は小。MoE RLでは増幅見込み、GSPO/GMPOと直交。VeRL・slime・OAT・SkyRL・OpenRLHF・REINFORCE++ が実装／統合済み
  - 査読: — n/a（ブログ記事, Feng Yao's Notion, 2025-08-05 公開 / 2025-10-13 最終更新）
  - `wiki/topics/RL/rlvr-capability-boundary.md` に「測定側のバイアス：off-policyミスマッチ問題」節を追記、sources/関連ページ/未解決の問いに反映
  - `index/topics.md` に "off-policy RL / importance sampling" トピック追加、RLVR capability boundary のソース数を 7→8 に更新
  - 各インデックス（wiki/index.md, index/recent.md, index/peer-review.md, index/topics.md）を更新

## 2026-04-20

- **論文追加**: ATLAS — Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality (Longpre, Kudugunta, Muennighoff et al., 2025 / MIT × Google × Stanford)
  - `sources/Pretraining/atlas-multilingual-scaling-laws.md` 作成
  - `evidence/Pretraining/atlas-multilingual-scaling-laws.md` 作成
  - `wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md` 作成
  - 内容: 過去最大規模の多言語スケーリング則研究（774実験 / 10M-8B / 400+学習言語 / 48評価言語）、ATLASが既存スケーリング則を out-of-sample で +0.3 R² 以上上回る、38×38=1444言語ペアの転移行列、language-agnosticスケーリング則、scratch学習 vs 多言語チェックポイントからのfinetuneの計算クロスオーバー点
  - 査読: ✅ accepted — ICLR 2026 (arXiv Comments に明記)
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新

## 2026-04-21

- **論文追加**: LiveBench — A Challenging, Contamination-Limited LLM Benchmark (White, Dooley, Roberts et al., 2024 / Abacus.AI × Meta × NYU × UMD × USC)
  - `sources/Evaluation/livebench.md` 作成
  - `evidence/Evaluation/livebench.md` 作成
  - `wiki/papers/Evaluation/livebench.md` 作成
  - 内容: 汚染耐性 + 客観採点 + 広範タスク（math/coding/reasoning/language/instruction-following/data analysis）+ 月次更新を同時達成した初のベンチマーク、arXiv・math competitions・news・datasets から問題構築、Big-Bench Hard / AMPS / IFEval 困難化版、0.5B-405Bモデル評価でトップ<70%、全問題・コード・回答公開
  - 査読: ✅ accepted — ICLR 2025 (Spotlight) / arXiv 2406.19314 / OpenReview sKYHBTAxVa
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
- **論文追加**: ScaleRL — The Art of Scaling Reinforcement Learning Compute for LLMs (Khatri, Madaan, Tiwari et al., 2025 / Meta × UT Austin)
  - `sources/RL/scale-rl.md` 作成
  - `evidence/RL/scale-rl.md` 作成
  - `wiki/papers/RL/scale-rl.md` 作成
  - 内容: 40万GPU時間超の体系実験、RL訓練の計算-性能曲線をsigmoidでフィッティング、設計選択をablationして「漸近性能を動かす要素」と「計算効率のみを動かす要素」を切り分け。loss aggregation / 正則化 / curriculum / off-policy 等は効率のみ調整。安定レシピは予測可能scalingを示し、10万GPU時間規模の単一ランで検証損失を事前予測。ベストプラクティス「ScaleRL」を提案
  - 査読: ✅ accepted — ICLR 2026 (Oral) / arXiv 2510.13786 / OpenReview FMjeC9Msws
  - `wiki/topics/RL/rlvr-capability-boundary.md` を更新（「漸近値 vs 効率の切り分け：ScaleRLの枠組み」節を追加、能力境界論争を再定式化する道具立てとして統合）
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
- **論文追加**: Video models are zero-shot learners and reasoners (Wiedemer, Li, Vicol et al., 2025 / Google DeepMind)
  - `sources/Multimodal/video-models-zero-shot-learners.md` 作成（Multimodalカテゴリ初エントリ）
  - `evidence/Multimodal/video-models-zero-shot-learners.md` 作成
  - `wiki/papers/Multimodal/video-models-zero-shot-learners.md` 作成
  - 内容: Veo 3 が明示訓練していないタスク（segmentation / edge detection / editing / 物理理解 / affordance / 道具使用シミュレーション）をゼロショットで解ける現象を体系的実証、迷路・対称性解きなど初期visual reasoningも発現、video modelが汎用視覚基盤モデルへ向かう軌道を主張
  - 査読: 📝 preprint（ICLR 2026 投稿 → Rejected_Submission / OpenReview MCWypEBtlF）
- **論文追加**: Attention to Mamba — A Recipe for Cross-Architecture Distillation (Moudgil, Huang, Dhekane et al., 2026 / Apple推定)
  - `sources/Architecture/attention-to-mamba-distillation.md` 作成
  - `evidence/Architecture/attention-to-mamba-distillation.md` 作成
  - `wiki/papers/Architecture/attention-to-mamba-distillation.md` 作成
  - 内容: Transformer→Mambaクロスアーキテクチャ蒸留の二段階レシピ（kernel trick適用linearized Attentionを経由）、hybrid不要の純Mamba蒸留、Pythia-1B teacher perplexity 13.86 → 蒸留後Mamba 14.11、1Bスケール・10Bトークンで体系的ablation
  - 査読: 📝 preprint / arXiv 2604.14191
- **記事追加**: LLM-as-a-Verifier — A General-Purpose Verification Framework (Kwok, Li, Atreya et al., 2026 / Stanford × UC Berkeley × NVIDIA)
  - `sources/Agent_ToolUse/llm-as-a-verifier.md` 作成
  - `evidence/Agent_ToolUse/llm-as-a-verifier.md` 作成
  - `wiki/papers/Agent_ToolUse/llm-as-a-verifier.md` 作成
  - 内容: scoring granularity / repeated verification / criteria decomposition の3軸でLLM検証をスケール。agent trajectoryの軌跡reward modelとしてtest-time scaling構成を取り、Terminal-Bench 2 で 86.4% (SOTA)、SWE-Bench Verified で 77.8%、Claude Opus 4.6 / GPT 5.4 / Gemini各モデルを上回る。Verifier に Gemini 2.5 Flash、候補trajectoryは Claude Opus 4.6・Gemini 3 Flash・Claude Opus 4.5 から。Terminal-Benchでは 81.8% → 86.4% を test-time scaling + verification のみで達成、pairwise検証精度78.9%
  - 査読: — n/a（Notion公開プロジェクトページ, 2026-04-09） / GitHub: llm-as-a-verifier/llm-as-a-verifier
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新

## 2026-04-23

- **論文追加**: Understanding R1-Zero-Like Training: A Critical Perspective / Dr. GRPO (Liu, Chen, Li, Qi, Pang, Du, Lee, Lin, 2025 / Sea AI Lab × sail-sg × NUS)
  - `sources/RL/dr-grpo.md` 作成
  - `evidence/RL/dr-grpo.md` 作成
  - `wiki/papers/RL/dr-grpo.md` 作成
  - 内容: DeepSeek-R1-Zero の「pure RL で推論創発」を **base model 要因 + RL要因** に分解して批判的検証。発見: (1) **DeepSeek-V3-Base は RL 前から "Aha moment" を示す** → 事前学習バイアス説、(2) **Qwen2.5 base はプロンプトテンプレなしで強い推論能力** → pretraining biases、(3) **GRPO には不正解出力の応答長を人為的に増やす最適化バイアス** が存在、(4) バイアス除去の **Dr. GRPO**（"done right" GRPO）を提案し token 効率を改善しつつ推論性能維持、(5) minimalist R1-Zero recipe で **7B base × AIME 2024 43.3%**（当時SOTA）。RLVR 能力境界論争に「事前学習バイアス」という第三の軸を追加し、ScaleRL の CISPO 採用や各種 GRPO 改良（RS-GRPO, MRPO）の理論的基盤を補強。Scaling Behaviors of LLM RL Post-Training (Qwen2.5 scaling則) の一般性の再検討材料にもなる
  - 査読: ✅ accepted — COLM 2025 (OpenReview 5PAF7PAY2Y, decision: Accepted, published 2025-07-08)
  - GitHub: sail-sg/understand-r1-zero / arXiv 2503.20783 / v1: 2025-03-26, v2: 2025-10-06
  - `wiki/index.md` 配置: rlvr-does-not-teach-new-reasoning（Yue et al., filtering派）の直後 — RLVR 能力境界論争クラスタを「filtering vs expansion + 事前学習バイアス」の3軸で整理
  - `index/topics.md` に新トピック `GRPO variants / analysis`（Dr. GRPO, RS-GRPO, MRPO, ScaleRL, MiniMax-M1 の5件）。既存 `RLVR capability boundary` にも追加（10→11）
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
- **論文追加**: Qwen3.5-Omni Technical Report (Qwen Team, 2026 / Alibaba)
  - `sources/Technical_Report/qwen35-omni.md` 作成
  - `evidence/Technical_Report/qwen35-omni.md` 作成
  - `wiki/papers/Technical_Report/qwen35-omni.md` 作成
  - 内容: 数百億パラメータ規模・256kコンテキストのomni-modal（text + vision + audio + video）モデル。**Thinker / Talker 双方に Hybrid Attention MoE** を採用、効率的な長系列推論を実現。1億時間超のaudio-visual学習、10時間超audio / 400秒720P動画（1 FPS）。**Qwen3.5-Omni-plus** が 215 audio/audio-visual benchmark で SOTA、主要audioで Gemini-3.1 Pro を上回り、audio-visual総合で同等。**ARIA**（text/speech tokenizer 符号化効率ミスマッチを動的整列）で安定ストリーミングTTS、10言語感情表現音声、script-level 構造化キャプション + temporal synchronization。**Audio-Visual Vibe Coding**（音声・映像指示→直接コード生成）という新規創発能力を観測。MiniMax-M1 と同系統の hybrid attention MoE 設計で、音声・映像軸への拡張事例として位置付けられる
  - 査読: — n/a（テクニカルレポート、arXiv 2604.15804 / v1: 2026-04-17, v2: 2026-04-21）
  - `wiki/index.md` 配置: MiniMax-M1 の直後（hybrid attention MoE 系譜 / オープンウェイト tech report 群）
  - `index/topics.md` に新トピック追加: `hybrid attention / linear attention`（MiniMax-M1, Qwen3.5-Omni, Attention Residuals, Attention to Mamba Distillation の4件）、`audio / speech`（Qwen3.5-Omni）。既存の `multimodal` / `long context` / `open-weight models` にも追加
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
- **論文追加**: MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention (MiniMax Team, 2025)
  - `sources/Technical_Report/minimax-m1.md` 作成
  - `evidence/Technical_Report/minimax-m1.md` 作成
  - `wiki/papers/Technical_Report/minimax-m1.md` 作成
  - 内容: 世界初のオープンウェイト大規模ハイブリッドアテンション推論モデル。hybrid MoE + lightning attention、456B total / 45.9B active per token、ネイティブ 1M context（DeepSeek R1 の8倍）。新規RLアルゴリズム **CISPO**（token updates ではなく importance sampling weights をクリップ）、他の競合RL派生を上回る効率。hybrid attention + CISPO で 512 H800 GPU × 3週間 / $534,700 でフルRL訓練完了。thinking budget 40K / 80K を2モデル公開、DeepSeek-R1 / Qwen3-235B に匹敵・上回る（特に complex SWE・tool use・long-context）。GitHub: MiniMax-AI/MiniMax-M1。CISPO は Flash-RL/TIS の Truncated Importance Sampling と同系統の IS-weight クリッピング系で、ScaleRL の「効率を動かす設計選択」に分類可能
  - 査読: — n/a（テクニカルレポート、arXiv 2506.13585, 2025-06-16）
  - `wiki/index.md` 配置: Kimi K2.5 の直後（オープンウェイト技術レポート系譜）
  - `index/topics.md` に新トピック3件追加: `open-weight models`（Kimi K2.5, MiniMax-M1, DeepSeek-R1）、`test-time compute`（MiniMax-M1, Reasoning with Sampling, LLM-as-a-Verifier）、既存の `long context`・`off-policy RL / importance sampling` に追加
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
- **SCHEMA更新**: 「インデックスの並び順」節を追加
  - `wiki/index.md`: カテゴリ内は話題クラスタ順 + 同一クラスタ内は追加順（機械的ソートは避ける）
  - `index/recent.md`: 日付降順、`index/peer-review.md`: 採択年昇順、`index/topics.md`: 運用で管理
  - カテゴリ20件超で `wiki/topics/{Category}/` サブ分割、Lint項目に追加
- **論文追加**: GVE-Leiden: Fast Leiden Algorithm for Community Detection in Shared Memory Setting (Sahu, Kothapalli, Banerjee, 2024 / IIIT Hyderabad)
  - `sources/Graph_Network/gve-leiden.md` 作成
  - `evidence/Graph_Network/gve-leiden.md` 作成
  - `wiki/papers/Graph_Network/gve-leiden.md` 作成
  - 内容: ライデン法の共有メモリ並列実装SOTA。dual 16-core Intel Xeon Gold 6226R（32コア）で オリジナル Leiden 比 436×、igraph Leiden 比 104×、NetworKit Leiden 比 8.2×、**cuGraph Leiden (A100 GPU) 比 3.0×**。3.8Bエッジで 403M edges/s、スレッド倍化ごと平均1.6× のスケーリング。CPU実装がGPU実装を上回る稀な事例で、ライデン法のGPU最適化がまだ十分でないことを示唆。[louvain-to-leiden](../wiki/papers/Graph_Network/louvain-to-leiden.md)（Traag et al., 2019）の直接的な実装フォロー
  - 査読: 📋 workshop — ICPP 2024 Workshops (DOI 10.1145/3673038.3673146)
  - `wiki/index.md` 配置: SCHEMA新規則に従い、louvain-to-leiden の直後（原論文→並列実装の系譜順）
  - `index/topics.md` に `parallel / HPC` トピック新設（GVE-Leiden, Flash-KMeans の2件）
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新

## 2026-04-27

- **論文追加**: Memory-Efficient Community Detection on Large Graphs Using Weighted Sketches (Sahu, 2024 / IIIT Hyderabad)
  - `sources/Graph_Network/memory-efficient-cd-sketches.md` 作成
  - `evidence/Graph_Network/memory-efficient-cd-sketches.md` 作成
  - `wiki/papers/Graph_Network/memory-efficient-cd-sketches.md` 作成
  - 内容: 共有メモリ並列の Louvain / Leiden / LPA で支配的になる **per-thread hashtable**（100M頂点 × 64スレッドで **51.2-102.4 GB**）を **weighted Misra-Gries sketch**（~0.5KB/sketch、グラフサイズ非依存）で置換するメモリ効率化。modularity 劣化は Louvain **≤1%** / Leiden **0.8%** / LPA ほぼゼロ、ランタイムオーバーヘッドは MG8 Louvain **1.48×**（web平均 2.07×）/ MG64 Leiden **3.15×** / MG8 LPA **2.11×**（web/social平均 2.78×）。SuiteSparse 13グラフ（最大3.8Bエッジ）/ dual 16-core Xeon Gold 6226R + 376GB RAM / 64スレッドで評価。Misra-Gries の k=8（Louvain/LPA）/ k=64（Leiden）。著者は GVE-Leiden と同一の Subhajit Sahu — 速度SOTA の GVE-Leiden に対し、本論文はメモリ側のSOTAとして相補、コア数×頂点数のスケーリング軸でメモリを物理メモリではなく計算予算で律速できる位置付け
  - 査読: 📝 preprint（arXiv 2411.02268 / v1: 2024-11-04, v2: 2024-11-06, v3: 2025-01-30、venue採択未確認）
  - `wiki/index.md` 配置: gve-leiden の直後（同著者・Graph_Network カテゴリ内、速度→メモリの系譜順）
  - `index/topics.md` に `sketch / streaming algorithms` トピック新設、既存の `community detection` / `parallel / HPC` を更新
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
- **論文追加**: LeWorldModel (LeWM): Stable End-to-End Joint-Embedding Predictive Architecture from Pixels (Maes, Le Lidec, Scieur, LeCun, Balestriero, 2026 / Meta FAIR)
  - `sources/Physical_AI/leworldmodel.md` 作成
  - `evidence/Physical_AI/leworldmodel.md` 作成
  - `wiki/papers/Physical_AI/leworldmodel.md` 作成
  - 内容: raw pixels から end-to-end で安定学習する最初のJEPA。既存JEPAが表現崩壊回避のためにmulti-term loss・EMA・事前学習エンコーダ・補助監督に依存していた脆弱性を、next-embedding prediction + Gaussian分布正則化の2損失項で解消。調整ハイパラは 6→1 に削減。~15Mパラメータ × 単GPU × 数時間で学習、foundation-model-based world model 比 最大48倍高速な計画を2D/3D制御タスクで実現。潜在空間は物理量をprobingで保持、surprise評価で物理的非現実事象を検出。JEPA普及の閾値を大きく下げた位置付け
  - 査読: 📝 preprint（arXiv 2603.19312 / v1: 2026-03-13 / v2: 2026-03-24、venue情報なし）
  - `index/topics.md` に `world model / JEPA` トピック新設（3件: V-JEPA 2, LeWM, DreamZero）
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新

## 2026-04-22

- **論文追加**: Scaling Behaviors of LLM Reinforcement Learning Post-Training (Tan, Geng, Yu, Zhang, Wan et al., 2025 / Shanghai AI Lab × Oxford)
  - `sources/RL/rl-scaling-math-qwen25.md` 作成
  - `evidence/RL/rl-scaling-math-qwen25.md` 作成
  - `wiki/papers/RL/rl-scaling-math-qwen25.md` 作成
  - 内容: Qwen2.5 dense 全系列（0.5B–72B）× GRPO × 数学推論RLポストトレーニングの体系的スケーリング則研究。log L(N, X) = −k(N)·log X + E(N) の power-law と学習効率飽和 k(N) = K_max/(1 + N_0/N) を定式化。4つのkey findings: (1) 大モデルほど計算・データ効率が高い、(2) test loss はbase/instructで頑健な power-law、(3) 学習効率 k(N) は飽和する、(4) データ制約下では最適化ステップ総数がサンプルユニーク数より支配的（高品質データ再利用が有効）。ScaleRL の sigmoid フィットと相補的な分析枠組みを提供し、「大モデルの効率優位性にも天井がある」という追加の定量的制約を RLVR 能力境界論争に持ち込む
  - 査読: ✅ accepted — ACL 2026 Main Conference (arXiv 2509.25300 v4 Comments に明記)
  - 各インデックス（wiki/index.md, index/topics.md, index/recent.md, index/peer-review.md, index/open-questions.md）を更新
