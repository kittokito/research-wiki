---
title: "MRPO: Manifold-Reshaping Policy Optimization"
aliases: ["MRPO", "Beyond Alignment"]
created: 2026-04-08
updated: 2026-04-08
tags: [RLVR, MRPO, manifold, reasoning, GRPO, effective-rank, spectral-orthogonal-exploration, math]
sources: [src-mrpo]
---

# MRPO: Manifold-Reshaping Policy Optimization

## ソースからの事実
- 標準RLVRはbias manifold（低ランク多様体）に閉じ込められ、能力境界を真に拡張できないと主張（"The Trap"） [source](../../../sources/RL/mrpo.md)
- 方策収束時にeffective rankが縮小するConfidence-Induced Rank Collapse（Proposition 3.3）を理論的に示す [source](../../../sources/RL/mrpo.md)
- Effective rankが正解予測に有意（βᵣ=0.56）だがエントロピーは無意：推論能力は確率的不確実性ではなく幾何的次元性に関係 [source](../../../sources/RL/mrpo.md)
- SOE（null space方向への幾何的脱出）+ rank-aware GRPO の二段階で4Bモデルが32Bを上回る [source](../../../sources/RL/mrpo.md)
- AIME 2024で56.7%（vs Qwen3-32B 33.3%）、平均+3.8pt over standard GRPO [source](../../../sources/RL/mrpo.md)

→ 詳細: [evidence](../../../evidence/RL/mrpo.md)

## 現時点の解釈

### RLVRの能力境界論争における位置づけ

MRPOはRLVR能力境界論争に対して最も積極的な立場を取る論文。Yue et al.やInvisible Leash系が指摘する「pretraining manifoldへの閉じ込め」を前提として受け入れた上で、それを幾何学的に打破しようとする。

核心的なアイデアは2つ：
1. **問題の形式化**: 「閉じ込め」をbias manifoldの低ランク性として定義し、effective rankで測定可能にした
2. **明示的な脱出**: SOEでnull spaceへの投影を最大化する軌跡を生成し、rank正則化で崩壊を防ぐ

### 「能力境界の論争」に対する貢献の3つの柱

- **Yue et al.のfiltering仮説への反論**: Pass@KでもMRPOはbase modelを上回り、単なるsharpeningでは説明しにくいと主張（4BがAIME24 Pass@32で89.1%）
- **Invisible Leash系への回答**: On-policyの制約をoff-policyのSOE段階で迂回。Base modelのsupport外に明示的に踏み出す手法を提供
- **二段階動態論文との接点**: "exploitation → exploration"の自然遷移を待つのではなく、SOEで強制的にexploration stageを作り出す

### 重要な留保

4Bが32Bを上回る結果は印象的だが、以下の点で慎重な評価が必要：

- **ドメイン限定**: 数学推論のみ。verifiable rewardのない領域での効果は不明
- **追試未了**: 2026年1月投稿でまだ新しく、独立した再現実験は見当たらない
- **安全性懸念**: 著者自身がbias manifold外の動作による安全ガードレール迂回リスクを指摘
- **実装コスト**: Student-Guides-Teacher + SVDの工学的複雑さは標準GRPOと比較して大きい
- **Ablation**: SOE単体では+1.6pt、主要な改善はCold Start + GRPOの組み合わせ（+4.5pt）から来ており、幾何的介入の寄与とデータ品質の寄与の分離が十分でない可能性

### コーディング領域への示唆

数学推論での成功がコーディングに転移するかは未検証だが、コーディングタスクも「正解を検証可能」という性質を共有する。テスト実行環境をverifierとして使えば、SOE的なアプローチ（repo環境のnull spaceへの探索）が適用できる可能性がある。ただし、コードの解空間は数学よりはるかに広く、manifoldの定義自体が難しくなる。

## 関連ページ
- [RLVRの能力境界論争](../../topics/RL/rlvr-capability-boundary.md) — 本論文が位置する議論の全体像
- [Does RLVR Truly Unlock New Reasoning?](rlvr-does-not-teach-new-reasoning.md) — MRPOが反論するfiltering主張
- [RLVR Capability Boundary Debate](rlvr-capability-boundary-debate.md) — 二段階動態モデル（MRPOはexploration stageを強制する手法）
- [DeepSeek-R1](deepseek-r1.md) — Pure RLでの能力拡張（MRPOはその「安定性の欠如」問題を解決しようとする）

## 未解決の問い
- SOEの効果はデータ品質の向上か、本当にmanifold脱出か？（Ablationではデータ品質寄与が大きい可能性）
- 数学以外のverifiable domain（コーディング等）でも同様の改善が得られるか？
- Effective rank正則化は長期的にモデルの安全性にどう影響するか？
- 独立した追試で結果は再現されるか？
