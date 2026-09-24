---
source: src-survey-on-negative-transfer
date_extracted: 2026-06-09
---

# A Survey on Negative Transfer からの抽出

## 主要な主張
- transfer learning の有効性は常に保証されるわけではなく、**negative transfer (NT)**——source の知識利用が target の学習性能を**低下させる**——は TL の長年の難問 [source](../../sources/Surveys_Overview/survey-on-negative-transfer.md)
- NT は特に **target domain にラベル付きデータがほとんど/全く無い**場合（アノテーション費用・プライバシー等）に重要な問題となる [source](../../sources/Surveys_Overview/survey-on-negative-transfer.md)
- これまで **NT の定式化・発生要因・緩和アルゴリズムを体系的に扱ったサーベイは存在しなかった**——本論文がそのギャップを埋める [source](../../sources/Surveys_Overview/survey-on-negative-transfer.md)

## 主要な貢献
- **NT の定義と発生要因**の導入
- 約50の代表的手法を **4カテゴリ**で整理 [source](../../sources/Surveys_Overview/survey-on-negative-transfer.md):
  - **secure transfer**（負の転移を起こさない安全な転移）
  - **domain similarity estimation**（ドメイン類似度の推定で転移可否を判断）
  - **distant transfer**（遠いドメイン間の転移）
  - **NT mitigation**（負の転移の緩和）
- **関連分野での NT** も議論: multi-task learning、lifelong learning、adversarial attacks [source](../../sources/Surveys_Overview/survey-on-negative-transfer.md)

## 制限・注意点
- 2020年提出のサーベイ（2022年ジャーナル掲載）で、対象は古典的 transfer learning / domain adaptation 中心。大規模 LLM 時代の転移（PEFT・instruction tuning 等）は射程外
- サーベイであり新規手法の提案・実験は行わない

## ベンチマーク結果
（サーベイのため該当なし）

## 実装関連
- 「domain similarity estimation で転移可否を事前判断する」という設計指針は、後年の [SHLPT](../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md) の「学習可能な類似度メトリックでタスクを分割」する発想に通じる
