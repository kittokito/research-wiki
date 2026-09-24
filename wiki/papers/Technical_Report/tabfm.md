---
title: "TabFM: A Zero-Shot Foundation Model for Tabular Data"
aliases: ["TabFM", "tabular foundation model", "zero-shot tabular"]
created: 2026-07-01
updated: 2026-07-01
tags: [tabular-data, foundation-model, in-context-learning, zero-shot, synthetic-data, TabPFN, structural-causal-model]
peer_review: n/a
venue: ""
sources: [src-tabfm]
---

# TabFM: A Zero-Shot Foundation Model for Tabular Data

> **査読**: — n/a（Google Research 発表ブログ）

Weihao Kong, Abhimanyu Das ほか (2026) — Google Research（2026-06-30）

## ソースからの事実
- 表形式データの分類・回帰を **in-context learning** 問題として定式化し、追加訓練・ハイパラ調整・特徴量エンジニアリングなしに**単一 forward pass** でゼロショット予測する基盤モデル [source](../../../sources/Technical_Report/tabfm.md)
- **ハイブリッドアーキテクチャ**: ① **alternating row/column attention**（行・列の両次元へ交互に attention、表の並び順不変性に対応）② **row compression**（各行を密ベクトルに圧縮）③ 圧縮行ベクトル上で動く **ICL transformer**（大規模データでも計算コストを抑制） [source](../../../sources/Technical_Report/tabfm.md)
- **完全合成データ学習**: **構造因果モデル（SCM）** で生成した**数億の合成データセット**のみで事前学習。実世界の良質・多様な表データの希少性を回避 [source](../../../sources/Technical_Report/tabfm.md)
- **TabArena**（38 分類 + 13 回帰、700〜150,000 サンプル）で **TabFM / TabFM-Ensemble** がトップ ELO、教師あり定番アルゴリズムを上回る [source](../../../sources/Technical_Report/tabfm.md)
- **TabPFN / TabICL の系譜**を統合したハイブリッド設計。重みは HF（`google/tabfm-1.0.0-pytorch`）・コードは GitHub（`google-research/tabfm`）で公開、BigQuery `AI.PREDICT` 統合も予定 [source](../../../sources/Technical_Report/tabfm.md)

→ 詳細: [evidence](../../../evidence/Technical_Report/tabfm.md)

## 現時点の解釈

TabFM は、本リポジトリで繰り返し現れる **「ゼロショット／in-context learning による基盤モデル化」** のパラダイムを、これまで勾配ブースティング木（XGBoost/LightGBM 等）が支配してきた**表形式データ**という領域に持ち込んだ事例。[CLIP](../Multimodal/clip.md) が画像分類を、[Video models are zero-shot learners](../Multimodal/video-models-zero-shot-learners.md) が視覚タスクをゼロショット化したのと同じ「基盤モデル＋ゼロショット転移」の構図を、表データで実現する。予測のたびに勾配降下で訓練するのではなく、**訓練データを文脈として与え forward pass 一発で予測する** ICL の枠組みは、TabPFN（および TabICL）が切り拓いた路線であり、TabFM はその強みを統合しつつ row compression で計算スケーラビリティを足した後継と位置づけられる。

特筆すべきは **「実データではなく構造因果モデル由来の合成データのみで事前学習する」** 設計思想。これは本リポジトリの合成データ／データ配合の系譜（[Rewriting Pre-Training Data](../Pretraining/rewriting-pretraining-data.md)・[Qwen3](qwen3.md) の synthetic self-curation）とは方向性が異なり、「実世界データが根本的に希少・非同型な領域では、因果構造をサンプリングして訓練分布そのものを合成する」というアプローチ。表データは各テーブルでスキーマ（列の意味・型・関係）が全く異なるため、テキスト・画像のような大規模実データの水平展開が効かず、SCM による合成が現実的な事前学習手段になる。

一方で発表はブログで定量 ELO の内訳が非開示であり、TabArena 上の既存 SOTA（TabPFN-2.5 等）との厳密な比較や、150,000 サンプル超・超高次元・強い分布シフト下での挙動は本発表の射程外。デフォルト TabFM と重い TabFM-Ensemble の差は、無調整運用の実力を見極める上で要注視。

## 関連ページ
- [CLIP](../Multimodal/clip.md) — 別モダリティ（画像）での「基盤モデル＋ゼロショット転移」の出発点
- [Video models are zero-shot learners and reasoners](../Multimodal/video-models-zero-shot-learners.md) — 訓練外タスクをゼロショットで解く基盤モデルの近例
- [Rewriting Pre-Training Data](../Pretraining/rewriting-pretraining-data.md) — 合成／書き換えデータで事前学習を強化する系譜（TabFM は SCM 合成で全面採用）
- [Qwen3](qwen3.md) — synthetic data self-curation を大規模 LLM で採用した対照例

## 未解決の問い
- SCM 合成データ事前学習は、実世界の表データが持つ**分布シフト・欠損・カテゴリの希少値**にどこまでゼロショットで頑健か？
- ICL 型表基盤モデルは、勾配ブースティング木が支配する産業実務（テーブルごとに専用モデルを組む運用）を本当に置換しうるか、それとも「無調整の初手ベースライン」に留まるか？
- 150,000 サンプル・数千特徴を超える大規模表で、row compression + ICL の計算・精度トレードオフはどこで破綻するか？
</content>
