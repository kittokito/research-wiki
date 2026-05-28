---
title: "Your Evals Will Break and You Won't See It Coming"
aliases: ["Your Evals Will Break", "eval phase transition", "self-evolving evaluation"]
created: 2026-05-19
updated: 2026-05-19
tags: [evaluation, benchmark, emergent-capabilities, grokking, phase-transition, order-parameter, self-evolving-evaluation, AI-safety]
peer_review: n/a
venue: ""
sources: [src-your-evals-will-break]
---

# Your Evals Will Break and You Won't See It Coming

> **査読**: — n/a（個人ブログ／ポジションエッセイ）

Lun Wang (2026) — [wanglun1996.github.io](https://wanglun1996.github.io/blog/your-evals-will-break.html) — Google DeepMind → NVIDIA Principal Research Scientist（AI Safety 専攻、PhD UMD）

## ソースからの事実
- 現在のLLM評価インフラは、モデルが新しい能力レジームに遷移するとき予測不可能に破綻する。既存ベンチマークは「次世代 = 現行の強化版」を暗黙前提に置く [source](../../../sources/Evaluation/your-evals-will-break.md)
- **評価は訓練目標の上流**にあり、最適化対象を規定する。評価の脆弱性は訓練・展開全体のボトルネック [source](../../../sources/Evaluation/your-evals-will-break.md)
- 評価メトリクス自体がアーティファクト化しうる（Schaeffer et al. 2023 の「emergence はメトリックの不連続性に起因」論との緊張） [source](../../../sources/Evaluation/your-evals-will-break.md)
- 物理学の**秩序パラメータ（order parameter）**を LLM に持ち込むべき。相転移の臨界点付近で値またはスケーリング挙動を変えるマクロ量を観測することで、能力遷移を予測可能にする [source](../../../sources/Evaluation/your-evals-will-break.md)
- **戦略的情報隠匿**のような能力は accuracy ベースの既存ベンチマークでは原理的に検出不可能 [source](../../../sources/Evaluation/your-evals-will-break.md)
- 評価スイートは「静的チェックリスト」ではなく、モデルと**共進化する生きたシステム**であるべき [source](../../../sources/Evaluation/your-evals-will-break.md)
- 行動指針: (1) スタイル化設定で発見した秩序パラメータを実 LLM に拡張、(2) スコア分布変化・評価間相関構造変動などメタシグナルを監視する適応型評価基盤を構築 [source](../../../sources/Evaluation/your-evals-will-break.md)

→ 詳細: [evidence](../../../evidence/Evaluation/your-evals-will-break.md)

## 現時点の解釈
本ブログの位置付けは「評価論争の抽象レイヤを一段上げる」ことにある。本リポジトリに既に存在する [LiveBench](livebench.md)（汚染耐性 + 月次更新）、[GSM-Symbolic](../Reasoning/gsm-symbolic.md)（数値変更耐性）、[P-hacking with one prompt](p-hacking-with-one-prompt.md)（メトリクス改ざんの誘発）はいずれも**個別ベンチマークの欠陥**を指摘するものだが、本記事は「能力相転移という現象クラスに対して観測装置自体が存在しない」という**構造的問題**を提示する。

物理学アナロジーの妥当性は限定的（LLM の能力空間に明確な秩序変数があるとは限らない）だが、「メタシグナル監視による自己陳腐化検知」という運用面の提案は実装可能性が高く、[ScaleRL](../RL/scale-rl.md) が示した sigmoid 計算-性能曲線や [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) の power-law フィットを「評価側の構造変動検出器」として再利用する余地がある。

セーフティ文脈での重要な含意は、[Sycophantic Delusional Spiraling](../Safety_Alignment/sycophantic-delusional-spiraling.md) や [Scalable Training Data Extraction](../Safety_Alignment/scalable-training-data-extraction.md) で示されたような「accuracy が高くなっても顕在化する新たな失敗モード」が、まさに著者の言う「能力レジーム遷移時の評価盲点」の実例だという点。本記事は具体的な実装提案を欠くポジションペーパーだが、評価設計者がチェックリスト追加ではなく**評価メタ構造の監視**へと視点を変える契機を与える。

## 関連ページ
- [LiveBench](livebench.md) — 汚染耐性・月次更新によるベンチマーク陳腐化への部分的回答（本記事の「自己進化型評価」の最も近い既存実装例）
- [P-hacking with one prompt](p-hacking-with-one-prompt.md) — メトリクス信頼性が崩れる別経路（プロンプト誘発）の実証
- [GSM-Symbolic](../Reasoning/gsm-symbolic.md) — accuracy ベンチマークの脆弱性をパターンマッチング側から実証
- [LLM Reasoning Failures](../Surveys_Overview/llm-reasoning-failures.md) — 個別失敗モードのサーベイ、本記事の「秩序パラメータが必要」主張の経験的根拠
- [Sycophantic Delusional Spiraling](../Safety_Alignment/sycophantic-delusional-spiraling.md) — accuracy では見えない安全性失敗の例
- [ScaleRL](../RL/scale-rl.md) — sigmoid 計算-性能曲線、能力スケーリングのメタシグナル化の道具立て
- [Scaling Behaviors of LLM RL Post-Training](../RL/rl-scaling-math-qwen25.md) — power-law フィットによる訓練曲線解析、評価側への転用候補

## 未解決の問い
- LLM の能力空間において具体的に何が「秩序パラメータ」たりうるか？（推論深度、ツール使用洗練性、欺瞞能力など著者が挙げる候補は計測手順が未確立）
- メタシグナル監視（スコア分布変化、評価間相関構造変動）の検出感度・偽陽性率はどの程度か？
- 「戦略的情報隠匿」のような accuracy 非可測能力を評価する手法は構築可能か？ [LLM-as-a-Verifier](../Agent_ToolUse/llm-as-a-verifier.md) 系の trajectory reward model がその端緒となりうるか？
- 「評価が訓練の上流」は RLHF/RLVR では自明だが、事前学習との関係はどう整理されるか？
