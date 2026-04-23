---
title: "The Geometry of Forgetting"
aliases: ["Geometry of Forgetting", "HIDE"]
created: 2026-04-14
updated: 2026-04-14
tags: [memory, forgetting, embedding, interference, false-memory, geometry, dimensionality]
peer_review: preprint
venue: ""
sources: [src-geometry-of-forgetting]
---

# The Geometry of Forgetting

> **査読**: 📝 preprint

Barman, Starenky, Bodnar, Narasimhan, Gopinath (2026) — arXiv 2604.06222 / Sentra + MIT

## ソースからの事実
- べき乗則忘却は時間減衰ではなく競合記憶間の干渉から発生（b = 0.460 ± 0.183、人間 b ≈ 0.5） [source: §Interference](../../../sources/Reasoning/geometry-of-forgetting.md)
- 減衰のみでは b ≈ 0.009で人間値の50分の1。干渉が支配的ドライバー [source: §Interference](../../../sources/Reasoning/geometry-of-forgetting.md)
- 本番用埋め込みモデルは名目384〜1,024次元に関わらず有効次元~16に集中（dimensionality illusion） [source: §Dimensionality illusion](../../../sources/Reasoning/geometry-of-forgetting.md)
- 未修正事前学習済み埋め込みのcosine類似度だけでDRM偽記憶を再現（偽警報率0.583 vs 人間~0.55） [source: §False memories](../../../sources/Reasoning/geometry-of-forgetting.md)
- 間隔効果を再現: long > medium > short > massed（Cohen's d = 13.1） [source: §Spaced repetition](../../../sources/Reasoning/geometry-of-forgetting.md)
- vector averaging fallacy: 近傍埋め込みの平均化は検索精度を破壊的に劣化させる [source: §Discussion](../../../sources/Reasoning/geometry-of-forgetting.md)

→ 詳細: [evidence](../../../evidence/Reasoning/geometry-of-forgetting.md)

## 現時点の解釈
忘却や偽記憶が「生物学的バグ」ではなく、意味による情報組織化と近接性による検索を行うあらゆるシステムの幾何学的必然であるという主張は、RAGシステムやベクトルDBの設計に直接的な示唆を持つ。

特に重要な実用的含意:
1. **ベクトルDBは必ず忘却する**: 有効次元~16の埋め込みモデルは干渉脆弱領域にあり、データベースサイズの増大とともにべき乗則で検索精度が劣化する。これは設計上の欠陥ではなく幾何学的必然。
2. **vector averaging fallacy**: 会話履歴や文書の要約を埋め込み平均で行う一般的手法は、角度差を崩壊させ検索を破壊する。
3. **偽記憶はゼロコスト**: セマンティッククラスタリングが検索を有用にする同じ構造が偽記憶を生む。除去すればモデルの有用性も失われるトレードオフ。

有効次元数の増加が干渉を低減するという知見は、埋め込みモデルの設計方針（d_eff > 100で干渉はほぼ消失）として具体的。ただしTOT率が人間の2.4倍であるなど、定量的一致は現象によってばらつきがある。

## 関連ページ
- [GSM-Symbolic](gsm-symbolic.md) — パターンマッチングへの依存、LLMの根本的制約
- [The Reversal Curse](reversal-curse.md) — LLMの汎化の根本的失敗
- [Sarashina-Embedding-v2](../Domain_Specific/sarashina-embedding-v2.md) — 埋め込みモデルの実例
- [Conditional Memory via Scalable Lookup](../Architecture/conditional-memory-scalable-lookup.md) — 記憶スパース性の別アプローチ

## 未解決の問い
- 有効次元数を意図的に増加させた埋め込みモデルは干渉をどの程度低減できるか？精度とのトレードオフは？
- LLMの内部表現の有効次元数は埋め込みモデルの~16と同程度か、それとも異なるレジームにあるか？
- メタデータ制約やハイブリッド検索（lexical + semantic）はvector averaging fallacyをどの程度緩和するか？
