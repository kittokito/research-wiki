---
title: "Learning, Fast and Slow: Towards LLMs That Adapt Continually"
aliases: ["Fast-Slow Training", "FST", "Learning Fast and Slow", "FST (Tiwari et al. 2026)"]
created: 2026-05-19
updated: 2026-05-19
tags: [RL, continual-learning, post-training, fast-slow-weights, prompt-optimization, GEPA, GRPO, CISPO, KL-divergence, drift, plasticity, sample-efficiency, Pareto-frontier]
peer_review: preprint
venue: ""
sources: [src-learning-fast-and-slow]
---

# Learning, Fast and Slow: Towards LLMs That Adapt Continually

> **査読**: 📝 preprint（arXiv 2605.12484、29ページ・14図、採択先未記載）

Tiwari, Sareen, Agrawal, Gonzalez, Zaharia, Keutzer, Dhillon, Agarwal, Khatri (2026) — UC Berkeley × Mila × UT Austin — [arXiv 2605.12484](https://arxiv.org/abs/2605.12484) / [Blog](https://gepa-ai.github.io/gepa/blog/2026/05/11/learning-fast-and-slow/) / [Code](https://rishabhtiwari.ai/projects/fst/code/)

## ソースからの事実
- **Fast-Slow Training (FST)**: parameter θ を slow weights（GRPO + CISPO loss）、discrete textual prompt Φ を fast weights（GEPA = Reflective Prompt Evolution）として interleave 最適化 [source](../../../sources/RL/learning-fast-and-slow.md)
- **Φ は単一ベストではなく per-instance Pareto frontier の population**として保持、T=6 RL ステップごとに GEPA が K={4,8} 候補を生成し次の T RL 更新を conditioning [source](../../../sources/RL/learning-fast-and-slow.md)
- RL 単独比 **最大3倍のサンプル効率** + **asymptote も上回り**: CodeIO 47.4% vs 43.0%（3.0×）/ HoVer-hard 25.0% vs 17.3%（3.0×）/ Math 49.2% vs 46.4%（1.4×） [source](../../../sources/RL/learning-fast-and-slow.md)
- **KL(π_train ∥ π_base) を最大70%削減**（matched reward で）——ベースからの drift 抑制で catastrophic forgetting を回避 [source](../../../sources/RL/learning-fast-and-slow.md)
- **継続学習**（600ステップ × 3 sequential tasks: HoVer→CodeIO→Physics）で RL は CodeIO に stall（20.7%）するが FST は near-peak（37.7%）に到達 [source](../../../sources/RL/learning-fast-and-slow.md)
- Reflection LM = **GPT-5.2 (frozen)**、slow side = GRPO + CISPO loss、group size G=8 rollouts/problem [source](../../../sources/RL/learning-fast-and-slow.md)
- Drift は **`KL(π_train ∥ π_base)`** で定量化、held-out validation prompts の token-level divergence [source](../../../sources/RL/learning-fast-and-slow.md)

→ 詳細: [evidence](../../../evidence/RL/learning-fast-and-slow.md)

## 現時点の解釈
本論文の核心は「context-in-learning（fast）と parameter update（slow）の二項対立は false dichotomy」という再定義にある。本リポジトリの [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](willccbb-sft-rl-opd.md) が future work で予告した **「学習可能 hint writer / self-prompt online RL / hint-writing RL」系の具体実装**として位置付けられ、SFT/RL/OPD/SDFT/OPSD の Pareto curve に **FST = (Φ optimization, θ RL)** という新軸を追加する。

CISPO loss を slow side に採用した点は、本リポジトリの [MiniMax-M1](../Technical_Report/minimax-m1.md)（CISPO の出典）から [Flash-RL / TIS](flash-rl-tis.md) の IS-weight clipping 系譜の **hybrid 設計への展開**を示す。CISPO の安定性が hybrid 二重ループでも保たれることを実証した最初の主要事例。

drift 抑制（−70% KL）が plasticity 保持に直結する観察は重要——本リポジトリの [SFT Memorizes, RL Generalizes](sft-memorizes-rl-generalizes.md) で示された「RL は OOD 汎化するが SFT は memorize する」結果と接続し、**「parameter update を必要最小限に抑え、prompt 側で task-specific 情報を運ぶ」**という分業原理を提示する。これは [Dr. GRPO](dr-grpo.md) の事前学習バイアス説とも整合的——「base model に既に存在する能力を引き出すのに parameter 更新は最小で十分」。

継続学習で RL が CodeIO に stall する観察（20.7%）は、長期 RL の plasticity loss を端的に示す——[ScaleRL](scale-rl.md) の sigmoid asymptote 曲線が**単一タスク内では予測可能**でも、**task switch では崩れる**ことを補完的に示唆する。FST はこの破綻を fast weight 経由で回避する。

GEPA 自体は本リポジトリにまだ独立ページがないが、本論文の登場により GEPA の理論的重要性が高まる——次回 GEPA 自体の ingest を検討すべき。Lakshya A Agrawal（GEPA 共著）が本論文に参加していることが、GEPA を RL ループ内 embedding するという質的拡張の理論的基盤を担保する。

## 関連ページ
- [On SFT, RL, and on-policy distillation (Brown & Claude Opus 4.7)](willccbb-sft-rl-opd.md) — future work で予告された hint writer / self-prompt online RL の具体実装、Pareto curve に FST 軸を追加
- [SFT Memorizes, RL Generalizes](sft-memorizes-rl-generalizes.md) — RL の OOD 汎化結果と本論文の drift 抑制 + plasticity 保持は補完関係
- [MiniMax-M1](../Technical_Report/minimax-m1.md) — CISPO loss の出典、本論文の slow side で採用
- [Flash-RL / TIS](flash-rl-tis.md) — IS-weight clipping 系譜、CISPO の hybrid 展開
- [ScaleRL](scale-rl.md) — sigmoid scaling 則と asymptote vs efficiency 切り分け、Devvrit Khatri は両論文の共通著者
- [Scaling Behaviors of LLM RL Post-Training](rl-scaling-math-qwen25.md) — power-law フィット、本論文の sample efficiency 観察の精緻化候補
- [Dr. GRPO](dr-grpo.md) — 事前学習バイアス説、「base の能力を引き出すのに最小限の parameter 更新」の理論基盤
- [DeepSeek-R1](deepseek-r1.md) — pure RL でのモデル変化、本論文の "RL は drift 大" 比較の参照点
- [ProRL](prorl.md) — 長期 RL での能力拡張、継続学習設定での比較対象候補

## 未解決の問い
- Reflection LM コスト（GPT-5.2 推論）を含めた **真の wall-clock 効率**は RL 単独に対してどうか？
- T (=6) や K (={4,8}) の感度はどの程度か？ 異なる reflection LM（より小型）で性能はどう変化するか？
- GEPA の textual mutation が **どの種類の reasoning に最も効くか**——CodeIO (3.0×) と Math (1.4×) の差は task の構造的差異か？
- 大規模 reasoning ベンチマーク（AIME / SWE-Bench / GPQA）で本手法は scale するか？
- fast weight Φ の **解釈可能性**——GEPA が見つけたプロンプトは task-specific shortcut か、それとも meta-skill か？
- Drift 抑制と plasticity 保持の因果関係は実証されているが、**メカニズム解釈**（attention / 回路レベル）は？ [The Geometry of Forgetting](../Reasoning/geometry-of-forgetting.md) の埋め込み幾何学と接続可能か？
- FST は **DPO / PPO / GRPO の他に、SFT との組み合わせ**でも有効か？ slow side の選択肢の体系評価が必要
