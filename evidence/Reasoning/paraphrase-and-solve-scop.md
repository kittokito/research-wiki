---
source: src-paraphrase-and-solve-scop
date_extracted: 2026-06-09
---

# Paraphrase and Solve (SCoP) からの抽出

## 主要な主張
- 数学問題の**表層形(surface form)のわずかな変更**が、答えの分布と solve rate を**大きく変える** [source](../../sources/Reasoning/paraphrase-and-solve-scop.md)
- これは LLM が複雑な問題の推論において表層形に**敏感で頑健性を欠く**ことを露呈する [source](../../sources/Reasoning/paraphrase-and-solve-scop.md)
- 改善策 **Self-Consistency-over-Paraphrases (SCoP)**: 問題の特定表層形から推論経路を**多様化(paraphrase)**して self-consistency を取る [source](../../sources/Reasoning/paraphrase-and-solve-scop.md)

## 主要な貢献
- 表層形が数学推論の可解性に与える影響の体系的調査
- SCoP の提案——4つの数学推論ベンチ×3 LLM で vanilla self-consistency を上回り、**特に当初「解けない」とされた問題で改善** [source](../../sources/Reasoning/paraphrase-and-solve-scop.md)
- 問題難易度と表層形に関する追加分析: cross-model difficulty agreement、paraphrasing transferability、評価のための **Variance of Variations (VOV)** [source](../../sources/Reasoning/paraphrase-and-solve-scop.md)

## 制限・注意点
- SCoP は推論時の緩和策であり、表層形脆弱性の**根本原因**を除去するものではない
- paraphrase 生成の質に依存

## ベンチマーク結果
| 設定 | 結果 |
|---|---|
| 4数学ベンチ × 3 LLM | SCoP が vanilla self-consistency を上回る（特に初期に unsolvable とされた問題） |

## 実装関連
- 同一問題の複数言い換えから推論経路を多様化し多数決を取る（self-consistency の拡張）
