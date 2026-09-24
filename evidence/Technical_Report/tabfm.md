---
source: src-tabfm
date_extracted: 2026-07-01
---

# Introducing TabFM からの抽出

## 主要な主張
- 表形式予測（分類・回帰）を **in-context learning** 問題として定式化し、未知の表に対し**追加訓練・ハイパラ調整・特徴量エンジニアリング不要**で**単一 forward pass** で予測する [source](../../sources/Technical_Report/tabfm.md)
- LLM が in-context learning でゼロショット予測するのと同じ発想を、表形式データに持ち込む [source](../../sources/Technical_Report/tabfm.md)

## 主要な貢献
- **ハイブリッドアーキテクチャ**（3機構）:
  1. **alternating row and column attention** — 生の表を多層 attention で行・列の両次元に沿って処理し、特徴間の相互作用を捉える（表は2次元・並び順に不変という性質に対応）
  2. **row compression** — 各行の文脈化情報を密なベクトル表現に圧縮
  3. **in-context learning (ICL) transformer** — 圧縮済み行ベクトル上で attention を行い、大規模データセットでも計算コストを抑える
- **完全合成データ事前学習**: **構造因果モデル（SCM）** で生成した**数億の合成データセット**のみで学習。高品質で多様な実世界表データの希少性を回避しつつ、複雑な特徴関係を反映した任意サイズの合成データを生成
- **2つの提供形態**: **TabFM**（デフォルト、無調整で即利用）と **TabFM-Ensemble**（cross features・SVD features・32-way ensembling ＋分類は Platt scaling による校正）
- 位置づけ: **TabPFN / TabICL の強みを統合**したハイブリッド設計（TabICL は column-then-row attention で in-context learning を大規模化）

## 制限・注意点
- ブログ発表（査読なし）。付随の技術論文（arXiv）は本ブログ時点で未確認 [source](../../sources/Technical_Report/tabfm.md)
- **TabFM-Ensemble** は最適な ensemble 重みと校正の計算を要する。裏を返せば**デフォルト TabFM は一部シナリオで劣る**可能性を示唆 [source](../../sources/Technical_Report/tabfm.md)
- TabArena 評価範囲は **700〜150,000 サンプル**。より大規模・超高次元の表での挙動は本発表の射程外

## ベンチマーク結果
| ベンチマーク | 内容 | 結果 |
|---|---|---|
| TabArena | 38 分類 + 13 回帰データセット（700〜150,000 サンプル） | TabFM / TabFM-Ensemble がトップ ELO、教師あり定番アルゴリズムを上回る |

（数値 ELO の内訳はブログでは非開示。TabArena 上の SOTA 級としては TabPFN-2.5 が既存の先頭）

## 実装関連
- 重み: HuggingFace `google/tabfm-1.0.0-pytorch`
- コード: GitHub `google-research/tabfm`
- BigQuery の `AI.PREDICT` SQL コマンドへの統合を予定（表 → 予測を SQL から直接呼び出し）
</content>
