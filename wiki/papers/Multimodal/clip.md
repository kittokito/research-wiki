---
title: "Learning Transferable Visual Models From Natural Language Supervision (CLIP)"
aliases: ["CLIP", "Contrastive Language-Image Pre-training"]
created: 2026-04-30
updated: 2026-04-30
tags: [CLIP, contrastive-learning, vision-language, zero-shot, multimodal, foundation-model, image-text-pretraining]
peer_review: accepted
venue: "ICML 2021 (PMLR v139)"
sources: [src-clip]
---

# CLIP: Learning Transferable Visual Models From Natural Language Supervision

> **査読**: ✅ accepted — ICML 2021 (PMLR v139, pp.8748-8763)

Radford, Kim, Hallacy, Ramesh, Goh, Agarwal, Sastry, Askell, Mishkin, Clark, Krueger, Sutskever (2021) — arXiv 2103.00020 / OpenAI

## 主要な図表

![Figure 1: CLIPの contrastive 事前学習（左）と zero-shot 分類への適用（右）](../../../figures/Multimodal/clip/clip-overview.png)
*出典: 論文 Figure 1（OpenAI公式リポジトリの概要図）。左：N枚の画像とN個のテキストキャプションをそれぞれの encoder で埋め込み、N×N類似度行列のうち正しいペア（対角）が高くなるよう contrastive loss で訓練。右：推論時はクラス名を "a photo of a {object}." の形でテキスト埋め込み化し、画像埋め込みとの cosine similarity で最も近いクラスを選ぶ — zero-shot 分類器。*

## ソースからの事実
- 4億の (image, text) ペアを web から収集（**WIT: WebImageText**）し、画像-キャプション対応予測の contrastive 目的関数で事前学習 [source: §2](../../../sources/Multimodal/clip.md)
- ImageNet zero-shot で **ResNet-50 fully supervised と同等の 76.2% top-1**（ViT-L/14@336px）。CLIP は ImageNet を1枚も訓練に使っていない [source: §3.1](../../../sources/Multimodal/clip.md)
- 30+ の視覚データセットでゼロショット転移を評価。OCR・ビデオ動作認識・地理位置推定・細粒度分類など多様な領域で非自明な性能 [source: §3.1](../../../sources/Multimodal/clip.md)
- distribution shift（ImageNet-V2, -R, -A, -Sketch, ObjectNet）に対して fully supervised モデルより **頑健**、effective robustness gap が大幅縮小 [source: §3.3](../../../sources/Multimodal/clip.md)
- 当初の captioning（生成）目的より **contrastive 目的の方が4倍効率的** に zero-shot 性能を伸ばす [source: §2.3](../../../sources/Multimodal/clip.md)
- linear probe 27データセット平均で EfficientNet-NoisyStudent / SimCLRv2 / BYOL 等の強い表現を上回る [source: §3.2](../../../sources/Multimodal/clip.md)

→ 詳細: [evidence](../../../evidence/Multimodal/clip.md)

## 現時点の解釈
**「視覚-言語基盤モデル」というカテゴリそのものを作った論文**。技術的本体（contrastive image-text pretraining）は LiT、ALIGN、SigLIP 等で改良されているが、CLIP がデモした以下の事実が後続全てに継承された：

1. **データ規模 × 自然言語 supervision のスケーリング**：固定ラベル集合からの解放。web からの自然な (image, alt-text) ペアが ImageNet 22k より遥かに広いカバレッジを持つ
2. **言語が分類器を「動的に書き換える」インターフェース**：クラスを増やすのに再訓練不要。これが現在の open-vocabulary detection / segmentation / retrieval の前提
3. **頑健性の副産物**：分布シフトに対する強さが「広いデータでの言語整列」の自然な帰結であること

実用面では、現在の主要 multimodal LLM（LLaVA, BLIP-2, Flamingo, MiniGPT-4 等）の **vision tower** はほぼ全て CLIP-ViT-L/14 系。Stable Diffusion / DALL-E 2 等の text-to-image 生成も CLIP テキストエンコーダ条件に依存する。**CLIP は研究対象というより既にインフラ** であり、新しい研究はその後継（SigLIP 2、DINOv2-based vision tower、native multimodal pretraining 等）に移っている。

ただし弱点も明確：細粒度分類・抽象タスク・OOD・typographic attack 脆弱性は LiT / SigLIP / EVA-CLIP / DINOv2 等で部分的に解消されつつある。「CLIP のどこが本質で、どこが副次的アーティファクトか」は未だ議論中。

## 関連ページ
- [Video models are zero-shot learners and reasoners](video-models-zero-shot-learners.md) — Veo 3 のビデオゼロショット汎化、CLIP の画像版主張をビデオに拡張
- [V-JEPA 2](../Physical_AI/v-jepa-2.md) — 自己教師あり動画モデル、テキスト整列に頼らない動画基盤モデル路線
- [Qwen3.5-Omni](../Technical_Report/qwen35-omni.md) — text + vision + audio + video の統合 omni-modal、CLIP 系統の延長

## 未解決の問い
- contrastive image-text の本質的な scaling 上限はどこか？SigLIP 2 / EVA-CLIP の改良はパラメトリックに見ると限界に近づいているのか？
- CLIP-ViT-L/14 が依然として MLLM の標準 vision tower である理由は **慣性** か **本質的優位性** か？DINOv2 / SAM-ViT 等への置換可能性は？
- 自然言語 supervision は本当に「教師信号として優れている」のか、それとも「web の規模に乗せやすい proxy」だったのか？
- typographic attack のような脆弱性は CLIP 系全般に内在するのか、特定の訓練レシピの結果か？
