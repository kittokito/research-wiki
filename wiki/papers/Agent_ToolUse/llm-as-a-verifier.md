---
title: "LLM-as-a-Verifier: A General-Purpose Verification Framework"
aliases: ["LLM-as-a-Verifier", "LaaV"]
created: 2026-04-21
updated: 2026-04-21
tags: [verifier, reward-model, test-time-scaling, swe-bench, terminal-bench, agent-eval, llm-as-judge]
peer_review: n/a
venue: ""
sources: [src-llm-as-a-verifier]
---

# LLM-as-a-Verifier: A General-Purpose Verification Framework

> **査読**: — n/a（Notion公開プロジェクトページ、Stanford AI Lab × UC Berkeley Sky Computing Lab × NVIDIA, 2026-04-09）

Kwok, Li, Atreya, Liu, Pavone, Stoica, Mirhoseini (2026)

## ソースからの事実
- 検証精度は **scoring granularity / repeated verification / criteria decomposition** の3軸をスケールすると一貫して向上 [source](../../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- Agent trajectoryに対する **軌跡reward model** として動作、test-time scalingと組み合わせて downstream 成功率を押し上げる [source](../../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- **Terminal-Bench 2 で 86.4% (SOTA)**、**SWE-Bench Verified で 77.8%**、Claude Opus 4.6 / GPT 5.4 / Gemini 各モデルを上回る [source](../../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- Terminal-Benchで 81.8% → 86.4% の改善幅を test-time scaling + verification のみで実現、pairwise検証精度は **78.9%** [source](../../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- Verifier に **Gemini 2.5 Flash**、trajectory generator に Claude Opus 4.6 / Gemini 3 Flash / Claude Opus 4.5、scaffold に ForgeCode・mini-swe-agent を使用 [source](../../../sources/Agent_ToolUse/llm-as-a-verifier.md)

→ 詳細: [evidence](../../../evidence/Agent_ToolUse/llm-as-a-verifier.md)

## 現時点の解釈
LLM-as-a-Judge の弱点（単一prompt依存・point estimate・細かい差異への鈍感さ）を、**「judgingを軸ごとに分解してスケールする」** という単純だが一般性の高い設計で克服した実用フレームワーク。Terminal-Bench 2 の SOTA 更新（86.4%）は **小型verifier（Gemini 2.5 Flash）で大型generator（Claude Opus 4.6）の出力プールを再ランキング** する形で成立しており、推論コスト対効果の観点で実務的価値が高い。**P-hacking with one prompt** で指摘された単一prompt脆弱性や **Mind the Gap** の「生成より検証が容易」テーゼを逆手に取り、検証側を scale して agentの行動品質を底上げする方向性を体系化した点が意義深い。RLVR能力境界論争（Yue et al. vs ProRL）の文脈では、**「verifier側のscalingが downstream capability を実質的に動かす」** ことの強い証拠で、reward model/process reward model 研究への接続も強い。ただしTerminal-Bench / SWE-Bench中心の評価で、数学・推論・マルチモーダル等への一般化は追試待ち。

## 関連ページ
- [Mind the Gap: Self-Improvement](../Reasoning/mind-the-gap-self-improvement.md) — 生成 vs 検証の容易さの非対称性
- [P-hacking with one prompt](../Evaluation/p-hacking-with-one-prompt.md) — 単一promptLLM-judgeのバイアス
- [SWE-CI](../Evaluation/swe-ci.md) — CI環境でのagent評価
- [LiveBench](../Evaluation/livebench.md) — LLM-judge回避型の客観ベンチマーク
- [AutoHarness](./autoharness.md) — agent自動評価の隣接手法
- [RLVRの能力境界論争](../../topics/RL/rlvr-capability-boundary.md) — verifier scaling と能力獲得の境界
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — agentic coding評価の文脈

## 未解決の問い
- 3軸スケール（granularity × repetition × decomposition）の計算コスト対downstream改善曲線は？最適配分は？
- 同一モデルでのself-verification（trajectory生成とverifierに同じLLMを使う）と異モデル構成の性能差はどこから生まれるか？
- 数学・マルチモーダル・長文要約等の非コーディング領域で同じ3軸スケーリングが成立するか？
- Terminal-Bench の pairwise 検証精度78.9%が downstream 86.4%までブーストされる理論的説明は？（BoN bound の観点）
- このフレームワークを **RLVRの reward model** として訓練時に組み込むと、inference-time利用を超える効果が出るか？
