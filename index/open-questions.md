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

### LeWorldModel (LeWM) より
- [ ] Gaussian-distributed latent 正則化は、V-JEPA 2相当の大規模video + robot trajectoryにスケールしても同じ安定性を維持するか？ → [paper](../wiki/papers/Physical_AI/leworldmodel.md)
- [ ] Gaussian事前分布はタスク一般に最適か？言語・マルチモーダル等では別の latent 分布が適切ではないか？ → [paper](../wiki/papers/Physical_AI/leworldmodel.md)
- [ ] 「foundation world model比48倍高速」の倍率は planner (MPC / sampling / policy rollout) や horizon 選択にどこまでロバストか？ → [paper](../wiki/papers/Physical_AI/leworldmodel.md)
- [ ] 2損失項・1ハイパラのシンプルさを維持したまま、action-conditioned（V-JEPA 2-AC相当）に拡張可能か？ → [paper](../wiki/papers/Physical_AI/leworldmodel.md)

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

### GVE-Leiden より
- [ ] cuGraph Leiden (A100) との3.0×差は実装最適化で縮むか、それともアルゴリズム構造上GPUに不利なのか？ → [paper](../wiki/papers/Graph_Network/gve-leiden.md)
- [ ] 1.6×/倍化 のスケーリングは 64/128/256コアでも維持されるか？ボトルネック位置は？ → [paper](../wiki/papers/Graph_Network/gve-leiden.md)
- [ ] 分散メモリ（複数ノードMPI）に拡張した場合、3.8Bエッジ超の規模で同じ原理が効くか？ → [paper](../wiki/papers/Graph_Network/gve-leiden.md)
- [ ] 同じ高速化アプローチは Louvain / Label Propagation / InfoMap 等の他アルゴリズムに移植可能か？ → [paper](../wiki/papers/Graph_Network/gve-leiden.md)

### Memory-Efficient Community Detection (Sahu, 2024) より
- [ ] ランタイム 1.5〜3.2× の劣化はアルゴリズム的最適化（ベクトル化、局所性改善）や sketch 構造の最適化でどこまで縮められるか？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)
- [ ] 64スレッドを超える領域（128/256スレッド、NUMAをまたぐ環境）で、メモリ削減とランタイムの両者は同じ傾きを保つか？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)
- [ ] 同じ sketch 化アプローチは GVE-Leiden の高速実装に直接組み込んで「速度SOTA かつメモリ非依存」を達成可能か？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)
- [ ] weighted Misra-Gries の誤差バウンド（ε vs k）は modularity 損失とどう対応するか？理論保証と実測 1% の関係は？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)
- [ ] bipartite graph・citation network・通信ネットワーク等の異なる構造でも同じ品質劣化幅で済むか？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)
- [ ] Leiden が k=64 必要な理由は精製ステップの構造に内在するか、実装上のチューニングで k を下げられるか？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)
- [ ] 分散メモリ（複数ノード、MPI）に拡張した場合、ノード間通信での sketch のマージ操作はどの程度効率化可能か？ → [paper](../wiki/papers/Graph_Network/memory-efficient-cd-sketches.md)

### The Lottery Ticket Hypothesis より
- [ ] LLM規模でのLTHの成立条件は？大規模Transformerでのwinning ticketの性質はCNN時代と異なるか？ → [paper](../wiki/papers/Efficiency_Optimization/lottery-ticket-hypothesis.md)

### The AI Layoff Trap より
- [ ] ピグー税の最適税率はどのように算定するか？AI能力の急速な変化にどう追従するか？ → [paper](../wiki/papers/Social_Science/ai-layoff-trap.md)
- [ ] 新タスク創出（compensating effect）をモデルに組み込んだ場合、過剰自動化の結論はどの程度変わるか？ → [paper](../wiki/papers/Social_Science/ai-layoff-trap.md)

### P-hacking with one prompt より
- [ ] RLHF等でp-hackingを明示的に拒否するようモデルを訓練できるか？正当な探索的分析の有用性を損なわないか？ → [paper](../wiki/papers/Evaluation/p-hacking-with-one-prompt.md)
- [ ] Code Interpreter付きLLMは、コード実行によりp-hackingの検出・抑止がしやすいか？ → [paper](../wiki/papers/Evaluation/p-hacking-with-one-prompt.md)

