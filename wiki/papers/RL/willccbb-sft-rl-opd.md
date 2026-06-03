---
title: "On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7, 2026)"
aliases: ["willccbb post", "Brown SFT-RL-OPD essay", "On-policy distillation analysis"]
created: 2026-05-07
updated: 2026-05-07
tags: [SFT, RL, on-policy-distillation, OPD, SDFT, OPSD, GRPO, post-training, gradient-geometry, Pareto-curve, meta-analysis]
peer_review: n/a
venue: ""
sources: [src-willccbb-sft-rl-opd]
---

# On SFT, RL, and on-policy distillation

> **査読**: — n/a（X 投稿に紐づく長文エッセイ、Will Brown × Claude Opus 4.7 共著）

Will Brown & Claude Opus 4.7 (2026-04-30) — https://x.com/willccbb/status/2050038277454143918

## 主要な図表
*本エッセイには Figure 1-6（性能 vs 計算コストカーブ、勾配ベクトル分布、Pareto curve など）が言及されているが、画像はリンク先 HTML 版のみで本リポジトリには未取り込み。図の内容は以下のソースからの事実セクションと evidence で文字情報として整理。*

## ソースからの事実

### 標準パイプラインの compounding argument
- SFT のサンプリング分布は **データ生成時に固定**、学生改善で更新されない → marginal example が teacher 近傍で memorization 化、**SFT 天井 ≈ teacher 性能** [source: §1](../../../sources/RL/willccbb-sft-rl-opd.md)
- RL は学生のロールアウトで compounding → 天井は **verifier の grading 能力** で決まる、teacher ではない [source: §1](../../../sources/RL/willccbb-sft-rl-opd.md)
- → **tipping point**：teacher 遠いとき SFT bits が安い、近傍では学生のロールアウトの lucky exploration が新戦略を生む。tipping point 後は RL に移すべき。これが SFT-then-RL 順序の実体 [source: §1](../../../sources/RL/willccbb-sft-rl-opd.md)

### Same-family vs Different-family teacher
- **Same-family**（tokenizer 一致 + recipe 一致、例: Qwen3-32B → Qwen3-8B-Base）：SFT 信号が capability gap だけを反映、logprob 直接比較可能 [source: §2](../../../sources/RL/willccbb-sft-rl-opd.md)
- **Different-family** の2コスト：tokenizer mismatch（boundary 情報損失、soft-target distillation 不可）/ recipe mismatch（teacher 出力の stylistic / structural artifact を学生が同時吸収、SFT bits の相当部分が surface form に消える）[source: §2](../../../sources/RL/willccbb-sft-rl-opd.md)

### On-Policy Distillation (OPD)
- 学生がロールアウト + teacher が **token 単位 reverse KL** で grading：dense, on-policy, reverse-KL [source: §3](../../../sources/RL/willccbb-sft-rl-opd.md)
- AIME 系で **RL の 9-30× 少ない計算で同等性能**、teacher logprob 並列化でさらに広がる [source: §3](../../../sources/RL/willccbb-sft-rl-opd.md)
- SFT-RS より practical ceiling が高いのは、SFT-RS が teacher state distribution で訓練・学生 state distribution で評価する **exposure-bias gap** が長いロールアウトで開くから。OPD は学生のロールアウトで訓練するため gap が開かない [source: §3](../../../sources/RL/willccbb-sft-rl-opd.md)
- 制約: tokenizer match + 概ね recipe match が必要（per-token KL gradient の意味を保つため）[source: §3](../../../sources/RL/willccbb-sft-rl-opd.md)

### Self-distillation (SDFT, OPSD)
- **SDFT** (Shenfeld et al. 2026): teacher を expert demonstration で条件づけ。**OPSD** (Zhao et al. 2026): teacher を ground-truth で条件づけ。後者は分布シフトが鋭い [source: §4](../../../sources/RL/willccbb-sft-rl-opd.md)
- 両者は **OPD と完全に同じダイアル設定**（α=1, λ=1）、違いは teacher choice π_T のみ [source: §4](../../../sources/RL/willccbb-sft-rl-opd.md)

