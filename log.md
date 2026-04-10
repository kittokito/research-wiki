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