### All elementary functions from a single binary operator より
- [ ] 定数を必要としない二項Sheffer演算子（純粋な2要素系）は存在するか？ → [paper](../wiki/papers/Symbolic_Computation/eml-single-operator.md)
- [ ] EML記号回帰は深さ5以上で実用的にスケールするか？構造探索との組み合わせは有効か？ → [paper](../wiki/papers/Symbolic_Computation/eml-single-operator.md)
- [ ] EMLツリーを活性化関数としたNNアーキテクチャは、標準NNと比較して解釈可能性・性能面でどのような特性を示すか？ → [paper](../wiki/papers/Symbolic_Computation/eml-single-operator.md)

### The Geometry of Forgetting より
- [ ] 有効次元数を意図的に増加させた埋め込みモデルは干渉をどの程度低減できるか？精度とのトレードオフは？ → [paper](../wiki/papers/Reasoning/geometry-of-forgetting.md)
- [ ] LLMの内部表現の有効次元数は埋め込みモデルの~16と同程度か、それとも異なるレジームにあるか？ → [paper](../wiki/papers/Reasoning/geometry-of-forgetting.md)
- [ ] メタデータ制約やハイブリッド検索（lexical + semantic）はvector averaging fallacyをどの程度緩和するか？ → [paper](../wiki/papers/Reasoning/geometry-of-forgetting.md)

### Scalable Extraction of Training Data from LMs より
- [ ] GPT-4o、Claude等の最新モデルはdivergence attackに対して根本的に堅牢か、それとも同種の攻撃が未発見なだけか？ → [paper](../wiki/papers/Safety_Alignment/scalable-training-data-extraction.md)
- [ ] 差分プライバシー付き学習は実用的なスケールでメモリゼーションをどの程度低減できるか？ → [paper](../wiki/papers/Safety_Alignment/scalable-training-data-extraction.md)
- [ ] メモリゼーション量とモデル性能のトレードオフはどこにあるか？ → [paper](../wiki/papers/Safety_Alignment/scalable-training-data-extraction.md)

### SECURE: Benchmarking LLMs for Cybersecurity より
- [ ] 最新モデル（Claude Opus 4.6, GPT-4o等）でVOODの性能差は縮小しているか？ → [paper](../wiki/papers/Evaluation/secure-cybersecurity-benchmark.md)
- [ ] ICS以外のサイバーセキュリティ領域（Web脆弱性、マルウェア分析等）に拡張した場合、同様の傾向が見られるか？ → [paper](../wiki/papers/Evaluation/secure-cybersecurity-benchmark.md)

### TurboQuant / MSA より
- [ ] TurboQuantとMSAのKVキャッシュ圧縮を組み合わせた効果は？ → [paper](../wiki/papers/Efficiency_Optimization/turboquant.md)

### ATLAS: Multilingual Scaling Laws より
- [ ] 8B以上（70B+ 規模）でATLASの外挿は成立するか？ → [paper](../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md)
- [ ] 400+学習言語のうち転移行列に含まれない大多数の言語について、ATLAS係数からの外挿はどの程度信頼できるか？ → [paper](../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md)
- [ ] Curse of Multilinguality はモデル容量拡大（MoE等のsparsity活用）で本質的に解消可能か、それとも capacity-agnostic な情報論的限界か？ → [paper](../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md)
- [ ] ATLAS は encoder-only / encoder-decoder アーキテクチャでも同等に成立するか？ → [paper](../wiki/papers/Pretraining/atlas-multilingual-scaling-laws.md)

### LiveBench より
- [ ] 月次更新スケジュールの運用持続性は？コミュニティ貢献が途絶えた場合のフォールバック設計は？ → [paper](../wiki/papers/Evaluation/livebench.md)
- [ ] 「公開 → 学習データ混入 → 汚染」のラグは実測でどの程度短縮しているか（モデルリリース頻度との関係）？ → [paper](../wiki/papers/Evaluation/livebench.md)
- [ ] 自由記述・創造的タスクを LiveBench 流の客観採点に落とし込む設計原則は可能か？ → [paper](../wiki/papers/Evaluation/livebench.md)
- [ ] トップモデル < 70% の制約は月次の困難化でどの程度維持されているか（寿命シミュレーション）？ → [paper](../wiki/papers/Evaluation/livebench.md)

