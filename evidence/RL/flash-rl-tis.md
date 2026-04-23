---
source: src-flash-rl-tis
date_extracted: 2026-04-17
---

# Your Efficient RL Framework Secretly Brings You Off-Policy RL Training からの抽出

## 主要な主張
- hybrid RLフレームワーク（rollout=vLLM/SGLang、train=FSDP/Megatron）では、同一パラメータθでも `π_sampler` と `π_learner` のトークン確率が大きく乖離し、正反対の予測さえ出る [source](../../sources/RL/flash-rl-tis.md)
- この乖離は on-policy 仮定を破り、RL訓練を暗黙のうちに off-policy 化する [source](../../sources/RL/flash-rl-tis.md)
- vLLM側のシステムレベル修正（真のサンプリング確率返却、lm_head fp32キャスト）では解消しない [source](../../sources/RL/flash-rl-tis.md)
- 重要度比 `π_learner/π_sampler` を上限 C でクランプする Truncated Importance Sampling (TIS) が、数行の修正で実効的に乖離を吸収する [source](../../sources/RL/flash-rl-tis.md)
- REINFORCE・PPO いずれにも形式的に同じ修正で適用可能 [source](../../sources/RL/flash-rl-tis.md)
- 乖離が小さい設定（小規模モデル + bf16 rollout）ではTISの追加利得は小さい／ほぼゼロ（重要度比≈1のため）[source](../../sources/RL/flash-rl-tis.md)

## 主要な貢献
- **問題の特定と命名**: "rollout–training mismatch" を、efficient RLフレームワーク共通の構造的バグとして定式化
- **TISの提案**: `min(π_learner/π_sampler, C) * R * ∇log π_learner` のシンプルな勾配補正
- **代替案との比較**: Vanilla-IS（クランプなし）と PPO-IS（PPOのclipに直接組込）の両方を上回る安定性・性能を示す
- **制御実験によるミスマッチ分解**:
  - 並列化設定（TP/SP）の学習側・生成側ギャップが Max Mismatch を増大
  - 生成長（4K vs 20K）が Max Mismatch を増大（Mean Mismatch はほぼ不変）
  - sampler backend（vLLM/SGLang、deterministic kernel）単独の寄与は小さい
- **失敗モードのケーススタディ**: entropy collapse、応答長暴走、負のKL推定、ログ報酬と実性能の乖離をTISが解消
- **MoE展望**: dynamic routing・MoE専用カーネルでミスマッチが増幅されるため、TISの重要性はさらに高い
- **コミュニティ実装**: VeRL / slime / OAT / SkyRL / OpenRLHF / REINFORCE++ が本ブログ提案のTISを統合

## ベンチマーク結果
| 設定 | 観察 | 備考 |
|---|---|---|
| Qwen2.5-32B + DAPO recipe, bf16 rollout, 4×8 H100 | TIS有りが通常RLを大きく上回る（250 step時点） | Figure 1 右; wandb公開 |
| Qwen2.5-0.5B + GSM8K, bf16 rollout (normal RL) | max token-prob差 ≈ 0.4 | Figure 2 左 |
| Qwen2.5-0.5B + GSM8K, INT8量子化rollout | 通常PPOは大きく性能劣化。PPO+TISは bf16相当まで回復 | Figure 2 右; Figure 4 |
| Qwen2.5-0.5B + GSM8K, FP8/INT8 rollout | TIS > PPO-IS ≈ Vanilla-IS（後二者は精度≈0）| Figure 4 |
| DeepSeek-R1-Distill-Qwen-1.5B + DAPO, bf16, 4×8 H100 | max token-prob差が小さくTISの上積みはわずか | Figure 3 |
| DAPO-32B + INT8 rollout | entropy < 0.2 で崩壊、応答長も暴走。TISで安定化 | Figure 5 |
| DAPO-32B + BF16 rollout | entropy崩壊は無いがTISが entropy を押し上げ、応答長は正常範囲 | Figure 6 |

- **並列化差分分析（DAPO-32B, Max Mismatch > 0.5 の応答数）**
  - Same Parallelism: 1
  - Different TP (vLLM TP2 vs FSDP SP1): 2
  - Different TP & SP (vLLM TP2 vs FSDP SP8): 二桁
  - Same Parallelism TP8/TP2/TP4 (sharding揃え) は Max Mismatch を大きく抑制
- **生成長の効果**: 20K応答 > 5×4K応答（同じ総トークン数でも）。ミスマッチは生成が進むほど累積、20K応答の最初の4K内だけでも独立4K応答より Max Mismatch が大きい
- **Mean Mismatch / KL divergence** は並列化・長さの違いでほぼ変化しない
- **Sampler backend 比較**: DAPO-32BではSGLangが Mean Mismatch 小、Polaris-7Bでは vLLM が小。SGLangの deterministic kernel を有効化しても学習側を揃えなければ大差なし

## KL推定ケーススタディ
- `k3` KL estimator は非負性を持つはずだが、INT8 rollout 下の PPO では負値を頻発（ill-conditioned signal）
- TIS 導入で、同じ `k3` estimator の値がほぼ正値に保たれ、well-conditioned な訓練挙動を回復

## 補足論点（著者見解）
- **なぜ Vanilla-IS は不安定か**: rolloutが低確率でサンプルされた場合に重要度比が爆発、勾配分散が `ratio²` で増幅（比=16 → Vanilla-ISは256倍、TIS-2は4倍、TIS-8は64倍に抑制）
- **なぜ PPO-IS より TIS か**: PPO-ISではbaseである `π_learner(a, θ_old)/π_sampler(a, θ_old)` が既に1でないためclipが常時発火、学習信号が消える
- **ログ報酬の逆転現象**: TISありの方がログ上の reward は低く見えるが、AIME等の downstream 精度ではTISが優位（ログは `π_sampler` 上の期待値、真の最適化対象は `π_learner` 上の期待値）
- **GxPOとの関係**: GSPO/GMPO は重要度比の **計算方式** の改良、TIS は **システム由来のミスマッチ** の修正。両者は直交して併用可能

## 制限・注意点
- ミスマッチが小さい設定（小モデル + bf16 rollout）では TIS の追加利得は小さい／ほぼゼロ
- クランプ定数 C の最適値は設定依存（本文ではTIS-2／TIS-8を比較的にしか示さない）
- MoE RLでの効果は示唆のみで、本ブログでは実験未実施
- ブログ形式（査読なし）。ただし VeRL/slime/OAT/SkyRL/OpenRLHF/REINFORCE++ で実装・確認済み

## 実装関連
- **TIS本体**: PPO/REINFORCE の勾配計算に `min(π_learner/π_sampler, C)` を掛けるだけ（数行）
- **vLLM patches**（著者によりupstream済みまたはオプション提供）
  - vLLM v1 engine が採用確率そのものを返却するよう修正
  - lm_head を fp32 にキャストするオプション
- **採用リポジトリ**
  - slime（TIS統合）
  - VeRL（TIS統合、[example](https://github.com/volcengine/verl)）
  - OAT（TIS検証・実装）
  - SkyRL（TIS統合）
  - REINFORCE++（Tool-Integrated-Reasoning文脈で検証）
  - OpenRLHF（TIS統合）
- **著者リポジトリ**: Flash-RL
