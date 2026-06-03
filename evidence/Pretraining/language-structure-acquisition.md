---
source: src-language-structure-acquisition
date_extracted: 2026-06-03
---

# Towards a theory of how the structure of language is acquired by deep neural networks からの抽出

## 生成モデル
- 自然言語の階層構造を捉える **PCFG（probabilistic context-free grammar, tree-like 生成モデル）** を解析対象とする [source](../../sources/Pretraining/language-structure-acquisition.md)
- 木構造の隠れ変数（hidden variables）が深さに沿って配置される [source](../../sources/Pretraining/language-structure-acquisition.md)

## 中心的な主張
- **token-token 相関を解析的に決定**できる。これを使って文法の隠れ変数の表現を構築できる [source](../../sources/Pretraining/language-structure-acquisition.md)
- **相関の range が長いほど、対応する隠れ変数は深い**（range と木の深さが対応） [source](../../sources/Pretraining/language-structure-acquisition.md)
- **有限の訓練集合は相関の解像度を effective range に制限**し、その range のサイズは訓練集合サイズとともに伸びる [source](../../sources/Pretraining/language-structure-acquisition.md)
- 結果として、**より多くの例で訓練された LM は文法構造のより深い表現を構築できる** [source](../../sources/Pretraining/language-structure-acquisition.md)

## スケーリングに関する結果
- テスト損失の訓練集合サイズに対する**スケーリング則が文脈窓（context window）長にどう依存するか**を予測 [source](../../sources/Pretraining/language-structure-acquisition.md)
- **Shakespeare・Wikipedia** で経験的に検証 [source](../../sources/Pretraining/language-structure-acquisition.md)

## RHM との関係
- [Random Hierarchy Model](../../sources/Pretraining/random-hierarchy-model.md)（分類タスクでのサンプル複雑度 P*=n_c m^L）の枠組みを、言語モデルの自己回帰/相関ベースの設定に展開したもの [source](../../sources/Pretraining/language-structure-acquisition.md)
- RHM の「階層を段階的に学ぶ」描像を、「データ量を増やすと相関の effective range が伸び、より深い隠れ変数を獲得する」という形で言語に翻訳 [source](../../sources/Pretraining/language-structure-acquisition.md)

## 制限・注意点
- PCFG という理想化された生成モデルに基づく。実際の自然言語の非文脈自由な構造・意味への一般化は別途検証が必要 [source](../../sources/Pretraining/language-structure-acquisition.md)
- 検証は Shakespeare・Wikipedia の比較的小規模設定。大規模 LM・多言語への定量転移は未検証 [source](../../sources/Pretraining/language-structure-acquisition.md)
