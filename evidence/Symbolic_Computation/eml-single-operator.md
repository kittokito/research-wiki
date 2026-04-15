---
source: src-eml-single-operator
date_extracted: 2026-04-14
---

# All elementary functions from a single binary operator からの抽出

## 主要な主張
- 二項演算子 eml(x, y) = exp(x) − ln(y) と定数1のみで、全ての標準的初等関数を構成的に生成できる（連続版NANDゲート） [source: §Abstract](../../sources/Symbolic_Computation/eml-single-operator.md)
- 例: e^x = eml(x, 1)、ln x = eml(1, eml(eml(1, x), 1))。EML式の深さは指数関数が1（最浅）、乗算が8 [source: §3 Results](../../sources/Symbolic_Computation/eml-single-operator.md)
- 36プリミティブ（定数8、関数20、演算8）からの系統的ablationで、最終的に{1, eml}の3要素（定数1 + 二項演算子eml + 入力変数）まで削減 [source: §2 Methods](../../sources/Symbolic_Computation/eml-single-operator.md)
- EMLは唯一ではない。少なくとも EDL: exp(x)/ln(y)（定数e）、-EML: ln(x)−exp(y)（定数-∞）が同等の性質を持つ [source: §3 Results](../../sources/Symbolic_Computation/eml-single-operator.md)
- 定数を必要としない二項Sheffer演算子（2要素系）の存在は未解決問題 [source: §5 Conclusions](../../sources/Symbolic_Computation/eml-single-operator.md)

## 主要な貢献
- 連続数学における初のSheffer型演算子の発見と構成的証明
- EML形式による初等関数の一様な二分木表現（文脈自由文法 S → 1 | eml(S, S)）
- EMLコンパイラ（Python）: 任意の初等関数式をEML形式に変換
- 勾配ベース記号回帰の実証: パラメータ化EMLツリー（master formula）をAdamで最適化し、閉じた形の初等関数を数値データから復元
- EML回路記号の提案（NANDゲート・オペアンプ・トランジスタに並ぶアナログ回路要素として）

## 制限・注意点
- EML表現は冗長: 乗算のRPNコード長は17（直接探索）、EMLコンパイラ経由では41。実用的な計算効率は標準表現に劣る [source: §Table 4](../../sources/Symbolic_Computation/eml-single-operator.md)
- 三角関数等の計算は内部的に複素数演算を必要とする（Euler公式経由）。IEEE754浮動小数点環境では ln 0 = -∞、e^(-∞) = 0 等の拡張実数に依存 [source: §4.1](../../sources/Symbolic_Computation/eml-single-operator.md)
- 記号回帰の復元率: 深さ2で100%、深さ3-4で約25%、深さ5で1%未満。ランダム初期化からの復元は深さが増すと急速に困難に [source: §4.3](../../sources/Symbolic_Computation/eml-single-operator.md)
- 正しいEMLツリーの重みにガウスノイズを加えた場合、深さ5-6で100%復元（正しい構造からの局所収束は可能） [source: §4.3](../../sources/Symbolic_Computation/eml-single-operator.md)
- Python/Julia/数値Mathematicaでは inf や signed zero のエッジケース処理が必要 [source: §4.1](../../sources/Symbolic_Computation/eml-single-operator.md)

## ベンチマーク結果
| 関数 | EMLコンパイラ (K) | 直接探索 (K) |
|---|---|---|
| e^x | 3 | 3 |
| ln x | 7 | 7 |
| x + y | 27 | 19 |
| x × y | 41 | 17 |
| x^y | 49 | 25 |
| π | 193 | >53 |
| √x | 139 | 43 |

※ K = RPN (逆ポーランド記法) コード長

## 実装関連
- EMLコンパイラ: Python実装（GitHub/Zenodo公開）
- VerifyBaseSet: Mathematica + Rust実装、数値クロスバリデーション（C, NumPy, PyTorch, mpmath）
- 記号回帰: PyTorch (torch.complex128)、Adamオプティマイザ、simplex再パラメータ化
- Master formula: 深さnのEMLツリーで 5×2^n − 6 パラメータ
