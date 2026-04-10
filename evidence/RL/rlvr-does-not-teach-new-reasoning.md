---
source: src-rlvr-does-not-teach-new-reasoning
date_extracted: 2026-04-08
---

# Does RLVR Truly Unlock New Reasoning Capabilities? からの抽出

## 主要な主張
- RLVRはpass@1を上げるが、大きいkでのpass@kではbase modelの方が高いことがある [source](../../sources/RL/rlvr-does-not-teach-new-reasoning.md)
- RLVRモデルのreasoning pathはbase modelの出力分布の中にすでに含まれている [source](../../sources/RL/rlvr-does-not-teach-new-reasoning.md)
- RLVRの効果は新しい推論の獲得ではなく、既存の正解経路へのサンプリング効率向上（filtering/sharpening）が主体 [source](../../sources/RL/rlvr-does-not-teach-new-reasoning.md)

## 主要な貢献
- Pass@k分析によるRLVRの効果分解の方法論を提示
- 「RLVRは多数のパスを絞っているだけ」説の実証的根拠を提供

## 制限・注意点
- 特定のGRPO系レシピでの観察であり、探索を強化した改良版RLVRには当てはまらない可能性
- Pass@kの比較だけではbase modelのtailに潜在的に存在する能力を完全に評価できない
