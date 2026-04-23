---
source: src-rl-scaling-math-qwen25
date_extracted: 2026-04-22
---

# Scaling Behaviors of LLM RL Post-Training (Tan et al., 2025) からの抽出

## 主要な主張
- 事前学習のスケーリング則は広範に研究されてきたが、RLポストトレーニングでのスケーリング挙動は未探索領域であると問題提起 [source](../../sources/RL/rl-scaling-math-qwen25.md)
- **Qwen2.5 dense シリーズ全系列（0.5B / 1.5B / 3B / 7B / 14B / 32B / 72B）** で、数学推論タスクにおけるRLポストトレーニングを体系的に実験 [source](../../sources/RL/rl-scaling-math-qwen25.md)
- **発見1**: 大きいモデルほど計算・データ両面で一貫して学習効率（learning efficiency）が高い [source](../../sources/RL/rl-scaling-math-qwen25.md)
- **発見2**: test loss と (compute, data) の関係は **log L(N, X) = −k(N)·log X + E(N)** という予測可能な power-law で記述でき、base / instruct 両方に頑健 [source](../../sources/RL/rl-scaling-math-qwen25.md)
- **発見3**: ただし学習効率 k(N) 自体が **k(N) = K_max / (1 + N_0/N)** の形で飽和傾向を示す。モデル規模を大きくしても効率向上はいつか天井に達する（latent saturation）[source](../../sources/RL/rl-scaling-math-qwen25.md)
- **発見4**: データ制約領域では **高品質データの繰り返し再利用** が非常に有効。最終性能は **ユニークサンプル数ではなく総最適化ステップ数** に主に支配される [source](../../sources/RL/rl-scaling-math-qwen25.md)
- RLの計算-性能関係は ScaleRL（sigmoid）に対し、**log-linear power-law** で十分にフィットする（論文の式 (1)）[source](../../sources/RL/rl-scaling-math-qwen25.md)

## 主要な貢献
- RLポストトレーニングの予測可能スケーリング則の定式化（パラメタライズされた学習効率 k(N) を含む）
- k(N) の解析的飽和式（K_max, N_0 の2パラメタ）の提案と実証
- データ制約下でのpolicy: 高品質小規模データ + 繰り返し最適化が広いデータより効果的という知見
- Qwen2.5 0.5B–72B 全系列という前例のないスケール範囲でのablation

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| モデル系列 | Qwen2.5 0.5B–72B | base / instruct 双方 |
| RLアルゴリズム | GRPO | RLVR/数学報酬 |
| In-domain 評価 | 訓練分布からの数学問題 | — |
| OOD 評価 | AIME2024, AMC2023, GSM8K, MATH500, HumanEval, Zebra Puzzle, SuperGPQA | math + code + logic + science |
| フィット形 | log L = −k(N)·log X + E(N) | power-law |
| 学習効率飽和式 | k(N) = K_max / (1 + N_0/N) | saturation curve |

## 制限・注意点
- **タスク特化**: 数学推論に特化。コード / agentic / 汎用reasoning での power-law と k(N) saturation が同じ形をとる保証はない
- **モデル系列依存**: Qwen2.5 dense のみ。Qwen-MoE / LLaMA / DeepSeek 系列で K_max, N_0 がどう変わるかは未検証
- **RLアルゴリズム依存**: GRPO を主に使用。DAPO / GSPO / RS-GRPO 等では係数や k(N) の形が変わる可能性
- **ScaleRLの sigmoid フィットとの整合性**: ScaleRL は計算量広範囲で sigmoid を主張、本論文は power-law を主張。どちらの関数形が「真」かは計算量レンジとタスク依存であり、両者は対立するというより相補的と見るのが妥当
- **「総最適化ステップが支配的」という主張**: データ制約下での観察であり、十分に大きいデータ領域では overfitting / memorization が顕在化する可能性
- **k(N) saturation の外挿**: Qwen2.5 72B までの観察で、100B+ 規模の外挿は理論的裏付けが弱い

## 実装関連
- 数式:
  - power-law: log L(N, X) = −k(N) · log X + E(N)
  - 学習効率飽和: k(N) = K_max / (1 + N_0 / N)
- 実験フレームワーク / ハイパーパラメータの詳細は Appendix A（Prompt Templates, Data Reuse Experiment Setup）, Appendix B（GRPO Hyperparameter Ablation, Advanced Models との比較）, Appendix C（FLOPs 計算方法, 係数比較, hyper-parameter fitting）, Appendix D（Loss Decomposition Model）に収録
- arXiv 2509.25300 / v4 (2026-04-17) — ACL 2026 Main 採択版
