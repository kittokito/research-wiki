---
source: src-gsm-symbolic
date_extracted: 2026-04-07
---

# GSM-Symbolic からの抽出

## 主要な主張
- 同一構造の問題で数値インスタンスを変えるだけでLLMの性能に有意なばらつきが生じる [source](../../sources/Reasoning/gsm-symbolic.md)
- 問題の複雑度が増すと性能が大幅に低下し、特に無関係な節の追加で一部モデルは65%以上の低下 [source](../../sources/Reasoning/gsm-symbolic.md)
- 現在のLLMは真の論理的推論を実行できず、学習データの推論ステップを複製しているに過ぎない [source](../../sources/Reasoning/gsm-symbolic.md)

## 主要な貢献
- GSM-Symbolic: シンボリックテンプレートによる多様な数学問題生成ベンチマーク
- LLMの数学的推論がパターンマッチングに過ぎないことの実証的証拠

## 制限・注意点
- GSM8K程度の算数レベルの問題が対象。より高度な数学推論での検証は別途必要
- 2024年時点のモデルでの評価。o1やo3等の推論特化モデルでの再評価が求められる
