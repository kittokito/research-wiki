---
title: "Risk-Sensitive RL for Alleviating Exploration Dilemmas in LLMs (RS-GRPO)"
aliases: ["RS-GRPO", "Risk-Sensitive GRPO"]
created: 2026-04-17
updated: 2026-04-17
tags: [RLVR, GRPO, pass-at-k, exploration-exploitation, risk-sensitive-RL, CVaR, Tsinghua, ByteDance-Seed]
peer_review: under-review
venue: "ICLR 2026（投稿中）"
sources: [src-rs-grpo]
---

# Risk-Sensitive RL for Alleviating Exploration Dilemmas in LLMs

> **査読**: 🔄 under-review — ICLR 2026 Conference Submission（OpenReview [7kC8ORye4l](https://openreview.net/forum?id=7kC8ORye4l)）/ arXiv 2509.24261

Jiang, Huang, Yuan, Mao, Yue, Zhao, Yan (2025) — 清華大学 × ByteDance Seed

## ソースからの事実
- 事前学習済みLLMの初期方針の尖鋭さ（sharpened prior）が標準RLの探索を狭める「exploration dilemma」を定式化 [source](../../../sources/RL/rs-grpo.md)
- 標準GRPOはpass@1を上げる一方でpass@k（多様性）を下げる傾向がある [source](../../../sources/RL/rs-grpo.md)
- 平均報酬と最大報酬を補間するCVaRベースのリスク感応的目的関数を導入 [source](../../../sources/RL/rs-grpo.md)
- RS-GRPOはGRPOへの数行修正で実装可能、困難プロンプトからの学習を増幅 [source](../../../sources/RL/rs-grpo.md)
- 6つの数学推論ベンチマーク × 5つのLLMでpass@k継続向上 + pass@1維持・強化を確認 [source](../../../sources/RL/rs-grpo.md)

→ 詳細: [evidence](../../../evidence/RL/rs-grpo.md)

## 現時点の解釈

RLVR能力境界論争に対し、「目的関数のリスク感応性」という切り口でアプローチした論文。Yue et al.の指摘する「pass@k低下（filtering化）」問題を、長期訓練（ProRL）でも幾何学的介入（MRPO）でもなく、標準GRPOの目的関数そのものに最小修正を入れることで緩和する。sharpened priorという観点は、pretraining manifoldへの閉じ込めという既存のexpansion派の議論とも接続する。

実装コストが非常に低い（few lines）ため、RLVRパイプライン全般への組み込みやすさが利点。ただし検証は数学タスクに限定されており、コード・エージェントでの再現は今後の課題。

## 関連ページ
- [[rlvr-capability-boundary]] — RLVR能力境界論争の全体像（pass@k問題の文脈）
- [[rlvr-does-not-teach-new-reasoning]] — pass@k低下を報告したfiltering派論文
- [[prorl]] — 長期訓練によるexpansion派アプローチ
- [[mrpo]] — 幾何学的（manifold reshaping）アプローチ

## 未解決の問い
- リスクパラメータの最適値はモデル規模・タスクにどう依存するか？
- コード・エージェントRLなど非数学タスクでも同様の効果が得られるか？
- CVaR以外のリスク尺度（例: entropic risk）との比較優位はあるか？
