---
source: src-willccbb-sft-rl-opd
date_extracted: 2026-05-07
---

# On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7, 2026) からの抽出

## 主要な主張

### §1 Standard pipeline と compounding argument
- **SFT のサンプリング分布はデータ生成時に固定** されており、学生が改善してもデータは改善しない。teacher 距離に近づくと marginal example が情報不足になり、それ以上のSFT は memorization に堕する。**SFT の天井は teacher 性能に等しい** [source: §1](../../sources/RL/willccbb-sft-rl-opd.md)
- **RL は逆**：学生自身がロールアウトをサンプル → 勾配更新 → 次バッチは改善後ポリシーから。**改善が分布に compound する**。天井は verifier の grading 能力で決まる、teacher ではない [source: §1](../../sources/RL/willccbb-sft-rl-opd.md)
- → **tipping point**：teacher から遠いとき SFT bits が情報量／計算量比で安く、teacher 近傍では学生のロールアウトが lucky exploration で新戦略を生み出す。tipping point 後は RL に移すべき。これが「SFT-then-RL」順序の理由 [source: §1](../../sources/RL/willccbb-sft-rl-opd.md)
- **Rejection-sampled SFT (SFT-RS / RFT)** は SFT より厳密に良いが compounding 問題は解決しない（カーブが上にシフトするだけで形状は不変）[source: §1](../../sources/RL/willccbb-sft-rl-opd.md)

### §2 Same-family vs Different-family teacher
- **Same-family teacher**：tokenizer 一致 + recipe 一致（Qwen3-32B → Qwen3-8B-Base のような構造）。SFT 信号は capability gap だけを反映、stylistic noise なし。logprob が直接比較可能 [source: §2](../../sources/RL/willccbb-sft-rl-opd.md)
- **Different-family teacher** の2つのコスト:
  1. **Tokenizer mismatch** — re-tokenization でboundary情報損失、soft-target distillation が事実上不可
  2. **Recipe mismatch** — teacher 出力の stylistic / structural artifact（CoT 様式、register、format）を学生が同時に吸収する必要、SFT bits の相当部分が surface form の習得に消える [source: §2](../../sources/RL/willccbb-sft-rl-opd.md)
- 大規模 cross-family distillation は「teacher が知っていること」と「学生が teacher のpipelineを学ばずに吸収できること」の差で損失。同じ family のSFTの方が capability transfer 効率が高い [source: §2](../../sources/RL/willccbb-sft-rl-opd.md)

### §3 On-Policy Distillation (OPD)
- 学生がロールアウト（compounding を獲得）+ teacher が token 単位 reverse KL で grading：
  ```
  ∇_θ J_OPD(θ) = E_{x,ŷ~π_θ} [Σ_t (log π_T(ŷ_t|ŷ_<t) − log π_θ(ŷ_t|ŷ_<t)) ∇_θ log π_θ(ŷ_t|ŷ_<t)]
  ```
- 各 token の advantage は「teacher が学生比でこの token をどれだけ好むか」。dense, on-policy, reverse-KL [source: §3](../../sources/RL/willccbb-sft-rl-opd.md)
- 報告値: AIME 系で **RL の 9-30 倍少ない計算で同等性能**、teacher logprob 並列化でさらに広がる [source: §3](../../sources/RL/willccbb-sft-rl-opd.md)
- **SFT-RS より practical ceiling が高い理由**: SFT-RS は teacher の state distribution で訓練・学生の state distribution で評価する exposure-bias gap が長いロールアウトで開く → off-policy の practical ceiling は teacher quality より下。OPD は学生のロールアウトで訓練するためその gap が開かない [source: §3](../../sources/RL/willccbb-sft-rl-opd.md)
- 制約: tokenizer match + 概ね recipe match が必要、これが満たされないと per-token KL gradient が「teacher なら違う phrasing」「teacher なら違う reasoning」を区別できない [source: §3](../../sources/RL/willccbb-sft-rl-opd.md)

