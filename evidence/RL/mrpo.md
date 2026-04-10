---
source: src-mrpo
date_extracted: 2026-04-08
---

# MRPO (Manifold-Reshaping Policy Optimization) からの抽出

## 主要な主張
- 標準的なRLVR/RLHFは事前学習のbias manifold（低ランク多様体）に閉じ込められ、能力境界を真に拡張できない（"The Trap"） [source](../../sources/RL/mrpo.md)
- Confidence-Induced Rank Collapse: 方策が収束するにつれ、logitスケール増大によりeffective rankが縮小し、k ≪ d に収束する（Proposition 3.3） [source](../../sources/RL/mrpo.md)
- Bias manifold内でnull-space投影が有意な軌跡をサンプルする確率は指数関数的に減衰する（Hypothesis 1） [source](../../sources/RL/mrpo.md)
- Effective rankは正解予測に統計的に有意（βᵣ=0.56, p≪10⁻⁵）だが、エントロピーは予測力を失う（βₑ≈0, p>0.05）：幾何的性質が確率的不確実性とは独立であることを示唆 [source](../../sources/RL/mrpo.md)
- 4Bモデル（MRPO）がQwen3-32Bを数学推論で大幅に上回る [source](../../sources/RL/mrpo.md)

## 主要な貢献
- **Spectral Orthogonal Exploration (SOE)**: Student-Guides-Teacher paradigmで、教師モデルのbias manifoldのnull spaceに位置する高ランク推論軌跡を10,000件生成。直交性スコアΩ(sⱼ)でフィルタリング
- **Effective Rank正則化**: Shannon entropy由来のerank(H) = exp(-Σpᵢ ln pᵢ)を推論軌跡の次元性指標として使用。報酬にα=0.5で統合し、高次元推論パターンを維持
- **二段階分離**: 能力発見（SOE）と分布安定性（rank-aware GRPO）を分離するアーキテクチャ
- **Local Bias Manifold の形式的定義** (Definition 3.2): 軌跡行列Hの上位k主成分が分散の1-ε以上を説明する低次元領域

## ベンチマーク結果
| ベンチマーク | Base (Qwen3-4B) | GRPO | MRPO | 備考 |
|---|---|---|---|---|
| AIME 2024 | 46.7% | 46.7% | **56.7%** | Qwen3-32Bの33.3%を大幅に上回る |
| AIME 2025 | 33.3% | 36.7% | **43.3%** | |
| MATH-500 | 84.8% | 87.6% | **88.8%** | |
| OlympiadBench | 42.6% | 42.1% | **43.0%** | |
| Omni-Hard | 14.9% | 16.8% | **17.4%** | コンテキスト長ミスマッチの影響あり |
| **Mean** | 44.5% | 46.0% | **49.8%** | +5.3 (vs base), +3.8 (vs GRPO) |

### Pass@K (AIME 2024, n=64)
| K | MRPO |
|---|---|
| Pass@1 | 56.4% |
| Pass@4 | 73.2% |
| Pass@16 | 85.3% |
| Pass@32 | 89.1% |

### Ablation
| 構成 | Mean |
|---|---|
| Base | 44.5% |
| Pure GRPO | 46.0% |
| Rank Reward GRPO (SOEなし) | 45.6% |
| SOEのみ (Cold Start) | 46.1% |
| Cold Start + GRPO (Rankなし) | 49.0% |
| **MRPO (Full)** | **49.8%** |

- SOE単体で+1.6pt、Cold Start + GRPOで+4.5pt、full MRPOでさらに+0.8pt
- 両段階の組み合わせが最も効果的

## 制限・注意点
- **安全性**: Bias manifold外での動作が従来の安全ガードレールを迂回するリスクを著者自身が指摘
- **汎化**: 検証はverifiable rewardを持つ数学ドメインのみ。open-endedなタスクでの効果は未検証
- **実装複雑性**: Student-Guides-Teacher + Micro-SVDの工学的コスト、リアルタイムSVD推定のオーバーヘッド
- **コンテキスト長**: 8192トークンで訓練、Omni-Hardでは4096評価との不整合で性能差が縮小
- **再現性**: 追試待ち（2026年1月投稿、まだ新しい）

## 実装関連
- ベースモデル: Qwen3-4B-Instruct-2507
- Student: Gemma-3-4B-IT（SOE段階で使用）
- SOE生成: 問題あたりn=16サンプル、Student M=8候補、Teacher N=8先読み
- Rank計算: スライディングウィンドウ w=64、軌跡全体の最小rankを使用
- Rank報酬係数: α=0.5
- 訓練: SOEデータ10,000件で1エポックSFT → rank-aware GRPO
- トークン消費: ベースモデル比40-60%削減
