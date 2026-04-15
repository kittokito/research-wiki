---
source: src-geometry-of-forgetting
date_extracted: 2026-04-14
---

# The Geometry of Forgetting からの抽出

## 主要な主張
- べき乗則忘却は時間減衰ではなく競合記憶間の干渉から生じる。減衰のみでは b ≈ 0.009（人間値の50分の1）、干渉を加えると b = 0.460 ± 0.183（人間 b ≈ 0.5の範囲内） [source: §Interference](../../sources/Reasoning/geometry-of-forgetting.md)
- 有効次元数（d_eff）が干渉脆弱性を決定する。名目次元数ではない。d = 64で顕著な干渉、d ≥ 128で干渉指数はほぼゼロ、d ≥ 256で0.004未満 [source: §Dimensionality illusion](../../sources/Reasoning/geometry-of-forgetting.md)
- 本番用埋め込みモデルは名目次元に関わらず分散を約16有効次元に集中: MiniLM-L6-v2 (d_nom=384) → d_eff=15.7±0.0、BGE-base (d_nom=768) → d_eff=16.6±0.1、BGE-large (d_nom=1,024) → d_eff=16.3±0.1 [source: §Dimensionality illusion](../../sources/Reasoning/geometry-of-forgetting.md)
- 偽記憶は事前学習済み埋め込み空間のセマンティッククラスタリングから自然に発生する。DRM偽警報率0.583、人間~0.55、パラメータ調整ゼロ [source: §False memories](../../sources/Reasoning/geometry-of-forgetting.md)
- 偽記憶は境界条件を必要としない（raw geometryから出現）。忘却は競合記憶とノイズを必要とする。間隔効果はさらにノイズと間隔パラメータを必要とする。現象ごとに境界条件の厳しさが異なる [source: §Discussion](../../sources/Reasoning/geometry-of-forgetting.md)
- vector averaging fallacy: 近傍埋め込みの平均化（会話履歴の要約等）は角度差を崩壊させ、類似度ベース検索を破壊的に劣化させる [source: §Discussion](../../sources/Reasoning/geometry-of-forgetting.md)

## 主要な貢献
- 高次元埋め込み空間における干渉理論の幾何学的定式化（Ebbinghaus曲線の再現）
- dimensionality illusion の発見: 本番モデルが名目次元数に関わらず~16有効次元で動作
- DRM偽記憶パラダイムのパラメータフリー再現（cosine類似度のみ）
- 間隔効果の幾何学的説明（最新トレースのリセンシー効果、Cohen's d = 13.1）
- TOT現象の質的再現（3.66% vs 人間~1.5%）
- 軽量射影（~10Kパラメータ）によるクロスモーダル検索（探索的）
- 持続的ホモロジーによる記憶多様体のトポロジー構造分析（探索的）

## 制限・注意点
- bAbIタスクでの記憶基盤テスト精度0.475（完全コンテキスト天井には未到達）
- 間隔効果は境界条件依存（特定のノイズ・distractor設定が必要）で、DRMのような完全出現型ではない
- TOT率は人間の~2.4倍で質的一致にとどまる
- クロスモーダル検索は探索的結果であり、忘却・偽記憶の中心主張を直接強化しない
- 持続的ホモロジー結果は記述的であり因果的証拠ではない
- 生物学的神経コードの有効次元数（100-500）との比較は直接的な橋渡しではなくもっともらしさの議論

## ベンチマーク結果
| 指標 | HIDE (モデル) | 人間 | 差異 |
|---|---|---|---|
| 忘却指数 b | 0.460 ± 0.183 | ~0.5 | <15% |
| DRM偽警報率 | 0.583 | ~0.55 | +6% |
| TOT率 | 3.66% | ~1.5% | +144% |
| 間隔効果 (massed retention) | 0.230 | 0.30 | -23% |
| 間隔効果 (long retention) | 0.994 | 0.65 | +53% |

## 実装関連
- 使用モデル: MiniLM-L6-v2、BGE-base、BGE-large、Sentence-Transformers
- ライブラリ: GUDHI（持続的ホモロジー）
- 埋め込み: 64次元の多スケール時間エンコーディング（3正弦波）+ cosine類似度 × 時間減衰
- 全実験でオープンウェイトモデルと公開データセットを使用