### §4 Self-distillation: SDFT と OPSD
- **SDFT (Shenfeld et al. 2026)**: teacher を expert demonstration（worked example）で条件づける。学生はdemonstration なしでサンプル、teacher は demonstration ありで logprob 計算 → reverse KL [source: §4](../../sources/RL/willccbb-sft-rl-opd.md)
- **OPSD (Zhao et al. 2026)**: teacher を ground-truth 答えで条件づける。teacher は正解を知っている、学生は知らない。SDFT より aggressive な distributional shift [source: §4](../../sources/RL/willccbb-sft-rl-opd.md)
- 両者とも tokenizer + recipe match は自動（同じモデル）。代わりに privileged-info conditioning が teacher 分布を学生分布から（SDFT は穏やか、OPSD は鋭く）動かす [source: §4](../../sources/RL/willccbb-sft-rl-opd.md)
- **OPD と完全に同じダイアル設定**（α=1, λ=1）、違いは teacher choice π_T のみ。失敗モードはここに集中 [source: §4](../../sources/RL/willccbb-sft-rl-opd.md)

### §5 Gradient geometry
- **RL（疎・非バイアス）**: 各 token に advantage が broadcast assign。多くは noise、小さな consistent bias が報酬と相関する次元に。**average で noise が destructive interference でキャンセル、報酬相関方向だけが残る** [source: §5](../../sources/RL/willccbb-sft-rl-opd.md)
- 経験的サポート: RL の更新は parameter space で sparse、small subnetwork を変える（Mukherjee et al. 2025）→ destructive-interference picture と一致 [source: §5](../../sources/RL/willccbb-sft-rl-opd.md)
- **SFT（密・バイアス・拡散）**: 各 token に one-hot label。bias は data 分布方向だが、データの多様性で bias direction が分散 → soft principal-components decomposition で data manifold へ drift。SFT が forgiving な理由 [source: §5](../../sources/RL/willccbb-sft-rl-opd.md)
- **OPSD（密・バイアス・集中）**: 数学ロールアウトで pivot token 1つ（学生 0.01、teacher 0.6）に reverse KL ≈ log(0.6/0.01) ≈ 4.1 が集中。typical token は ~0、つまり **1 pivot token が typical の 100倍** 寄与。1 step、1 方向、信じていなかった領域への集中したtug [source: §5](../../sources/RL/willccbb-sft-rl-opd.md)
- **OPSD の防衛策（per-token point-wise KL clipping）**: vocabulary entry per-position で divergence cap。これがないと ~100 step で performance collapse [source: §5](../../sources/RL/willccbb-sft-rl-opd.md)

### §6 Sparse/dense × biased/unbiased × concentration の分類
| 手法 | 密度 | バイアス | 集中度 | 安定条件 |
|---|---|---|---|---|
| RL | sparse | unbiased | diffuse (noise cancel) | large batch + patience |
| SFT | dense | data 方向 | diffuse (data variety) | data on-distribution |
| OPD (same-family) | dense | teacher 方向 | diffuse (calibrated teacher) | same-family teacher |
| OPSD | dense | self+hint 方向 | **concentrated on pivot** | aggressive clipping 必須 |

→ OPSD が unique に density + bias + concentration の3つを同時に持つ。だから他にはない明示的防御（KL clipping、teacher を初期 policy に固定）が必要 [source: §6](../../sources/RL/willccbb-sft-rl-opd.md)

### §7 統一メタアルゴリズム
全メソッドを単一の token-level policy gradient で記述:
```
∇_θ J(θ) = E_{x~D, ŷ~μ_α(·|x)} [Σ_t A_t(x,ŷ) ∇_θ log π_θ(ŷ_t|ŷ_<t)]
μ_α = α·π_θ + (1−α)·π_data
A_t = λ·[log π_T(ŷ_t|c_T) − log π_θ(ŷ_t|ŷ_<t)] + (1−λ)·[R(ŷ) − b(x)]
```
3つのダイアル: **α**（on-policy 度）, **λ**（teacher KL vs outcome reward の比）, **π_T**（teacher policy） [source: §7](../../sources/RL/willccbb-sft-rl-opd.md)

