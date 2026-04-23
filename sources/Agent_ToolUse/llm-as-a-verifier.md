---
id: src-llm-as-a-verifier
title: "LLM-as-a-Verifier: A General-Purpose Verification Framework"
authors: ["Jacky Kwok", "Shulu Li", "Pranav Atreya", "Yuejiang Liu", "Marco Pavone", "Ion Stoica", "Azalia Mirhoseini"]
year: 2026
url: "https://llm-as-a-verifier.notion.site/"
type: blog
peer_review: n/a
venue: ""
tags: [verifier, reward-model, test-time-scaling, swe-bench, terminal-bench, agent-eval, llm-as-judge]
date_added: 2026-04-21
status: processed
---

# LLM-as-a-Verifier: A General-Purpose Verification Framework

## 概要
「scoring granularity・repeated verification・criteria decomposition の3軸をスケールすると、LLM検証精度が一貫して向上する」という観察を軸にした汎用検証フレームワーク。agentのtrajectoryをtest-time scalingで採点する軌跡reward modelとして用いることで、Terminal-Bench 2 で **86.4% (SOTA)**、SWE-Bench Verified で **77.8%** を達成。Claude Opus 4.6、GPT 5.4、Gemini各モデルを上回る結果を報告。verifier には Gemini 2.5 Flash を使用し、trajectory候補はClaude Opus 4.6・Gemini 3 Flash・Claude Opus 4.5 からサンプル（ForgeCode・mini-swe-agent scaffold）。Terminal-Benchでは 81.8% → 86.4% の改善幅を test-time scaling + verification で実現。

## メモ
Stanford AI Lab × UC Berkeley Sky Computing Lab × NVIDIA 連合（Ion Stoica・Azalia Mirhoseini・Marco Pavone 等が Advising）。Posted: April 9, 2026。Notion公開記事＋GitHub公開（llm-as-a-verifier/llm-as-a-verifier）。査読論文ではなくプロジェクトページ扱いだが、既存のLLM-as-a-Judgeの弱点（point estimate・自信過剰・単一prompt依存）を構造的にスケール可能な3軸で克服する実用フレームワークとして重要。
