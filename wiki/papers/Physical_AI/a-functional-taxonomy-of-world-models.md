---
title: "A Functional Taxonomy of World Models"
aliases: ["A Functional Taxonomy of World Models", "world model taxonomy", "renderer simulator planner"]
created: 2026-06-09
updated: 2026-06-09
tags: [world-model, spatial-intelligence, renderer, simulator, planner, POMDP, JEPA, taxonomy]
peer_review: n/a
venue: ""
sources: [src-a-functional-taxonomy-of-world-models]
---

# A Functional Taxonomy of World Models

> **査読**: — n/a（Substack 論説エッセイ）

Fei-Fei Li (2026) — World Labs / Stanford / Substack（2026-06-03）

## ソースからの事実
- 「world model」を **機能で3分類**: **renderer**（ピクセル観測を出力、visual fidelity 最優先）/ **simulator**（幾何・物理・動力学的に忠実な表現を出力）/ **planner**（観測＋目標→action、renderer の逆関数） [source](../../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- 3機能は **POMDP 由来の agent loop** に位置づく。**state（世界の完全記述）** と **observation（部分的知覚）** を区別 [source](../../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- 言語モデル＝テキストの統計的構造、world model＝**空間と時間の統計的構造**。言語は抽象化、ピクセルは投影、**geometry/physics/dynamics は世界そのもの** [source](../../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- 評価指標の対応: **visual quality → renderer / forward-prediction fidelity → simulator / decision performance → planner** [source](../../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- **simulation is the bridge**（成熟した renderer と黎明期の planner を simulator が橋渡し）、終着点は **unified world model** [source](../../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)

→ 詳細: [evidence](../../../evidence/Physical_AI/a-functional-taxonomy-of-world-models.md)

## 現時点の解釈

本リポジトリの Physical_AI クラスタを **「どの機能を担う world model か」** で読み直す座標系を与えるエッセイ。実証研究ではなく概念整理だが、乱立する「world model」を renderer / simulator / planner に切り分ける軸は、既存ページの位置づけを明快にする:

- **planner 寄り**: [V-JEPA 2](v-jepa-2.md) は "Understanding, Prediction and **Planning**"、[DreamZero](dreamzero-world-action-models.md) は video 生成（renderer 的）を**ゼロショット policy（planner）**に転用する例。本 taxonomy の「planner は renderer の逆関数」「simulation is the bridge」という主張の具体例として読める。
- **simulator/表現学習の基盤**: [LeWorldModel](leworldmodel.md) や [V-JEPA 2](v-jepa-2.md) の **JEPA（latent prediction）** は「ピクセル再構成（renderer）を捨て、潜在空間で前方予測する」設計で、本記事の「pixels は投影に過ぎず、geometry/physics/dynamics こそ世界」という立場と整合。JEPA 系の源流である [data2vec](../Pretraining/data2vec.md) / [Learn from your own latents](../Pretraining/latent-sample-complexity.md)（token でなく latent を予測する方がサンプル効率的）とも接続。
- **scaling の射程**: [Scaling Laws of Motion Forecasting and Planning](scaling-laws-motion-forecasting-planning.md) は planner 機能（自動運転の予測・計画）に LLM 型スケーリング則が及ぶことを示し、本記事の「unified world model へ収束」という展望に定量的根拠を添える。

「言語モデル vs world model」という対比は、本リポジトリの [言語構造の獲得理論](../Pretraining/language-structure-acquisition.md) 系（言語の統計的・階層的構造の学習理論）の **空間・時間版**を要求するもの、とも位置づけられる。

未解決課題（3D/ロボットデータの不足、sim-to-real、生成モデルの幾何的矛盾）は、現状の world model 研究が renderer に偏り simulator/planner が未成熟、という現実の裏返し。

## 関連ページ
- [V-JEPA 2](v-jepa-2.md) — JEPA による理解・予測・計画。planner 機能の実体
- [LeWorldModel (LeWM)](leworldmodel.md) — raw pixels から end-to-end の JEPA world model
- [DreamZero](dreamzero-world-action-models.md) — video 生成（renderer）→ゼロショット policy（planner）
- [Scaling Laws of Motion Forecasting and Planning](scaling-laws-motion-forecasting-planning.md) — planner 機能のスケーリング則
- [data2vec](../Pretraining/data2vec.md) — latent 予測（JEPA 系設計）の起点

## 未解決の問い
- renderer / simulator / planner は本当に **単一の unified world model** に収束するか、それとも機能ごとに別アーキテクチャが残るか？
- 「simulation is the bridge」は実証可能か——simulator の前方予測忠実度の向上が、planner の意思決定性能にどれだけ転移するか？
- 言語モデルの統計的・階層的構造の理論（[言語構造の獲得理論](../Pretraining/language-structure-acquisition.md)）に対応する「空間・時間の構造獲得理論」は構築できるか？
