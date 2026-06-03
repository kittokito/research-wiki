---
source: src-your-evals-will-break
date_extracted: 2026-05-19
---

# Your Evals Will Break and You Won't See It Coming からの抽出

## 主要な主張
- 現在のLLM評価インフラは、モデルが新しい能力レジームに遷移するときに**予測不可能な形で破綻する**。既存ベンチマーク・セーフティ評価は「次世代モデルは現行モデルの強化版」を暗黙の前提とするため、創発（emergence）やグロッキング（grokking）のような不連続変化を捕捉できない [source](../../sources/Evaluation/your-evals-will-break.md)
- **評価は訓練目標の上流にある**——評価が最適化対象を規定するため、評価の脆弱性は訓練・展開全体のボトルネックとなる [source](../../sources/Evaluation/your-evals-will-break.md)
- 評価メトリクス自体が**アーティファクト**になりうる。Schaeffer et al. (2023) が示したように、accuracy のような離散メトリックが「創発」の見え方を作っている可能性がある一方、連続メトリックでは捉えきれない真の不連続も存在する [source](../../sources/Evaluation/your-evals-will-break.md)
- 物理学の**秩序パラメータ（order parameter）**——相転移の臨界点付近で値またはスケーリング挙動を変えるマクロ量——を LLM 評価に持ち込むべき。Shan, Li, Sompolinsky (2026) が継続学習で秩序パラメータを導出し相転移を予測した先例がある [source](../../sources/Evaluation/your-evals-will-break.md)
- **戦略的情報隠匿（strategic information withholding）**のような能力は、accuracy ベースの既存ベンチマークでは原理的に検出できない。能力クラスが質的に変わると評価指標自体が無効化される [source](../../sources/Evaluation/your-evals-will-break.md)
- 評価スイートは「昨年のベンチマーク静的チェックリスト」ではなく、モデル進化と**共進化する生きたシステム**であるべき [source](../../sources/Evaluation/your-evals-will-break.md)

## 主要な貢献
- 評価インフラの構造的脆弱性を、「個別ベンチマークの欠陥」ではなく「能力相転移に対する観測装置の不在」として再定義
- 物理学の秩序パラメータ概念を LLM 評価設計の指針として導入
- 「自己進化型評価（self-evolving evaluation）」の方向性を提示——スコア分布の変化や評価間相関構造の変動などメタシグナルを監視し、評価自体の陳腐化を自己検出する仕組み
- 「推論深度・ツール使用の洗練性・欺瞞能力」といった軸でスケーリング曲線を追跡することを具体策として提案

## 制限・注意点
- ポジションエッセイであり、具体的な秩序パラメータの候補や自己進化型評価の実装は提示されていない
- 引用論文の一つ Shan et al. (2026) は本文中で言及されるが現時点で検索検証は未実施（著者個人の参照リスト依存）
- 「評価が訓練の上流」という主張は RLHF / RLVR 文脈では自明だが、事前学習との関係は本文ではあまり掘り下げられていない
- "戦略的情報隠匿" のような能力を検出する具体的な評価手法は今後の課題として残されている

## 引用された主要文献
| 文献 | 文脈 |
|---|---|
| Wei et al. (2022) | 創発能力（emergent abilities）の経験的観測 |
| Power et al. (2022) | Grokking 現象の発見（訓練後期の突然的汎化） |
| Liu et al. (2022) | Grokking の理論化（NeurIPS） |
| Schaeffer et al. (2023) | 創発はメトリックのアーティファクトであるとする反論 |
| Nanda et al. (2023) | メカニスティック解釈による grokking 前予測（ICLR） |
| Shan, Li, Sompolinsky (2026) | 継続学習での秩序パラメータ導出と相転移予測 |

## 言及される既存ベンチマーク
GPQA、SWE-bench、ARC-AGI、Humanity's Last Exam ——いずれも「accuracy 軸での難易度向上」という同一パラダイム内に留まり、能力クラスの転移には対応できないと指摘される。

## 行動指針（What Do We Do）
1. **秩序パラメータの発見**: スタイル化された設定（toy model、合成タスク）から始め、実スケール LLM に拡張可能な計測量を探索する
2. **適応型評価基盤の構築**: スコア分布の変化、評価間相関構造の変動、スムーズなトレンドの破綻などのメタシグナルを継続監視し、「評価の自己陳腐化」を検知するシステムを構築する
