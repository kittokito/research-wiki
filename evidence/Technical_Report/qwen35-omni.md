---
source: src-qwen35-omni
date_extracted: 2026-04-23
---

# Qwen3.5-Omni (Qwen Team, 2026) からの抽出

## 主要な主張
- Qwen-Omni 系列の最新モデル、**数百億パラメータ** 規模・**256k コンテキスト** 長 [source](../../sources/Technical_Report/qwen35-omni.md)
- 学習データ: テキスト・画像ヘテロ対 + **1億時間超の audio-visual コンテンツ** [source](../../sources/Technical_Report/qwen35-omni.md)
- **Qwen3.5-Omni-plus**: 215 audio / audio-visual 理解・推論・インタラクション subtasks / benchmarks で SOTA [source](../../sources/Technical_Report/qwen35-omni.md)
- 主要 audio タスクで **Gemini-3.1 Pro を上回り**、audio-visual 総合理解では **Gemini-3.1 Pro と同等** [source](../../sources/Technical_Report/qwen35-omni.md)
- **Hybrid Attention MoE** を Thinker / Talker 双方で採用、効率的な長系列推論 [source](../../sources/Technical_Report/qwen35-omni.md)
- **10時間超の audio 理解**、1 FPS で **400秒の 720P 動画** 処理をサポート [source](../../sources/Technical_Report/qwen35-omni.md)
- ストリーミング音声合成の不安定性の原因を **text / speech tokenizer の符号化効率ミスマッチ** と特定 [source](../../sources/Technical_Report/qwen35-omni.md)
- **ARIA**: text/speech 単位を動的に整列することで、最小レイテンシで会話音声の安定性と韻律を改善 [source](../../sources/Technical_Report/qwen35-omni.md)
- 10言語の多言語理解・音声生成を **人間的な感情表現つき** でサポート [source](../../sources/Technical_Report/qwen35-omni.md)
- audio-visual grounding: **script-level 構造化キャプション** + 精密な temporal synchronization + 自動シーンセグメンテーション [source](../../sources/Technical_Report/qwen35-omni.md)
- **Audio-Visual Vibe Coding**: 音声・映像の指示から直接コード生成する新規創発能力を観測 [source](../../sources/Technical_Report/qwen35-omni.md)

## 主要な貢献
- 「Thinker / Talker 両方に hybrid attention MoE」という統一設計によるomni-modal長系列推論
- ストリーミング音声合成の技術的ボトルネック（tokenizer ミスマッチ）の特定と **ARIA** による動的整列解
- 10時間 audio / 400秒 720P 動画という、実用規模を大きく超える時系列対応
- 215 audio/audio-visual ベンチマークでの網羅的 SOTA
- Audio-Visual Vibe Coding という、omni-modal 特有の創発能力の報告

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| パラメータ規模 | 数百億（hundreds of billions） | MoE |
| コンテキスト長 | 256k tokens | — |
| 学習 audio-visual | 100M+ hours | — |
| audio 理解範囲 | 10+ hours | — |
| 動画処理 | 400 sec @ 720P, 1 FPS | — |
| SOTA task 数 | 215 audio / audio-visual | Qwen3.5-Omni-plus |
| vs Gemini-3.1 Pro | 主要audioで上回る / audio-visual総合で同等 | — |
| 多言語 | 10 languages | 感情表現つき音声 |

## 制限・注意点
- テクニカルレポートで **査読なし**。215 ベンチマークの選定・比較の公平性は独立検証必要
- 「数百億パラメータ」以外の具体的なパラメータ数・活性パラメータ数の表記は原文要確認
- Gemini-3.1 Pro との比較は Qwen 側が選んだ benchmark セットに依存
- ARIA の効果は Qwen3.5-Omni のアーキテクチャに密結合の可能性があり、他TTSへの移植可能性は別途検証
- Audio-Visual Vibe Coding は事例報告で、定量評価の強度は要確認
- Hybrid Attention MoE の具体的な layer mix 比率は原文要確認（MiniMax-M1 との差分を理解するため）
- オープンウェイト公開の有無は原文要確認（Qwen シリーズ慣行からは期待されるが、Omni-plus は閉じる可能性あり）

## 実装関連
- arXiv 2604.15804 / v1: 2026-04-17 / v2: 2026-04-21
- Qwen Team（Alibaba）
- Thinker / Talker 分離アーキテクチャは Qwen-Omni 系列を継承
- ARIA: text-speech token alignment の具体アルゴリズムは本文詳述
