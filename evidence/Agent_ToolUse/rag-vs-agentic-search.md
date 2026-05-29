---
source: src-rag-vs-agentic-search
date_extracted: 2026-05-29
---

# RAGとAgentic Searchの戦争を終わらせに来た!!! からの抽出

## 主要な主張
- **論争は用語の定義のズレから生じた**: 「RAG は終わった」という言説は、各手法が評価された背景コンテキストが省略されたまま拡散し、初学者に混乱を招いている [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **RAG の定義は拡張された**: 初期は「ベクトル検索を用いること」が前提だったが、現在は「外部データを参照して生成を強化する」より広い定義に進化。Microsoft / AWS / NVIDIA も広義解釈を採用 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **Agentic Search の本質**: 単なるファイルシステム探索ではなく「**推論を用いて複数回の検索を繰り返すアプローチ**」。検索手段（ベクトル検索 / grep・glob コマンド等）は限定されない [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **ベクトル検索 RAG は死んでいない**: 「死んでいない。必要な場面はたくさんある。ただし、最盛期のように何でもかんでもベクトル検索という間違った状況からは抜け出した」 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **結論（使い分け原則）**: 「ベクトル検索 RAG とファイルシステム探索 RAG は、対象データの性質・規模・タスクで使い分けることが大事」 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

## 論争の発端（固有名）
- **Anthropic @bcherny 氏**: 「Claude Code の初期バージョンでは RAG + ローカルベクトル DB を使用していたが、エージェント型検索の方が一般的にうまく機能することがすぐにわかった」 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **Karpathy 氏**: LLM Wiki（知識データをローカルに加工・集約してナレッジグラフ化し Agentic Search する方法）がベクトル検索 RAG より手軽で機能しやすいことを示唆 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **大規模コンテキスト論**: コンテキストウィンドウ拡大により「テキスト全体を LLM に渡せば RAG 不要では？」という議論（CAG 推進） [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

## 技術的整理

### Agentic な検索アプローチの留意点（3点）
- ① **検索の長時間化**: 複数回検索と吟味時間により処理時間が延伸
- ② **コスト増加**: 検索結果の吟味によりコンテキスト消費量が増加
- ③ **後続フェーズへの精度低下**: エージェントコンテキストに検索履歴が残るとノイズ化し、後続作業の精度が劣化
- **対策トレンド**: 検索エージェントをエンジン側に寄せる / 軽量モデルを使う / 良い結果のみ返送する、等の実装工夫が増加中 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

### 取得手段の比較
| 手法 | 利点 | 制限 |
|---|---|---|
| ベクトル検索 RAG | 曖昧な意味検索に優れる | インデックス構築コスト |
| ファイルシステム探索 RAG | 事前準備不要・高速・クエリが一般的なら高精度 | 探索空間が狭くないと破綻しやすい |
| CAG（Context-Augmented Generation） | 小規模データで高精度・キャッシュが効く | 小型モデル / 多タスク / 大型ドキュメントでは破綻 |

### CAG（Context-Augmented Generation）
- **基本概念**: 大規模コンテキストウィンドウを活用し、必要情報を事前に入力してキャッシュを効かせる方式 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **成功する場面**: フラッグシップモデル使用時 / 数ファイル程度の軽い読み込み / 単純質問対応 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **破綻する場面**: 小型モデル使用 / 複数タスクを実行するエージェント用途 / 大型ドキュメント保持時（コンテキストノイズ増加） [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

### ファイルシステム探索 RAG
- **利点**: 「事前にインデックスを構成せずファイルシステムに置くだけでいい」「探索範囲が狭く、クエリが一般的なもので済む場合は精度が高い」「コマンド実行で済むため検索ステップが高速」 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **有利なデータ**: コードベースのような具体的文字列検索が有効な領域 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **破綻条件**: 「探索空間がある程度狭くないと破綻しやすい点に注意」 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

### Karpathy の LLM Wiki 考察
- LLM にナレッジファイルを解釈・Wiki 化させ、Obsidian 等で関連性を磨き、ファイルシステム探索 RAG で取得しやすいナレッジベースを自動構築する手法 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **特徴**: Graph RAG に近い概念をファイルシステムで完結させた工夫 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **利点**: Graph RAG の弱点（大規模時の高コスト・結果判定困難）を、小規模範囲での可視化・精度維持で克服 [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **位置づけ**: ファイルシステム探索 RAG 活用の 1 アイディア [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

## まとめの提言
- **LLM 発信者へ**: X 等でのポスト拡散時、コンテキスト省略が初学者の混乱を招くため、技術評価の前提コンテキストを明示すべき [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)
- **初学者へ**: 発信者が「どの具体的コンテキストで技術を評価しているか」に注視すべき [source](../../sources/Agent_ToolUse/rag-vs-agentic-search.md)

## 制限・注意点
- 査読なしのオピニオン記事。定量評価・ベンチマークは含まれず、業界の言説整理と技術的直観の提示が主
- 各手法の優劣を裏付ける数値や実験は示されておらず、「使い分け」という結論の有効性は別途検証が必要
- 論争の発端として引用される主張（@bcherny / Karpathy）は SNS 投稿に基づく二次的要約
