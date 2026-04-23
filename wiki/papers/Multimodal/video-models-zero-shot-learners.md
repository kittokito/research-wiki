---
title: "Video models are zero-shot learners and reasoners"
aliases: ["Veo 3 zero-shot", "Video foundation models"]
created: 2026-04-21
updated: 2026-04-21
tags: [video-foundation-model, Veo-3, zero-shot, emergent-capability, visual-reasoning, multimodal]
peer_review: preprint
venue: ""
sources: [src-video-models-zero-shot]
---

# Video models are zero-shot learners and reasoners

> **査読**: 📝 preprint （ICLR 2026 に投稿 → Rejected_Submission, OpenReview MCWypEBtlF）

Wiedemer, Li, Vicol et al. (2025) — arXiv 2509.20328 / Google DeepMind

## ソースからの事実
- Veo 3 は **明示的に訓練されていない多様なタスク** をゼロショットで解ける：オブジェクトセグメンテーション、エッジ検出、画像編集、物理特性理解、アフォーダンス認識、道具使用シミュレーション [source](../../../sources/Multimodal/video-models-zero-shot-learners.md)
- 迷路解き・対称性解きなど **初期的な visual reasoning** の発現を実証 [source](../../../sources/Multimodal/video-models-zero-shot-learners.md)
- 「大規模・生成的・web-scaleデータ」というLLMを汎用言語基盤モデルにしたプリミティブが、現代の video model にもそのまま当てはまるという観察 [source](../../../sources/Multimodal/video-models-zero-shot-learners.md)

→ 詳細: [evidence](../../../evidence/Multimodal/video-models-zero-shot-learners.md)

## 現時点の解釈
LLMでの「scaling + 生成事前学習 → 汎用性」が視覚領域でも再現しつつあるという **強い主張** を定性事例で支える論文。V-JEPA 2（Meta）・DreamZero（身体性）と並んで「動画基盤モデル = 世界モデル = 汎用視覚AI」という大きな方向性を形成する。ただし評価が定性中心で、ICLR 2026 では Rejected されており、「定量的SOTA比較の不足」「cherry-picking 懸念」が査読側の焦点だった可能性が高い。**主張の方向性は重要だが、厳密検証は別論文（V-JEPA 2 等）に託される構図**。Veo 3 自体がクローズドモデルである点も学術再現性の壁で、主張の検証はオープンなvideo modelでの追試待ち。

## 関連ページ
- [V-JEPA 2](../Physical_AI/v-jepa-2.md) — 自己教師あり動画モデル、ロボット理解・予測・計画
- [DreamZero](../Physical_AI/dreamzero-world-action-models.md) — ビデオ拡散によるゼロショットロボットポリシー
- [Scaling Laws of Motion Forecasting and Planning](../Physical_AI/scaling-laws-motion-forecasting-planning.md) — スケーリング則の物理領域への拡張

## 未解決の問い
- Veo 3 の「emergent zero-shot」はパラメータ数・データ量のスケーリングと比例するか、それとも質的閾値を超えたときに発現するか？
- 迷路・対称性以外の難しい視覚推論（多段因果推論、抽象パターン認識）でもゼロショットが成立するか？
- オープン video model（Wan 等）で同様のゼロショット能力は再現するか？ Veo 3 特有の何が効いているか？
- ICLR 2026 での Rejection 理由（公開査読コメント）は主張のどの部分を否定したか？
