---
title: "Conditional Memory via Scalable Lookup"
aliases: ["Engram", "Conditional Memory"]
created: 2026-04-07
updated: 2026-04-07
tags: [sparsity, MoE, N-gram, embedding, scaling-law, architecture, efficiency]
sources: [src-conditional-memory-scalable-lookup]
---

# Conditional Memory via Scalable Lookup

Cheng, Zeng, Dai et al. (2026) — arXiv 2601.07372

## ソースからの事実
- MoE（条件付き計算）に対する補完的スパース性軸として「条件付きメモリ」を提案。古典的N-gram埋め込みをO(1)ルックアップで近代化した**Engram**モジュールを導入 [source](../../../sources/Architecture/conditional-memory-scalable-lookup.md)
- ニューラル計算と静的メモリの最適配分にU字型スケーリング則を発見（Sparsity Allocation問題） [source](../../../sources/Architecture/conditional-memory-scalable-lookup.md)
- 27BパラメータまでスケールしMMLU +3.4%, BBH +5.0%, Multi-Query NIAH 84.2→97.0%等の改善を達成 [source](../../../sources/Architecture/conditional-memory-scalable-lookup.md)
- メカニスティック分析により、Engramが初期層の静的再構成負荷を軽減し、注意機構の容量をグローバルコンテキストに振り向けることを示した [source](../../../sources/Architecture/conditional-memory-scalable-lookup.md)

→ 詳細な主張・ベンチマーク: [evidence](../../../evidence/Architecture/conditional-memory-scalable-lookup.md)

## 現時点の解釈
MoEが「どのエキスパートを活性化するか」という条件付き計算によるスパース性であるのに対し、Engramは「静的メモリからのO(1)ルックアップ」という異なる軸のスパース性を提供する。この二軸の組み合わせにおけるU字型スケーリング則の発見は、今後のLLMアーキテクチャ設計において計算とメモリの配分を最適化する新たな指針となり得る。

特に長文コンテキスト検索（NIAH）での大幅改善は、ローカル依存関係をルックアップに委譲することで注意機構の負荷を軽減するという仮説を強く支持している。

## 関連ページ
- （MoE関連ページが追加され次第リンク）

## 未解決の問い
- U字型スケーリング則はモデルサイズやドメインによってどう変化するか？
- Engramモジュールはdense modelにも有効か、それともMoEとの組み合わせが前提か？
- 推論時のメモリフットプリントとレイテンシへの影響は実用上許容範囲か？
