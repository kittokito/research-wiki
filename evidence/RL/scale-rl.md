---
source: src-scale-rl
date_extracted: 2026-04-21
---

# The Art of Scaling RL Compute for LLMs (ScaleRL) からの抽出

## 主要な主張
- LLM向けRLには、pretrainingで確立された予測可能スケーリング則に匹敵する方法論が存在しなかった [source](../../sources/RL/scale-rl.md)
- 総計 **40万GPU時間以上** を投じた初の大規模体系研究で、RLスケーリングの原理的枠組みを定義 [source](../../sources/RL/scale-rl.md)
- RL訓練の計算-性能曲線を **sigmoid** でフィッティング（pretrainingのpower lawとは異なる形状）[source](../../sources/RL/scale-rl.md)
- **発見1**: 全てのRLレシピが同じ漸近性能に収束するわけではない。レシピ選択は asymptote を動かす [source](../../sources/RL/scale-rl.md)
- **発見2**: loss aggregation、正則化、curriculum、off-policy algorithm などの細部は **計算効率** を調整するだけで、**漸近性能を実質的に変えない** [source](../../sources/RL/scale-rl.md)
- **発見3**: 安定・スケーラブルなレシピは **予測可能な軌道** をたどり、小規模実行から外挿できる [source](../../sources/RL/scale-rl.md)
- ベストプラクティス統合として **ScaleRL** レシピを提案 [source](../../sources/RL/scale-rl.md)
- ScaleRL の有効性を **10万GPU時間規模の単一RLラン** で検証、検証性能を事前予測して的中 [source](../../sources/RL/scale-rl.md)

## 主要な貢献
- RL scaling の科学的枠組み（sigmoid フィッティング + 漸近値 / 効率 の分離分析）
- 実務レシピ ScaleRL（10万GPU時間スケールで予測可能）
- 「設計選択が漸近性能に効くか効率に効くか」を切り分ける ablation 方法論
- pretraining 的な予測可能性を RL 訓練にもたらす基礎

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| 総計算量 | 400,000+ GPU-hours | 体系研究として |
| 単一ラン最大 | 100,000 GPU-hours | ScaleRL の予測外挿検証 |
| 曲線フィット | sigmoid | 計算-性能関係 |
| ablation 軸 | loss aggregation / 正則化 / curriculum / off-policy | 主要設計選択 |

## 制限・注意点
- 「漸近性能」はフィットしたsigmoidの上限で、実測が十分近づいていないレシピの比較は外挿を含む
- どの設計選択が asymptote に効きどれが効率に効くかの境界は、タスク・モデル規模で変動しうる
- 「predictable scaling」はレシピが **安定** である前提。不安定なレシピ（報酬ハッキング・entropy collapse 等）は予測外挿が破綻
- 評価はタスク固有の validation loss 中心で、pass@k や分布外一般化の扱いは別論点（Yue et al. / ProRL の軸とは直交）
- GPU時間ベースのスケーリングは実装効率・rollout/学習のミスマッチ（Flash-RL/TIS で指摘された問題）と絡み、絶対値の移植は要注意

## 実装関連

### ScaleRL レシピの具体構成要素（8要素）
ScaleRLは新規手法の発明ではなく、既存手法の **最適組み合わせ** として定義される。各要素はLOO（leave-one-out）ablation で 16,000 GPU-hours/ランで独立検証済み:

| # | 要素 | 採用した設定 | 競合案と選ばなかった理由 |
|---|---|---|---|
| 1 | **非同期RLセットアップ** | **PipelineRL**（off-policy パラメータ k=8） | ストリーミング方式で on-policy に近い更新が可能。PPO-offpolicy の alternating phase よりも安定 |
| 2 | **生成長制御** | **Forced length interruption**（強制打ち切り） | length penalty に置換しても性能改善なし。打ち切り方式を採用 |
| 3 | **損失タイプ** | **CISPO**（Truncated Importance Sampling loss、[MiniMax-M1](../../wiki/papers/Technical_Report/minimax-m1.md) 由来） | GRPO/DAPO はクリップ比 ε_max に高感度。CISPO / GSPO は robust で、CISPO を ScaleRL で採用 |
| 4 | **損失集約** | **Prompt-level averaging**（DAPO方式） | Sample average（GRPO）/ Token average と比較し、漸近性能で優位 |
| 5 | **アドバンテージ正規化** | **Batch-level**（バッチ全体で標準化） | Prompt-level（GRPO）より漸近性能が高い |
| 6 | **LMヘッド精度** | **FP32 precision at logits** | bf16のままでは漸近性能 A=0.52 → FP32 に変更で A=0.61 へ**劇的改善** |
| 7 | **ゼロ分散フィルタリング** | **Effective batch**（再サンプリング） | 0-variance プロンプトを単にドロップする方式より、再サンプリングで有効バッチを維持する方が漸近性能で優位 |
| 8 | **データカリキュラム** | **No-Positive-Resampling**（pass rate ≥ 0.9 のプロンプトを永久除外） | 「一度簡単になったプロンプトはその後も簡単」という観察に基づく。全プロンプト維持より計算効率で優位 |

### ベース RL アルゴリズム
- GRPO（Shao et al., 2024）類似だが **KL正則化項なし**（MiniMax, Magistral 等の大規模訓練報告に沿う）
- **Asymmetric DAPO clipping** を含める（entropy collapse 回避・出力多様性維持のため広く採用されている）

### 他レシピとの比較（論文 §A.16 より）
| レシピ | 損失 | 集約 | off-policy | LMヘッド精度 | ScaleRL との差分 |
|---|---|---|---|---|---|
| **ScaleRL** | CISPO | Prompt avg | PipelineRL (k=8) | FP32 | — |
| DeepSeek (GRPO) | GRPO (ε=0.2) | Sample avg | PPO-off-8 | — | 6k GPU-hours 後に truncation で不安定化 |
| Qwen2.5 (DAPO) | DAPO (ε_max=0.26) | Prompt avg | PPO-off-8 | — | 損失・off-policy |
| Magistral | DAPO様 | Prompt avg | PipelineRL | — | 損失 |
| MiniMax | CISPO | Prompt avg | PPO-off | FP32 | off-policy（PipelineRL でない） |

### 実運用の中核
- 小規模ラン（数千GPU時間）から大規模ラン（10万GPU時間）への **予測外挿ワークフロー**
- Truncation rate の継続監視（>10–15% で不安定化のwarning signal。ScaleRL 8Bモデルでは全訓練の90%超で <5%、Scout（MoE）では >90% のステップで <1%）
- 複数軸（batch size 2.5×、context 32,768 tokens、multi-task RL、モデルサイズ）での predictable scaling を確認
- コード: [www.devvrit.com/scalerl_curve_fitting](https://www.devvrit.com/scalerl_curve_fitting)（scaling curve fitting minimal code repo）
- OpenReview FMjeC9Msws / arXiv 2510.13786
