---
source: src-llm-reasoning-failures
date_extracted: 2026-04-07
---

# Large Language Model Reasoning Failures からの抽出

## 主要な主張
- LLMはワーキングメモリ、抑制制御、認知的柔軟性において人間の認知障害に匹敵する欠陥を示す [source: §3.1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- モデルは確証バイアス、順序バイアス、アンカリングバイアスなどの人間の認知バイアスを再現する。バイアスの源泉は事前学習データ、アーキテクチャ特性（因果マスキング）、アラインメント手続きの3つ [source: §3.1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 先進的なモデルでも人間の幼児には容易なToMタスクで失敗し、軽微な摂動で能力が崩れる [source: §3.2](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 逆転の呪い（Reversal Curse）：「AはBである」で訓練されたモデルは「BはA」を推論できない [source: §4.1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 構成的推論は深さやディストラクタの増加に伴い破綻する [source: §4.1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- SOTAモデルはベンチマークで高スコアを達成するが、軽微な摂動で劇的な性能低下を示す [source: §4.2](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- LLMはテキスト訓練ベースのため接地された物理的理解を欠き、VLMも視覚よりテキストに過度に依存する [source: §5.1, §5.2](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 既存の緩和策はいずれも失敗を完全排除できず、タスク固有のエンジニアリングが必要 [source: §6](../../sources/Surveys_Overview/llm-reasoning-failures.md)

## 主要な貢献
- LLMの推論失敗に関する初の包括的サーベイとして、断片化した研究を統合 [source: §1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 二軸分類体系の提案: 推論タイプ（embodied vs non-embodied; informal vs formal）と失敗タイプ（fundamental, application-specific, robustness） [source: §2](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 失敗の3分類:
  1. **Fundamental Failures** — LLMアーキテクチャに固有、幅広いタスクで発現（ワーキングメモリ限界、認知バイアス、逆転の呪い、カウント失敗）
  2. **Application-Specific Limitations** — 特定ドメインに紐づく限界（ToM不整合、道徳推論の不一致、物理理解のギャップ）
  3. **Robustness Issues** — 軽微な変動で性能が不安定化（プロンプト言い換え、ベンチマーク摂動）
- GitHub リポジトリ "Awesome-LLM-Reasoning-Failures" を公開 [source: §1](../../sources/Surveys_Overview/llm-reasoning-failures.md)

## 制限・注意点
- ブラックボックスシステムのため、失敗メカニズムの確定的な追跡が困難 [source: §6](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- LLMが人間のような推論を本当に行っているかは未解決の議論であり、本サーベイはその決着を目指していない [source: §6](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- 緩和策の多くは表面的かつタスク固有であり、汎用化が困難 [source: §6](../../sources/Surveys_Overview/llm-reasoning-failures.md)

## ベンチマーク結果
| ベンチマーク | 対象領域 | 参照セクション |
|---|---|---|
| FANToM | マルチエージェントToM | §3.2 |
| MoralBench | 道徳推論 | §3.2 |
| LogicAsker / LogicGame / RuleBreakers | 形式論理 | §4.1 |
| GSM-Plus / VarBench | 数学ロバストネス | §4.2 |
| MATH-perturb | 数学摂動分析 | §4.2 |
| PhysReason / UGPhysics / ABench-Physics | 物理推論 | §5.1 |
| PhysBench | VLM物理理解 | §5.2 |
| EvoEval / ReCode | コーディング | §4.2 |

## 緩和策まとめ
- **CoTプロンプティング**: 明示的推論ステップにより多くの失敗を部分的に緩和するが万能ではない [source: §3.1, §4.1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- **データ拡張**: 逆転の呪いに対する構文反転、ロバストネスに対する摂動データ追加 [source: §4.1, §4.2](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- **検索拡張（RAG）**: ワーキングメモリ限界への対処 [source: §3.1](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- **アクティベーションエンジニアリング**: 道徳推論向けの内部活性化操作 [source: §3.2](../../sources/Surveys_Overview/llm-reasoning-failures.md)
- **マルチエージェント構造**: 検証フェーズや監視エージェントの導入 [source: §3.3](../../sources/Surveys_Overview/llm-reasoning-failures.md)
