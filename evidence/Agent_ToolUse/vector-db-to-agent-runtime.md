---
source: src-vector-db-to-agent-runtime
date_extracted: 2026-05-27
---

# Vector DBを外したら、RAGではなくAgent Runtimeが残った からの抽出

## 主要な主張
- **RAG の限界**: 「retrieve → generate」の単純構造では、推論内部の矛盾・ギャップが平均化され、根拠と解釈の境界が曖昧になる [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **RAR (Retrieval Augmented Reasoning) の定義**: 目的は "externalize reasoning structure so the runtime can make reasoning visible, controllable, recoverable, and inspectable" — 推論構造をランタイム側へ外出しする [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **設計パラダイム転換**: 「より多くの context を与える」のではなく「推論構造を runtime に外出しする」 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **LLM の役割再定義**: 「自律的推論者」から「スキーマを埋める変換コンポーネント」へ。これにより軽量モデルでも頑健な推論が成立 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **権限境界の明確化**: Agent に最終判断を委譲するのではなく「解釈の枠組み（Claims / Conflicts / Gaps）」を返すことで、人間や専門家による最終判断との責務境界を構造化 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)
- **キーフレーズ**: "Agent design is not inside the model. It is the structure around the model" [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

## 主要な貢献
### Retrieval Lane の二分化
- **canonical_query**（長期信号）と **emerging_query**（現在のノイズ）を分離
- 検索が推論意図に従属するよう構造化、「何を見るために検索するか」を先行決定 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

### Typed Artifacts
- 中間表現全体をスキーマ化（**WebSource / Claim / StructuredDraft** 等）
- Claim には **Observation / Interpretation / Signal / Norm** 等の属性を付与
- LLM を「制御された変換コンポーネント」として位置付け、出力の構造を runtime 側で保証 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

### Conflicts / Gaps の維持
- 構造化ドラフトの**必須フィールド**として対立（conflicts）と欠損（gaps）を明示的に保持
- 不確実性を「推論の境界が見える」形で runtime に残す [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

### LangGraph + SQLite による状態管理
実装スタック:
```
Streamlit UI → FastAPI → LangGraph 状態機械 → SQLite checkpoint → 型付きアーティファクト → SSE ワークフロー状態
```
- 単なるステップ実行ではなく **中断・障害・復旧・可視性をシステム語彙に組み込む** 設計
- 操作対象は **Resume / Checkpoint / Workflow State / Persisted Artifact / SSE Status**
- UI は「Thinking...」ではなく **「Retrieving evidence...」「Extracting claims...」** などワークフローステップを可視化 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

## 適用ドメイン
- **主要例**: ファッション/スタイリング領域のトレンド分析（trend-to-rule）
  - 正解が曖昧でノイズが多く、Vector DB の急速な陳腐化（「昨日の信号 = 今日のノイズ」）が顕在化
- **副次例**: 契約レビュー（contract-question-agent）
  - 最終判断ではなく、専門家レビュー前の検証質問を返却 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

## 著者の開発上の教訓
- **Happy path の限界**: デモが動いても本番課題は隠れたまま。Poor E2E から問題構造が見える
- **軽量モデル制約下の設計**: 強力なモデルでの試行は問題を隠す。制約下での設計が堅牢性を高める
- **Disclaimer 不十分性**: 免責事項の増加は責務境界設計の代替にならない
- **FISI 哲学**: 完全設計より「小さく通す → 困る → 構造追加」の反復が実効的 [source](../../sources/Agent_ToolUse/vector-db-to-agent-runtime.md)

## 制限・注意点
- 実装途上（著者自身が「未完成な部分も多い」と述べる）
- 検証は特定ドメイン（ファッション・トレンド分析 / 契約レビュー）に限定、一般化可能性への定量的言及なし
- ベンチマーク・定量評価は無く、設計パラダイムの提示が主
- ブログ記事による一次資料の経験報告（査読なし、再現実装も公開リポジトリのみ）

## 実装関連
- GitHub: [trend-to-rule](https://github.com/mofuteq/trend-to-rule)
- 技術スタック: LangGraph, SQLite, FastAPI, Streamlit, SSE
- contract-question-agent（詳細URL記載なし）
