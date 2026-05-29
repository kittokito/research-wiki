---
title: "RAGとAgentic Searchの戦争を終わらせに来た!!!"
aliases: ["RAG vs Agentic Search", "ベクトル検索RAGは死んだのか", "CAG / ファイルシステム探索RAG"]
created: 2026-05-29
updated: 2026-05-29
tags: [RAG, agentic-search, vector-search, CAG, filesystem-search, graph-rag, llm-wiki, retrieval]
peer_review: n/a
venue: ""
sources: [src-rag-vs-agentic-search]
---

# RAGとAgentic Searchの戦争を終わらせに来た!!!

> **査読**: — n/a（ブログ記事 / Zenn・Microsoft publication）

Hirosato Gamo (2026) — Microsoft / Zenn 記事 / 公開: 2026-04-08

## ソースからの事実
- **論争の正体は定義のズレ**: 「RAG は終わった」は、各手法が評価された背景コンテキストの省略により拡散した誤解 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **RAG の定義拡張**: 「ベクトル検索前提」から「外部データを参照して生成を強化する」広義へ。Microsoft / AWS / NVIDIA も広義採用 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **Agentic Search の本質**: ファイルシステム探索と同義ではなく「**推論を用いて複数回検索を反復するアプローチ**」。手段（ベクトル検索 / grep・glob）は不問 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **ベクトル検索 RAG は死んでいない**: 「必要な場面は多い。ただし何でもベクトル検索という間違った状況からは抜け出した」 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **Agentic 検索の3留意点**: ①検索の長時間化 ②コンテキスト消費増 ③検索履歴のノイズ化による後続精度低下。対策として検索のエンジン側寄せ・軽量モデル・良結果のみ返送 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **CAG**: 大コンテキスト＋キャッシュ方式。フラッグシップ＋数ファイル＋単純質問で有効、小型モデル / 多タスク / 大型ドキュメントで破綻 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **ファイルシステム探索 RAG**: 事前インデックス不要・高速、コードベースのような文字列検索向き。探索空間が狭くないと破綻 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **Karpathy の LLM Wiki**: LLM でナレッジを Wiki 化し Obsidian 等で関連を磨く。Graph RAG をファイルシステムで完結させ、Graph RAG の大規模コストを小規模可視化で回避 [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **結論**: 対象データの性質・規模・タスクで使い分けることが重要。発信者は評価コンテキストを明示し、受け手はそれを注視すべき [source](../../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

→ 詳細: [evidence](../../../evidence/Agent_ToolUse/rag-vs-agentic-search.md)

## 現時点の解釈

本記事は **「RAG vs Agentic Search」という二項対立そのものが用語の定義ズレに起因する疑似論争**だと整理し、検索手段（vector / grep）と検索戦略（single-shot / agentic reasoning loop）を分離して論じる点が要点。本リポジトリの議論軸との接続は以下:

- **同一クラスタの実務報告との対比**: [Vector DBを外したら、RAGではなくAgent Runtimeが残った](vector-db-to-agent-runtime.md) は「Vector DB を外したら runtime が残った」という**実装側**の発見であり、本記事の「ベクトル検索は手段の一つに過ぎず agentic search は推論ループだ」という**言説整理側**の主張と、同じ結論（手段ではなく構造・戦略が本質）に異なる経路で到達している。両者を並べると「RAG という語が retrieval 手段の名前から reasoning 戦略の名前へ滑った」過程が読める。
- **Karpathy Wiki との接続**: [Karpathy Wiki Workflow](../Press_Releases/karpathy-tweet.md) を「Graph RAG をファイルシステムで完結させ、ファイルシステム探索 RAG で引きやすくする工夫」と位置付ける解釈は、本リポジトリ自体（LLM が source → evidence → wiki に構造化コンパイルする運用）のメタな自己言及でもある。本 wiki の SCHEMA はまさにこの「LLM Wiki / 小規模 Graph RAG」の実装例。
- **大コンテキスト vs 検索の境界**: CAG の適用条件（フラッグシップ＋少数ファイル＋単純質問で有効、多タスク・大ドキュメントで破綻）は、長コンテキストの実効性能が文脈量とともに劣化するという [in-context retrieval / needle-in-haystack](../Architecture/memory-sparse-attention.md) 系の知見と整合的 — 「全部入れれば良い」が成立しないことの実務的言明。
- **検索ノイズの後続劣化**: 「検索履歴がコンテキストに残るとノイズ化し後続精度を落とす」という留意点は、[Vector DBを外したら](vector-db-to-agent-runtime.md) の Conflicts/Gaps を typed artifact に隔離して runtime に残す設計や、context 圧縮・選別の必要性と同じ問題（agent の作業文脈の汚染管理）を指している。

実務的含意としては、**「RAG か Agentic Search か」ではなく「どの retrieval 手段を、single-shot で使うか agentic loop に組み込むか」をデータ規模とタスク性質で選ぶ**という設計判断のフレームを与える。定量裏付けのないオピニオン記事である点には留保が必要だが、用語インフレによる議論の混乱を解く整理として価値がある。

## 関連ページ
- [Vector DBを外したら、RAGではなくAgent Runtimeが残った](vector-db-to-agent-runtime.md) — 同一論点クラスタ。実装経験から「RAG → RAR（retrieve to reason）」へ再定義する報告
- [Karpathy Wiki Workflow](../Press_Releases/karpathy-tweet.md) — 本記事が「ファイルシステム探索 RAG 活用の 1 アイディア」として引く LLM Wiki の元ネタ
- [Agentic RL Training (Kimi/Cursor/Chroma)](kimi-cursor-chroma-agentic-rl.md) — agentic search を訓練側から扱う系統（本記事は手法整理側）

## 未解決の問い
- 「データの性質・規模・タスクで使い分ける」という結論を、定量的な選択基準（ドキュメント規模・クエリ曖昧性・タスク段数の閾値）に落とせるか？
- agentic search の3留意点（遅延・コスト・履歴ノイズ）に対する「検索のエンジン側寄せ」は、検索の表現力（推論との結合）をどこまで犠牲にするか？
- CAG / ファイルシステム探索 / ベクトル検索を 1 システム内で動的に切り替える router の設計は成立するか？切り替え判定自体のコストは？
