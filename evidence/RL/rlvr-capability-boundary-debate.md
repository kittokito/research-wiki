---
source: src-rlvr-capability-boundary-debate
date_extracted: 2026-04-08
---

# The Debate on RLVR Reasoning Capability Boundary からの抽出

## 主要な主張
- RLVRの能力境界をめぐるshrinkage派もexpansion派もどちらも部分的に正しい [source](../../sources/RL/rlvr-capability-boundary-debate.md)
- Probability mass dynamicsは二段階で進行する：exploitation stage（高報酬トークンへの確率集中）→ exploration stage（低確率だが有望なトークンへの質量移動） [source](../../sources/RL/rlvr-capability-boundary-debate.md)
- 期待logit updateの大きさは現在の方策確率に依存し、確率極小のtail行動は有限サンプル下では更新にほぼ寄与しない（Theorem 1） [source](../../sources/RL/rlvr-capability-boundary-debate.md)
- Softmax上では理論的に全トークン確率が正だが、実務上は極端なtailはサンプリングされず effectively omitted になる [source](../../sources/RL/rlvr-capability-boundary-debate.md)
- 既存研究の多くが数百ステップで学習を止めており、exploration stageに到達する前に打ち切っている可能性がある [source: §4](../../sources/RL/rlvr-capability-boundary-debate.md)

## 主要な貢献
- Shrinkage vs expansion を二択ではなく二段階動態として統一的に再解釈
- GRPO-N / GSPO-N の提案：relative negative gradientsに集中することで分布の多様性を保ちつつprolonged trainingを可能にする
- 早期終了がshrinkage観測を強めているというメタ的指摘

## 制限・注意点
- "manifold" という用語を使わず、support / probability mass の言葉で議論しているため、pretraining manifold仮説そのものの直接的証明・反証ではない
- 低確率tailを後半で育てることが「完全に新しい領域の創発」なのか「もともと極薄で存在していたtailの増幅」なのかは切り分け切れていない
- GRPO-N/GSPO-Nの大規模実験による検証は限定的（追試待ち）

## 実装関連
- GRPO-N: 正例軌跡全体を強く押し上げる代わりに、negative gradientsに集中して分布多様性を保つ
- GSPO-N: 同様の発想をGSPOに適用