| Method | α | λ | Teacher π_T |
|---|---|---|---|
| SFT | 0 | 1 | data-delta δ_y |
| Off-policy distillation | 0 | 1 | external strong model |
| SFT-RS / RFT | 0 | 1 | data-delta on filtered |
| RL / GRPO | 1 | 0 | — |
| **OPD** | 1 | 1 | external same-family |
| **OPSD** | 1 | 1 | self with y* |
| **SDFT** | 1 | 1 | self with demo |
| DAGGER | 1 | 1 | expert policy |

- **SFT は "退化した teacher からの distillation"**（δ_{y_data} に質量が点）。SFT が安全な理由は teacher が悪くないからではなく、多様な example で平均されることで bias が拡散すること
- **RL は "teacher なし"**（λ=0）、destructive interference の物語が直接導かれる
- **OPSD と OPD はダイアル設定が完全に同じ** — 違いは teacher choice。これが失敗モードの本質を明確にする [source: §7](../../sources/RL/willccbb-sft-rl-opd.md)
- **重要な caveat**: 中間 (α, λ) の混合は importance sampling correction 込みで統計が成立せず、実用的でない。clean な corner (SFT, RL, OPD) が β（KL budget）の異なる regime に対応 [source: §7](../../sources/RL/willccbb-sft-rl-opd.md)

### §8 最適 teacher 探索 — Pareto curve
最適 teacher を Lagrangian で:
```
max_{π_T} E[R(ŷ) − R(π_θ)] − β·E[D_KL(π_T(·|x) ‖ π_θ(·|x))]
```
β を変えると Pareto curve を描く。各メソッドはその上の点 [source: §8](../../sources/RL/willccbb-sft-rl-opd.md)
- **RL**: π_T → π_θ (KL → 0) の極限、原点での tangent。slope は局所的に gain ∝ √KL なので KL→0 で unbounded、多数の小ステップで累積
- **OPD (same-family)**: 中程度 KL、中程度 reward gain、KL が多 token に拡散
- **SFT (cross-family strong teacher)**: 高 KL、高 reward gain、recipe-mismatch overhead が代償
- **OPSD / SDFT**: hint 選択次第で KL の大きさと集中度が決まる、frontier 上か下かは hint 設計依存
- **internal of curve（中間 teacher 選択、混合 advantage、学習可能 hint）はほぼ未開拓** [source: §8](../../sources/RL/willccbb-sft-rl-opd.md)

### §8 候補アプローチ群（最適 teacher の構築）
- **Per-task prompt optimization** over Lagrangian — GEPA 様の最適化で hint / conditioning prompt を per-task に探索、E[ΔR] − β·KL の inner loop
- **Distribution-level prompt optimization** — bad hint（whitebox RF access、答え、demonstration）を min hint に書き換える hint-rewriter を Lagrangian で訓練
- **Self-prompt-optimization online RL** — hint をparallel environment の rollout として扱い、reward-delta と KL の smoothed minmax で hint-writer と student を共進化
- **Hint-writing model を直接 RL** — correctness-delta × (1 − KL-delta) を objective に
- **"Expert RL + OPD" 系統**（DeepSeek V4 等）— locally-optimal RL の上に teacher 信号を重ねる、本メタアルゴリズムで teacher KL と outcome reward を同時に live にする実例 [source: §8](../../sources/RL/willccbb-sft-rl-opd.md)
- 共通点: すべて **fixed external teacher policy 不要** で Lagrangian を target、teacher は per-task / per-distribution / online で **学生に locally optimal**（high reward, low KL, surgical not broadcast）に構築される
- 最終予想: 無限計算の極限・最も heavy-tail な問題分布では RL が最適、しかし interpolation は real teacher なしで compute-optimal な学習として実現可能性大 [source: §8](../../sources/RL/willccbb-sft-rl-opd.md)

