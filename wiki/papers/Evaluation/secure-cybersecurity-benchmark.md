---
title: "SECURE: Benchmarking Large Language Models for Cybersecurity"
aliases: ["SECURE benchmark", "SECURE"]
created: 2026-04-15
updated: 2026-04-15
tags: [cybersecurity, benchmark, ICS, evaluation, LLM-reliability]
peer_review: accepted
venue: "ACSAC 2024"
sources: [src-secure-cybersecurity-benchmark]
---

# SECURE: Benchmarking Large Language Models for Cybersecurity

> **査読**: ✅ accepted — ACSAC 2024

## ソースからの事実
- ICSセクター特化の6データセット（MAET, CWET, KCV, VOOD, RERT, CPST）で知識抽出・理解・推論を評価 [source](../../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- ChatGPT-4が6タスク中4タスクで最高性能、Llama3-70BはCWE知識でのみ上回る [source](../../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- 文脈なしOOD検出（VOOD）で最も大きな性能差が発生: ChatGPT-4（87.9%）に対しChatGPT-3.5は8.4%、Llama3-70Bは27.1%に劣化 [source](../../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- 知識抽出タスクでは全モデル80%前後で比較的均質、差が出るのは理解・推論タスク [source](../../../sources/Evaluation/secure-cybersecurity-benchmark.md)

→ 詳細: [evidence](../../../evidence/Evaluation/secure-cybersecurity-benchmark.md)

## 現時点の解釈

SECUREはサイバーセキュリティ領域のLLM評価として、単なる知識QAに留まらず「OOD検出」「CVSS計算」など実務的判断力を測る点に価値がある。VOODでの壊滅的な性能差は、LLMが「知っている知識を引き出す」能力と「知らないことを知らないと認識する」能力の間に大きなギャップがあることを示唆しており、セキュリティのような高リスク領域でのLLM運用には信頼度推定の仕組みが不可欠であることを裏付ける。

ただし、ICSセクター限定・2024年時点のモデル評価という制約は大きく、最新モデル（Claude、GPT-4oなど）や汎用セキュリティタスクへの一般化には追試が必要。

## 関連ページ
- [SWE-CI](../Evaluation/swe-ci.md) — コードベース保守能力の評価ベンチマーク
- [P-hacking with one prompt](../Evaluation/p-hacking-with-one-prompt.md) — LLM評価の信頼性問題
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — サイバーセキュリティ性能が際立つモデル

## 未解決の問い
- 最新モデル（Claude Opus 4.6, GPT-4o等）でVOODの性能差は縮小しているか？
- ICS以外のサイバーセキュリティ領域（Web脆弱性、マルウェア分析等）に拡張した場合、同様の傾向が見られるか？
