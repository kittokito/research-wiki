---
id: src-qwen3
title: "Qwen3 Technical Report"
authors: ["Qwen Team"]
year: 2025
url: "https://arxiv.org/abs/2505.09388"
type: paper
peer_review: n/a
venue: ""
tags: [technical-report, open-weight, dense, MoE, multilingual, thinking-mode, thinking-budget, strong-to-weak-distillation, GRPO, Qwen, QK-Norm, multi-stage-pretraining, instance-level-data-mixture, synthetic-data, Apache-2.0]
date_added: 2026-05-11
status: processed
---

# Qwen3 Technical Report

## 概要
Alibaba Qwen Team による Qwen3 シリーズのテクニカルレポート。**dense 6 モデル**（0.6B / 1.7B / 4B / 8B / 14B / 32B）と **MoE 2 モデル**（30B-A3B / 235B-A22B）の8モデルを Apache 2.0 で公開。フラッグシップは **Qwen3-235B-A22B**（235B total / 22B active、128 experts うち8 active、94層）。

**アーキテクチャ**は Qwen2.5 系列を踏襲しつつ、attention に **QK-Norm**（QK softmax 前の RMSNorm）を導入し QKV-bias を除去、訓練安定性を改善。GQA / SwiGLU / RoPE / pre-RMSNorm。MoE は **shared expert を廃止** し（Qwen2.5-MoE と異なる）、**global-batch load balancing loss** で expert 特化を促進。**最大 context 128K**。

**データ戦略**: pre-training は **36T tokens / 119 言語・方言**（Qwen2.5 比でデータ量2倍・言語数3倍）。**Qwen2.5-VL で PDF からテキスト抽出 + Qwen2.5-Math/Coder で合成データ生成** のパイプライン、**インスタンスレベルでデータミックス最適化**（従来のソース／ドメインレベルではなく）。Pre-training は **3 stage**: (S1) General 30T@4K、(S2) Reasoning 5T@4K（STEM/coding 比率を上げる）、(S3) Long-Context @32K（YARN + Dual Chunk Attention で 4× sequence length 拡張）。

**Post-training** は **thinking mode と non-thinking mode を単一モデルに統合**（QwQ-32B 等の分離を解消）、**thinking budget** で計算量を動的制御可能。フラッグシップは **4 stage**: (1) Long-CoT Cold Start、(2) Reasoning RL（GRPO、170 step で AIME'24 70.1→85.1）、(3) Thinking Mode Fusion（continual SFT で /think /no_think フラグを統合）、(4) General RL（20+ task の reward system: rule-based / reference-based / preference-based）。軽量モデルは **Strong-to-Weak Distillation**（off-policy → on-policy distillation、4 stage 訓練比 **1/10 GPU 時間**）。

ベンチマーク: Qwen3-235B-A22B (Thinking) が AIME'24 85.7 / AIME'25 81.5 / LiveCodeBench v5 70.7 / CodeForces 2056 / BFCL v3 70.8 で DeepSeek-R1 (671B/37B active) を 23 ベンチ中 17 で上回り、OpenAI-o1 / Gemini2.5-Pro と互角。

## メモ
arXiv 2505.09388 / v1: 2025-05-14。GitHub: QwenLM/Qwen3、HuggingFace: huggingface.co/Qwen。Apache 2.0 License。**本リポジトリの [Qwen3.5-Omni](./qwen35-omni.md) の前世代テキスト基盤**、Hybrid Attention MoE 化前のスタンダード MoE 設計。**OPD (On-Policy Distillation) を軽量モデルの訓練に大規模採用** した最初のオープン flagship 級事例（DeepSeek-V4 より早い 2025-05 時点）、[willccbb & Claude Opus 4.7 OPD メタ分析](../RL/willccbb-sft-rl-opd.md) の OPD ダイアル整理の主要参照点。Thinking mode unification は OpenAI o-series や Anthropic Claude の reasoning effort 制御の open-weight 対応物。**Strong-to-Weak Distillation で 4 stage 訓練比 1/10 GPU 時間** は post-training コスト削減の代表的データポイント。**Instance-level data mixture optimization** は本リポジトリの [Rewriting Pre-Training Data (SwallowCode/SwallowMath)](../Pretraining/rewriting-pretraining-data.md) と並ぶデータ品質研究の主要事例。テクニカルレポート扱い（査読 n/a）。
