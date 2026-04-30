---
title: "Qwen3.5-Omni: Hybrid Attention MoE Omnimodal Model"
aliases: ["Qwen3.5-Omni", "Qwen3.5-Omni-plus", "ARIA"]
created: 2026-04-23
updated: 2026-04-23
tags: [technical-report, multimodal, omni-modal, audio-visual, hybrid-attention, MoE, speech-synthesis, ARIA, long-context, Qwen, vibe-coding]
peer_review: n/a
venue: ""
sources: [src-qwen35-omni]
---

# Qwen3.5-Omni Technical Report

> **査読**: — n/a（テクニカルレポート）

Qwen Team (2026) — arXiv 2604.15804 / v2 (2026-04-21) / Alibaba

## ソースからの事実
- **数百億パラメータ** 規模・**256k コンテキスト**・**1億時間超の audio-visual** データで学習 [source](../../../sources/Technical_Report/qwen35-omni.md)
- **Qwen3.5-Omni-plus**: **215 audio/audio-visual ベンチマーク** で SOTA、**主要 audio タスクで Gemini-3.1 Pro を上回り**、audio-visual 総合で同等 [source](../../../sources/Technical_Report/qwen35-omni.md)
- **Hybrid Attention MoE** を Thinker（理解・推論）／Talker（発話生成）双方で採用 [source](../../../sources/Technical_Report/qwen35-omni.md)
- **10時間超の audio 理解** / **400秒の 720P 動画（1 FPS）** 処理 [source](../../../sources/Technical_Report/qwen35-omni.md)
- **ARIA**: text / speech tokenizer の符号化効率ミスマッチ問題に対し、text-speech 単位を動的整列 → ストリーミング音声合成の安定性・韻律を最小レイテンシで改善 [source](../../../sources/Technical_Report/qwen35-omni.md)
- 10言語の音声理解・生成を感情表現つきでサポート、script-level 構造化キャプションと temporal synchronization で audio-visual grounding を実現 [source](../../../sources/Technical_Report/qwen35-omni.md)
- **Audio-Visual Vibe Coding**: 音声・映像の指示から直接コード生成する創発能力を観測 [source](../../../sources/Technical_Report/qwen35-omni.md)

→ 詳細: [evidence](../../../evidence/Technical_Report/qwen35-omni.md)

## 現時点の解釈
Qwen3.5-Omni の位置付けは **「omni-modal（text + vision + audio + video）× hybrid attention MoE × 実用的長系列（10時間 audio / 400秒 video / 256k context）」** の交差点。2025-2026 の大規模LLM競争で、**hybrid attention（softmax + linear/lightning attention の混在）が long-context omni-modal の標準技術** になりつつあることを示す事例として重要。[MiniMax-M1](./minimax-m1.md) が「hybrid MoE + lightning attention」で推論向けに 1M コンテキストを実現したのと同系統の設計思想で、**Qwen3.5-Omni は同じ方向性を audio/video に拡張**した。

**ARIA** の貢献は実務的に大きい: 従来のストリーミングTTS系が直面してきた「text tokenizer と speech tokenizer の符号化粒度のミスマッチ」という技術的ボトルネックを、動的アライメントで解消する。Emotional nuance つき10言語音声生成と併せて、**対話エージェントの音声層のUX** を実用レベルに引き上げる論文。

**Audio-Visual Vibe Coding** は興味深い創発現象で、[Video models are zero-shot learners and reasoners](../Multimodal/video-models-zero-shot-learners.md) の「明示訓練外タスクの創発」と同じ方向性の観察。Veo 3 が視覚中心だったのに対し、Qwen3.5-Omni は **audio + video 同時指示 → コード生成** という別モダリティ組み合わせで創発を示しており、omni-modal の一般的性質として「訓練データ分布を跨ぐ能力が自然発生する」可能性を示唆する。

**Gemini-3.1 Pro 超え** の主張は Qwen チーム選定の benchmark 群での結果で、独立検証待ち。ただし215 subtask での網羅的評価は、audio ドメインにおけるオープン／半オープンモデルの SOTA 主張としては現状最も強い部類。[Kimi K2.5](./kimi-k25.md)（visual agentic multimodal）がエージェント軸、[MiniMax-M1](./minimax-m1.md) が推論軸だったのに対し、Qwen3.5-Omni は **audio-visual 軸** のomni-modal 頂点を狙う位置取り。

**2026年4月公開** のモデルで本wiki現時点（2026-04-23）で最新の大規模技術レポート。オープンウェイト公開可否は原文要確認（Qwenシリーズは通常オープンだが、Omni-plus は商用の可能性）。

## 関連ページ
- [MiniMax-M1](./minimax-m1.md) — hybrid attention MoE の同系統設計、推論軸 vs Qwen3.5-Omni の audio-visual 軸
- [Kimi K2.5](./kimi-k25.md) — visual agentic multimodal、エージェント軸の omni-modal
- [Video models are zero-shot learners and reasoners](../Multimodal/video-models-zero-shot-learners.md) — omni-modal 創発（Audio-Visual Vibe Coding と呼応）
- [Attention Residuals](../Architecture/attention-residuals.md) — Kimi Linear 系の注意機構改良、hybrid attention系譜
- [Memory Sparse Attention](../Architecture/memory-sparse-attention.md) — long-context 注意機構
- [Sarashina-Embedding-v2](../Domain_Specific/sarashina-embedding-v2.md) — 多言語（日本語）特化埋め込み、言語拡張との接続

## 未解決の問い
- Qwen3.5-Omni の Hybrid Attention MoE における softmax / linear の層混在比率は？[MiniMax-M1](./minimax-m1.md) と比べてどう異なるか？
- ARIA の tokenizer ミスマッチ整列は他の TTS / omni-modal（Kimi / Gemini）に移植可能か？
- Audio-Visual Vibe Coding の定量評価（成功率・タスク範囲・コード品質）はどの程度報告されているか？
- 215 ベンチマークの選定基準と、Gemini-3.1 Pro 比較での未公開タスク群の成績は？
- 10時間 audio / 400秒 video という長系列での実効理解性能は、needle-in-haystack 的評価でどこまで堅牢か？
- Qwen3.5-Omni-plus（topモデル）のオープンウェイト公開方針は？商用API only か？
- Audio-Visual Vibe Coding は scaling で伸びるか、特定データ構成に依存する現象か？
