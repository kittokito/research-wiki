---
source: src-curriculum-instruction-tuning
date_extracted: 2026-06-03
---

# Curriculum Instruction Tuning からの抽出

## 定義・コアアイデア
- **curriculum instruction tuning** = 訓練データと学習スケジュールを難易度指標・教育学的原則に基づいて系統的に順序づけ・最適化する instruction tuning [source](../../sources/Post_Training/curriculum-instruction-tuning.md)
- 人間の教育設計（複雑性による段階的学習）を LLM の指示調整に適用。ランダムシャッフルではなく「易→難（easy-to-hard）」で組織化 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)

## 難易度（difficulty）の測り方
- **ヒューリスティック**: テキスト長・多様性・論理的深さ
- **モデル中心**: 訓練損失・検証 perplexity・敵対的報酬
- **教育学的**: Bloom の分類法（想起→理解→応用）、教育段階
- **学習された予測器**: Model-Fitting-Difficulty (MFD) スコア等 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)

## 代表的手法
- **CAMPUS**: 複数の難易度ベース副カリキュラムを管理し、モデル能力に応じて適応的に進行 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)
- **TAPIR**: 困難指示の初期プール構築 → 教師生成例で反復拡張 → 困難サンプルの重み調整 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)
- **Data-CUBE**: タスク間干渉を最小化し、インスタンス単位で正負マージンによりソート（TSP 最適化でタスク順序を決定） [source](../../sources/Post_Training/curriculum-instruction-tuning.md)
- **D-MoLE**: 勾配ノルムに基づき各層に動的に LoRA アダプタを配置（継続マルチモーダル指示調整） [source](../../sources/Post_Training/curriculum-instruction-tuning.md)
- **CITING**: 教師 LLM がカテゴリ別ルーブリックを生成 → 学生モデルが自己修正 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)

## 順序づけ戦略
- **字句順序づけ**: 段階 s × 認知レベル c の組 (s,c) でソート
- **動的範囲拡張**: 能力に応じてカリキュラム範囲を s(t) で拡張
- **Traveling Salesman (TSP) 最適化**: タスク間干渉を削減する順序を求める [source](../../sources/Post_Training/curriculum-instruction-tuning.md)

## 主要な実験結果（各フレームワークの報告値）
| フレームワーク | 改善 | ベンチマーク |
|---|---|---|
| CORGI CIT | +2.98 MMLU / +4.76 TruthfulQA | accuracy(%) |
| TAPIR | +0.75 | AlpacaEval（勝率） |
| CAMPUS | +7.0% 平均 | GSM8K / HumanEval / MT-Bench |
| D-MoLE | +15pt 平均 | 9 マルチモーダルタスク |
| CITING | SFT/RLHF に対し 70〜90% 勝率 | GPT-4 評価（詳細性） |

- 全体傾向: 段階的カリキュラムは**ほぼ常に収束を加速**し、保持タスク・難タスクへの一般化を強化 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)

## 効果
- 収束加速、教育成果（Course Learning Outcomes）への明示的整合、ノイズある合成データへの頑健性、パラメータ数非依存 [source](../../sources/Post_Training/curriculum-instruction-tuning.md)

## 限界・注意点
- **静的カリキュラムの硬直性**: 進化するモデル能力に追従しにくい
- **難易度の主観性**: 人間の直感（Bloom 分類）が LLM の知覚と不一致の可能性
- **転移性**: ファインチューン一貫性は改善するが、ゼロショット・広範な言語タスクへの転移は限定的
- **負の転移**: カリキュラム幅が最適点を超えると性能低下
- **スケーラビリティ**: 完全なメタデータ整合は計算集約的
- **出典の性質**: 本抽出は EmergentMind（AI 統合の二次ソース）由来であり、各数値は一次論文での確認が望ましい [source](../../sources/Post_Training/curriculum-instruction-tuning.md)
