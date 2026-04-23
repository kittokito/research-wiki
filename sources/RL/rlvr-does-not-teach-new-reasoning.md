---
id: src-rlvr-does-not-teach-new-reasoning
title: "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"
authors: ["Yang Yue", "Zhiqi Chen", "Rui Lu", "Andrew Zhao", "Zhaokai Wang", "Shiji Song", "Gao Huang"]
year: 2025
url: "https://arxiv.org/abs/2504.13837"
type: paper
peer_review: accepted
venue: "NeurIPS 2025"
tags: [RLVR, pass-at-k, reasoning, filtering, sampling-efficiency, distillation, capability-analysis]
date_added: 2026-04-08
status: processed
---

# Does RLVR Truly Unlock New Reasoning Capabilities?

## 概要
RLVRはpass@1を改善するがpass@kではbase modelが上回ることがあり、RLVRモデルのreasoning pathはbase modelの出力分布にすでに含まれていると報告。RLVRの主な効果はサンプリング効率の向上（filtering/sharpening）であると主張。

## メモ
- 「多数のパスを絞っているだけ」説の代表的論文
- 新しい推論を生むのではなく、既存の正解経路への確率集中が主効果
