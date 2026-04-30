---
source: src-minimax-m1
date_extracted: 2026-04-23
---

# MiniMax-M1 (MiniMax Team, 2025) からの抽出

## 主要な主張
- **世界初のオープンウェイト・大規模ハイブリッドアテンション推論モデル** と自称 [source](../../sources/Technical_Report/minimax-m1.md)
- アーキテクチャ: **hybrid MoE + lightning attention**、MiniMax-Text-01 ベースで推論向けに発展 [source](../../sources/Technical_Report/minimax-m1.md)
- **パラメータ: 456B total / 45.9B activated per token** [source](../../sources/Technical_Report/minimax-m1.md)
- **コンテキスト長: ネイティブ 1M トークン**（DeepSeek R1 の8倍）[source](../../sources/Technical_Report/minimax-m1.md)
- lightning attention により **test-time compute を効率的にスケール可能** [source](../../sources/Technical_Report/minimax-m1.md)
- RL訓練は **sandbox ベースの実ソフトウェアエンジニアリング環境** を含む多様なタスクで実施 [source](../../sources/Technical_Report/minimax-m1.md)
- **CISPO（新規RLアルゴリズム）**: importance sampling weights を clip（token updates ではなく）→ 他の競合RL派生を上回る [source](../../sources/Technical_Report/minimax-m1.md)
- hybrid attention + CISPO の組み合わせで **512 H800 GPU × 3週間、レンタル費用 $534,700** でフルRL訓練完了 [source](../../sources/Technical_Report/minimax-m1.md)
- 公開モデルは **thinking budget 40K と 80K の2版**（40Kは80K訓練の途中段階）[source](../../sources/Technical_Report/minimax-m1.md)
- **DeepSeek-R1 / Qwen3-235B に匹敵または上回る**、特に complex software engineering / tool use / long-context で強み [source](../../sources/Technical_Report/minimax-m1.md)

## 主要な貢献
- オープンウェイトで 456B MoE + lightning attention + 推論特化 + 1Mコンテキストを組み合わせた大規模モデル公開
- 新規RLアルゴリズム **CISPO**（importance sampling weight clipping）
- test-time compute scaling に適した lightning attention の実戦デモ
- $534,700 / 3週間 / 512 H800 という、大規模推論モデルRL訓練のコスト公開（再現可能性にとって重要）
- thinking budget 40K/80K を別モデルとして公開することで、推論長と性能のトレードオフを研究可能にした
- GitHub: MiniMax-AI/MiniMax-M1（weight + code）

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| 総パラメータ | 456B | MoE |
| 活性パラメータ/token | 45.9B | — |
| ネイティブ context | 1M tokens | DeepSeek R1 の 8× |
| thinking budget | 40K / 80K | 2モデル公開 |
| RL GPU/時間 | 512 H800 × 3週間 | — |
| RL レンタルコスト | $534,700 | フルRL訓練 |

## 制限・注意点
- テクニカルレポートで **査読なし**。CISPO の比較対象の強度・ハイパラチューニングの公平性は独立検証が必要
- 「世界初のオープンウェイト大規模ハイブリッドアテンション推論モデル」は定義次第（Kimi Linear 等との位置関係）
- 「DeepSeek-R1/Qwen3-235B に匹敵」の根拠は論文内のベンチマーク群で、SWE-Bench や Tool-use 系のタスク選択に依存
- 1M context の実効性能（長文推論の needle-in-haystack, long-range dependency）は個別評価が必要
- CISPO の有効性は MiniMax-M1 の hybrid attention 構造と密結合の可能性があり、標準 Transformer RL での一般化は別途検証必要
- 100名超の共著者・alphabetical order というクレジット方針は貢献度の把握が困難
- $534,700 は「レンタル」コストであり、データ準備・事前学習・データセット収集の総コストは別途

## 実装関連
- arXiv 2506.13585（single version, 2025-06-16）
- GitHub: MiniMax-AI/MiniMax-M1（オープンウェイト）
- CISPO (Clipped Importance Sampling Policy Optimization 想定) の具体式・ハイパラは論文本体に詳述
- hybrid MoE + lightning attention: MiniMax-Text-01 アーキテクチャをベース
- RL インフラ: sandbox-based real-world software engineering environments を含む
