---
source: src-attention-to-mamba-distillation
date_extracted: 2026-04-21
---

# Attention to Mamba: Cross-Architecture Distillation からの抽出

## 主要な主張
- MambaはTransformerと比べ生成時のメモリ消費が少なくスループットが高いため、代替アーキテクチャとして人気 [source](../../sources/Architecture/attention-to-mamba-distillation.md)
- しかし、既存のTransformer訓練ノウハウ・事前学習済みモデル資産を活かす形でSSM採用を進めるクロスアーキテクチャ蒸留レシピが未成熟 [source](../../sources/Architecture/attention-to-mamba-distillation.md)
- 従来のナイーブなTransformer→Mamba蒸留は教師の性能を保てず、Attention+SSMのhybrid構成でごまかすのが通例 [source](../../sources/Architecture/attention-to-mamba-distillation.md)
- **核心の主張**: Mambaに **原理的な初期化** を施すことで、hybridに頼らない純Mamba蒸留レシピを確立できる [source](../../sources/Architecture/attention-to-mamba-distillation.md)
- **二段階蒸留**:
  - 第1段階: Transformerを **kernel trickを応用したlinearized Attention** に蒸留
  - 第2段階: linearized版を **Attention非使用のadapted Mamba** に蒸留 [source](../../sources/Architecture/attention-to-mamba-distillation.md)
- Pythia-1B の蒸留後Mambaが **perplexity 14.11**（teacher 13.86）を達成し、downstream性能を保持 [source](../../sources/Architecture/attention-to-mamba-distillation.md)
- 1Bスケール・10Bトークンでsequence mixerアーキテクチャを変えたablation、モデルサイズ・蒸留トークン量のスケーリング、二段階間トークン配分の感度分析を実施 [source](../../sources/Architecture/attention-to-mamba-distillation.md)

## 主要な貢献
- hybrid不要の純Mambaクロスアーキテクチャ蒸留レシピ
- kernel trick に基づくlinearized Attention仲介という二段階設計
- Pythia-1B teacher からのほぼ完全な性能保持（Δperplexity ≈ 0.25）
- 体系的ablationとスケーリング分析

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| Pythia-1B teacher perplexity | 13.86 | 基準 |
| 蒸留後Mamba perplexity | 14.11 | +0.25 のみの劣化 |
| 蒸留スケール | 1B params × 10B tokens | ablation/scaling実験 |
| アーキテクチャ | 純Mamba | Attention層を含まない |

## 制限・注意点
- 現状は1Bスケールでの実証、7B+や大規模への外挿妥当性は scaling analysis 提示はあるが実測は限定
- downstream 性能の詳細（個別タスク別）はペーパー本体参照が必要
- 「kernel trickの応用」具体形の安定性がモデルサイズで変化する可能性
- 10Bトークンは比較的小規模、より大規模蒸留での挙動は未検証
- Mambaの世代・バリアント（Mamba-2 等）との互換性は明示が必要

## 実装関連
- 二段階蒸留の**トークン配分**が感度パラメータ、適切な分割比を実験ガイド化
- linearized Attention への一次蒸留は既存Transformer資産を最大限活用する手順
- Mamba本体の初期化方法が性能保持の鍵
- arXiv 2604.14191
