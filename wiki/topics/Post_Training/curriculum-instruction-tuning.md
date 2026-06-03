---
title: "Curriculum Instruction Tuning：難易度順序づけによる指示調整"
aliases: ["curriculum instruction tuning", "カリキュラム指示調整", "data curriculum for SFT"]
created: 2026-06-03
updated: 2026-06-03
tags: [curriculum-learning, instruction-tuning, SFT, difficulty-ordering, data-curriculum, easy-to-hard, post-training]
sources: [src-curriculum-instruction-tuning]
---

# Curriculum Instruction Tuning：難易度順序づけによる指示調整

## 問いの構造

instruction tuning（SFT）の性能は、**どんなデータを使うか**だけでなく **どんな順序で見せるか**に依存するのではないか——という問い。curriculum instruction tuning は、人間教育の「易→難」原則を SFT に持ち込み、**難易度指標でデータ/タスクを順序づけ・適応的にスケジュール**することで収束を速め、一般化を高めようとする一連の手法群。

> 本ページは EmergentMind のトピック概観（~11 本の論文を統合した二次ソース）に基づく。各数値は一次論文での確認が望ましい。

## ソースからの事実

### 難易度（difficulty）の定義軸
- **ヒューリスティック**: テキスト長・多様性・論理的深さ
- **モデル中心**: 訓練損失・検証 perplexity・敵対的報酬
- **教育学的**: Bloom の分類法（想起→理解→応用）・教育段階
- **学習された予測器**: Model-Fitting-Difficulty (MFD) スコア等
- → 難易度は単一指標でなく複数を組み合わせるのが実態 [source](../../../sources/Post_Training/curriculum-instruction-tuning.md)

### 代表的フレームワーク
- **CAMPUS** (arXiv 2509.13790) — 複数の難易度ベース副カリキュラムを能力に応じ適応進行。GSM8K/HumanEval/MT-Bench で **+7.0%平均**
- **TAPIR** (arXiv 2405.13448) — 困難指示プール構築→教師生成例で反復拡張→困難サンプル重み調整。AlpacaEval **+0.75**
- **Data-CUBE** (arXiv 2401.03563) — タスク間干渉を最小化、インスタンス単位の正負マージンでソート、**TSP 最適化**でタスク順序決定
- **D-MoLE** (arXiv 2506.11672) — 勾配ノルムに基づき各層へ動的に LoRA アダプタ配置（継続マルチモーダル）。9タスク平均 **+15pt**
- **CITING** (arXiv 2310.02527) — 教師 LLM がルーブリック生成→学生が自己修正。SFT/RLHF に **70〜90% 勝率**（GPT-4 評価）
- その他: INSTA（タスク選択, 2404.16418）、LACT（KG 論理推論, 2405.01649）、Human Curriculum（2310.09518）、CLASS-IT（小規模・講義整合, 2510.25364）、教育学応用（Gagne 2503.09276 / CLO-PLO 2510.25905） [source](../../../sources/Post_Training/curriculum-instruction-tuning.md)

### 順序づけ戦略
- 字句順序づけ（段階 s × 認知レベル c の組でソート）、動的範囲拡張 s(t)、TSP によるタスク間干渉削減 [source](../../../sources/Post_Training/curriculum-instruction-tuning.md)

→ 手法別の数値・難易度指標の詳細: [evidence](../../../evidence/Post_Training/curriculum-instruction-tuning.md)

## 現時点の解釈

curriculum instruction tuning の中身は **「SFT データの順序・配合・スケジュールを設計変数として扱う」** という一点に集約でき、本リポジトリの既存議論と強く接続する:

- **DMT / SFT Data Composition との直結**: [How Abilities in LLMs are Affected by SFT Data Composition (DMT)](../../papers/Post_Training/sft-data-composition.md) は「能力ごとにスケーリング特性が異なり、専門→（少量混合つき）一般 の順で学習すると conflict と forgetting を緩和できる」と示した。これは curriculum instruction tuning の**最も基礎的なケース**——「順序と配合が性能を決める」——の実証であり、curriculum 手法群（CAMPUS の適応進行、Data-CUBE のタスク順序最適化）は DMT の2段固定スケジュールを動的・多段に一般化したものと読める。
- **継続学習・忘却との関係**: 静的カリキュラムの硬直性（モデル能力の進化に追従できない）という限界は、[Learning, Fast and Slow (FST)](../../papers/RL/learning-fast-and-slow.md) が fast/slow weights で動的適応を狙うのと同じ問題に直面している。D-MoLE の「勾配ノルムで層ごとに LoRA を動的配置」は、curriculum を**能力の変化に追従させる**試みとして FST と同じ方向。
- **学習順序（ordering）の系譜**: 「易→難」は [On SFT, RL, and on-policy distillation](../../papers/RL/willccbb-sft-rl-opd.md) の compounding argument（土台を作ってから伸ばす順序の正当化）と同じ直観の SFT データ内版。
- **難易度＝主観性という弱点**: 「Bloom 分類などの人間直感が LLM の知覚難易度と一致しない」という限界は、[Your Evals Will Break](../../papers/Evaluation/your-evals-will-break.md) の「人間が設計した尺度がモデルの能力相転移を捉え損なう」問題と通底する。MFD のような**学習された難易度予測器**が、人間ヒューリスティックより信頼できる order parameter になりうる。

要するに、curriculum instruction tuning は独立した魔法ではなく、**「SFT のデータ順序・配合・難易度」という設計空間**を体系化する枠組み。効果（収束加速・一般化強化）はほぼ一貫して報告される一方、**負の転移（カリキュラム幅が最適点を超えると劣化）・転移性の限界（広範ゼロショットへは効きにくい）・難易度指標の主観性**が共通の弱点として残る。

## 関連ページ
- [SFT Data Composition / DMT](../../papers/Post_Training/sft-data-composition.md) — 順序と配合が能力を決める最基礎ケース（curriculum の2段固定版）
- [Learning, Fast and Slow (FST)](../../papers/RL/learning-fast-and-slow.md) — 静的カリキュラムの硬直性に対する動的適応
- [On SFT, RL, and on-policy distillation](../../papers/RL/willccbb-sft-rl-opd.md) — 学習順序の正当化（compounding argument）
- [Your Evals Will Break](../../papers/Evaluation/your-evals-will-break.md) — 人間設計の難易度尺度の限界（学習された order parameter の必要性）

## 未解決の問い
- 難易度は人間ヒューリスティック（Bloom 等）と学習された予測器（MFD）のどちらが信頼できるか？両者の不一致はどこで生じるか？
- 「負の転移が起きるカリキュラム幅の最適点」はモデルサイズ・タスク多様性の関数として予測できるか？
- curriculum instruction tuning は後続の RLHF/RLVR 段階の能力にも波及するか（SFT 内の順序が RL の到達点を変えるか）？
- DMT の固定2段と、CAMPUS/D-MoLE の適応多段は、どの条件でどちらが優るか？
