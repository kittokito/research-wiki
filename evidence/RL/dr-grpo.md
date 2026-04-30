---
source: src-dr-grpo
date_extracted: 2026-04-23
---

# Understanding R1-Zero-Like Training (Liu et al., 2025 / Dr. GRPO) からの抽出

## 主要な主張
- DeepSeek-R1-Zero 流の「pure RL で推論能力向上」を **ベースモデル要因** と **RL要因** に分解して検証 [source](../../sources/RL/dr-grpo.md)
- **DeepSeek-V3-Base は RL 以前から "Aha moment" を示す** — R1-Zero の "Aha moment" 現象の一部は事前学習由来のバイアス [source](../../sources/RL/dr-grpo.md)
- **Qwen2.5 base models はプロンプトテンプレートなしでも強い推論能力を示す** — 事前学習段階に潜在する instruction-like 能力の証拠 [source](../../sources/RL/dr-grpo.md)
- GRPO には **最適化バイアス** が存在: **不正解出力の応答長を人為的に増加** させる方向に偏る [source](../../sources/RL/dr-grpo.md)
- GRPO の「長い応答 = 効率的学習」という観察は、能力向上ではなく **バイアスの副産物** の可能性 [source](../../sources/RL/dr-grpo.md)
- **Dr. GRPO**（"done right" GRPO）を提案: バイアス除去の unbiased 最適化手法 [source](../../sources/RL/dr-grpo.md)
- Dr. GRPO は **token 効率を改善しつつ推論性能を維持** [source](../../sources/RL/dr-grpo.md)
- Dr. GRPO + minimalist R1-Zero recipe で **7B base model が AIME 2024 で 43.3% accuracy** を達成（論文公開時点でSOTA）[source](../../sources/RL/dr-grpo.md)

## 主要な貢献
- R1-Zero 流 RL の批判的分解（base model contribution vs RL contribution）
- "Aha moment" の事前学習起源仮説とその実証（DeepSeek-V3-Base で RL 前観察）
- GRPO の length bias の同定と数学的分析
- Dr. GRPO（unbiased GRPO）の定式化と実装
- Minimalist R1-Zero レシピの提示（再現性を意識した公開）
- GitHub: sail-sg/understand-r1-zero

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| AIME 2024 accuracy | 43.3% | 7B base model + minimalist Dr. GRPO recipe（当時SOTA） |
| 分析対象 base model | DeepSeek-V3-Base, Qwen2.5 ほか | 複数ベースモデルを横断分析 |
| GRPO バイアス方向 | 不正解出力の応答長を増加 | 特に正解率低いプロンプトで顕著 |

## 制限・注意点
- 「"Aha moment" は事前学習由来」という主張は定性観察が中心で、**全ての "Aha moment" を RL の貢献から除外できるかは未証明**。RL がベースの傾向を増幅する効果までは否定していない
- Qwen2.5 base model の「プロンプトテンプレートなし推論」は、Qwen2.5 特有の pretraining data 構成に依存する可能性（他系列への一般化は別途検証必要）
- Dr. GRPO のバイアス除去が「漸近性能」を改善するのか、それとも [ScaleRL](../../wiki/papers/RL/scale-rl.md) の分類で言う「効率」のみを改善するのかは、両論のある領域（論文では「推論性能を維持」と控えめに主張）
- 43.3% AIME 2024 は 2025-03 時点の SOTA で、2026 時点ではすでに多数のレシピに追い越されている（歴史的ベースラインとして参照）
- 「不正解出力の応答長を増加させるバイアス」の実害は、計算コスト増と学習不安定化の2軸だが、推論性能への直接悪影響は限定的という指摘もあり得る
- Base model の選定が結論に強く影響: DeepSeek-V3-Base と Qwen2.5 以外の系列（LLaMA 3, Gemma 2 等）で同じ事前学習バイアスが観察されるかは未検証

## 実装関連
- GitHub: https://github.com/sail-sg/understand-r1-zero
- Dr. GRPO の具体式は論文本体に詳述（GRPO の bias 項の除去）
- arXiv 2503.20783 / v1: 2025-03-26, v2: 2025-10-06
- OpenReview: 5PAF7PAY2Y (COLM 2025)
- Sea AI Lab / sail-sg / NUS
