---
id: src-livebench
title: "LiveBench: A Challenging, Contamination-Limited LLM Benchmark"
authors: ["Colin White", "Samuel Dooley", "Manley Roberts", "Arka Pal", "Benjamin Feuer", "Siddhartha Jain", "Ravid Shwartz-Ziv", "Neel Jain", "Khalid Saifullah", "Sreemanti Dey", "Shubh-Agrawal", "Sandeep Singh Sandha", "Siddartha Venkat Naidu", "Chinmay Hegde", "Yann LeCun", "Tom Goldstein", "Willie Neiswanger", "Micah Goldblum"]
year: 2024
url: "https://openreview.net/forum?id=sKYHBTAxVa"
type: paper
peer_review: accepted
venue: "ICLR 2025 (Spotlight)"
tags: [benchmark, evaluation, contamination, llm-judge, math, coding, reasoning, instruction-following]
date_added: 2026-04-21
status: processed
---

# LiveBench: A Challenging, Contamination-Limited LLM Benchmark

## 概要
テストセット汚染（training set混入）とLLM-judge / クラウドソーシングのバイアス問題に耐性を持つLLMベンチマーク。(1) 最新情報源から頻繁に更新される問題、(2) 客観的なground-truthによる自動スコアリング、(3) math/coding/reasoning/language/instruction-following/data analysisの広範なタスク群、の3条件を初めて同時に満たす。最近のmath competitions、arXiv論文、ニュース、datasetsから問題を構築し、Big-Bench Hard・AMPS・IFEvalの困難化版も含む。0.5B-405Bの多数のクローズド/オープンモデルを評価、トップモデルでも70%未満。月次で問題を更新・追加。

## メモ
arXiv 2406.19314 / OpenReview sKYHBTAxVa。著者はAbacus.AI、Meta (Yann LeCun)、NYU、UMD、USC等の国際チーム。ICLR 2025 Spotlight採択。コード・問題・モデル回答すべて公開、月次更新という継続運用が特徴。
