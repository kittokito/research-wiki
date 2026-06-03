---
source: src-data2vec
date_extracted: 2026-06-03
---

# data2vec からの抽出

## 主要な主張
- **モダリティ非依存の統一 SSL レシピ**: 音声・画像・言語に同一の学習方法を適用。違いは入力の前処理とマスク戦略のみ [source](../../sources/Pretraining/data2vec.md)
- **予測対象 = 自己の文脈化潜在表現**: 局所的な離散ターゲット（音声単位・visual token・単語）ではなく、入力全体に基づく **contextualized latent representations** を予測 [source](../../sources/Pretraining/data2vec.md)
- **self-distillation（teacher-student）**: teacher は student の重みの EMA（指数移動平均）。マスクされた student 表現から、マスクなしを見た teacher の表現を回帰予測 [source](../../sources/Pretraining/data2vec.md)
- **ターゲットは上位 K 層の平均**: 単一層ではなく Transformer 上位複数層の出力を平均した「文脈化された」ターゲットを用いる [source](../../sources/Pretraining/data2vec.md)

## 手法の構成
- 標準 Transformer エンコーダ。入力 embedding 部のみモダリティ固有（音声=多層 1D conv、画像=パッチ、言語=サブワード）
- マスクした位置に対してのみ損失を計算（masked prediction）、回帰損失（Smooth L1）
- teacher の表現は正規化してから平均（representation collapse 回避） [source](../../sources/Pretraining/data2vec.md)

## 主要な結果
- **画像（ImageNet-1K）**: 同規模 ViT の masked prediction 系手法を上回る [source](../../sources/Pretraining/data2vec.md)
- **音声（LibriSpeech ASR）**: wav2vec 2.0 / HuBERT など先行 SSL を上回る [source](../../sources/Pretraining/data2vec.md)
- **言語（GLUE）**: 再学習した RoBERTa に匹敵する性能を、より短い学習時間で達成 [source](../../sources/Pretraining/data2vec.md)
- 3モダリティすべてで単一レシピが competitive〜SOTA を示した点が貢献 [source](../../sources/Pretraining/data2vec.md)

## 制限・注意点
- モダリティ「横断」（cross-modal fusion）ではなく、同一レシピを各モダリティに**個別適用**するもの。マルチモーダル統合モデルではない [source](../../sources/Pretraining/data2vec.md)
- teacher が student の EMA であるため、collapse 回避のための正規化・ハイパラ調整に敏感 [source](../../sources/Pretraining/data2vec.md)
- 後続の data2vec 2.0（ICML 2023）で計算効率が大幅改善されており、本論文は効率面では後継に劣る [source](../../sources/Pretraining/data2vec.md)
