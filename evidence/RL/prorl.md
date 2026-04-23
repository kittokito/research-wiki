---
source: src-prorl
date_extracted: 2026-04-16
---

# ProRL からの抽出

## 主要な主張
- 長期RL訓練（2,000+ステップ）はベースモデルのサンプリングでは到達不可能な新しい推論戦略を発見する [source](../../sources/RL/prorl.md)
- 標準的なRLVRが「filtering」に見えるのは訓練期間が短すぎるため [source](../../sources/RL/prorl.md)
- ベースモデルの出発性能が低いほどRLによる改善幅が大きい（逆相関） [source](../../sources/RL/prorl.md)

## 主要な貢献
- KLダイバージェンス制御＋参照ポリシーリセット＋多タスク多様性によるProRL手法の提案
- Nemotron-Research-Reasoning-Qwen-1.5B: 数学+14.7%, コード+13.9%, 論理パズル+54.8%, STEM+25.1%
- 未知タスク・高難度問題へのOOD汎化の実証

## ベンチマーク結果
| ベンチマーク | 改善幅 | 備考 |
|---|---|---|
| Math (pass@1) | +14.7% | vs base model |
| Code (pass@1) | +13.9% | vs base model |
| Logic Puzzles | +54.8% | vs base model |
| STEM | +25.1% | vs base model |

## 制限・注意点
- 1.5Bモデルでの検証が中心、大規模モデルでの再現性は未確認
- NVIDIA社内研究であり、独立した第三者追試はまだ少ない
