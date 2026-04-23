---
title: "The Debate on RLVR Reasoning Capability Boundary"
aliases: ["RLVR Boundary Debate", "RLVR二段階動態"]
created: 2026-04-08
updated: 2026-04-08
tags: [RLVR, reasoning, capability-boundary, GRPO, exploration, exploitation, probability-mass]
peer_review: under-review
venue: ""
sources: [src-rlvr-capability-boundary-debate]
---

# The Debate on RLVR Reasoning Capability Boundary

> **査読**: 🔄 under-review

## ソースからの事実
- RLVRのcapability boundaryをめぐるshrinkage派とexpansion派はどちらも部分的に正しいと整理 [source](../../../sources/RL/rlvr-capability-boundary-debate.md)
- Probability mass dynamicsの二段階モデルを提示：exploitation stage → exploration stage [source](../../../sources/RL/rlvr-capability-boundary-debate.md)
- Theorem 1: 期待logit updateは現在の方策確率に依存し、tail行動は有限サンプルで事実上無視される [source](../../../sources/RL/rlvr-capability-boundary-debate.md)
- 既存研究の多くが数百ステップで学習を止めており、exploration stageに未到達の可能性 [source: §4](../../../sources/RL/rlvr-capability-boundary-debate.md)
- GRPO-N/GSPO-N: negative gradientsに集中して分布多様性を保ちつつprolonged trainingを安定化 [source](../../../sources/RL/rlvr-capability-boundary-debate.md)

→ 詳細: [evidence](../../../evidence/RL/rlvr-capability-boundary-debate.md)

## 現時点の解釈

この論文は「pretraining manifoldに閉じ込められている」説を否定していない。むしろ初期段階でのsupport constraintを明示的に認めている（Theorem 1）。ただし、それを固定的上限ではなく学習前半の現象として位置づけ、prolonged trainingによる部分的なexpansionの余地を主張している。

核心的な問いは、後半のexploration stageで起こることが「pretraining manifold外への脱出」なのか「manifold内の極薄tailの増幅」なのかだが、この論文単体ではそれを切り分けていない。Softmaxにより全トークンに理論上正の確率があるため、長い学習で薄いtailを拾える余地はあるが、「自動的に探索できる」ほど簡単ではなく、初期は事実上閉じ込められるという認識が前提にある。

## 関連ページ
- [[rlvr-capability-boundary]] — RLVRの能力境界に関するトピック総合
- [[rlvr-does-not-teach-new-reasoning]] — Yue et al.のfiltering主張
- [[deepseek-r1]] — Pure RLでの推論能力獲得

## 未解決の問い
- Prolonged trainingによるexploration stageの発現は、大規模モデル・複雑タスクでも再現するか？
- GRPO-N/GSPO-Nのnegative gradient手法は他のRL手法（PPO等）にも適用可能か？
- Exploitation → exploration の遷移タイミングは予測可能か？
