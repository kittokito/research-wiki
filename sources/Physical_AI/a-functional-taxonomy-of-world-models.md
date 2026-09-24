---
id: src-a-functional-taxonomy-of-world-models
title: "A Functional Taxonomy of World Models"
authors: ["Fei-Fei Li"]
year: 2026
url: "https://drfeifei.substack.com/p/a-functional-taxonomy-of-world-models"
type: blog
peer_review: n/a
venue: ""
tags: [world-model, spatial-intelligence, renderer, simulator, planner, POMDP, JEPA, taxonomy]
date_added: 2026-06-09
status: processed
---

# A Functional Taxonomy of World Models

## 概要
「world model」と総称される系を **機能（function）で3分類**するエッセイ。**renderer（ピクセル観測を生成、visual fidelity 最優先）/ simulator（幾何・物理・動力学的に忠実な表現を生成）/ planner（観測＋目標から行動を決定、renderer の逆関数）** に整理し、これらを **POMDP に由来する古典的 agent loop**（state → observation → agent → action → state）の中に位置づける。言語モデルがテキストの統計的構造を学ぶのに対し、world model は **空間と時間の統計的構造**を学ぶ、という対比を主軸に、評価指標・アーキテクチャ選択・最終的な統合（unified world model）への展望を述べる。

## メモ
- World Labs CEO / Stanford の Fei-Fei Li による論説。Substack 公開（2026-06-03）。a16z 等で拡散。
- ユーザー提示元は X 投稿（[@drfeifei](https://x.com/drfeifei/status/2062247238143996275)）からリンクされた X article（同記事）。
- 査読対象外（n/a）。記事冒頭は Wittgenstein『論理哲学論考』の "The world is everything that is the case." を引く。
