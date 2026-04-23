# Research Wiki Schema

このファイルはwiki全体の運用規約を定義する。LLMがページを作成・更新する際はこのスキーマに従うこと。

## ディレクトリ構成

```
research-wiki/
├── SCHEMA.md           # 本ファイル（運用規約）
├── log.md              # 時系列変更ログ（append-only）
├── sources/            # 生ソース（不変）
│   └── {Category}/     # カテゴリ別サブフォルダ
│       └── {slug}.md   # 1ソース1ファイル
├── wiki/
│   ├── index.md        # wikiコンテンツカタログ
│   ├── topics/         # トピック別ページ
│   │   └── {Category}/ # カテゴリ別サブフォルダ
│   ├── models/         # モデル別ページ
│   ├── papers/         # 論文別ページ
│   │   └── {Category}/ # カテゴリ別サブフォルダ
│   ├── comparisons/    # 比較ページ
│   ├── benchmarks/     # ベンチマーク結果
│   └── engineering/    # 実装メモ・ノウハウ
├── evidence/           # 抽出されたクレーム・引用・数値
│   └── {Category}/     # カテゴリ別サブフォルダ
│       └── {slug}.md   # 1ソースにつき1ファイル
├── decisions/          # 採用・棄却・未決の判断ログ
│   └── {slug}.md       # 1判断1ファイル
└── index/              # 各種インデックス
    ├── topics.md       # トピック索引
    ├── models.md       # モデル索引
    ├── recent.md       # 最近の追加
    ├── peer-review.md   # 査読・採択状況一覧
    └── open-questions.md # 未解決の問い
```

## カテゴリ一覧

`sources/`、`evidence/`、`wiki/topics/`、`wiki/papers/` は以下のカテゴリでサブフォルダを持つ。
同一論文は `sources/`、`evidence/`、`wiki/papers/` で同じカテゴリに配置すること。

| カテゴリ | 内容 |
|---|---|
| `Surveys_Overview` | サーベイ論文・分野概観 |
| `Technical_Report` | テクニカルレポート（モデルリリース等） |
| `Architecture` | モデルアーキテクチャ（Transformer改良、MoE等） |
| `Pretraining` | 事前学習（データ、目的関数、スケーリング則） |
| `Post_Training` | 事後学習（SFT、DPO、RLHF等） |
| `RL` | 強化学習（RLHF以外の純RL手法含む） |
| `Evaluation` | 評価・ベンチマーク設計 |
| `Safety_Alignment` | 安全性・アラインメント・ガードレール |
| `Inference_Decoding` | 推論高速化・デコーディング戦略 |
| `Reasoning` | 推論能力（CoT、論理、計画） |
| `Multimodal` | マルチモーダル（Vision-Language等） |
| `Efficiency_Optimization` | 効率化・最適化（量子化、蒸留、プルーニング） |
| `Math` | 数学的推論・数学特化モデル |
| `Domain_Specific` | ドメイン特化（医療、法律、科学等） |
| `Agent_ToolUse` | エージェント・ツール使用・関数呼び出し |
| `Physical_AI` | 物理AI・ロボティクス・身体性 |
| `Graph_Network` | グラフ・ネットワーク科学（コミュニティ検出、GNN、グラフ分割等） |
| `Symbolic_Computation` | 記号計算・数式処理・数学的基礎（記号回帰、形式的手法、計算代数等） |
| `Social_Science` | 社会科学・経済学・政策・労働（AI導入の社会的帰結等） |
| `Press_Releases` | プレスリリース・発表・ニュース |

## ファイル命名規則

- スラッグは kebab-case: `attention-is-all-you-need.md`
- 日本語タイトルはfrontmatter内に記載、ファイル名は英語スラッグ
- ファイルパス例: `sources/Architecture/attention-is-all-you-need.md`

## ソースファイル形式 (`sources/`)

```markdown
---
id: src-{連番 or slug}
title: "論文/記事タイトル"
authors: ["著者1", "著者2"]
year: 2024
url: "https://..."
type: paper | blog | code | video | book
peer_review: accepted | workshop | under-review | preprint | n/a
venue: "学会・ジャーナル名（例: ICLR 2024, Nature 2025）"
tags: [tag1, tag2]
date_added: 2026-04-07
status: unprocessed | processed | stale
---

# {タイトル}

## 概要
（1-3文の要約）

## メモ
（取り込み時のメモ）
```

## Evidenceファイル形式 (`evidence/`)

```markdown
---
source: src-{id}
date_extracted: 2026-04-07
---

# {ソースタイトル} からの抽出

## 主要な主張
- 主張1 [source](../sources/{slug}.md)
- 主張2 [source](../sources/{slug}.md)

## 主要な貢献
- ...

## 制限・注意点
- ...

## ベンチマーク結果
| ベンチマーク | スコア | 備考 |
|---|---|---|
| ... | ... | ... |

## 実装関連
- ...
```

## Wikiページの粒度ガイドライン

- `wiki/` ページは**要約と解釈**に徹する。詳細な主張リスト・ベンチマーク・緩和策は `evidence/` に置く
- `wiki/` からは `→ 詳細: [evidence](../evidence/{slug}.md)` でリンクし、必要なときだけ掘れる構造にする
- これにより論文数が増えてもwikiページの肥大化を防ぎ、evidence（抽出）とwiki（合成）の役割分離を維持する

