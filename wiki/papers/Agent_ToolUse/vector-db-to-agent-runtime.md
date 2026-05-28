---
title: "Vector DBを外したら、RAGではなくAgent Runtimeが残った"
aliases: ["RAR: Retrieval Augmented Reasoning", "Agent Runtime over RAG"]
created: 2026-05-27
updated: 2026-05-27
tags: [RAG, RAR, agent, runtime, LangGraph, typed-artifacts, design-pattern]
peer_review: n/a
venue: ""
sources: [src-vector-db-to-agent-runtime]
---

# Vector DBを外したら、RAGではなくAgent Runtimeが残った

> **査読**: — n/a（ブログ記事 / Zenn）

mofuteq (2026) — Zenn 記事 / 公開: 2026-05-21

## ソースからの事実
- **RAG → RAR への転換**: 「retrieve → generate」を「retrieve to reason」に再定義。Retrieval は推論意図に従属する [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **Retrieval Lane の二分化**: canonical_query（長期信号）と emerging_query（現在のノイズ）を分離 [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **Typed Artifacts**: WebSource / Claim / StructuredDraft をスキーマ化、Claim には Observation / Interpretation / Signal / Norm を属性付与 [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **Conflicts / Gaps の明示保持**: StructuredDraft の必須フィールドとして対立と欠損を残し、推論の境界を可視化 [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **LangGraph + SQLite 状態機械**: Resume / Checkpoint / Workflow State / Persisted Artifact / SSE Status を操作対象として中断・障害・復旧を runtime の語彙に組み込む [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **LLM の位置付け**: 「自律的推論者」ではなく「スキーマを埋める変換コンポーネント」として運用 [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **適用ドメイン**: ファッション/スタイリング領域のトレンド分析（trend-to-rule）、契約レビュー（contract-question-agent） [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **キーフレーズ**: "Agent design is not inside the model. It is the structure around the model" [source](../../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

→ 詳細: [evidence](../../../evidence/Agent_ToolUse/vector-db-to-agent-runtime.md)

## 現時点の解釈

本記事は **「RAG vs Agent」という二項対立を、Vector DB の有無ではなく runtime 構造の有無で再切断** する位置付け。本リポジトリの議論軸との接続点は以下:

- **検索の有用性 vs ノイズ**: ドメインが速く変化する（トレンド分析）と Vector DB の意味的近接性は「昨日の信号 = 今日のノイズ」へ反転する。[Geometry of Forgetting](../Reasoning/geometry-of-forgetting.md) が指摘する vector averaging fallacy（dimensionality illusion ~16）の実務側カウンターパートとして読める — 「意味的に近い」ことが「現在の判断に有用」を意味しなくなる現象が、ベクトル空間の構造的限界から自然に説明される。
- **構造化された推論 vs 大モデル依存**: 「LLM を自律的推論者でなく変換コンポーネントとして扱う」設計は、[LLM-as-a-Verifier](llm-as-a-verifier.md) の "small verifier + large generator pool" や [On SFT, RL, and on-policy distillation](../RL/willccbb-sft-rl-opd.md) の "teacher π_T を制御ダイアルとして扱う" の **推論時版**。能力をモデル内に閉じ込めず、外部構造（typed artifacts / state machine）に分配する設計哲学を共有する。
- **責務境界としての Conflicts/Gaps**: 「最終判断を委譲せず解釈枠組みを返す」点は、[AI Agent Traps](../Safety_Alignment/ssrn-6372438.md) の 6 カテゴリ攻撃（Agent に最終権限を持たせると攻撃面が拡大する）への防御的設計パターンと整合。Disclaimer の増加ではなく structural boundary で対処する点が新しい。
- **継続学習との関係**: emerging_query / canonical_query の二層化は [Learning, Fast and Slow (FST)](../RL/learning-fast-and-slow.md) の slow weights (θ) / fast weights (Φ) と概念的にパラレル — 「遅い意図」と「速いノイズ」を分離するという同じ問題構造に対する、推論時側の対応とも読める。
- **ベンチマーク欠如の留保**: 経験報告であり定量評価がないため、設計原則の有効性は別途検証が必要。[Your Evals Will Break](../Evaluation/your-evals-will-break.md) の指摘する「能力レジーム遷移を捕捉する order parameter」を typed artifacts の構造（Claims / Conflicts / Gaps の出現頻度・型分布）から構築できる可能性は興味深い。

実務的には、**LangGraph + SQLite 上で「中断・復旧・可視性」を一級市民として扱う runtime design** が記事の中核貢献。Streamlit の「Thinking...」表示を「Retrieving evidence... / Extracting claims...」に置き換えるという小さな UX 変更が、内部構造設計を強制する逆方向の制約として機能している点が観察に値する。

## 関連ページ
- [Agentic RL Training (Kimi/Cursor/Chroma)](kimi-cursor-chroma-agentic-rl.md) — production 環境で agent を動かす別系統のアプローチ（訓練側 / runtime 側の対比）
- [LLM-as-a-Verifier](llm-as-a-verifier.md) — 「LLM をスキーマを埋める変換コンポーネントとして扱う」設計の test-time scaling 側カウンターパート
- [AI Agent Traps](../Safety_Alignment/ssrn-6372438.md) — Agent に最終権限を持たせる構造的リスク（本記事の責務境界設計の動機）
- [The Geometry of Forgetting](../Reasoning/geometry-of-forgetting.md) — Vector DB の意味的近接性が判断有用性に直結しない理由の理論的基盤
- [Karpathy Wiki Workflow](../Press_Releases/karpathy-tweet.md) — LLM で source 文書を構造化 wiki にコンパイルする並列的アイデア

## 未解決の問い
- typed artifacts のスキーマ設計はドメイン依存か、抽象化可能か？ファッション・契約以外の領域（医療・法務・科学レビュー）で同じ Claim/Conflicts/Gaps スキーマが流用できるか？
- 「LLM を変換コンポーネントとして扱う」場合の最適モデルサイズは？軽量モデルで成立する閾値はどこか？
- RAR 設計が RAG ベンチマーク（NQ / HotpotQA / RAGAS）で定量化されたら何が見えるか？評価軸自体が設計に追従していないという [Your Evals Will Break](../Evaluation/your-evals-will-break.md) 的問題が露呈するか？
- Conflicts / Gaps を runtime に残す設計は、最終ユーザーへの提示時の認知負荷とどうトレードオフするか？
