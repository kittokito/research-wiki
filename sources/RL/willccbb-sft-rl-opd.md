---
id: src-willccbb-sft-rl-opd
title: "On SFT, RL, and on-policy distillation: Why the standard pipeline is what it is, where on-policy distillation fits, and how self-distillation goes wrong"
authors: ["Will Brown", "Claude Opus 4.7"]
year: 2026
url: "https://x.com/willccbb/status/2050038277454143918"
type: blog
peer_review: n/a
venue: ""
tags: [SFT, RL, on-policy-distillation, OPD, SDFT, OPSD, GRPO, post-training, gradient-geometry, Pareto-curve, meta-analysis]
date_added: 2026-05-07
status: processed
---

# On SFT, RL, and on-policy distillation

## 概要
Will Brown と Claude Opus 4.7 の共著エッセイ（2026-04-30 公開）。post-training パイプラインの **「SFT 先 → RL 後」** の標準的順序を、**サンプリング分布の compounding** という観点から論じる。さらに on-policy distillation (OPD) を **same-family teacher が使えるときの中間解** として位置付け、teacher が使えないときの **self-distillation 派生 (SDFT, OPSD)** の失敗モードを **勾配幾何学** で分析。**密／疎 × バイアス／非バイアス × 集中／拡散** の3軸でメソッドを分類し、SFT・RL・OPD・OPSD・SDFT・DAGGER をすべて単一の token-level policy gradient（α、λ、π_T の3つのダイヤルを持つ）の特殊ケースとして統一。最後に、最適 teacher 探索を Lagrangian `max E[ΔR] − β·D_KL(π_T ‖ π_θ)` の最適化問題として定式化し、その内部空間（学習可能な hint writer、prompt optimization、self-prompt RL 等）を future work として提示。

## メモ
著者: Will Brown (handle: willccbb) — Prime Intellect / 元 Morgan Stanley researcher、verifiers ライブラリの作者。GRPO 関連の解説で著名 / **Claude Opus 4.7** との共著。本リポジトリの GRPO variants / RLVR capability boundary / off-policy RL / importance sampling クラスタの **メタ分析的整理** として位置付け。形式は X 投稿（2050038277454143918, 2026-04-30）に紐づく長文エッセイ、本文中で Figure 1-6 が言及されているが画像はリンク先 HTML 版のみで本リポジトリには未取り込み。**著者が Claude Opus 4.7 と共著** という形式自体が、AI 共著で技術メタ分析を出版する近年の運用例として注目に値する。参照論文: Lu (Thinking Machines, 2025) OPD / Shenfeld et al. (2026) SDFT / Zhao et al. (2026) OPSD / Agarwal et al. (2023) On-Policy KD / Mukherjee et al. (2025) RL fine-tunes small subnetworks / Qwen3 TR (2025) / Ross et al. (2010) DAGGER。
