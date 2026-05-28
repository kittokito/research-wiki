---
id: src-deepseek-v4
title: "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence"
authors: ["DeepSeek-AI"]
year: 2026
url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf"
type: paper
peer_review: n/a
venue: ""
tags: [technical-report, open-weight, MoE, hybrid-attention, CSA, HCA, mHC, long-context, million-token, DSA, Muon, DeepSeek, on-policy-distillation, FP4, TileLang]
date_added: 2026-05-11
status: processed
---

# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

## 概要
DeepSeek-AIによるDeepSeek-V4シリーズのpreview版テクニカルレポート。**DeepSeek-V4-Pro（1.6T total / 49B active）** と **DeepSeek-V4-Flash（284B total / 13B active）** の2つのMoE言語モデル、共に **ネイティブ1Mトークンcontext** をサポート。主要なアーキテクチャ革新は3点: (1) **hybrid attention** — Compressed Sparse Attention (CSA) と Heavily Compressed Attention (HCA) をinterleaveに配置し long-context 効率を抜本改善、(2) **Manifold-Constrained Hyper-Connections (mHC)** で従来のresidual connectionを多様体制約付きに強化、(3) **Muon optimizer** で収束と訓練安定性を改善。pre-trainingはFlash 32T tokens / Pro 33T tokens。**1Mトークンcontext時の single-token推論FLOPsはDeepSeek-V3.2比でV4-Pro 27% / V4-Flash 10%**、**KV cacheはV4-Pro 10% / V4-Flash 7%**。Post-trainingは "Specialist Training（SFT+GRPO）→ On-Policy Distillation (OPD) で統合" の2段構成（DeepSeek-V3.2のmixed RLをOPDで置換）。**Think Max / Think High / Non-thinkの3 reasoning effort モード** を提供、最大effort版「DeepSeek-V4-Pro-Max」がopen modelのSOTAを更新。FP4 quantization-aware training、TileLang DSL、batch-invariant deterministic kernels、anticipatory routing、SwiGLU clamping等の infrastructure 工夫を多数公開。

## メモ
DeepSeek-AI公式 HuggingFace https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro でPDF・inference実装公開。MIT License、4.48 MB PDF（55+ページ）。著者は "DeepSeek-AI"（個別著者リストは Appendix A）。**CSAは [DeepSeek-V3.2](https://github.com/deepseek-ai/DeepSeek-V3.2)（2025）のDeepSeek Sparse Attention (DSA) を内包し、KV cacheを更にm倍圧縮してからDSA top-k を適用** する2段構成。HCAは更に強い圧縮率 m'（≫m）でKVを1エントリに統合し dense attention を維持（sparse でない）。**mHCは本リポジトリ既存ページ [Xie et al., 2025](../Architecture/manifold-constrained-hyper-connections.md) の理論を実装適用** した最初の大規模事例。Muonは Jordan/Liu 2024-2025 系列のNewton-Schulz orthogonalization optimizer、AdamWはembedding/output head/RMSNorm/mHC/static biasesにのみ使用。Anticipatory Routing（routing indices を θ_{t-Δt} で計算しloss spike抑制）と SwiGLU clamping ([-10, 10]) が training instability 緩和のキー。Post-trainingで mixed RL を On-Policy Distillation (OPD) で置換した点は [willccbb/Claude Opus 4.7のOPDメタ分析](../RL/willccbb-sft-rl-opd.md) のSDFT/OPSDダイアル整理と直接連関、DeepSeek-V4 が実プロダクションでOPD移行した最初の主要事例。"DeepSeek-V4-Pro-Max" は post-training の Think Max mode を指し、別モデルではない。査読n/a（テクニカルレポート、HuggingFace公開）。
