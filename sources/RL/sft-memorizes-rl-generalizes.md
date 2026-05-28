---
id: src-sft-memorizes-rl-generalizes
title: "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training"
authors: ["Tianzhe Chu", "Yuexiang Zhai", "Jihan Yang", "Shengbang Tong", "Saining Xie", "Dale Schuurmans", "Quoc V. Le", "Sergey Levine", "Yi Ma"]
year: 2025
url: "https://arxiv.org/abs/2501.17161"
type: paper
peer_review: accepted
venue: "ICML 2025 (PMLR 267)"
tags: [RL, SFT, post-training, generalization, memorization, out-of-distribution, PPO, outcome-based-reward, multimodal, V-IRL, GeneralPoints]
date_added: 2026-05-19
status: processed
---

# SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training

## 概要
SFT（supervised fine-tuning）と RL（強化学習）の post-training における役割を**汎化 vs 暗記**の軸で実証的に対比した論文。算術カードゲーム **GeneralPoints**（GP-L / GP-VL: language-only / vision-language 版）と実世界ナビゲーション環境 **V-IRL**（同様に L / VL 版）で、ルール変動と視覚変動の OOD 評価を実施。**RL（PPO + outcome-based reward）はルール・視覚の両 OOD で汎化、SFT は in-distribution に過適合し OOD で劇的劣化**。一方で **SFT は RL 訓練の前段として依然必要**（指示追従能力を持たないベースモデルへの直接 RL は全て失敗）。**V-IRL-VL の visual OOD で +33.8pt の SOTA 更新**（16.7% → 77.8%）。

## メモ
- 著者陣: Tianzhe Chu / Yuexiang Zhai / Jihan Yang / Shengbang Tong / Saining Xie / Dale Schuurmans / Quoc V. Le / Sergey Levine / Yi Ma（UC Berkeley × HKU × Google DeepMind × University of Alberta、Saining Xie 在籍時 SenseTime 名義）。
- arXiv 2501.17161 v1: 2025-01-28 / v2: 2025-05-26。ICML 2025 採択（PMLR 267, Vancouver）。
- プロジェクトページ: https://tianzhechu.com/SFTvsRL — 公式実装: https://github.com/LeslieTrue/SFTvsRL
- ベースモデル: **Llama-3.2-Vision-11B**（Dubey et al., 2024）。RL は **PPO**（Schulman et al., 2017）。
- Outcome-based reward の具体例（GeneralPoints）: 正解 +5 / 全カード使用したが不正解 −1 / 不正な数値使用 −2 / その他違法式 −3 / GP-VL のカード認識失敗 −1.5。
- 重要観察: **RL 訓練は副作用としてカード認識精度を向上**、SFT は逆に視覚認識精度を低下させる（reasoning token への過適合仮説）。
- "SFT necessary" の限定条件: backbone が指示追従できないとき。**DeepSeek-R1**（DeepSeek-AI 2025）の "pure RL で SFT 不要" 結果は別 backbone 知識前提による差異と本論文は注釈する → 本リポジトリの [DeepSeek-R1](../../wiki/papers/RL/deepseek-r1.md) / [Dr. GRPO](../../wiki/papers/RL/dr-grpo.md) の "事前学習バイアス説" と接続。
- [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](../../wiki/papers/RL/willccbb-sft-rl-opd.md) の **compounding argument**（SFT は分布固定で天井 ≈ teacher、RL はロールアウトで compounding し天井 = verifier 能力）の経験的先行事例。
- 検証反復数 {1, 3, 5, 10} で OOD 改善量 {+0.48, +2.15, +2.99, +5.99}pt のスケーリング（test-time compute scaling 性質）。
