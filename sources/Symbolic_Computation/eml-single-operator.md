---
id: src-eml-single-operator
title: "All elementary functions from a single binary operator"
authors: ["Andrzej Odrzywołek"]
year: 2026
url: "https://arxiv.org/abs/2603.21852"
type: paper
tags: [EML, Sheffer-operator, elementary-functions, symbolic-regression, binary-tree, NAND-analog, completeness]
date_added: 2026-04-14
status: processed
---

# All elementary functions from a single binary operator

## 概要
デジタル論理におけるNANDゲートの連続版として、単一の二項演算子 eml(x, y) = exp(x) − ln(y) と定数1だけで、関数電卓の全機能（四則演算、べき乗、三角関数、双曲線関数、逆関数、定数 e, π, i を含む全36プリミティブ）を生成できることを示す。EML形式では全ての初等関数式が同一ノードの二分木になり、文脈自由文法 S → 1 | eml(S, S) で表現される。この一様な構造を利用し、パラメータ化されたEMLツリーを勾配法（Adam）で最適化する記号回帰を実証。深さ4までのツリーで閉じた形の初等関数を数値データから正確に復元。

## メモ
- cs.SC (Symbolic Computation), cs.LG。Jagiellonian University（ポーランド・クラクフ）理論物理学研究所。
- 2026年3月公開、4月改訂（v2）。
- 網羅的探索 + VerifyBaseSetによる検証（Mathematica + Rust実装）。
- EML以外にも EDL (exp(x)/ln(y), 定数e) や -EML (ln(x)-exp(y), 定数-∞) など近縁演算子を発見。
- コード・データは Zenodo (DOI: 10.5281/zenodo.19183008) で公開。
