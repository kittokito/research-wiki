---
source: src-learning-fast-and-slow
date_extracted: 2026-05-19
---

# Learning, Fast and Slow: Towards LLMs That Adapt Continually からの抽出

## 主要な主張
- **パラメータ更新（slow）と context-in-learning（fast）の二項対立は false dichotomy**、両者を interleave する Fast-Slow Training (FST) でジレンマを解消できる [source](../../sources/RL/learning-fast-and-slow.md)
- **Slow weights θ = model parameters**、**fast weights Φ = discrete textual prompts**として明示分離、Φ は単一ベストではなく **per-instance Pareto frontier の population** として保持 [source](../../sources/RL/learning-fast-and-slow.md)
- **T=6 RL ステップごとに GEPA が K={4,8} 候補プロンプトを生成**し Pareto frontier を更新、次の T RL 更新をその frontier で conditioning する two-loop interleave [source](../../sources/RL/learning-fast-and-slow.md)
- RL 単独比 **最大3倍のサンプル効率**（CodeIO/HoVer-hard で 3.0×、Math で 1.4× の最適化ステップ削減）、**asymptote 自体も RL を上回る**（CodeIO 47.4% vs 43.0% / HoVer-hard 25.0% vs 17.3% / Math 49.2% vs 46.4%） [source](../../sources/RL/learning-fast-and-slow.md)
- **KL(π_train ∥ π_base) を最大70%削減**（matched reward で）——ベースモデルからの drift が少なく、catastrophic forgetting を抑制 [source](../../sources/RL/learning-fast-and-slow.md)
- 継続学習設定（600ステップ × 3 sequential tasks）で **RL は CodeIO に stall（20.7%）するが FST は near-peak（37.7%）に到達**、後続 Physics タスクでも部分回復のみの RL に対し FST は near-peak 適応 [source](../../sources/RL/learning-fast-and-slow.md)
- Drift 抑制は plasticity 保持に直結——「ベースから離れすぎないことで、次タスクへの適応余地が残る」 [source](../../sources/RL/learning-fast-and-slow.md)

## 主要な貢献
- **fast/slow weight 二項分離の post-training 文脈での明示的定式化**：parameter (slow) と prompt (fast) を独立に最適化し、後者を per-instance population として維持
- **GEPA を frozen checkpoint への post-hoc 適用から、RL ループ内に embed する hybrid optimization へ拡張**——前作 GEPA（Agrawal et al.）の運用形態を質的に変える
- **継続学習（catastrophic forgetting + plasticity loss）と RL post-training の交点を実証的に攻略**——drift 抑制と sample efficiency の同時改善を達成
- **GRPO + CISPO loss（MiniMax-M1 由来）を slow side のベースラインに採用**、CISPO 系の hybrid 設計への展開を示す
- **Star-graph synthetic zero-reward exploration task** を含む、reward signal が疎な状況での hybrid 探索性能を分離評価

## 制限・注意点
- Reflection LM として **GPT-5.2（frozen）** に依存——本手法の効率向上の一部は外部 LLM の能力に由来する可能性
- GEPA の textual mutation コストは論文の sample efficiency 計算でどう扱われているか要確認（"3× サンプル効率" は RL step 単位、reflection LM 推論コストを含むか不明）
- 評価ベンチマークは CodeIO / Polaris (Math) / HoVer-hard / Physics / Star-graph に限定、大規模 reasoning（AIME / SWE-Bench）への外挿は未実証
- T=6, K={4,8}, G=8 のハイパラ感度分析が本論文範囲で十分か不明
- **査読: preprint**（採択先記載なし、29ページ・14図、blog reference あり）

## ベンチマーク結果

### サンプル効率と asymptote（RL 単独 vs FST）

| ベンチマーク | RL asymptote | FST asymptote | 効率比 |
|---|---|---|---|
| CodeIO | 43.0% | **47.4%** | 3.0× |
| Math (Polaris) | 46.4% | **49.2%** | 1.4× |
| HoVer-hard | 17.3% | **25.0%** | 3.0× |
| Physics | (cross-domain 評価) | — | — |
| Star-graph | (zero-reward exploration) | — | — |

### KL drift（基盤モデルからの divergence）

| 条件 | KL(π_train ∥ π_base) |
|---|---|
| RL（matched reward） | baseline |
| **FST（matched reward）** | **−70%** |

### 継続学習（600ステップ × 3 sequential tasks）

| 訓練順序 | RL 到達精度 | FST 到達精度 |
|---|---|---|
| HoVer-hard（step 1-200） | near-peak | near-peak |
| **CodeIO（step 201-400）** | **stall 20.7%** | **near-peak 37.7%** |
| Physics（step 401-600） | partial recovery | near-peak |

## 実装関連
- 公式ブログ: [gepa-ai.github.io/gepa/blog/2026/05/11/learning-fast-and-slow/](https://gepa-ai.github.io/gepa/blog/2026/05/11/learning-fast-and-slow/)
- コード: [rishabhtiwari.ai/projects/fst/code/](https://rishabhtiwari.ai/projects/fst/code/)
- 動画: [rishabhtiwari.ai/projects/fst/video.mp4](https://rishabhtiwari.ai/projects/fst/video.mp4)
- **Slow side**: GRPO + CISPO loss、group size G=8 rollouts/problem
- **Fast side**: GEPA (Reflective Prompt Evolution)、reflection LM = **GPT-5.2 (frozen)**、per-instance Pareto frontier、K={4, 8} candidates
- **Interleave**: 6 RL steps → 1 GEPA cycle → conditioning for next 6 RL steps
- **Drift metric**: `KL(π_train ∥ π_base)`、held-out validation prompts での token-level divergence
