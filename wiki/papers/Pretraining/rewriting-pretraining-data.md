---
title: "Rewriting Pre-Training Data Boosts LLM Performance in Math and Code"
aliases: ["SwallowCode", "SwallowMath"]
created: 2026-04-07
updated: 2026-04-07
tags: [pretraining-data, data-quality, code, math]
sources: [src-rewriting-pretraining-data]
---

# Rewriting Pre-Training Data Boosts LLM Performance in Math and Code

Fujii, Tajima, Mizuki et al. (2025) — arXiv 2505.02881

## ソースからの事実
- SwallowCode（~16.1Bトークン）でPythonコードを強化、SwallowMath（~2.3Bトークン）で数学コンテンツを改善 [source](../../../sources/Pretraining/rewriting-pretraining-data.md)
- 50Bトークン予算内でLlama-3.1-8BのHumanEval pass@1を+17.0改善 [source](../../../sources/Pretraining/rewriting-pretraining-data.md)

→ 詳細: [evidence](../../../evidence/Pretraining/rewriting-pretraining-data.md)

## 現時点の解釈
データ品質向上がモデルサイズ拡大と同等以上の効果を持ちうることを示す重要な実証。日本のチーム（Swallowプロジェクト）による貢献。

## 関連ページ
- [HuggingFace FineData](../../papers/Pretraining/huggingface-finedata.md)

## 未解決の問い
- リライティングのコスト対効果は？
- 他の言語・ドメインへの適用は？
