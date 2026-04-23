---
id: src-scaling-laws-motion-forecasting-planning
title: "Scaling Laws of Motion Forecasting and Planning -- Technical Report"
authors: ["Mustafa Baniodeh", "Kratarth Goel", "Scott Ettinger", "Carlos Fuertes", "Ari Seff", "Tim Shen", "Cole Gulino", "Chenjie Yang", "Ghassen Jerfel", "Dokook Choe", "Rui Wang", "Benjamin Charrow", "Vinutha Kallem", "Sergio Casas", "Rami Al-Rfou", "Benjamin Sapp", "Dragomir Anguelov"]
year: 2025
url: "https://arxiv.org/abs/2506.08228"
type: paper
peer_review: n/a
venue: ""
tags: [scaling-law, autonomous-driving, motion-forecasting, planning, transformer, compute-optimal, closed-loop]
date_added: 2026-04-08
status: processed
---

# Scaling Laws of Motion Forecasting and Planning

## 概要
自動運転における動作予測・計画タスクでのエンコーダ・デコーダ型自己回帰Transformerの経験的スケーリング則を調査。50万時間の走行データを使用。性能は総計算予算のべき乗関数に従い、LLMで観測されたパターンと一致。閉ループ評価でもスケーリングが成立することを示した重要な知見を含む。

## メモ
- Waymo（Alphabet傘下）の研究チーム。cs.LG, cs.AI, cs.RO。
- 84モデル（900K〜118Mパラメータ）を訓練し、2桁以上の計算量範囲でスケーリング関係を調査。
- 初投稿: 2025年6月、最新改訂: 2025年9月。
