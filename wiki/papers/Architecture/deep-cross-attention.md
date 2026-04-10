---
title: "DeepCrossAttention: Supercharging Transformer Residual Connections"
aliases: ["DCA", "DeepCrossAttention", "GRN"]
created: 2026-04-07
updated: 2026-04-07
tags: [residual-connection, transformer, attention, architecture, training-efficiency]
sources: [src-deep-cross-attention]
---

# DeepCrossAttention: Supercharging Transformer Residual Connections

Heddes, Javanmard, Axiotis, Fu, Bateni, Mirrokni (2025) — arXiv 2502.06785

## ソースからの事実
- 標準的な残差接続は全層出力を均等加算するため深い層で情報が希薄化するという問題を指摘し、**入力依存の学習可能重み**で各層出力を動的に結合するDeepCrossAttention（DCA）を提案 [source](../../../sources/Architecture/deep-cross-attention.md)
- GRNの3バリアント（v1: 次元非依存, v2: 次元依存, v3: 入力依存）を設計し、DCAではGRN-v3を3インスタンス（Q, K, V）使用して深さ方向のクロスアテンションを実現。パラメータ増加はほぼゼロ [source: §3](../../../sources/Architecture/deep-cross-attention.md)
- 6層LM1Bで既存手法（DenseFormer 18.80, Hyper-Connections 18.65）を大幅に上回るperplexity 18.06を達成。同品質を**最大3倍高速**に達成可能 [source](../../../sources/Architecture/deep-cross-attention.md)
- 理論的にも集合的ランクと次元の比が臨界値以下のとき、テスト誤差-モデル複雑度トレードオフの改善を証明（Theorem 4.3） [source: §4](../../../sources/Architecture/deep-cross-attention.md)

→ 詳細な主張・ベンチマーク: [evidence](../../../evidence/Architecture/deep-cross-attention.md)

## 現時点の解釈
DCAは「残差接続の改良」という比較的シンプルな変更で、DenseFormerやHyper-Connectionsといった先行手法を明確に上回る性能を示している。特に、層出力のスタックに対して入力依存の重み付けを行うアプローチは、深さ方向の情報フローを最適化する上で直感的かつ効果的。

ただし、**幅が大きいモデルほど改善幅が縮小する**（幅64で-2.82 → 幅1024で-0.39）という結果は重要な制約。大規模モデル（数十〜数百B）では残差接続の情報希薄化がそもそも問題になりにくい可能性があり、DCAの恩恵は主に中小規模モデルや深いが狭いアーキテクチャに集中する可能性がある。

処理速度のオーバーヘッド（8.14→5.62 batch/s）も実用上の考慮点。学習効率の改善（3倍高速）がこれを補うかはユースケース次第。

## 関連ページ
- [Conditional Memory via Scalable Lookup](conditional-memory-scalable-lookup.md) — 同じArchitectureカテゴリの残差・層間情報伝達に関する研究

## 未解決の問い
- 大規模モデル（数十B以上）での改善幅は実用的に有意か？
- DCAとMoEの組み合わせは有効か？層間の動的結合とエキスパート選択の相互作用は？
- メモリ効率化のlast-k戦略において、最適なkの選び方は？
