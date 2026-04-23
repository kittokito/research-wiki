---
source: src-reasoning-with-sampling
date_extracted: 2026-04-16
---

# Reasoning with Sampling からの抽出

## 主要な主張
- べき分布（p^α）からのサンプリングにより、追加学習なしでベースモデルから高精度な推論を引き出せる [source](../../sources/Inference_Decoding/reasoning-with-sampling.md)
- 自己回帰MCMCでトークン部分列を反復的に再サンプリングすることで、べき分布を近似 [source](../../sources/Inference_Decoding/reasoning-with-sampling.md)
- RLポストトレーニングと異なりサンプル多様性を維持し、pass@kでも優れた性能 [source](../../sources/Inference_Decoding/reasoning-with-sampling.md)

## 主要な貢献
- 訓練不要・検証器不要の推論時サンプリングによるreasoning改善手法
- MATH500でGRPO相当、HumanEval・AlpacaEval 2.0ではGRPOを上回るOOD性能
- pass@kでもRL訓練モデルを上回る多様性保持

## 制限・注意点
- 推論時の計算コストが高い（反復MCMCサンプリング）
- サンプリングステップ数とα値のチューニングが必要
