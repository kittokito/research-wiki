---
source: src-rs-grpo
date_extracted: 2026-04-17
---

# Risk-Sensitive RL (RS-GRPO) からの抽出

## 主要な主張
- 事前学習済みLLMの初期方針は鋭く尖鋭化しており、標準RLはその狭い解集合内に留まる（exploration dilemma） [source](../../sources/RL/rs-grpo.md)
- 標準GRPOなどはpass@1を向上させる一方で、pass@k（解の多様性）を低下させる [source](../../sources/RL/rs-grpo.md)
- CVaRベースのリスク感応的な目的関数（平均報酬と最大報酬を補間）により、困難なプロンプトからの学習を増幅できる [source](../../sources/RL/rs-grpo.md)
- RS-GRPOはGRPOへの数行の修正で実装可能 [source](../../sources/RL/rs-grpo.md)

## 主要な貢献
- exploration dilemmaの定式化: sharpened prior × 標準RL目的関数 → 解空間の狭窄
- リスクパラメータで「平均」と「最大」を補間する目的関数の導入
- RS-GRPO: CVaR風に下位（または上位）テールを重み付けするpolicy gradient修正
- 6つの数学推論ベンチマーク × 5つのLLM（Qwen系、DeepSeek系等）で一貫した改善

## ベンチマーク結果
| 指標 | 結果 | 備考 |
|---|---|---|
| pass@1 | 維持または強化 | vs 標準GRPO |
| pass@k | 継続的に向上 | 解の多様性が保たれる |
| 検証対象 | 6 math benchmarks × 5 LLMs | MATH-500等を含む |

（具体的な数値はPDFの表に記載。本wikiでは今後追補）

## 制限・注意点
- 数学推論タスクに検証が限定されており、コード・エージェントタスクでの効果は未検証
- リスクパラメータの最適設定はタスク依存の可能性
- プレプリント段階（査読未了）
