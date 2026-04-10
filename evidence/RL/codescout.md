---
source: src-codescout
date_extracted: 2026-04-08
---

# CodeScout からの抽出

## 主要な主張
- Unix端末のみのミニマルなエージェントをRLで訓練すれば、言語固有の静的解析ツールや専門的な検索ツールなしで強力なコード検索が可能 [source](../../sources/RL/codescout.md)
- 1.7Bモデルが8-18倍大きいベースモデルを上回り、14Bモデルはクローズドモデル（Claude Sonnet 4.5）に迫る [source](../../sources/RL/codescout.md)
- RL訓練中にエージェントが多様なツール使用から最小限（ripgrep+sed）に収束し、効率的な検索戦略を自律的に発見 [source](../../sources/RL/codescout.md)
- 特殊scaffoldの設計は必ずしも性能向上につながらず、フロンティアモデルはシンプルなBash scaffoldの方が高性能 [source](../../sources/RL/codescout.md)
- CodeScoutの予測で下流タスク（issue解決）が13.40%→17.20%に改善、トークン消費17.46%削減 [source](../../sources/RL/codescout.md)

## 主要な貢献
- **RL環境設計**: OpenHands-Bash scaffold（Unixターミナル + LocalizationFinish構造化出力ツール）。コンテナ化不要、依存インストール不要
- **報酬設計**: File/Module/Function F1スコアの合計を報酬に使用。14Bではturn-based補助報酬（ステップ予算内の終了を促進）を追加しtraining collapse回避
- **RLアルゴリズム**: GSPO（DR. GRPOに準拠、KL正則化と標準偏差を除去）
- **蒸留パイプライン**: 14B→1.7Bへの rejection sampling fine-tuning（F1=1.0の軌跡4K件）

## ベンチマーク結果

### SWE-Bench Verified (500件)
| モデル | File F1 | Module F1 | Function F1 |
|---|---|---|---|
| CodeScout-1.7B | 55.46% | 36.45% | 28.22% |
| CodeScout-4B | 68.52% | 45.97% | 36.78% |
| CodeScout-14B | 68.57% | 50.88% | 40.32% |
| RepoNavigator-32B | 67.75% | — | 34.09% |
| Claude Sonnet 4.5 (RepoNavigator) | 79.94% | — | 43.62% |
| Claude Sonnet 4.5 (OpenHands-Bash) | 82.01% | 67.19% | — |
| GPT-5 (OpenHands-Bash) | 78.18% | 61.17% | — |

### SWE-Bench Lite (300件)
| モデル | File F1 | Module F1 | Function F1 |
|---|---|---|---|
| CodeScout-14B | 71.84% | 59.23% | 44.43% |
| Qwen3-32B (Thinking) | 58.98% | 37.20% | 23.76% |

### 下流タスク（issue解決率, SWE-Bench Verified）
| 設定 | 解決率 |
|---|---|
| Vanilla Qwen3-4B | 13.40% |
| + CodeScout予測 | 17.20% (+3.8pt) |

### 訓練コスト
- CodeScout-4B: 200ステップ、8×H100、1.6Kインスタンス
- CodeScout-14B: 300ステップ、8×H100、9.6Kインスタンス
- CodeScout-1.7B: RFT + 100ステップRL

## 制限・注意点
- Pythonリポジトリのみで評価、他言語への汎化は未検証
- ファイル作成/削除を含むissueは除外
- SWE-Smithデータセットの128リポジトリに偏り
- フロンティアモデルはプロンプト感度が極めて高く（リマインダーなしでほぼゼロ性能）、比較条件に注意が必要

## 実装関連
- ベースモデル: Qwen3-1.7B, Qwen3-4B-Instruct-2507, Qwen3-14B
- フレームワーク: SkyRL（非同期RL訓練）、vLLM推論
- コンテキスト長: 32K-50K（YaRN拡張）
- ターン数: 4-6ターン/エピソード
- コード: https://github.com/OpenHands/codescout
- モデル: https://huggingface.co/collections/OpenHands/codescout
