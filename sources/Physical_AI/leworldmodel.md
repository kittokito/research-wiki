---
id: src-leworldmodel
title: "LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels"
authors: ["Lucas Maes", "Quentin Le Lidec", "Damien Scieur", "Yann LeCun", "Randall Balestriero"]
year: 2026
url: "https://arxiv.org/abs/2603.19312"
type: paper
peer_review: preprint
venue: ""
tags: [JEPA, world-model, self-supervised, control, planning, representation-collapse, physical-ai]
date_added: 2026-04-23
status: processed
---

# LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

## 概要
JEPA（Joint Embedding Predictive Architecture）を raw pixels から end-to-end で安定学習する最初の構成として **LeWorldModel (LeWM)** を提案。既存のJEPA系列がmulti-term loss・EMA（exponential moving average）・事前学習エンコーダ・補助監督などのトリックに依存して表現崩壊（representation collapse）を回避していたのに対し、**次埋め込み予測損失＋Gaussian分布正則化の2項のみ** で安定学習を達成。調整必要な損失ハイパラは（既存end-to-end JEPAの）6個から1個に削減。約15Mパラメータで単GPU・数時間で学習可能、foundation model系 world model に比べ **最大48倍高速な計画** を実現しつつ、2D/3D制御タスクで競争力を維持。潜在空間に物理量がprobeで取り出せる形でエンコードされ、surprise評価で物理的に非現実な事象を検出可能。

## メモ
cs.LG 想定。著者は Meta FAIR / LeCun ラボ系（Yann LeCun, Randall Balestriero ほか）。v1: 2026-03-13、v2: 2026-03-24。arXiv Comments・venue情報なしで現状 preprint。V-JEPA 2 系列（actionlessやV-JEPA 2-AC）がスケール重視でロボット応用を主目的としたのに対し、LeWMは **表現崩壊問題の理論的・実装的ミニマル解** を提示する点で別角度。JEPA系world modelの **普及可能性（small model, single GPU, 1 hyperparameter）** を大きく押し下げたという意味で、個人研究者・小規模ラボでも world model を実用的に扱える道を開く可能性がある。
