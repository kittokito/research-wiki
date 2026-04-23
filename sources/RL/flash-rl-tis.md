---
id: src-flash-rl-tis
title: "Your Efficient RL Framework Secretly Brings You Off-Policy RL Training"
authors: ["Feng Yao", "Liyuan Liu", "Dinghuai Zhang", "Chengyu Dong", "Jingbo Shang", "Jianfeng Gao"]
year: 2025
url: "https://fengyao.notion.site/off-policy-rl"
type: blog
peer_review: n/a
venue: ""
tags: [RLHF, RLVR, off-policy, importance-sampling, TIS, vLLM, FSDP, VeRL, PPO, GRPO, DAPO, MoE, rollout-training-mismatch, Flash-RL]
date_added: 2026-04-17
status: processed
---

# Your Efficient RL Framework Secretly Brings You Off-Policy RL Training

## 概要
VeRL等の主要LLM向けRLフレームワークは、rollout生成（vLLM/SGLang）と勾配計算（FSDP/Megatron）に別実装を採用する。同一パラメータθでも両者のトークン確率は大きく乖離し、on-policy RLが黙ってoff-policy化する。著者らはこの `π_sampler` と `π_learner` のギャップを、重要度比に対するクランプを加えた Truncated Importance Sampling (TIS) による数行の修正で吸収する。Qwen2.5-32B + DAPO、Qwen2.5-0.5B + GSM8K（INT8 rollout含む）等で性能・安定性が大幅改善し、entropy collapse／応答長暴走／負のKL推定といった失敗モードを解消。VeRL・slime・OAT・SkyRL・OpenRLHF・REINFORCE++に統合済み。

## メモ
- 2025-08-05 公開、2025-10-13 最終更新（"Policy Gradient, Sequence, and Token" Part I/II 節を追加）
- 著者所属: Feng Yao, Chengyu Dong, Jingbo Shang (UCSD); Liyuan Liu, Dinghuai Zhang, Jianfeng Gao (Microsoft Research); Feng & Liyuan が共同筆頭
- 連絡先: fengyao@ucsd.edu, llychinalz@gmail.com
- "Flash-RL" を実装／検証の母体リポジトリとして言及（[GitHub](https://github.com/yaof20/Flash-RL)）
- 査読: n/a（ブログ）。ただし採用事例が既に多数で、事実上 community-accepted な修正
- GSPO/GMPO（sequence-level／幾何平均な重要度比）とは直交、TISはシステムレベルのミスマッチに対処