### Dr. GRPO / Understanding R1-Zero-Like Training より
- [ ] DeepSeek-V3-Base で観察される "Aha moment" の本質: 訓練データにCoT類似パターンが潜在していたのか、真の emergence か？ → [paper](../wiki/papers/RL/dr-grpo.md)
- [ ] Dr. GRPO のバイアス除去は ScaleRL 分類で「漸近性能」を改善するのか、「効率のみ」を改善するのか？ → [paper](../wiki/papers/RL/dr-grpo.md)
- [ ] Qwen2.5 以外のベース（LLaMA 3, Gemma 2, DeepSeek-V3-Base）で同じ事前学習バイアスが観察されるか？ → [paper](../wiki/papers/RL/dr-grpo.md)
- [ ] 「不正解出力の応答長バイアス」は最新のGRPO派生（CISPO, RS-GRPO, MRPO）でどこまで除去されているか？ → [paper](../wiki/papers/RL/dr-grpo.md)
- [ ] Dr. GRPO + CISPO は相加的に効くか重複するか？ → [paper](../wiki/papers/RL/dr-grpo.md)
- [ ] 事前学習バイアスの有無を定量化する統一的指標はあるか？ → [paper](../wiki/papers/RL/dr-grpo.md)

### Qwen3.5-Omni より
- [ ] Hybrid Attention MoE における softmax / linear の層混在比率は？ MiniMax-M1 との具体的差分は？ → [paper](../wiki/papers/Technical_Report/qwen35-omni.md)
- [ ] ARIA の tokenizer ミスマッチ動的整列は他のTTS/omni-modal（Kimi/Gemini）に移植可能か？ → [paper](../wiki/papers/Technical_Report/qwen35-omni.md)
- [ ] Audio-Visual Vibe Coding の定量評価（成功率・タスク範囲・コード品質）はどこまで報告されているか？ → [paper](../wiki/papers/Technical_Report/qwen35-omni.md)
- [ ] 10時間 audio / 400秒 video という長系列での実効理解性能は、needle-in-haystack 的評価でどこまで堅牢か？ → [paper](../wiki/papers/Technical_Report/qwen35-omni.md)
- [ ] Qwen3.5-Omni-plus のオープンウェイト公開方針は？ → [paper](../wiki/papers/Technical_Report/qwen35-omni.md)

### MiniMax-M1 より
- [ ] CISPO の利点は MiniMax-M1 の hybrid attention と密結合か、標準 Transformer + GRPO でも同等効果が出るか？ → [paper](../wiki/papers/Technical_Report/minimax-m1.md)
- [ ] 1M context の needle-in-haystack / long-range dependency の実効性能は、lightning attention でどこまで保たれるか？ → [paper](../wiki/papers/Technical_Report/minimax-m1.md)
- [ ] thinking budget 40K → 80K で得られる追加性能の内訳（タスク別の伸び/頭打ち）は？ → [paper](../wiki/papers/Technical_Report/minimax-m1.md)
- [ ] CISPO はなぜ token-level clipping ではなく IS-weight clipping が優位か（理論的根拠）？ → [paper](../wiki/papers/Technical_Report/minimax-m1.md)
- [ ] hybrid attention における lightning / softmax の比率（何層ごと）と、その比率が推論能力・long context にどう効くか？ → [paper](../wiki/papers/Technical_Report/minimax-m1.md)

