---
source: src-potemkin-understanding
date_extracted: 2026-06-09
---

# Potemkin Understanding in Large Language Models からの抽出

## 主要な主張
- ベンチマーク（AP試験等）は本来**人間用のテスト**であり、その正解から能力を推論できるのは「LLM が**人間と同じ仕方で**概念を取り違える」場合に限り妥当 [source](../../sources/Reasoning/potemkin-understanding.md)
- そうでなければ、ベンチ成功は **potemkin understanding（理解の幻想）**——どの人間の解釈とも整合しない答えに駆動された見せかけの理解——を示すに過ぎない [source](../../sources/Reasoning/potemkin-understanding.md)
- potemkin を定量化する2手続きを提示: ①3ドメインの専用ベンチ、②prevalence の**下限**を与える一般手続き [source](../../sources/Reasoning/potemkin-understanding.md)
- **potemkin はモデル・タスク・ドメインを問わず遍在**する [source](../../sources/Reasoning/potemkin-understanding.md)
- これらの失敗は単なる誤答ではなく、**概念表現の深い内的非一貫性(internal incoherence)** を反映する [source](../../sources/Reasoning/potemkin-understanding.md)

## 主要な貢献
- 「ベンチ正解 → 能力」という推論の妥当性条件を**形式的枠組み**で定式化
- potemkin understanding という概念の導入と、その存在・遍在性の定量化手続き
- 概念表現の内的非一貫性という、より深い失敗構造の同定

## 制限・注意点
- 「人間の誤解パターンと一致するか」を妥当性の基準に据える枠組み自体が、人間側の誤解分布の特定に依存
- potemkin の下限推定であり、真の prevalence や因果機序の特定は今後

## ベンチマーク結果
- potemkin はモデル・タスク・3ドメインを通じて ubiquitous（具体数値は本文参照）

## 実装関連
- concept の定義・例示・分類・編集など複数操作の整合性を測ることで internal incoherence を検出する設計
