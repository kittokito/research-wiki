---
source: src-dreamzero-world-action-models
date_extracted: 2026-04-07
---

# DreamZero World Action Models からの抽出

## 主要な主張
- ビデオ拡散を用いて将来の世界状態とアクションを予測するDreamZeroを提案 [source](../../sources/Physical_AI/dreamzero-world-action-models.md)
- 新規タスク・環境への汎化でSOTA VLAに対して2倍以上の改善 [source](../../sources/Physical_AI/dreamzero-world-action-models.md)
- 7Hzのリアルタイム閉ループ制御を実現 [source](../../sources/Physical_AI/dreamzero-world-action-models.md)
- 限られたデモデータでクロスエンボディメント転移において未見タスク性能で42%以上の相対改善 [source](../../sources/Physical_AI/dreamzero-world-action-models.md)

## 主要な貢献
- DreamZero: World Action Model
- ゼロショットポリシーとしての世界モデル活用

## ベンチマーク

| ベンチマーク | スコア | 備考 |
|---|---|---|
| 新規タスク汎化 | 2×以上改善 | vs SOTA VLA |
| 未見タスク性能 | +42%相対改善 | クロスエンボディメント |
| 制御周波数 | 7Hz | リアルタイム閉ループ |

## 制限・注意点
- 限られたデモデータ条件での評価