### Scaling Behaviors of LLM RL Post-Training (Tan et al., 2025) より
- [ ] k(N) saturation の K_max, N_0 はタスク / RLアルゴリズム / 報酬形状でどう変化するか？普遍定数は存在するか？ → [paper](../wiki/papers/RL/rl-scaling-math-qwen25.md)
- [ ] Qwen2.5 以外の系列（MoE / LLaMA / DeepSeek / Kimi）でも同じ power-law + k(N) 飽和式が成立するか？ → [paper](../wiki/papers/RL/rl-scaling-math-qwen25.md)
- [ ] 「最適化ステップ総数 vs サンプルユニーク数」の支配関係は agentic RL でも成立するか？ → [paper](../wiki/papers/RL/rl-scaling-math-qwen25.md)
- [ ] 本論文の power-law と ScaleRL の sigmoid はどの計算量レンジで切り替わるか？ → [paper](../wiki/papers/RL/rl-scaling-math-qwen25.md)
- [ ] k(N) saturation の物理的（アーキテクチャ的）起源は何か？表現容量と報酬信号分布のミスマッチが支配因子か？ → [paper](../wiki/papers/RL/rl-scaling-math-qwen25.md)

### ScaleRL より
- [ ] 「asymptote を動かす設計選択」のリスト化・体系化は可能か？タスク・モデル規模を跨いで一般化するか？ → [paper](../wiki/papers/RL/scale-rl.md)
- [ ] 70B+ の大規模モデルでも sigmoid フィッティングが維持されるか、power law に遷移するか？ → [paper](../wiki/papers/RL/scale-rl.md)
- [ ] 「効率のみ調整する設計選択」は本当に asymptote に影響しないのか、実測計算量が不足しているだけの可能性は？ → [paper](../wiki/papers/RL/scale-rl.md)
- [ ] ScaleRL の外挿能力は agentic RL（環境内行動・長鎖ツール使用）でも成立するか？ → [paper](../wiki/papers/RL/scale-rl.md)
- [ ] rollout/学習ミスマッチ（Flash-RL/TIS）を補正しない場合、ScaleRL の sigmoid漸近値推定はどの程度歪むか？ → [paper](../wiki/papers/RL/scale-rl.md)

### Video models are zero-shot learners より
- [ ] Veo 3 の emergent zero-shot 能力はスケーリング単調比例か、閾値的（phase transition）か？ → [paper](../wiki/papers/Multimodal/video-models-zero-shot-learners.md)
- [ ] 迷路・対称性以外の難視覚推論（多段因果・抽象パターン）もゼロショットで成立するか？ → [paper](../wiki/papers/Multimodal/video-models-zero-shot-learners.md)
- [ ] オープンvideo model（Wan 等）で同様の能力は再現するか？ Veo 3 特有の要因は何か？ → [paper](../wiki/papers/Multimodal/video-models-zero-shot-learners.md)
- [ ] ICLR 2026 Rejection の査読側の具体的な反論は何か（公開コメント確認）？ → [paper](../wiki/papers/Multimodal/video-models-zero-shot-learners.md)

### Attention to Mamba Distillation より
- [ ] 7B+ 以上でも教師性能保持（Δperplexity < 0.5）が維持されるか？ → [paper](../wiki/papers/Architecture/attention-to-mamba-distillation.md)
- [ ] Mamba-2・Mamba-3 等の新世代SSMバリアントへの移植は追加設計なしで可能か？ → [paper](../wiki/papers/Architecture/attention-to-mamba-distillation.md)
- [ ] 二段階蒸留のトークン配分最適解はモデルサイズ依存か、普遍定数か？ → [paper](../wiki/papers/Architecture/attention-to-mamba-distillation.md)
- [ ] long-chain推論・数学・コード等のタスクで純Mamba蒸留モデルの限界はどこに現れるか？ → [paper](../wiki/papers/Architecture/attention-to-mamba-distillation.md)

### LLM-as-a-Verifier より
- [ ] 3軸スケール（granularity × repetition × decomposition）の計算コスト対 downstream 改善曲線は？最適配分は？ → [paper](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md)
- [ ] 同一モデルでのself-verificationと異モデル構成の性能差はどこから生まれるか？ → [paper](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md)
- [ ] 数学・マルチモーダル・長文要約等の非コーディング領域で同じ3軸スケールが成立するか？ → [paper](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md)
- [ ] Terminal-Bench pairwise 78.9% が downstream 86.4% までブーストされる理論的説明は？（BoN bound） → [paper](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md)
- [ ] このフレームワークを RLVR の reward model として訓練時に組み込むと inference-time 利用を超える効果が出るか？ → [paper](../wiki/papers/Agent_ToolUse/llm-as-a-verifier.md)
