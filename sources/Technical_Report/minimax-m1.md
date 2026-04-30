---
id: src-minimax-m1
title: "MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"
authors: ["MiniMax Team"]
year: 2025
url: "https://arxiv.org/abs/2506.13585"
type: paper
peer_review: n/a
venue: ""
tags: [technical-report, open-weight, reasoning, MoE, lightning-attention, long-context, rl, CISPO, test-time-compute, MiniMax]
date_added: 2026-04-23
status: processed
---

# MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention

## 概要
MiniMax が公開した **世界初のオープンウェイト・大規模ハイブリッドアテンション推論モデル** のテクニカルレポート。**456Bパラメータ total / 45.9B activated per token** の hybrid MoE（Mixture-of-Experts） + **lightning attention** を採用し、前世代の MiniMax-Text-01 をベースに推論向けに継続学習。ネイティブで **100万トークンのコンテキスト**（DeepSeek R1 の 8倍）をサポート、lightning attention によりtest-time compute を効率的にスケール可能。RLは **sandbox ベースの実ソフトウェアエンジニアリング環境** を含む多様なタスクで実施。新規のRLアルゴリズム **CISPO** を提案、「token updates ではなく importance sampling weights をクリップ」することで競合RL派生（GRPO 等）を上回る効率。hybrid attention + CISPO の組み合わせにより **512 H800 GPU × 3週間、総計 $534,700** のレンタル費用で full RL 訓練を完了。thinking budget 40K / 80K の2版を公開。DeepSeek-R1・Qwen3-235B に匹敵ないし上回る、特にソフトウェアエンジニアリング・ツール使用・長文脈で強み。

## メモ
cs.CL / cs.LG。MiniMax（中国のAIラボ、海螺AIの開発元）。arXiv Comments: "A technical report from MiniMax. The authors are listed in alphabetical order." — 100名以上の著者。2025-06-16 公開（single version）。GitHub: MiniMax-AI/MiniMax-M1 でオープンウェイト公開。テクニカルレポート扱い（査読 n/a）。**CISPO** は RLVR / GRPO / DAPO 系列の新しい派生で、本wikiの RLVR 能力境界・off-policy ミスマッチ議論（Flash-RL/TIS）、ScaleRL の「効率を動かす設計選択」等と直結する。
