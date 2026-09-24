---
source: src-a-functional-taxonomy-of-world-models
date_extracted: 2026-06-09
---

# A Functional Taxonomy of World Models からの抽出

## 主要な主張
- 「world model」と呼ばれる系は単一ではなく、**3つの機能**に分解できる: **renderer / simulator / planner** [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
  - **Renderer**: ピクセル形式の観測を出力。最優先は **visual fidelity（視覚的忠実性）**。テキストから映像を生成する video model が典型 [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
  - **Simulator**: **幾何（geometrically）・物理（physically）・動力学（dynamically）的に忠実な表現**を出力。建築家・設計者・RL エージェント・ロボットコントローラが利用者 [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
  - **Planner**: 観測と目標から適切な **action** を決定。**renderer の逆関数**として機能 [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- これらは **POMDP 由来の古典的 agent loop** に位置づく。**state（世界の完全記述）** と **observation（エージェントが直接知覚する部分情報）** を区別する [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- 言語モデルがテキストの統計的構造を学ぶのに対し、world model は **空間と時間の統計的構造**を学ぶ。言語は世界の抽象化、ピクセルは投影、**geometry/physics/dynamics は世界そのもの**を表す [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- **simulation is the bridge**: simulator が、商業的に最も成熟した renderer と最も黎明期の planner を橋渡しする [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- 論理的な終着点は **unified world model**: 基盤となる物理理解は共通で、出力形式（ピクセル/構造/行動予測）の違いとして投影される単一モデルへ収束する [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)

## 主要な貢献
- 乱立する「world model」概念を **機能（何を出力し、何のためか）** で切り分ける taxonomy を提示
- taxonomy を評価指標にマップ: **visual quality → renderer / forward-prediction fidelity → simulator / decision performance → planner**。「アーキテクチャ選択は機能要件に従う」という設計指針を与える

## 制限・注意点
- 査読のないエッセイ（論説）であり、実証データではなく概念整理 [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)
- 未解決課題として **3D アセット・ロボット実演データの極端な不足**、**sim-to-real ギャップの持続**、**生成モデルによる幾何的矛盾（自己交差・スケール誤差）** を挙げる [source](../../sources/Physical_AI/a-functional-taxonomy-of-world-models.md)

## ベンチマーク結果
（該当する定量結果なし。エッセイ）

## 実装関連
- 「機能ごとに評価指標を分けよ」という運用指針: renderer は視覚品質、simulator は前方予測の忠実度、planner は意思決定性能で測る
