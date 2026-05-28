---
id: src-learning-fast-and-slow
title: "Learning, Fast and Slow: Towards LLMs That Adapt Continually"
authors: ["Rishabh Tiwari", "Kusha Sareen", "Lakshya A Agrawal", "Joseph E. Gonzalez", "Matei Zaharia", "Kurt Keutzer", "Inderjit S Dhillon", "Rishabh Agarwal", "Devvrit Khatri"]
year: 2026
url: "https://arxiv.org/abs/2605.12484"
type: paper
peer_review: preprint
venue: ""
tags: [RL, continual-learning, post-training, fast-slow-weights, prompt-optimization, GEPA, GRPO, CISPO, KL-divergence, drift, plasticity, sample-efficiency, Pareto-frontier]
date_added: 2026-05-19
status: processed
---

# Learning, Fast and Slow: Towards LLMs That Adapt Continually

## 概要
LLM の継続適応における **parameter forgetting / plasticity loss vs context-in-learning の弱さ** のジレンマを、**Fast-Slow Training (FST)** という hybrid post-training パラダイムで解消する論文。**モデルパラメータ θ を slow weights**（GRPO + CISPO loss で更新）、**離散テキストプロンプト Φ を fast weights**（[GEPA](https://gepa-ai.github.io/) = Reflective Prompt Evolution で進化、GPT-5.2 を reflection LM として使用）として扱い、**T=6 RL ステップごとに GEPA が K={4,8} 候補プロンプトを生成し Pareto frontier を維持**、次の T RL 更新を conditioning する。RL 単独比 **最大3倍のサンプル効率**（CodeIO 47.4% vs RL 43.0% / HoVer-hard 25.0% vs 17.3% / Math 49.2% vs 46.4%）、**KL(π_train ∥ π_base) を最大70%削減**しベースモデルからの drift を抑制、**継続学習設定（HoVer→CodeIO→Physics 各200ステップ）で RL は CodeIO に stall（20.7%）するが FST は near-peak（37.7%）に到達**。

## メモ
- 著者陣: Rishabh Tiwari, Lakshya A Agrawal, Joseph E. Gonzalez, Matei Zaharia, Kurt Keutzer（UC Berkeley）/ Kusha Sareen, Rishabh Agarwal（Mila）/ Inderjit S Dhillon, Devvrit Khatri（UT Austin）。一部 Eragon / Periodic Labs / Mirendil 関連の所属あり。
- arXiv 2605.12484 v1: 2026-05-12 / v2: 2026-05-14。29ページ、14図。査読: preprint（採択先記載なし）。
- 公式ブログ: [gepa-ai.github.io/gepa/blog/2026/05/11/learning-fast-and-slow/](https://gepa-ai.github.io/gepa/blog/2026/05/11/learning-fast-and-slow/)
- コード: [rishabhtiwari.ai/projects/fst/code/](https://rishabhtiwari.ai/projects/fst/code/)
- **Lakshya A Agrawal は前作 GEPA（Reflective Prompt Evolution）の主要著者**、本論文は GEPA を「frozen checkpoint への post-hoc 適用」から「RL ループ内に embed する hybrid optimization」へ拡張した位置付け。
- **Devvrit Khatri は [ScaleRL](../../wiki/papers/RL/scale-rl.md) の主要著者**（Khatri, Madaan, Tiwari et al., 2025）、scaling 軸での RL 効率研究の系譜を継ぐ。
- **Rishabh Agarwal は Google DeepMind → Meta → Mila の RL/post-training 系研究者**、on-policy distillation 系の議論にも関与。
- Slow weights (θ): model parameters、GRPO + **CISPO loss**（[MiniMax-M1](../../wiki/papers/Technical_Report/minimax-m1.md) で導入された importance sampling weight clipping）で更新、group size G=8 rollouts/problem。
- Fast weights (Φ): discrete textual prompts、GEPA で進化、GPT-5.2 (frozen reflection LM) が textual mutation を提案、per-instance Pareto frontier を維持。
- Drift = `KL(π_train ∥ π_base)`、held-out validation prompts での token-level divergence で測定。
- Continual learning 評価: 600 step uninterrupted run × 3 sequential task switch（HoVer → CodeIO → Physics、各200ステップ）。
- **本リポジトリの [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](../../wiki/papers/RL/willccbb-sft-rl-opd.md) が future work で予告した「学習可能 hint writer / self-prompt online RL / hint-writing RL」系の具体実装**として位置付けられる。
