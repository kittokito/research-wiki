---
source: src-leworldmodel
date_extracted: 2026-04-23
---

# LeWorldModel (Maes, Le Lidec, Scieur, LeCun, Balestriero, 2026) からの抽出

## 主要な主張
- 既存JEPAは表現崩壊（representation collapse）を避けるために、multi-term loss・EMA・事前学習エンコーダ・補助監督などの複雑な仕組みに依存していて脆弱 [source](../../sources/Physical_AI/leworldmodel.md)
- **LeWorldModel (LeWM)** は raw pixels から **end-to-end で安定学習する最初のJEPA** [source](../../sources/Physical_AI/leworldmodel.md)
- 損失は **2項のみ**: (1) next-embedding prediction loss、(2) 潜在埋め込みをGaussian分布に寄せる正則化 [source](../../sources/Physical_AI/leworldmodel.md)
- 調整対象の損失ハイパラを **既存end-to-end代替の6個から1個に削減** [source](../../sources/Physical_AI/leworldmodel.md)
- **~15Mパラメータ** で単GPU・数時間で学習可能 [source](../../sources/Physical_AI/leworldmodel.md)
- Foundation-model-based world model に対し **最大48倍高速な計画** [source](../../sources/Physical_AI/leworldmodel.md)
- 多様な **2D / 3D 制御タスク** で競争力 [source](../../sources/Physical_AI/leworldmodel.md)
- 潜在空間が **物理量（物理的構造）をprobingで取り出せる形** でエンコード [source](../../sources/Physical_AI/leworldmodel.md)
- **Surprise評価** で物理的に非現実な（implausible）事象を信頼性高く検出 [source](../../sources/Physical_AI/leworldmodel.md)

## 主要な貢献
- JEPAの表現崩壊問題に対するミニマル解（2損失項・1ハイパラ）
- End-to-end JEPA の「fragile さ」を突破する設計原理（Gaussian-distributed latent の正則化）
- 小規模（15M）・単GPU・数時間学習という実用性能プロファイル
- Foundation-model world model に対する計画速度48倍の実証
- 潜在空間が物理量を保持していることの probing ベース検証、surprise評価による実装的実用性

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| パラメータ数 | ~15M | 単GPU・数時間で学習可能 |
| 損失項数 | 2 | next-embedding prediction + Gaussian正則化 |
| 調整ハイパラ数 | 1 | 既存end-to-end代替の6から削減 |
| 計画速度 | foundation world model比 最大48倍 | — |
| 評価領域 | 2D / 3D control tasks | 複数環境 |
| 潜在空間評価 | 物理量 probing / surprise evaluation | 物理的非現実事象の検出 |

## 制限・注意点
- 「最初のstable end-to-end JEPA」はJEPA系列でのクレームで、他流派のworld model（Dreamer系、拡散系）との比較は限定的
- 15M規模での結果が中心で、V-JEPA 2 相当（大規模video + robot trajectory）にスケールした時に同じ安定性が保たれるかは未検証
- 「Gaussian-distributed latent」の正則化がタスク一般で最適かは不明（タスクごとに適切な事前分布が変わる可能性）
- 48倍高速の比較対象（どの foundation-model world model か）と計画設定（horizon, planner）に依存した相対値
- 2D/3D制御での「competitive」の定義・具体benchmark数値は本論文参照（arXiv preprint、未査読）
- v2（2026-03-24）の段階で venue 情報なし。preprint ステータス

## 実装関連
- 2損失項 + 1ハイパラの設計のため、実装再現性が高い
- 15M × 単GPU × 数時間 という profile は、個人研究者・小規模ラボで world model 研究を回す障壁を大きく下げる
- arXiv 2603.19312 / v1: 2026-03-13 / v2: 2026-03-24
