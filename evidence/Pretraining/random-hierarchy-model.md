---
source: src-random-hierarchy-model
date_extracted: 2026-06-03
---

# Random Hierarchy Model (RHM) からの抽出

## RHM の定義
- 言語・画像の階層構造に着想した**合成分類タスク族**（PCFG 的生成モデル） [source](../../sources/Pretraining/random-hierarchy-model.md)
- 各クラスが高レベル特徴のグループに対応し、各特徴がさらに下位特徴のグループに対応する構造が**深さ L にわたり再帰**する [source](../../sources/Pretraining/random-hierarchy-model.md)
- 主要パラメータ: 深さ **L**、branching factor **s**（各特徴 → s 個の下位特徴）、クラス数 **n_c**、**multiplicity m**（各高レベルシンボルが持つ同義＝synonymic な下位表現＝production rule の数）。入力次元 **d = s^L** [source](../../sources/Pretraining/random-hierarchy-model.md)

## 中心的な結果（サンプル複雑度）
- **経験的サンプル複雑度 P\* = n_c · m^L** [source](../../sources/Pretraining/random-hierarchy-model.md)
- これは入力次元 d = s^L に対して**多項式**であり、深いネットは**次元の呪いを回避**する [source](../../sources/Pretraining/random-hierarchy-model.md)
- 対照的に、浅いネットは指数的サンプル複雑度に苦しむ — **深さが本質的** [source](../../sources/Pretraining/random-hierarchy-model.md)

## 学習メカニズム
- P\* は「**同義（synonyms）の交換に対して不変な内部表現**を構築するのに必要なサンプル数」と一致する [source](../../sources/Pretraining/random-hierarchy-model.md)
- synonyms = 同じ高レベル特徴に写る入力。第1レベルで synonyms を同定できれば、各パッチを単一シンボルに置換でき、これを再帰的に繰り返して階層表現を構築 [source](../../sources/Pretraining/random-hierarchy-model.md)
- 学習が起きる閾値は、**低レベル特徴（タプル/パッチ）とクラスの相関がサンプリングノイズを超えて検出可能になる点**に対応 [source](../../sources/Pretraining/random-hierarchy-model.md)

## 検証
- 深い CNN を RHM 上で訓練し、P\* = n_c · m^L のスケーリングと、同義不変表現の段階的構築を経験的に確認 [source](../../sources/Pretraining/random-hierarchy-model.md)

## 制限・注意点
- RHM/PCFG という理想化された合成生成モデル（一様ランダムな production rule、分類タスク）に基づく。実データ（自然言語・画像）への転移は定性的 [source](../../sources/Pretraining/random-hierarchy-model.md)
- 結果は主に深い CNN / 階層的アーキテクチャを対象 [source](../../sources/Pretraining/random-hierarchy-model.md)
