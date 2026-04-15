---
source: src-lottery-ticket-hypothesis
date_extracted: 2026-04-10
---

# The Lottery Ticket Hypothesis からの抽出

## 主要な主張
- 密に初期化されたフィードフォワードネットワークにはサブネットワーク（winning tickets）が含まれ、単独で訓練しても元のネットワークと同等のテスト精度に到達可能 [source](../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)
- 標準的なプルーニング手法で、訓練を効果的にする初期重みを持つサブネットワークを自然に発見できる [source](../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)
- winning ticketは「初期化の宝くじ」に当選している — 接続の初期重みが訓練を特に効果的にする [source](../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)
- 既存のプルーニング手法は訓練済みネットワークのパラメータ数を90%以上削減可能だが、プルーニング後のスパースアーキテクチャはスクラッチからの訓練が困難 [source](../../sources/Efficiency_Optimization/lottery-ticket-hypothesis.md)

## 主要な貢献
- 宝くじ仮説（Lottery Ticket Hypothesis）の提唱
- winning ticketを特定するアルゴリズム（iterative magnitude pruning + weight rewinding）
- MNIST・CIFAR10での体系的な実験的検証

## ベンチマーク結果
| ベンチマーク | スコア | 備考 |
|---|---|---|
| winning ticket size | 元のサイズの10-20%未満 | MNIST・CIFAR10の全結合・畳み込みアーキテクチャ |
| 学習速度 | 元ネットワークより高速 | 10-20%サイズ以上のwinning ticketの場合 |
| テスト精度 | 元ネットワークと同等以上 | 同等イテレーション数 |

## 制限・注意点
- 実験はMNIST・CIFAR10の比較的小規模なアーキテクチャに限定
- 大規模モデル（ImageNet規模）への直接適用には後続研究（weight rewinding等）が必要
- winning ticketの発見には事前に一度フル訓練→プルーニングが必要（訓練コスト削減は推論時に限定）
