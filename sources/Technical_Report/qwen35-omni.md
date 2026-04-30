---
id: src-qwen35-omni
title: "Qwen3.5-Omni Technical Report"
authors: ["Qwen Team"]
year: 2026
url: "https://arxiv.org/abs/2604.15804"
type: paper
peer_review: n/a
venue: ""
tags: [technical-report, multimodal, omni-modal, audio-visual, hybrid-attention, MoE, speech-synthesis, ARIA, long-context, Qwen, vibe-coding]
date_added: 2026-04-23
status: processed
---

# Qwen3.5-Omni Technical Report

## 概要
Qwen-Omni 系列の最新版 **Qwen3.5-Omni** のテクニカルレポート。**数百億パラメータ規模** で **256k コンテキスト** をサポートするオムニモーダルモデル。テキスト・画像のヘテロ対ペアに加え **1億時間超の audio-visual コンテンツ** で学習。**215の audio / audio-visual 理解・推論・インタラクションサブタスク** で SOTA を達成し、**Gemini-3.1 Pro を主要 audio タスクで上回り、audio-visual 総合理解では同等**。アーキテクチャは **Thinker / Talker 双方で Hybrid Attention Mixture-of-Experts (MoE)** を採用、効率的な長系列推論を実現。**10時間超の audio 理解**、1 FPS で **400秒の 720P 動画** に対応。ストリーミング音声合成の不安定性（text tokenizer と speech tokenizer の符号化効率ミスマッチ）に対し、text/speech 単位を動的整列する **ARIA** を導入し、安定性と韻律を最小レイテンシで改善。10言語の多言語音声理解・生成を感情表現つきでサポート。script-level 構造化キャプションと精密な temporal synchronization で superior な audio-visual grounding を実現。**Audio-Visual Vibe Coding**（音声・映像の指示からの直接コード生成）という新規創発能力を観測。

## メモ
cs.CL / eess.AS。Qwen Team（Alibaba）。v1: 2026-04-17、v2: 2026-04-21。**Hybrid Attention MoE** は [MiniMax-M1](./minimax-m1.md)（lightning attention + hybrid MoE）と同系統の設計で、**大規模omni-modalでのhybrid attentionの有効性の追加事例**として位置付けられる。Thinker（理解・推論）と Talker（発話生成）を分離するアーキテクチャは Qwen-Omni 系列の継続。Audio-Visual Vibe Coding は [Video models are zero-shot learners](../Multimodal/video-models-zero-shot-learners.md) 系の「明示訓練外タスクの創発」と呼応する現象。
