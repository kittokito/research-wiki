---
title: "LiveBench: A Challenging, Contamination-Limited LLM Benchmark"
aliases: ["LiveBench"]
created: 2026-04-21
updated: 2026-04-21
tags: [benchmark, evaluation, contamination, llm-judge, math, coding, reasoning]
peer_review: accepted
venue: "ICLR 2025 (Spotlight)"
sources: [src-livebench]
---

# LiveBench: A Challenging, Contamination-Limited LLM Benchmark

> **査読**: ✅ accepted — ICLR 2025 (Spotlight)

White, Dooley, Roberts et al. (2024) — arXiv 2406.19314 / OpenReview sKYHBTAxVa

## ソースからの事実
- LiveBench は (1) 最新情報源からの頻繁更新、(2) 客観的ground-truthによる自動スコアリング、(3) 6領域の広範タスク（math / coding / reasoning / language / instruction following / data analysis）を同時達成した初のベンチマーク [source](../../../sources/Evaluation/livebench.md)
- 問題は最近の math competitions・arXiv 論文・ニュース・datasets に基づき、Big-Bench Hard / AMPS / IFEval の汚染耐性・困難化版も含む [source](../../../sources/Evaluation/livebench.md)
- 0.5B-405Bの多数のクローズド/オープンモデルを評価、**トップモデルでも 70% 未満** [source](../../../sources/Evaluation/livebench.md)
- 問題は **月次** で追加・更新され、全問題・コード・回答が公開される [source](../../../sources/Evaluation/livebench.md)

→ 詳細: [evidence](../../../evidence/Evaluation/livebench.md)

## 現時点の解釈
「汚染耐性 × 客観採点 × 広範タスク × 継続運用」という評価の4条件を同時に満たした点が意義深く、LLM-judgeの限界（P-hacking with one prompt や sycophancy に通じるバイアス問題）を回避する実用路線を提示する。月次更新による経年対応はGSM-Symbolic的な「同一タスクでの数値変更」とも相補的な戦略で、**静的ベンチマークの寿命限界**への構造的回答となっている。ただし公開後の汚染再発リスクは残り、また自由記述タスクの評価は対象外という制約もあるため、LLM-judgeベンチ（MT-Bench等）や人手評価との併用が現実的。フロンティアモデル評価で引用頻度が急増しているため、他ベンチマークとの比較の基礎点として wiki 横断的に参照されるべき。

## 関連ページ
- [GSM-Symbolic](../Reasoning/gsm-symbolic.md) — 数値変更でLLM数学推論がばらつく、パターンマッチング限界
- [P-hacking with one prompt](./p-hacking-with-one-prompt.md) — LLM-judge/探索の落とし穴
- [SECURE: Benchmarking LLMs for Cybersecurity](./secure-cybersecurity-benchmark.md) — ドメイン特化ベンチマーク
- [SWE-CI](./swe-ci.md) — CI環境でのエージェント評価
- [Large Language Model Reasoning Failures](../Surveys_Overview/llm-reasoning-failures.md) — LLM推論失敗のサーベイ

## 未解決の問い
- 月次更新スケジュールの運用持続性は？コミュニティ貢献が途絶えた場合のフォールバック設計は？
- 「公開 → 学習データ混入 → 汚染」のラグは実測でどの程度短縮しているか（モデルリリース頻度との関係）？
- 自由記述・創造的タスクをLiveBench流の客観採点に落とし込む設計原則は可能か？
- LiveBenchで70%未満のトップモデル制約は、月次の困難化でどの程度維持されているか？（寿命シミュレーション）
