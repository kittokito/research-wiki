# 勉強会発表資料 (2026-04-16)

## 発表テーマ一覧

| # | タイトル | カテゴリ | 発表資料 |
|---|---------|---------|---------|
| 1 | [Claude Mythos Preview (Project Glasswing)](01-claude-mythos-preview.md) | Technical Report | Anthropic, 2026年4月 |
| 2 | [Rewriting Pre-Training Data Boosts LLM Performance](02-rewriting-pretraining-data.md) | Pretraining | ICLR 2026 |
| 3 | [Mind the Gap: Self-Improvement Capabilities of LLMs](03-mind-the-gap.md) | Reasoning / Self-Improvement | ICLR 2025 |
| 4 | [SWE-CI: Evaluating Agent Capabilities via CI](04-swe-ci.md) | Evaluation / Benchmark | Preprint 2026 |

## 概要

今回の勉強会では、LLMの最前線に位置する4つのトピックを取り上げる。

1. **Claude Mythos Preview** -- Anthropicが防御的サイバーセキュリティ用途限定で公開した史上最高性能モデル。SWE-bench Verified 93.9%、自律的exploit開発能力など、能力と安全性のトレードオフを考えるうえで重要なケーススタディ。

2. **Rewriting Pre-Training Data** -- 東工大Swallowチームによる、事前学習データの「捨てる」から「書き直す」へのパラダイムシフト。LLMによるコード・数学データのリライティングで、HumanEval +17.0ptの大幅改善を実証。

3. **Mind the Gap** -- LLMの自己改善メカニズムを理論的・実証的に分析。「生成より検証が簡単」というGV-Gapの概念を定式化し、自己改善のスケーリング則を発見。

4. **SWE-CI** -- SWE-benchの先にある、継続的コードベース保守能力を評価するベンチマーク。一発修復から進化型評価への移行を提案し、Claude Opus 4.6のみがゼロ回帰率50%超を達成。

## 図表ディレクトリ

`figures/` に各論文の主要図表を格納。

```
figures/
  rewriting-fig1.png    # SwallowCode vs 既存コーパス (学習曲線)
  rewriting-fig2.png    # SwallowCode構築パイプライン
  rewriting-fig3.png    # フィルタリング手法比較
  rewriting-fig4.png    # リライティング段階別効果
  rewriting-fig5.png    # SwallowMath vs Finemath-4+ (数学)
  mindgap-fig1-*.png    # GV-Gapスケーリング (Figure 1)
  mindgap-fig2-*.png    # 自己改善フレームワーク (Figure 2)
  mindgap-fig3-*.png    # 交差検証ヒートマップ (Figure 3)
  mindgap-fig4-*.png    # 反復的自己改善 (Figure 4)
  mindgap-fig5-*.png    # 検証閾値分析 (Figure 5-6)
  sweci-fig1.png        # Snapshot vs Evolution評価の対比
  sweci-fig2.png        # データキュレーションパイプライン
  sweci-fig3.png        # Architect-Programmerワークフロー
  sweci-fig4.png        # EvoScore変遷 (モデル比較)
  sweci-fig5.png        # γ値によるランキングシフト
  sweci-fig6.png        # ゼロ回帰率ランキング
```