## 主要な貢献
- **Compounding argument の明示化**：SFT vs RL の標準ピペラインが採用される実体的理由を「サンプリング分布の compounding」で整理、tipping point の概念
- **Same-family vs different-family の効率差** を tokenizer / recipe の両軸で整理、cross-family の隠れたコスト（recipe mismatch tax）を明示化
- **Gradient geometry による分類**：sparse/dense × biased/unbiased × concentration の3軸で SFT/RL/OPD/OPSD/SDFT を整理、OPSD の失敗モードを pivot token concentration で説明
- **統一メタアルゴリズム**：α, λ, π_T の3ダイアルで主要 post-training アルゴリズムを単一の policy gradient 形式に表現
- **Pareto curve 枠組み**：optimal teacher を `max E[ΔR] − β·D_KL` の最適化問題として定式化、内部の未開拓空間を future work として提示
- **AI 共著での技術メタ分析の運用例**：Will Brown × Claude Opus 4.7 共著という形式自体が、AI 共著研究記事の publication norm の事例となる

## 制限・注意点
- **形式はブログ的長文エッセイ**、formal proof やオリジナル実験はなく、既存知見の整理と概念フレームワークの提案
- **gradient geometry の議論は概念的説明**、destructive interference / pivot token concentration は intuitive な説明であって厳密な分散解析・収束証明ではない
- **Pareto curve 図示は schematic**、実測の (KL, gain) 点を多数比較した実験的 Pareto frontier ではない
- **OPD vs RL の "9-30× less compute" は引用ベース**、独立検証は本記事内では行っていない
- **「中間 (α, λ) は実用的でない」は強い主張**、importance sampling correction 込みのアルゴリズム設計の可能性を否定的に扱っている — この主張自体が後続研究の批判対象になりうる
- **"AI co-authored" の取り扱い**：技術内容の責任所在・査読基準・引用規範について業界的合意が未形成
- **本リポジトリの既存論文との関係**: [Dr. GRPO](dr-grpo.md) / [ScaleRL](scale-rl.md) / [Flash-RL/TIS](flash-rl-tis.md) / [RL Scaling Laws (Qwen2.5)](rl-scaling-math-qwen25.md) で議論されている GRPO バイアス・効率の話題と直接連関、特に `index/topics.md` の `GRPO variants / analysis` および `off-policy RL / importance sampling` クラスタの**メタ分析的整理**として機能

## 実装関連
- 形式: X 投稿（2050038277454143918, 2026-04-30）に紐づく長文エッセイ。Will Brown handle: willccbb / verifiers ライブラリ著者
- 共著: Claude Opus 4.7（Anthropic）、本リポジトリで **「Mythos Preview」 / Opus 4.7 が共著の技術記事** として最初の事例
- 参照論文（出典 References セクション）:
  - **Lu, K. & Thinking Machines Lab** — On-Policy Distillation (2025): OPD の現代的代表
  - **Shenfeld, I. et al.** — SDFT (2026): expert demonstration 条件付け
  - **Zhao, S. et al.** — OPSD (2026): ground-truth 条件付け
  - **Agarwal, R. et al.** — On-Policy KD (2023): 自家ロールアウトでの distillation 系統
  - **Mukherjee, A. et al.** — RL fine-tunes small subnetworks (2025): RL 更新の sparsity 経験的サポート
  - **Qwen3 Technical Report** (2025): same-family teacher OPD の実証、Will Brown は「OPD レシピは Qwen3 TR で originating」と明示
  - **Ross, S. et al.** — DAGGER (2010): expert policy + on-policy の古典系
- **本リポジトリで取り込み未済の重要関連論文**:
  - Lu (2025) OPD, Shenfeld (2026) SDFT, Zhao (2026) OPSD, Agarwal (2023) On-Policy KD は別 sources/ 候補
  - Mukherjee (2025) RL subnetwork は [Lottery Ticket Hypothesis](../Efficiency_Optimization/lottery-ticket-hypothesis.md) と関連付けて取り込む価値
- 概念用語の定義集として：本記事は post-training literacy の「読解辞書」として機能、既存 [RLVR capability boundary](../../topics/RL/rlvr-capability-boundary.md) topic の上位整理と読める
