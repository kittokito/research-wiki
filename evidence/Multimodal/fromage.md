---
source: src-fromage
date_extracted: 2026-04-30
---

# Grounding Language Models to Images (FROMAGe) からの抽出

## 主要な主張
- 大規模事前学習済み LLM は、**重みを凍結したまま線形マッピング層のみ追加** することで、画像入出力を扱う multimodal モデルへ転換できる [source](../../sources/Multimodal/fromage.md)
- 入力側：凍結 visual encoder（CLIP ViT-L/14）の画像埋め込みを線形射影で LLM のテキスト埋め込み空間に変換し、text token と同列に concat。出力側：LLM 語彙に **special `[RET]` token** を追加し、その隠れ状態を線形射影して **画像検索クエリ** として使う [source: §3](../../sources/Multimodal/fromage.md)
- 学習目的は image captioning loss + image-text retrieval loss の合計のみ。Conceptual Captions (CC3M) のみで訓練し、追加の人手アノテーションや multimodal instruction tuning は不要 [source: §3](../../sources/Multimodal/fromage.md)
- LLM の in-context learning 能力がそのまま継承され、interleaved image-text input から **zero-shot で文脈付き画像検索 / multi-turn dialogue with images / visual storytelling** が可能 [source: §4](../../sources/Multimodal/fromage.md)
- 凍結 LLM だからこそ、テキストのみ事前学習で得られた **世界知識・推論・compositionality** が画像生成（検索）タスクに直接利用される（例: "a chair shaped like a cat" のような合成的クエリで適切な画像を検索）[source: §4.4](../../sources/Multimodal/fromage.md)

## 主要な貢献
- **凍結 LLM + 線形マッピングのみ**で interleaved image-text 入出力を可能にする最初期の手法（trainable parameters は全体の0.1%未満）
- **`[RET]` token による生成的 retrieval**：autoregressive 生成の最中に画像を「取り出す」インターフェースを提供し、出力側 grounding を decoder の単一トークンに圧縮
- **contextual image retrieval ベンチマーク**：従来の単一クエリ retrieval ではなく、対話履歴を含む multi-turn 文脈での retrieval を評価する設定を提示
- 任意長の interleaved image-text 入力（dialogue + 複数画像）を扱える汎用インターフェース、コードと事前学習済み重みを公開
- パラメータ効率（数百万）と訓練データ規模（CC3M、~3M ペア）を抑えつつ、専用 multimodal モデルに匹敵する文脈理解性能

## ベンチマーク結果

### Contextual Image Retrieval
| ベンチマーク | 指標 | FROMAGe | 比較 | 備考 |
|---|---|---|---|---|
| **Visual Storytelling (VIST)** | R@1 (last image, 5 captions context) | **20.8** | CLIP ViT-L/14 (zero-shot): 5.9 | 文脈長を増やすほど CLIP との差が拡大 |
| **VisDial (10ターンdialogue)** | R@1 zero-shot | 20.8 | 単一 caption ベース CLIP より大幅向上 | LLM の対話履歴解釈能力が効く |

### Image-and-text generation
- 凍結 LLM の世界知識を活用：抽象クエリ（"the most popular sport in {country}"）でも適切な画像を検索
- compositional クエリ（属性合成、想像物）に対しても zero-shot で機能、CLIP 単独より優位

### Ablation
- visual encoder を凍結せず fine-tune すると性能低下 → 凍結維持が CLIP 表現を壊さないために重要
- LLM サイズ（OPT-125M → OPT-6.7B）スケーリングで retrieval 性能が向上
- `[RET]` token なしで通常の hidden state を平均する方式は性能劣化

## 制限・注意点
- **画像生成は retrieval のみ**：固定の画像プールから選ぶ方式で、未見シーンの新規生成はできない（後続の GILL, Emu, Anole で diffusion / autoregressive 生成へ拡張される）
- **画像エンコーダの能力上限**：CLIP ViT-L/14 で表現できないドメイン（細粒度・OCR 重視タスク等）はそのまま FROMAGe の弱点に
- **CC3M のみの訓練**：3M ペアは現代基準では小さく、より大規模な LAION 系データで再訓練すれば差が縮む可能性
- **対話の事実性**：LLM の幻覚は引き継ぐ。検索された画像が幻覚テキストと整合しないケースあり
- **OPT 系の倫理・バイアス問題**を継承：性別・人種・地理バイアスがそのまま retrieval 出力に反映
- **長い対話文脈での retrieval ベンチマークは独自構成**：再現は可能だが業界標準として固まっていない
- **凍結 LLM のため事後微調整は限定的**：domain adaptation は線形層の再学習のみで、深い知識更新は困難

## 実装関連
- 公式実装: https://github.com/kohjingyu/fromage（PyTorch、HuggingFace Transformers ベース）
- ベース: OPT-6.7B（凍結）、CLIP ViT-L/14（凍結）
- 学習可能パラメータ: visual→text 線形射影 + text→visual 線形射影 + `[RET]` token embedding（合計数百万）
- 学習データ: Conceptual Captions (CC3M)
- 学習時間: 単一 A100 で約1日（CC3M 1 epoch）
- 推論: text token 生成中に `[RET]` が出たら直前までの hidden state を使って画像 DB から最近傍検索
- 後続研究での参照点:
  - **GILL** (Koh, Fried, Salakhutdinov, NeurIPS 2023) — 同著者による拡張、凍結 LLM + Stable Diffusion で **生成** 画像に対応
  - **Emu** (Sun et al., ICLR 2024) — 凍結 LLM 路線を unified pretraining に拡張
  - **Flamingo / OpenFlamingo / IDEFICS** — visual encoder + LLM の cross-attention 結合系列との対比
  - **LLaVA / BLIP-2** — visual encoder の強い側（FROMAGeより linear projector 重視 vs Q-Former / MLP projector）
