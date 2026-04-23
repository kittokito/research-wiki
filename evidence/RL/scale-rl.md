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
- ScaleRL レシピの具体構成要素（loss aggregation/正則化/curriculum/off-policy choice）の推奨設定が論文本体に詳細記載
- 小規模ラン（数千GPU時間）から大規模ラン（10万GPU時間）への予測外挿ワークフローが実務の中核
- OpenReview FMjeC9Msws / arXiv 2510.13786
