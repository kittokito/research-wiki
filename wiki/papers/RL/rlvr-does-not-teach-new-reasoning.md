---
title: "Does RLVR Truly Unlock New Reasoning Capabilities?"
aliases: ["Yue et al. RLVR filtering"]
created: 2026-04-08
updated: 2026-04-08
tags: [RLVR, pass-at-k, reasoning, filtering, sharpening]
sources: [src-rlvr-does-not-teach-new-reasoning]
---

# Does RLVR Truly Unlock New Reasoning Capabilities?

## ソースからの事実
- Pass@1は向上するがpass@k（大きいk）ではbase modelが上回ることがある [source](../../../sources/RL/rlvr-does-not-teach-new-reasoning.md)
- RLVRモデルのreasoning pathはbase modelの出力分布にすでに含まれている [source](../../../sources/RL/rlvr-does-not-teach-new-reasoning.md)
- 効果の主体はfiltering / sharpening [source](../../../sources/RL/rlvr-does-not-teach-new-reasoning.md)

→ 詳細: [evidence](../../../evidence/RL/rlvr-does-not-teach-new-reasoning.md)

## 現時点の解釈

「RLVRは多数のパスを絞っているだけ」説の代表的論文。Pass@k分析は説得力があり、標準的なGRPOレシピでは確かにfiltering成分が大きいことを示している。ただし、これは探索を強化した改良版RLVRや、prolonged trainingのケースには直接当てはまらない。Invisible Leash系の議論もこの方向を補強している。

## 関連ページ
- [[rlvr-capability-boundary]] — RLVRの能力境界に関するトピック総合
- [[rlvr-capability-boundary-debate]] — 二段階動態による再解釈

## 未解決の問い
- 探索を強化した改良版RLVRでpass@kはどう変化するか？