### Gradient geometry の3分類（密度・バイアス・集中度）
- **RL（疎・非バイアス・拡散）**: noise vector が destructive interference でキャンセル、報酬相関方向だけ残る。RL 更新が parameter space で sparse・small subnetwork という経験的観察（Mukherjee et al. 2025）と一致 [source: §5](../../../sources/RL/willccbb-sft-rl-opd.md)
- **SFT（密・バイアス・拡散）**: data 多様性で bias が拡散、soft principal-components で data manifold へ drift。「forgiving」な理由 [source: §5](../../../sources/RL/willccbb-sft-rl-opd.md)
- **OPSD（密・バイアス・集中）**: pivot token に reverse KL 集中（学生 0.01・teacher 0.6 で KL ≈ 4.1 vs typical token 0）、1 pivot が typical の 100倍寄与。**KL clipping なしでは ~100 step で performance collapse** [source: §5](../../../sources/RL/willccbb-sft-rl-opd.md)

### 統一メタアルゴリズム（§7）
全メソッドを `α`（on-policy 度）・`λ`（teacher KL vs outcome reward 比）・`π_T`（teacher 政策）の3ダイアルで記述：
- **SFT**: α=0, λ=1, π_T=δ_{y_data} — 退化した teacher
- **RL/GRPO**: α=1, λ=0 — teacher なし
- **OPD**: α=1, λ=1, π_T=external same-family
- **OPSD**: α=1, λ=1, π_T=self|y* — OPD と同じダイアル
- **SDFT**: α=1, λ=1, π_T=self|demo
- **DAGGER**: α=1, λ=1, π_T=expert policy [source: §7](../../../sources/RL/willccbb-sft-rl-opd.md)

### Pareto curve と最適 teacher（§8）
最適 teacher を `max_{π_T} E[ΔR] − β·E[D_KL(π_T ‖ π_θ)]` の Lagrangian で。β を変えると Pareto curve、各メソッドはその上の点：
- **RL** = 原点での tangent（KL→0 limit、slope unbounded、多数小ステップで累積）
- **OPD same-family** = 中程度 KL・中程度 gain・KL 拡散
- **SFT cross-family strong teacher** = 高 KL・高 gain・recipe mismatch overhead が代償
- **OPSD/SDFT** = hint 選択次第で frontier 上か下か [source: §8](../../../sources/RL/willccbb-sft-rl-opd.md)

→ 詳細: [evidence](../../../evidence/RL/willccbb-sft-rl-opd.md)

## 現時点の解釈

**本リポジトリの GRPO variants / RLVR capability boundary / off-policy RL クラスタの "メタ整理" として機能する記事**。個別アルゴリズムの新提案ではなく、既存の SFT / RL / OPD / OPSD / SDFT を **単一の policy gradient form** にまとめ、それぞれの実用的な使い分けと失敗モードを **gradient geometry** で説明する。

3つの読みどころ:

1. **Compounding argument の鋭さ**: 「なぜ SFT-then-RL 順序か」を「サンプリング分布の compounding がどこにあるか」で説明する単純で強力な観点。tipping point の概念は実務上の compute allocation に直結。
2. **OPSD の pivot token concentration 分析**: OPSD が KL clipping を必須とする理由を、勾配が「学生が信じていなかった rare token への集中したtug」になることで説明。これは [Dr. GRPO](dr-grpo.md) で明らかにされた GRPO の応答長バイアスと**同じ系統の現象**（dense biased gradient の集中点が暴走する問題）として読める。
3. **統一メタアルゴリズム**: α, λ, π_T の3ダイアルで主要 post-training アルゴリズムを表現する枠組み。**「OPSD と OPD のダイアル設定は完全同一、違いは teacher choice のみ」** という事実が pivot 失敗モードの本質を明示。

ただし著者が §7 で明示するように、**中間 (α, λ) の混合は importance sampling correction 込みでも統計が成立せず実用的でない**。clean な corner（SFT, RL, OPD）が β（KL budget）の異なる regime に対応するという立場で、interpolation 軸より β（KL budget）軸が興味深いという主張。これは ScaleRL / Dr. GRPO / Flash-RL TIS の系譜で「設計選択を asymptote 影響と efficiency 影響に切り分ける」議論と整合する。

