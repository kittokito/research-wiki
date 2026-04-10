---
source: src-deepseek-r1
date_extracted: 2026-04-08
---

# DeepSeek-R1 からの抽出

## 主要な主張
- DeepSeek-V3-Baseに対してSFTなしのpure RLでreasoning capabilityが大幅に向上 [source](../../sources/RL/deepseek-r1.md)
- R1-Zeroではself-verificationやreflectionのような挙動が自然に出現 [source](../../sources/RL/deepseek-r1.md)
- 「人間が書いたCoTをそのままなぞっただけ」では説明しにくい新しい推論パターンが確認された [source](../../sources/RL/deepseek-r1.md)

## 主要な貢献
- Pure RL（SFTなし）でも高度な推論能力が獲得可能であることを大規模に実証
- 人間データで直接学習していない推論軌跡が出現しうる証拠を提供

## 制限・注意点
- 新しい軌跡が「base modelの外側」なのか「base modelの長いtailに薄く存在していたもの」なのかは厳密には切り分けられていない
- 内部的なSFT warmup等の詳細が完全には公開されていない
