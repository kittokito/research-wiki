---
source: src-scaling-laws-motion-forecasting-planning
date_extracted: 2026-04-08
---

# Scaling Laws of Motion Forecasting and Planning からの抽出

## 主要な主張

### スケーリング則の成立
- 動作予測・計画の性能は総計算予算のべき乗関数に従う（LLMと同様のパターン） [source: §Abstract](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 損失関数: `L(N,D) = E + A/N^α + B/D^β`（N=パラメータ数、D=訓練例数） [source: §3](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 計算量に対する損失: `L(C) = aC^b + L∞` のべき乗則改善を確認 [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### 最適資源配分
- `N_opt ∝ C^(0.63±0.08)`（モデルサイズの計算量スケーリング） [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- `D_opt ∝ C^(0.44±0.06)`（データセットサイズの計算量スケーリング） [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 最適モデルサイズは訓練例数の約1.5倍の速さで成長すべき [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 同じ計算予算でのLLMと比較すると、動作予測タスクに必要な最適モデルは約50倍小さい [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### 閉ループ評価でもスケーリング成立（重要知見）
- 閉ループ性能（失敗率η）も事前学習計算量のべき乗則で減少 [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 先行研究では「開ループと閉ループの評価は不整合」とされていたが、本研究では一致を確認 [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 「最小限の帰納バイアスを持つシンプルなアーキテクチャ」がこの結果達成の重要要素と推測 [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### 推論時計算量スケーリング
- 8〜1024軌道をサンプリングして検証（2倍刻み） [source: §6](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 各モデルに推論FLOPsにおいて最適となる固有の範囲が存在 [source: §6](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 小モデル＋多数サンプリングは交差点まで大モデルに匹敵。交差点を超えると大モデルが推論計算効率で優位 [source: §6](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### エージェント間スキル転移
- 非AVエージェント8体で訓練したモデルをAV予測にゼロショット適用 [source: §7](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 「観測10マイル ≈ デモンストレーション2〜3マイル」のデータ等価性 [source: §7](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

## 主要な貢献
- 自動運転の動作予測・計画でLLM型のスケーリング則が成立することを経験的に実証 [source: §1](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 閉ループ評価でもスケーリング成立（先行研究の「開/閉ループ不整合」説に反論） [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 推論時計算量スケーリング（小モデル＋多数サンプリング vs 大モデルのトレードオフ）を定量化 [source: §6](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 一般走行ログからの学習がego-agent性能を改善するクロスエージェント転移を確認 [source: §7](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

## 実験設定
| 項目 | 値 |
|---|---|
| データ規模 | 約50万時間（447K時間、541M訓練例、59.8Mランセグメント、5.6Mマイル） |
| データ品質 | セーフティドライバーのデモのみ（自律走行マイルなし） |
| 入力窓 | 5秒の履歴 → 11秒の将来予測 |
| モデル数 | 84モデル（900K〜118Mパラメータ） |
| 計算量範囲 | 2桁以上 |
| バッチサイズ | 512例（434Kトークン） |
| 最適化 | AdamW + cosineスケジュール（LR peak 2×10⁻⁴ → 2×10⁻⁵） |
| 損失関数 | 離散トークンに対する交差エントロピー |
| アーキテクチャ | 対称型エンコーダ・デコーダTransformer（joint agent-time self-attention） |
| 行動空間 | 離散Verlet-wrapped 2D変位トークン（BEV） |
| デコーダ比率 | 非embedding パラメータの4/7がデコーダ |

## ベンチマーク結果

### 開ループ指標
| 指標 | 説明 |
|---|---|
| minADE | K本の軌道のうちGTに最も近いものの平均変位誤差 |
| wADE | 各軌道クラスタの確率で重みづけした平均変位誤差 |
| minFDE | 最終タイムステップのみのminADE |
| Miss Rate | 時空間許容範囲内の予測割合 |
| mAP | 行動バケット（直進、ターン、Uターン、静止）ごとの平均精度 |

- 64ロールアウト → NMS+K-meansで12代表軌道に集約 [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- minADE、wADEは計算量に対してべき乗則改善 [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### 閉ループ指標
- 30秒間・10Hzのシミュレーションエピソードで評価 [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 失敗条件: (1) 手動運転より大幅に進みすぎ、(2) 大幅に進まなさすぎ、(3) 衝突 [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 行動選択: 128ロールアウトからADE最小化＋進捗バランスで最適行動を選択 [source: §5](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

### エージェントタイプ別の難易度
- AV: 最も容易（最低損失）
- 他車両: より困難
- 歩行者・自転車: さらに困難（異なるべき乗指数） [source: §4](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

## アーキテクチャの特徴（先行研究との違い）
- グローバル座標系エンコーディング（Wayformer/MotionLMのエージェント局所座標系と異なる） [source: §3](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 離散トークン化（連続予測の累積誤差を回避） [source: §3](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- フラット化アテンション（因子分解アテンションではなく単一のjoint agent-timeパス） [source: §3](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)

## 制限・注意点
- スライディングウィンドウによるデータ重複（特徴量の重複） [source: §8](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 知覚インターフェースが限定的（end-to-end visionではない） [source: §8](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 不可逆損失L∞が認識論的限界かアーティファクトか不明 [source: §8](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- べき乗則の厳密な確立にはより多くの桁数にわたる研究が必要 [source: §8](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- ロングテールシナリオの表現がデータ効率に影響 [source: §8](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
- 単一プラットフォームのデータのみ（地理的汎化の検証なし） [source: §8](../../sources/Physical_AI/scaling-laws-motion-forecasting-planning.md)
