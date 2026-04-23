---
id: src-codescout
title: "CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents"
authors: ["Lintang Sutawika", "Aditya Bharat Soni", "Bharath Sriraam R R", "Apurva Gandhi", "Taha Yassine", "Sanidhya Vijayvargiya", "Yuchen Li", "Xuhui Zhou", "Yilin Zhang", "Leander Melroy Maben", "Graham Neubig"]
year: 2026
url: "https://arxiv.org/abs/2603.17829"
type: paper
peer_review: preprint
venue: ""
tags: [RL, code-search, localization, SWE-Bench, agent, GSPO, OpenHands]
date_added: 2026-04-08
status: processed
---

# CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents

## 概要
Unix端末のみを装備したコード検索エージェントをRLで訓練し、2-18倍大きいモデルに匹敵・上回る性能を達成。環境の再利用、報酬設計、RL最適化の3つの軸でレシピを整理。SWE-Bench Verified/Lite/Proで評価。コード・モデル・データを公開。

## メモ
- Base model（Qwen3-1.7B）のファイルF1が2.4%→55.46%に跳ね上がり、filtering/sharpeningでは説明しにくい能力獲得の好例
- エージェントがRL訓練中にツール使用を多様→最小限に収束させる現象が観察され、効率的検索戦略の発見を示唆
- 特殊ツール不要でripgrep+sed程度に収束する点が実用的
- Graham Neubig研究室（CMU）
