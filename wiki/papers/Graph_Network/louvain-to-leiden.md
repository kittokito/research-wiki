---
title: "From Louvain to Leiden: guaranteeing well-connected communities"
aliases: ["Leiden algorithm", "ライデン法"]
created: 2026-04-10
updated: 2026-04-10
tags: [community-detection, graph-algorithm, Leiden, Louvain, modularity]
peer_review: accepted
venue: "Scientific Reports 2019"
sources: [src-louvain-to-leiden]
---

# From Louvain to Leiden: guaranteeing well-connected communities

> **査読**: ✅ accepted — Scientific Reports 2019

Traag, Waltman & van Eck (2019) — Scientific Reports 9, 5233 / arXiv 1810.08473

## ソースからの事実

- ルーヴァン法は最大25%のコミュニティが疎結合、16%が完全非連結になりうる [source](../../../sources/Graph_Network/louvain-to-leiden.md)
- ライデン法は連結コミュニティを保証し、反復適用で局所最適に収束 [source](../../../sources/Graph_Network/louvain-to-leiden.md)
- ルーヴァン法より高速かつ高品質なパーティションを生成 [source](../../../sources/Graph_Network/louvain-to-leiden.md)

### ルーヴァン法 vs ライデン法

| 側面 | ルーヴァン法 | ライデン法 |
|---|---|---|
| ノード走査 | 全ノードを毎回なめる | キュー管理で影響を受ける隣接ノードのみ再点検 |
| 精製 | なし | 親コミュニティ内で密結合部分を再グループ化 |
| 集約単位 | 移動フェーズの結果（親） | 精製結果の密結合部分（子） |
| 品質保証 | なし（非連結コミュニティが発生しうる） | 連結性を保証 |
| 速度 | 遅い（不要な再計算） | 速い（キュー管理で無駄を排除） |

### ライデン法の2つの核心

**高速化 — 隣接ノードキュー管理**: ノードが移動した際、影響を受けるのは隣接ノードだけ。移動が発生した周辺だけをキューに入れて再点検することで、無駄な計算を劇的に削減する。

**高品質化 — 精製（Refinement）**: 移動フェーズ後の「親」コミュニティの中で、ノードをシングルトンに戻し枠内で再グループ化する。「少しでも得なら統合」ではなく十分な接続密度を要求し、さらに確率的に移動先を選択することで局所最適への陥穽を回避。集約は密結合の「子」単位で行うため、不自然な結合が排除される。

→ 詳細: [evidence](../../../evidence/Graph_Network/louvain-to-leiden.md)

## 現時点の解釈

ライデン法はルーヴァン法の「速いが雑」な問題を、キュー管理（速度）と精製ステップ（品質）の2つの工夫で同時に解決した。精製は実装に自由度があり、接続密度の閾値や確率的選択の設計によってコミュニティ分割に望ましい性質を持たせられる。ルーヴァン法が非連結コミュニティを生む根本原因は、移動フェーズの結果をそのまま集約に使うことにあり、ライデン法の「検品してから集約」というアプローチがこれを構造的に防ぐ。

## 関連ページ
- [Flash-KMeans](../Efficiency_Optimization/flash-kmeans.md) — グラフアルゴリズムの高速化という共通テーマ

## 未解決の問い
- 精製ステップで孤立ノード（どのサブコミュニティにも属さない）が発生した場合の挙動の詳細は？
- 解像度パラメータの選択指針（resolution limit問題への対処）はどの程度確立されているか？
