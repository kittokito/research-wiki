---
source: src-conditional-memory-scalable-lookup
date_extracted: 2026-04-07
---

# Conditional Memory via Scalable Lookup からの抽出

## 主要な主張
- MoE（条件付き計算）と並ぶ新たなスパース性の軸として「条件付きメモリ」（静的メモリのO(1)ルックアップ）を提案 [source: §1](../../sources/Architecture/conditional-memory-scalable-lookup.md)
- ニューラル計算（MoE）と静的メモリ（Engram）のトレードオフにU字型スケーリング則が存在し、最適なスパース性配分が導出可能 [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)
- Engramモジュールはバックボーンの初期層を静的再構成負荷から解放し、注意機構の容量をグローバルコンテキスト処理に振り向ける [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)
- ローカルな依存関係をルックアップに委譲することで、ネットワークを実質的に深くし複雑な推論性能を向上させる [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)

## 主要な貢献
- **Engramモジュール**: 古典的N-gram埋め込みをO(1)ルックアップ複雑度で近代化した新モジュール [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)
- **Sparsity Allocation問題**: MoEとEngramの最適配分を定式化し、U字型スケーリング則を発見 [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)
- **メカニスティック分析**: Engramが初期層の静的再構成負荷を軽減するメカニズムを解明 [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)

## 制限・注意点
- iso-parameterおよびiso-FLOPsベースラインとの比較のみ。Dense modelとの直接比較の詳細は限定的 [source](../../sources/Architecture/conditional-memory-scalable-lookup.md)

## ベンチマーク結果
| ベンチマーク | 改善幅 | 備考 |
|---|---|---|
| MMLU | +3.4% | 知識検索 |
| CMMLU | +4.0% | 中国語知識検索 |
| BBH | +5.0% | 推論 |
| ARC-Challenge | +3.7% | 推論 |
| HumanEval | +3.0% | コード生成 |
| MATH | +2.4% | 数学 |
| Multi-Query NIAH | 84.2 → 97.0% | 長文コンテキスト検索 |

※ iso-parameter および iso-FLOPs MoEベースラインとの比較

## 実装関連
- Engramモジュール: 27Bパラメータまでスケール
- O(1)ルックアップ複雑度により推論時のオーバーヘッドが小さい
