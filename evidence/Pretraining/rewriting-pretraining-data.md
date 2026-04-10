---
source: src-rewriting-pretraining-data
date_extracted: 2026-04-07
---

# Rewriting Pre-Training Data Boosts LLM Performance in Math and Code からの抽出

## 主要な主張
- SwallowCode（約16.1Bトークン）：構文検証・スタイルフィルタリング・LLMベースのリライティングでPythonコードを強化 [source](../../sources/Pretraining/rewriting-pretraining-data.md)
- SwallowMath（約2.3Bトークン）：ボイラープレート除去と解法の再フォーマットで数学コンテンツを改善 [source](../../sources/Pretraining/rewriting-pretraining-data.md)
- 50Bトークン予算内でLlama-3.1-8BのHumanEval pass@1を+17.0改善 [source](../../sources/Pretraining/rewriting-pretraining-data.md)

## 主要な貢献
- SwallowCode/SwallowMathデータセット
- データリライティングによる事前学習データ品質向上手法

## ベンチマーク

| ベンチマーク | スコア | 備考 |
|---|---|---|
| HumanEval pass@1 | +17.0 | Llama-3.1-8B継続事前学習 |

## 制限・注意点
- Llama-3.1-8B固有の実験。他モデルへの汎化は未検証
