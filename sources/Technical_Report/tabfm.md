---
id: src-tabfm
title: "Introducing TabFM: A zero-shot foundation model for tabular data"
authors: ["Weihao Kong", "Abhimanyu Das"]
year: 2026
url: "https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/"
type: blog
peer_review: n/a
venue: ""
tags: [tabular-data, foundation-model, in-context-learning, zero-shot, synthetic-data, TabPFN, structural-causal-model]
date_added: 2026-07-01
status: processed
---

# Introducing TabFM: A zero-shot foundation model for tabular data

## 概要
Google Research による**表形式データ（tabular data）向けゼロショット基盤モデル**の発表ブログ（2026-06-30）。表の予測（分類・回帰）を **in-context learning (ICL)** 問題として定式化し、学習済みモデルの追加訓練・ハイパラ調整・特徴量エンジニアリングなしに、未知の表に対して**単一の forward pass** で高品質な予測を返す。**構造因果モデル（SCM）で生成した数億の合成データセット**のみで事前学習し、TabArena ベンチで教師あり定番アルゴリズムを上回る ELO を達成。重みは HuggingFace、コードは GitHub で公開、BigQuery の `AI.PREDICT` への統合も予定。

## メモ
- 著者は Weihao Kong・Abhimanyu Das（Google Research, Research Scientists）ほか。
- 位置づけ: **TabPFN / TabICL の系譜**を統合したハイブリッド設計。alternating row/column attention は TabPFN 同様「表は2次元で行・列の並びに不変」という性質に対応する。
- 付随 arXiv 論文は本ブログ時点で未確認。公開物は HF（`google/tabfm-1.0.0-pytorch`）と GitHub（`google-research/tabfm`）。
- 査読対象外（n/a、ブログ発表）。定量ベンチは TabArena（38 分類 + 13 回帰、700〜150,000 サンプル）。
</content>
</invoke>
