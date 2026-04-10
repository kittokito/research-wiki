# Open Questions

未解決の問い・調査課題。解決したら status を `resolved` に変更し、解決先ページへリンクする。

---

### LLM Reasoning Failures より
- [ ] Fundamental Failuresのうち、アーキテクチャ変更で解消可能なものと本質的に困難なものの境界はどこか？ → [paper](../wiki/papers/Surveys_Overview/llm-reasoning-failures.md)
- [ ] 緩和策の組み合わせ（CoT + RAG + マルチエージェント等）による相乗効果はどの程度か？ → [paper](../wiki/papers/Surveys_Overview/llm-reasoning-failures.md)

### DeepCrossAttention より
- [ ] 大規模モデル（数十B以上）での改善幅は実用的に有意か？ → [paper](../wiki/papers/Architecture/deep-cross-attention.md)
- [ ] DCAとMoEの組み合わせは有効か？ → [paper](../wiki/papers/Architecture/deep-cross-attention.md)

### Mixture-of-Depths Attention より
- [ ] MoDAの大規模モデル（数十B以上）での効果は？ → [paper](../wiki/papers/Architecture/mixture-of-depths-attention.md)
- [ ] MoDAとMoEの組み合わせは有効か？ → [paper](../wiki/papers/Architecture/mixture-of-depths-attention.md)

### Continuous Autoregressive LM より
- [ ] 連続ベクトル予測の品質は離散トークン予測と同等か？ → [paper](../wiki/papers/Architecture/continuous-autoregressive-lm.md)

### MSA: Memory Sparse Attention より
- [ ] 100Mトークンでの実用的なユースケースは？RAGとの詳細比較は？ → [paper](../wiki/papers/Architecture/memory-sparse-attention.md)

### mHC より
- [ ] mHCとDCAの組み合わせは有効か？ → [paper](../wiki/papers/Architecture/manifold-constrained-hyper-connections.md)

### Mind the Gap より
- [ ] 検証が生成より容易でないケース（検証ギャップが閉じるケース）はどのような条件で発生するか？ → [paper](../wiki/papers/Reasoning/mind-the-gap-self-improvement.md)

### Reversal Curse より
- [ ] 双方向モデルや検索拡張はReversal Curseを緩和するか？ → [paper](../wiki/papers/Reasoning/reversal-curse.md)

### Sycophantic Delusional Spiraling より
- [ ] シカンシーを軽減しつつユーザー満足度を維持する最適戦略は？ → [paper](../wiki/papers/Safety_Alignment/sycophantic-delusional-spiraling.md)

### Self-Organizing LLM Agents より
- [ ] 自己組織化が失敗するタスク特性は？ → [paper](../wiki/papers/Agent_ToolUse/self-organizing-llm-agents.md)

### Scaling Laws of Motion Forecasting and Planning より
- [ ] 閉ループでのスケーリング成立は他のアーキテクチャ（因子分解アテンション等）でも再現するか？ → [paper](../wiki/papers/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- [ ] end-to-end vision入力にした場合もスケーリング則は維持されるか？ → [paper](../wiki/papers/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### DreamZero / V-JEPA 2 より
- [ ] World Action Model vs JEPAの優劣は？ → [paper](../wiki/papers/Physical_AI/dreamzero-world-action-models.md)
- [ ] 7Hz以上（30Hz+）のリアルタイム制御は達成可能か？ → [paper](../wiki/papers/Physical_AI/dreamzero-world-action-models.md)

### Claude Mythos Preview より
- [ ] Mythosの性能改善のうち、モデル本体の能力向上分とscaffold/harness最適化分はどの程度分離可能か？ → [model](../wiki/models/claude-mythos-preview.md)
- [ ] Claude Code利用データのflywheel仮説はどの程度検証可能か？ → [model](../wiki/models/claude-mythos-preview.md)
- [ ] 実行環境つきRLのスケーリング則（計算量 vs 改善幅）はどこまで明らかか？ → [model](../wiki/models/claude-mythos-preview.md)

### RLVRの能力境界論争より
- [ ] 標準RLVRがfilteringに留まりやすい部分と、本当に新戦略獲得になりやすい部分（特にコーディング領域）の境界は？ → [topic](../wiki/topics/RL/rlvr-capability-boundary.md)
- [ ] Exploration stageの発現条件（rollout数、モデルサイズ、タスク難易度の閾値）は定量化できるか？ → [paper](../wiki/papers/RL/rlvr-capability-boundary-debate.md)
- [ ] MRPOのSOEの効果はデータ品質向上か、本当にmanifold脱出か？（ablationではデータ品質寄与が大きい可能性） → [paper](../wiki/papers/RL/mrpo.md)
- [ ] MRPOは数学以外のverifiable domain（コーディング等）でも同様の改善を示すか？ → [paper](../wiki/papers/RL/mrpo.md)
- [ ] Effective rank正則化によるbias manifold外動作は安全性にどう影響するか？ → [paper](../wiki/papers/RL/mrpo.md)
- [ ] 環境内方策学習（code execution, web browsing等）はtext-only RLVRとqualitativeに異なる能力を引き出すか？ → [topic](../wiki/topics/RL/rlvr-capability-boundary.md)

### CodeScout より
- [ ] RFTなしpure RLでの小型モデル（1.7B）のコード検索性能は？（filtering vs 能力獲得の切り分け） → [paper](../wiki/papers/RL/codescout.md)
- [ ] ツール収束現象（多様→最小限）は他のエージェントタスクでも再現するか？ → [paper](../wiki/papers/RL/codescout.md)

### From Louvain to Leiden より
- [ ] 精製ステップで孤立ノード（どのサブコミュニティにも属さない）が発生した場合の挙動の詳細は？ → [paper](../wiki/papers/Graph_Network/louvain-to-leiden.md)
- [ ] 解像度パラメータの選択指針（resolution limit問題への対処）はどの程度確立されているか？ → [paper](../wiki/papers/Graph_Network/louvain-to-leiden.md)

### TurboQuant / MSA より
- [ ] TurboQuantとMSAのKVキャッシュ圧縮を組み合わせた効果は？ → [paper](../wiki/papers/Efficiency_Optimization/turboquant.md)
