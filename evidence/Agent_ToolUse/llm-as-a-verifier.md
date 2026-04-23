---
source: src-llm-as-a-verifier
date_extracted: 2026-04-21
---

# LLM-as-a-Verifier からの抽出

## 主要な主張
- 既存のLLM-as-a-Judgeは単一promptでpoint estimateを出すが、これには多くの落とし穴（自信過剰・prompt依存・評価の粗さ）がある [source](../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- 検証精度は以下の **3軸** をスケールすると一貫して向上する：
  - **scoring granularity**（採点粒度の細分化）
  - **repeated verification**（繰り返し検証）
  - **criteria decomposition**（評価基準の分解）[source](../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- Agent trajectoryに対する **軌跡reward model** として動作、test-time scalingと組み合わせることで downstream 成功率を大きく押し上げる [source](../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- **Terminal-Bench 2 で 86.4% (SOTA)**、**SWE-Bench Verified で 77.8%** を達成、Claude Opus 4.6 / GPT 5.4 / Gemini 各モデルを上回る [source](../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- Terminal-Benchでは 81.8% → 86.4% の改善幅を test-time scaling + verification のみで実現 [source](../../sources/Agent_ToolUse/llm-as-a-verifier.md)
- Terminal-Bench pairwise検証精度は **78.9%** [source](../../sources/Agent_ToolUse/llm-as-a-verifier.md)

## 主要な貢献
- LLM-as-a-Judge の汎用的強化フレームワーク（3軸スケーリング）
- Agent trajectory評価における SOTA を実用的scaffoldで達成
- 小型verifier（Gemini 2.5 Flash）で大型trajectory generator（Claude Opus 4.6等）を超える性能に引き上げる test-time scaling ワークフロー
- 完全再現可能な GitHub 公開

## ベンチマーク結果
| ベンチマーク | スコア | 備考 |
|---|---|---|
| Terminal-Bench 2 (SOTA) | 86.4% | trajectory reward modelとしてtest-time scaling |
| SWE-Bench Verified | 77.8% | 同上 |
| Terminal-Bench pairwise検証精度 | 78.9% | verifier単体の正確性 |
| Terminal-Benchベースライン | 81.8% | 本手法なし |
| Terminal-Benchブースト幅 | +4.6pt | test-time scaling + verification |

## 実験条件
- **Verifier**: Gemini 2.5 Flash
- **Trajectory Generator**: Terminal-Bench は Claude Opus 4.6 から5軌跡、SWE-Bench は Claude Opus 4.6・Gemini 3 Flash・Claude Opus 4.5 から各3軌跡
- **Scaffold**: ForgeCode（Terminal-Bench）、mini-swe-agent（SWE-Bench）

## 制限・注意点
- プロジェクトページ（Notion）公開、査読論文ではない
- Verifier 側とTrajectory Generator側で別モデルを使う構成が前提で、同モデルでの自己検証の挙動は不明
- 3軸スケールの計算コスト（検証回数 × 粒度 × 基準数）と downstream 改善のトレードオフが実務設計の要
- Terminal-Bench / SWE-Bench 中心で、数学・推論・マルチモーダル等への汎化検証は別途
- 候補生成に使ったモデル（Claude Opus 4.6・Gemini 3 Flash 等）自体が強いため、verifier の貢献と generator のプール効果の切り分けには注意

## 実装関連
- GitHub: llm-as-a-verifier/llm-as-a-verifier（完全再現可能）
- scaffold: ForgeCode、mini-swe-agent
- 既存agent実装に「trajectory採点 → 最良軌跡選択」を差し込む形で利用可能
