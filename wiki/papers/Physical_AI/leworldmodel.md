---
title: "LeWorldModel (LeWM): Stable End-to-End JEPA from Pixels"
aliases: ["LeWM", "LeWorldModel", "Stable End-to-End JEPA"]
created: 2026-04-23
updated: 2026-04-23
tags: [JEPA, world-model, self-supervised, control, planning, representation-collapse, physical-ai]
peer_review: preprint
venue: ""
sources: [src-leworldmodel]
---

# LeWorldModel: Stable End-to-End JEPA from Pixels

> **査読**: 📝 preprint — arXiv 2603.19312 (v2, 2026-03-24)

Maes, Le Lidec, Scieur, LeCun, Balestriero (2026) — Meta FAIR / LeCun ラボ系

## ソースからの事実
- **raw pixels から end-to-end で安定学習する最初の JEPA** を提案（LeWorldModel / LeWM）[source](../../../sources/Physical_AI/leworldmodel.md)
- 損失項は **2つのみ**: next-embedding prediction loss + Gaussian分布正則化 [source](../../../sources/Physical_AI/leworldmodel.md)
- 調整ハイパラは **1個**（既存 end-to-end JEPA代替の6個から削減）[source](../../../sources/Physical_AI/leworldmodel.md)
- **~15M パラメータ**、**単GPU・数時間** で学習可能 [source](../../../sources/Physical_AI/leworldmodel.md)
- Foundation-model-based world model に対し **最大48倍高速な計画** [source](../../../sources/Physical_AI/leworldmodel.md)
- 多様な2D / 3D制御タスクで競争力、潜在空間が **物理量をprobingで取り出せる形** で構造化、**surprise評価** で物理的非現実事象を検出 [source](../../../sources/Physical_AI/leworldmodel.md)

→ 詳細: [evidence](../../../evidence/Physical_AI/leworldmodel.md)

## 現時点の解釈
JEPAの **「端から端まで pixels で安定に学習できない」** という長年の脆弱性（representation collapse 回避のためにEMA・事前学習エンコーダ・多項損失・補助監督が必要だった）に対し、**Gaussian-distributed latent 正則化のみ** で端から端まで安定させたミニマル解。損失項を6ハイパラ→1ハイパラへ削減したのは工学的インパクトが大きく、**「JEPAは使いこなしが難しいからスケール勝負しかない」** という近年の流れに対して、**小規模・単GPU・数時間** の実用profileで反例を提示した位置付け。

[V-JEPA 2](./v-jepa-2.md) が「大規模video + robot trajectory」でJEPAをスケールアップして汎用性を示したのに対し、LeWMは **底側（設計原理のシンプルさ）** から攻めており、両者は直交する。今後V-JEPA 系列にGaussian正則化が取り込まれる可能性、逆にLeWMをスケールアップして同等の安定性を保てるかが次の論点。

「foundation model 系 world model に対し計画48倍高速」という主張は、推論ループ全体での性能が重要なロボット制御・plan-based agentic設定で実用的意味が大きい。[DreamZero](./dreamzero-world-action-models.md) がvideo diffusionベースのゼロショットworld modelであるのに対し、LeWMは **JEPA 系の効率重視 alternative** であり、ロボット界隈の world model ランドスケープを 「diffusion vs JEPA」「スケール vs 効率」の2軸で整理する材料を提供する。

**ラボや個人研究者がworld modelを現実に触れる閾値を下げた** という意味で、JEPA普及のティッピングポイント候補。ただし現状 preprint、arXiv commentsに会議採択情報もなく、大規模 video / robot trajectory への拡張時に同じ安定性が保たれるかは未検証である点に注意。

## 関連ページ
- [V-JEPA 2](./v-jepa-2.md) — 大規模videoでJEPAをスケール、LeWMは設計原理のミニマル化で直交
- [DreamZero: World Action Models](./dreamzero-world-action-models.md) — video diffusionベースのworld model、LeWMはJEPA系対抗軸
- [Scaling Laws of Motion Forecasting and Planning](./scaling-laws-motion-forecasting-planning.md) — Waymoによる運動予測のスケーリング則、LeWMは小規模効率側

## 未解決の問い
- LeWM の Gaussian-distributed latent 正則化は、V-JEPA 2相当の大規模video + robot trajectoryにスケールしても同じ安定性を維持するか？
- Gaussian事前分布はタスク一般に最適か？コード実行・言語・マルチモーダル等のドメインでは別の latent 分布が適切ではないか？
- 「foundation model 世代 world model に48倍高速」の48という倍率は、planner（MPC / sampling / policy rollout）と horizon の選択にどこまでロバストか？
- 潜在空間の物理量 probing 能力は、LeWM特有か、JEPA系一般の性質か（V-JEPA 2 の潜在空間との比較）？
- 2損失項・1ハイパラのシンプルさを維持したまま、action-conditioned（V-JEPA 2-AC相当）に拡張可能か？
- LeWMは今後 どの venue で採択されるか（NeurIPS 2026 / ICLR 2027 等の候補）？
