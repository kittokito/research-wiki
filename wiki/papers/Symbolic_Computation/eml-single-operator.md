---
title: "All elementary functions from a single binary operator"
aliases: ["EML operator", "EML Sheffer"]
created: 2026-04-14
updated: 2026-04-14
tags: [EML, Sheffer-operator, elementary-functions, symbolic-regression, binary-tree, completeness]
peer_review: preprint
venue: ""
sources: [src-eml-single-operator]
---

# All elementary functions from a single binary operator

> **査読**: 📝 preprint

Odrzywołek (2026) — arXiv 2603.21852 / Jagiellonian University

## ソースからの事実
- 単一の二項演算子 eml(x, y) = exp(x) − ln(y) と定数1で、全初等関数（四則演算、三角・双曲線関数、e, π, i 等の定数を含む36プリミティブ）を生成可能 [source: §Abstract](../../../sources/Symbolic_Computation/eml-single-operator.md)
- デジタル論理のNANDゲートに対応する「連続版Sheffer演算子」の初発見 [source: §1 Introduction](../../../sources/Symbolic_Computation/eml-single-operator.md)
- 全EML式は文脈自由文法 S → 1 | eml(S, S) で生成される二分木。Catalan数や完全二分木と同型 [source: §Summary](../../../sources/Symbolic_Computation/eml-single-operator.md)
- 勾配ベース記号回帰への応用: パラメータ化EMLツリーをAdamで最適化し、深さ2で100%、深さ3-4で~25%の確率で閉じた形の初等関数を数値データから正確に復元 [source: §4.3](../../../sources/Symbolic_Computation/eml-single-operator.md)
- 標準的活性化関数は初等関数であるため、任意の通常NNはEMLツリーアーキテクチャの特殊ケース [source: §5 Conclusions](../../../sources/Symbolic_Computation/eml-single-operator.md)

→ 詳細: [evidence](../../../evidence/Symbolic_Computation/eml-single-operator.md)

## 現時点の解釈
NANDゲートがデジタル回路設計の基盤であるのと同様に、EML演算子は連続関数の計算において「最小限の構成要素」を提供する。理論的には美しいが、実用面での含意は2つの方向に分かれる。

**記号回帰への応用**が最も直接的: 従来の記号回帰（PySR等）は {+, -, ×, /, sin, cos, exp, log, ...} のような異種混合文法を探索するが、EMLは完全かつ一様な探索空間を提供する。master formulaにより「全ての初等関数を含む」ことが設計上保証され、探索空間の不完全性リスクを排除する。ただし深さ5以上でのランダム初期化からの復元率は1%未満であり、実用的なスケーラビリティは未解決。

**NNアーキテクチャとの接点**は示唆的: 標準的活性化関数（ReLU, tanh, sigmoid等）は全て初等関数であるため、既存のNNは全てEMLツリーの特殊ケースとみなせる。EMLツリーで訓練された回路は初等関数式として解読可能であり、従来のNNにはない形の解釈可能性を提供する可能性がある。

## 関連ページ
- [The Lottery Ticket Hypothesis](../Efficiency_Optimization/lottery-ticket-hypothesis.md) — NNの冗長性と最小構造という共通テーマ
- [GSM-Symbolic](../Reasoning/gsm-symbolic.md) — 数学的推論の限界、記号的手法の潜在的価値

## 未解決の問い
- 定数を必要としない二項Sheffer演算子（純粋な2要素系）は存在するか？
- EML記号回帰は深さ5以上で実用的にスケールするか？構造探索との組み合わせは有効か？
- EMLツリーを活性化関数としたNNアーキテクチャは、標準NNと比較して解釈可能性・性能面でどのような特性を示すか？
