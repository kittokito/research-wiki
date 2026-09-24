---
title: "Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models"
aliases: ["Paraphrase and Solve", "SCoP", "Self-Consistency over Paraphrases"]
created: 2026-06-09
updated: 2026-06-09
tags: [mathematical-reasoning, surface-form, robustness, self-consistency, paraphrase]
peer_review: accepted
venue: "NAACL 2024"
sources: [src-paraphrase-and-solve-scop]
---

# Paraphrase and Solve: Surface Form と数学推論 (SCoP)

> **査読**: ✅ accepted — NAACL 2024 (Long)

Zhou, Zhu, Antognini, Kim, Zhang (2024) — NAACL 2024 (pp.2793–2804)

## ソースからの事実
- 数学問題の**表層形のわずかな変更**で答えの分布・solve rate が大きく変わり、LLM の推論は表層形に**敏感で頑健性を欠く** [source](../../../sources/Reasoning/paraphrase-and-solve-scop.md)
- 緩和策 **SCoP (Self-Consistency-over-Paraphrases)**: 問題の言い換えで推論経路を多様化して self-consistency を取る。4数学ベンチ×3 LLM で vanilla を上回り、**特に初期に解けない問題で改善** [source](../../../sources/Reasoning/paraphrase-and-solve-scop.md)
- 追加分析: cross-model difficulty agreement、paraphrasing transferability、**Variance of Variations (VOV)** [source](../../../sources/Reasoning/paraphrase-and-solve-scop.md)

→ 詳細: [evidence](../../../evidence/Reasoning/paraphrase-and-solve-scop.md)

## 現時点の解釈

[GSM-Symbolic](gsm-symbolic.md) が「数値や項を変えるだけで数学推論がばらつく」と示したのと**同型の脆弱性**を、**表層形(言い換え)**の軸で示した論文。両者は「LLM は問題の意味でなく**表層パターン**に依存して解いている」という [LLMと真の論理的理解の壁](../../topics/Reasoning/llm-logical-understanding-wall.md) ポジションの経験的支柱。

SCoP は self-consistency の拡張で、脆弱性を**推論時に緩和**するが、根本原因（表層形依存）を除去はしない。この「症状の緩和に留まる」点は、壁が学習・推論レシピで容易に消えないことの傍証でもある。

## 関連ページ
- [[llm-logical-understanding-wall]] — 本論文を含むポジション
- [GSM-Symbolic](gsm-symbolic.md) — 数値摂動での数学推論のばらつき（同型の脆弱性）
- [RobustLR](robustlr.md) — 論理摂動版（演繹推論）
- [Potemkin Understanding](potemkin-understanding.md) — 脆弱性のメタ評価的一般化

## 未解決の問い
- 表層形依存は、より大規模・推論特化モデルでどこまで縮減するか
- SCoP のような推論時緩和の上限はどこか（根本対処は学習側で可能か）
