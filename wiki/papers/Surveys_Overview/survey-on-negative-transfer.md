---
title: "A Survey on Negative Transfer"
aliases: ["A Survey on Negative Transfer", "negative transfer survey", "NT survey"]
created: 2026-06-09
updated: 2026-06-09
tags: [negative-transfer, transfer-learning, survey, domain-adaptation, multi-task-learning, lifelong-learning]
peer_review: accepted
venue: "IEEE/CAA Journal of Automatica Sinica 2022"
sources: [src-survey-on-negative-transfer]
---

# A Survey on Negative Transfer

> **査読**: ✅ accepted — IEEE/CAA Journal of Automatica Sinica 2022

Zhang, Deng, Zhang, Wu (2022) — arXiv 2009.00909

## ソースからの事実
- **negative transfer (NT)** = source のデータ/知識を使うことで target の学習性能が**低下**する現象。TL の長年の難問 [source](../../../sources/Surveys_Overview/survey-on-negative-transfer.md)
- NT の定式化・要因・緩和を体系的に扱った**初のサーベイ**。約50手法を **4カテゴリ**（**secure transfer / domain similarity estimation / distant transfer / NT mitigation**）で整理 [source](../../../sources/Surveys_Overview/survey-on-negative-transfer.md)
- multi-task learning・**lifelong learning**・adversarial attacks における NT も議論 [source](../../../sources/Surveys_Overview/survey-on-negative-transfer.md)

→ 詳細: [evidence](../../../evidence/Surveys_Overview/survey-on-negative-transfer.md)

## 現時点の解釈

転移学習における **negative transfer** の概念地図を与えるサーベイで、本リポジトリの post-training / 継続学習系の論文を読む際の**上位概念**として機能する。とくに直前に追加した [SHLPT](../Post_Training/shlpt-lifelong-prompt-tuning.md) はこのサーベイの枠組みの **LLM・lifelong prompt tuning における具体的実装**として読める:

- **domain similarity estimation の系譜**: 本サーベイが NT 緩和の一カテゴリに挙げる「ドメイン類似度の推定で転移可否を判断」は、[SHLPT](../Post_Training/shlpt-lifelong-prompt-tuning.md) の「**学習可能な類似度メトリックでタスクを類似/非類似に分割**」する設計の直接の先祖。SHLPT は本サーベイの「secure transfer × similarity estimation」を prompt tuning に持ち込んだ例と位置づけられる。
- **post-training の能力 conflict との接続**: [SFT Data Composition (DMT)](../Post_Training/sft-data-composition.md) が報告する「数学/コード/一般能力の干渉・catastrophic forgetting」は、NT を **タスク（能力）間**で捉えた現れ。本サーベイの NT 要因論はその一般的背景を与える。
- **多言語転移の定量化**: [ATLAS: Multilingual Scaling Laws](../Pretraining/atlas-multilingual-scaling-laws.md) は1444言語ペアの転移行列で**正/負の転移**を定量化し、scratch vs finetune のクロスオーバー点を同定する——本サーベイの NT を大規模・定量的に観測した現代版。
- **継続学習との重なり**: 本サーベイが扱う lifelong learning の NT は、[Learning, Fast and Slow](../RL/learning-fast-and-slow.md) の plasticity / 継続適応の議論と同じ問題系。

2020年提出（2022年掲載）で対象は古典的 TL/domain adaptation 中心のため、LLM 時代の転移（PEFT・instruction tuning）は射程外。だが「いつ・なぜ転移が害になるか」「類似度で転移可否を測る」という枠組みは、現在の post-training 設計にそのまま効く。

## 関連ページ
- [SHLPT: Similarity Heuristic Lifelong Prompt Tuning](../Post_Training/shlpt-lifelong-prompt-tuning.md) — 本サーベイの「類似度推定 × NT 緩和」を lifelong prompt tuning で具体化
- [SFT Data Composition / DMT](../Post_Training/sft-data-composition.md) — 能力間の干渉・忘却（タスク間 NT の現れ）
- [ATLAS: Multilingual Scaling Laws](../Pretraining/atlas-multilingual-scaling-laws.md) — 多言語の正/負転移を転移行列で定量化
- [Learning, Fast and Slow (FST)](../RL/learning-fast-and-slow.md) — 継続学習・plasticity の問題系

## 未解決の問い
- 古典的 TL の NT 緩和（secure transfer / similarity estimation 等）は、LLM の PEFT・instruction tuning にどこまで移植可能か
- 「ドメイン/タスク類似度」を測る指標は、LLM スケールで何が最良か（[SHLPT](../Post_Training/shlpt-lifelong-prompt-tuning.md) の学習可能メトリック vs 表現類似度など）
- 大規模事前学習自体が暗黙の NT 緩和になっているのか、それとも別の NT を生むのか