## Wikiページ形式 (`wiki/**`)

```markdown
---
title: "ページタイトル"
aliases: ["別名1"]
created: 2026-04-07
updated: 2026-04-07
tags: [tag1, tag2]
sources: [src-id1, src-id2]
---

# {タイトル}

## ソースからの事実
- 事実1 [source](../sources/{slug}.md)

## 現時点の解釈
（合成・分析・判断）

## 関連ページ
- [[リンク先]]

## 未解決の問い
- ?
```

## Decisionファイル形式 (`decisions/`)

```markdown
---
title: "判断タイトル"
date: 2026-04-07
status: adopted | rejected | open
related_sources: [src-id1]
---

# {タイトル}

## 判断
（結論を1-2文で）

## 根拠
- ...

## 代替案
- ...

## フォローアップ
- ...
```

## peer_review フィールド定義

`sources/` の frontmatter に含める `peer_review` フィールドの値は以下のいずれかとする。

| 値 | 意味 |
|---|---|
| `accepted` | 査読付き学会（conference）またはジャーナル（journal）に採択済み |
| `workshop` | 査読付きワークショップに採択（メイントラックではない） |
| `under-review` | 査読中（投稿先が判明しているがまだ採否が出ていない） |
| `preprint` | プレプリント（arXiv等に投稿のみ、査読なし） |
| `n/a` | 査読の対象外（ブログ記事、ツイート、プレスリリース、テクニカルレポート等） |

`venue` には採択先の学会名・ジャーナル名・年を記載する（例: `"ICLR 2024"`, `"Nature 2025"`, `"ACSAC 2024"`）。
`preprint` や `n/a` の場合は `venue: ""` とする。

#### venue調査時の注意

**arXivだけを見て `preprint` と判定しない**。arXivのCommentsフィールドに採択情報が記載されていないケースが多く、以下の追加ソースを必ず確認すること:

- **OpenReview**: 論文タイトルで `site:openreview.net` 検索。ICLR/NeurIPS等のconference submissionがあれば `under-review`（decision未了の場合）または `accepted`（decision確定の場合）
- **arXiv Comments**: `"Submitted to X"` / `"Accepted at X"` / `"To appear in X"` などのフレーズを確認
- **著者所属サイト・著者個人ページ**: 公式論文リストに採択venue記載がある場合が多い
- **会議公式の採択リスト**: paperlist.semanticscholar.org、papercopilot.com 等

**偽陽性に注意**: 検索結果で「Published as a conference paper at X」が出ても、**それが対象論文自体のものか、対象論文を引用する別論文のものか**を必ず確認する（PDF冒頭のタイトル・著者を照合）。OpenReviewのforum IDは別論文の可能性があるため、タイトル完全一致を確認すること。

## 運用ルール

### 取り込み（Ingest）
1. `sources/` にソースメタデータファイルを作成（不変）
2. `evidence/` にクレーム・数値を抽出
3. `wiki/` の既存ページを更新（新規作成より更新優先）
4. 既存の結論が変わる場合は `decisions/` を更新
5. 未解決の問いがあれば `index/open-questions.md` に追加
6. `log.md` に変更を記録
7. `wiki/index.md` と `index/` 配下を更新

### 記述スタイル
- 簡潔な技術日本語
- 1ページ1役割
- 抽出した事実はbullet、合成はshort paragraph
- 「ソースからの事実」と「現時点の解釈」を明確に分離
- ソースリンクを必ず付与

### リンク規約
- wiki内リンク: 相対パス `../topics/{Category}/{slug}.md`
- ソース参照（evidenceから）: `[source](../../sources/{Category}/{slug}.md)`
- ソース参照（wiki/papersから）: `[source](../../../sources/{Category}/{slug}.md)`
- ソース参照（セクション指定）: `[source: §3.1](../../sources/{Category}/{slug}.md)` — 主張の根拠となる論文内セクションを明示する
- evidence参照（wiki/papersから）: `[evidence](../../../evidence/{Category}/{slug}.md)`
- 外部URL: `[表示名](https://...)`

### インデックスの並び順

各インデックスファイルは役割ごとに異なるソート規則を持つ。

| ファイル | 並び順 |
|---|---|
| `wiki/index.md` | カテゴリ内は**話題クラスタ順**（関連論文が隣接するよう手動配置）。同一クラスタ内は**追加順（append）**。論争・系譜・手法バリエーションなど、論点構造が読めるよう配置する。機械的ソートは避ける |
| `index/recent.md` | **日付降順**（新しい追加が上） |
| `index/peer-review.md` | 査読状態グループ内で**採択年の昇順**（古い研究から新しい研究へ） |
| `index/topics.md` | 特に規定なし（トピック追加順が基本。アルファベット順への整列は任意） |

`wiki/index.md` のカテゴリが20件を超えたら、`wiki/topics/{Category}/` にサブトピックページを切り出すことを検討する。

### メンテナンス（Lint）
定期的に以下を検出する:
- 重複ページ
- 陳腐化したページ（updated が古い）
- ソースなしの主張
- 孤立ページ（被リンクゼロ）
- index未登録のページ
- `wiki/index.md` のカテゴリ肥大化（20件超）
