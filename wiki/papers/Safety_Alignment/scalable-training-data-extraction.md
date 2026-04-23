---
title: "Scalable Extraction of Training Data from (Production) Language Models"
aliases: ["Divergence Attack", "Training Data Extraction"]
created: 2026-04-15
updated: 2026-04-15
tags: [privacy, memorization, alignment-bypass, data-extraction, adversarial-attack]
peer_review: accepted
venue: "ICLR 2025"
sources: [src-scalable-training-data-extraction]
---

# Scalable Extraction of Training Data from (Production) Language Models

> **査読**: ✅ accepted — ICLR 2025

## ソースからの事実
- 単一トークン単語の反復指示（divergence attack）によりChatGPTが学習データを通常の150倍の速度で漏洩 [source](../../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- 約$200の費用で10,000件以上のユニークな逐語的メモリゼーション系列をChatGPTから抽出 [source](../../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- gpt-3.5-turbo-instructが同一系列の75%を復元 — アラインメントはメモリゼーションを隠蔽するだけで除去しない [source](../../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- 抽出データにはPII（メール、電話番号、住所; テスト生成の16.9%）、コード、文学作品、URL、暗号識別子を含む [source](../../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- オープンソースモデル（GPT-Neo 6B, Pythia 6.9B, RedPajama 7B等）では10億トークン生成から数十万〜数百万のユニーク系列を抽出 [source](../../../sources/Safety_Alignment/scalable-training-data-extraction.md)

→ 詳細: [evidence](../../../evidence/Safety_Alignment/scalable-training-data-extraction.md)

## 現時点の解釈

本論文の核心的インサイトは「アラインメントはプライバシー保護にならない」という点にある。RLHF等のアラインメント手法はモデルの振る舞いを変えるが、学習データのメモリゼーション自体は事前学習時に固定され、ファインチューニングでは除去されない。Divergence attackは巧妙だが原理は単純で、アラインメントの行動制約を迂回して基盤モデルの生成モードに「リセット」させるだけである。

これはLLMプロバイダにとって、アラインメントをプライバシー対策として位置づけることのリスクを示す。プライバシー保護には学習データの事前処理（PII除去・重複排除の徹底）や差分プライバシーなど、モデルの重み自体に情報を残さないアプローチが必要となる。

2024年以降のモデル（GPT-4o, Claude等）がこの攻撃を修正済みかは公開情報が限られるが、divergence attackの具体的パターンへのパッチは容易でも、根本的なメモリゼーションの問題は解決されていない可能性が高い。

## 関連ページ
- [Sycophantic Delusional Spiraling](../Safety_Alignment/sycophantic-delusional-spiraling.md) — アラインメントの別の脆弱性
- [AI Agent Traps](../Safety_Alignment/ssrn-6372438.md) — LLMに対する攻撃の体系化

## 未解決の問い
- GPT-4o、Claude等の最新モデルはdivergence attackに対して根本的に堅牢か、それとも同種の攻撃が未発見なだけか？
- 差分プライバシー付き学習は実用的なスケールでメモリゼーションをどの程度低減できるか？
- メモリゼーション量とモデル性能のトレードオフはどこにあるか？
