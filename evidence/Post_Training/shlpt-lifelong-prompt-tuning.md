---
source: src-shlpt-lifelong-prompt-tuning
date_extracted: 2026-06-09
---

# Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning からの抽出

## 主要な主張
- lifelong prompt tuning は効率的かつ低ストレージで継続学習を進めるが、**転移可能性に制約**がある: **全タスクで一貫した positive transfer を保証する万能アルゴリズムは現状達成不能**、特に非類似タスクは **negative transfer** を招きうる [source](../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)
- negative transfer の主因は **アルゴリズム選択とタスク特性のミスアラインメント** [source](../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)
- **SHLPT** は、**学習可能な類似度メトリック**でタスクを2つのサブセット（類似/非類似）に分割し、**類似・非類似いずれのタスクからも有益な転移**を引き出す [source](../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)
- **parameter pool** を組み込み、catastrophic forgetting に効果的に対処 [source](../../sources/Post_Training/shlpt-lifelong-prompt-tuning.md)

## 主要な貢献
- negative transfer を「タスク類似性に応じた処理の出し分け」で緩和する SHLPT フレームワークの提案
- 類似度メトリックによるタスク分割という heuristic で、類似タスク（正の転移を活用）と非類似タスク（負の転移を回避）を同時に扱う設計
- lifelong learning ベンチマークで SOTA を上回り、多様なタスク系列で negative transfer への頑健性を実証

## 制限・注意点
- 「学習可能な類似度メトリック」の品質に性能が依存しうる（類似度判定の誤りが転移制御の誤りに直結）
- prompt tuning（PEFT）の枠組み内での結果であり、full finetuning 等への一般化は別途検証が必要

## ベンチマーク結果
| ベンチマーク | 結果 | 備考 |
|---|---|---|
| lifelong learning benchmarks | SOTA を上回る | 具体スコアは本文参照。多様なタスク系列で negative transfer に頑健 |

## 実装関連
- 学習可能な類似度メトリック＋タスク2分割＋parameter pool の3要素で構成
