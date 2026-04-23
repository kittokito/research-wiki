---
title: "Scaling Laws of Motion Forecasting and Planning"
aliases: []
created: 2026-04-08
updated: 2026-04-08
tags: [scaling-law, autonomous-driving, motion-forecasting, planning, transformer, closed-loop]
peer_review: n/a
venue: ""
sources: [src-scaling-laws-motion-forecasting-planning]
---

# Scaling Laws of Motion Forecasting and Planning

> **査読**: — n/a（テクニカルレポート）

自動運転の動作予測・計画タスクでのスケーリング則を50万時間の走行データ・84モデルで実証。LLMと同様のべき乗則が成立し、閉ループ評価でもスケーリングが機能することを示した。Waymo研究チーム。

→ 詳細: [evidence](../../../evidence/Physical_AI/scaling-laws-motion-forecasting-planning.md)

## ソースからの事実

### スケーリング則
- 性能は総計算予算のべき乗関数: `L(N,D) = E + A/N^α + B/D^β` [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 最適モデルサイズ `N_opt ∝ C^0.63`、データサイズ `D_opt ∝ C^0.44` — モデルはデータの約1.5倍速く成長すべき [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 同じ計算予算でLLMの約50倍小さいモデルが最適（走行データの分布特性による） [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### 閉ループでのスケーリング成立（最重要知見）
- 閉ループ失敗率もべき乗則で減少 — 先行研究の「開/閉ループ不整合」説に反論 [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 「最小限の帰納バイアスを持つシンプルなアーキテクチャ」が鍵と推測 [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### 推論時計算量スケーリング
- 小モデル＋多数サンプリングは交差点まで大モデルに匹敵 [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 交差点を超えると大モデルが推論計算効率で優位 [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### クロスエージェント転移
- 非AVエージェントで訓練→AV予測にゼロショット適用。「観測10マイル ≈ デモ2〜3マイル」 [source](../../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

## 現時点の解釈

LLMのスケーリング則が自動運転の動作予測・計画にもそのまま成立することを大規模に実証した重要な研究。特に閉ループ評価でもスケーリングが機能する点は、自動運転研究のコミュニティで「開ループメトリクスは実走行と相関しない」という通説に対する反論として意義が大きい。

実務的含意として:
- **計算予算→性能が予測可能**: リソース計画が立てやすくなる
- **モデルはデータより速く大きくすべき**: Chinchilla則（LLMではデータ重視）と異なる傾向
- **LLM比50倍小さいモデルが最適**: 走行データの分布がLLMのテキストより構造化されていることを示唆
- **推論時スケーリング**: 小モデル＋サンプリングという実用的な戦略が有効範囲内では成立

制限として、知覚はend-to-endではなく特徴量入力であり、単一プラットフォーム（Waymo）のデータのみ。

## 関連ページ
- [DreamZero](dreamzero-world-action-models.md) — ロボティクスにおけるスケーリング（ビデオ拡散経由）
- [V-JEPA 2](v-jepa-2.md) — 自己教師あり動画モデルのロボット応用

## 未解決の問い
- 閉ループでのスケーリング成立は他のアーキテクチャ（因子分解アテンション等）でも再現するか？
- end-to-end vision入力にした場合もスケーリング則の形は維持されるか？
- Waymo以外のプラットフォーム・地理でもスケーリング指数は一致するか？