最後の §8 で提示される **「最適 teacher 探索」**（学習可能 hint writer、prompt optimization、self-prompt RL）は **本リポジトリで未取り込みの open question**。同方向の DeepSeek V4「Expert RL + OPD」も言及され、locally-optimal RL に teacher 信号を重ねる方向が示唆される。

**AI 共著（Will Brown × Claude Opus 4.7）という形式自体** が、業界的に「AI が共同筆者として技術メタ分析を出版する規範」がどう確立されるかの観察対象として注目される。本リポジトリで [Claude Mythos Preview](../../models/claude-mythos-preview.md) の「実行環境つきRL」議論とも連関。

## 関連ページ

### RLVR capability boundary / GRPO variants の系譜
- [topics/RLVR capability boundary](../../topics/RL/rlvr-capability-boundary.md) — 本記事はこの topic の上位 meta integration として読める
- [Dr. GRPO: Understanding R1-Zero-Like Training](dr-grpo.md) — GRPO の応答長バイアスを同定、本記事の「dense biased concentrated gradient」分析と同系統
- [Does RLVR Truly Unlock New Reasoning?](rlvr-does-not-teach-new-reasoning.md) — RL の天井論争、本記事の「天井 = verifier」と同じ立場
- [ProRL](prorl.md) — 長期 RL で reasoning boundary 拡張、本記事の RL 天井議論と連動
- [MRPO](mrpo.md), [RS-GRPO](rs-grpo.md) — GRPO 改良、本記事メタアルゴリズムの λ=0 corner の派生

### off-policy RL / importance sampling
- [Flash-RL / TIS](flash-rl-tis.md) — vLLM rollout × FSDP 学習の暗黙 off-policy 化、本記事の「on-policy 度 α」ダイアルと直接連関
- [ScaleRL](scale-rl.md) — RL 設計選択を asymptote vs efficiency に切り分け、本記事 §7 の caveat と整合

### Scaling laws / 効率
- [Scaling Behaviors of LLM RL Post-Training](rl-scaling-math-qwen25.md) — Qwen2.5 0.5B-72B の RL scaling、本記事の compounding argument を定量化
- [DeepSeek-R1](deepseek-r1.md) — pure RL で reasoning emerge、本記事の RL ceiling 議論の起点

### sub-network / Lottery Ticket
- [The Lottery Ticket Hypothesis](../Efficiency_Optimization/lottery-ticket-hypothesis.md) — RL 更新が small subnetwork に局在する経験的観察 (Mukherjee 2025) との連関

## 未解決の問い

### 本記事が明示する open questions
- **最適 teacher の構築アルゴリズム**: per-task prompt optimization (GEPA 様) / distribution-level hint rewriter / self-prompt online RL / 専用 hint-writing model — どれが Pareto curve を最も内側に押し込めるか？
- **無限計算極限**: heavy-tail 問題分布で RL が真に optimal か、それとも学習可能 teacher が常に勝るか？
- **Expert RL + OPD（DeepSeek V4 系統）の体系化**: locally-optimal RL に teacher 信号を重ねる枠組みの compute-optimal 設計
- **中間 (α, λ) は本当に駄目か**: 著者は importance sampling correction 込みでも実用的でないと判断、この主張への反論可能性

### 本リポジトリ視点での追加問い
- 本エッセイの個別参照論文（Lu OPD 2025, Shenfeld SDFT 2026, Zhao OPSD 2026, Agarwal On-Policy KD 2023, Mukherjee subnetwork 2025）の取り込み優先度
- AI 共著（Will Brown × Claude Opus 4.7）形式の **査読・引用・責任所在** に関する業界規範の現状把握
- 本記事の Pareto curve 枠組みを実測 (KL, gain) 点で **実験的に再現** した研究はあるか？schematic から定量へ
- **OPSD の pivot token concentration は本リポジトリで観察された他の concentration 現象**（[Sycophantic Delusional Spiraling](../Safety_Alignment/sycophantic-delusional-spiraling.md) の attractor、[Geometry of Forgetting](../Reasoning/geometry-of-forgetting.md) の low-dimensional drift）と理論的に統合できるか？
