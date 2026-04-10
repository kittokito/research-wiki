---
source: src-neural-thickets
date_extracted: 2026-04-07
---

# Neural Thickets からの抽出

## 主要な主張
- 事前学習重みの近傍に多様なタスク固有のエキスパートソリューションが密集して存在 [source](../../sources/Post_Training/neural-thickets.md)
- 小さなモデルではエキスパートの占める体積が最小限で勾配降下による発見が必要 [source](../../sources/Post_Training/neural-thickets.md)
- 大規模で十分に事前学習されたモデルではエキスパートが実質的な割合で存在 [source](../../sources/Post_Training/neural-thickets.md)
- N個のランダムパラメータ摂動サンプリング→上位K選択→多数決アンサンブルでPPO・GRPO・ESと競争力のある結果 [source](../../sources/Post_Training/neural-thickets.md)

## 主要な貢献
- 事前学習モデルの「ニューラル叢」仮説
- 並列事後学習手法（ランダム摂動+アンサンブル）

## 制限・注意点
- アンサンブルのためN個のモデルを保持する必要がありメモリコストが高い可能性
