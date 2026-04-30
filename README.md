# research-wiki

LLM・機械学習・関連分野の論文／技術レポート／ブログ等を継続的に取り込み、要約・抽出・解釈・横断インデックスとして整理するための個人研究 wiki。

人間と LLM の双方が同じ規約に従って読み書きすることを前提に、ファイルベースで運用している。詳細な運用規約は [SCHEMA.md](SCHEMA.md) を参照。

## 設計思想

- **生ソース・抽出・合成を分離する** — 同じ論文に対して `sources/`（メタ）・`evidence/`（クレーム抽出）・`wiki/papers/`（解釈・要約）の3層を持ち、役割を混ぜない。
- **wiki ページは肥大化させない** — 詳細な主張・ベンチマーク・引用は `evidence/` に追い出し、`wiki/` 側は要約と判断に徹する。
- **論点構造で並べる** — `wiki/index.md` は機械的ソートではなく「関連論文が隣接する」ように手動で配置し、論争・系譜・手法バリエーションを読みやすくする。
- **append-only な変更ログ** — 取り込み・更新は `log.md` に時系列で記録し、後から経緯を辿れるようにする。

## ディレクトリ構成（概略）

```
research-wiki/
├── SCHEMA.md         # 運用規約（命名・カテゴリ・frontmatter・リンク規約）
├── log.md            # 時系列の変更ログ（append-only）
├── sources/          # 生ソースのメタデータ（不変）
├── evidence/         # ソースから抽出したクレーム・数値・ベンチ
├── wiki/             # 合成・解釈ページ
│   ├── index.md      # wiki 全体のカタログ
│   ├── papers/       # 論文別ページ
│   ├── topics/       # トピック別ページ
│   ├── models/       # モデル別ページ
│   ├── comparisons/  # 比較ページ
│   ├── benchmarks/   # ベンチマーク結果
│   └── engineering/  # 実装メモ・ノウハウ
├── decisions/        # 採用・棄却・未決の判断ログ
├── index/            # 索引（recent / topics / models / peer-review / open-questions）
└── presentations/    # 発表資料
```

`sources/` `evidence/` `wiki/papers/` `wiki/topics/` はカテゴリ別サブフォルダ（`Architecture`、`RL`、`Reasoning`、`Graph_Network` 等）で分類される。カテゴリ一覧は [SCHEMA.md](SCHEMA.md#カテゴリ一覧) を参照。

## 主要なエントリポイント

| 目的 | パス |
|---|---|
| wiki 全体のカタログ | [wiki/index.md](wiki/index.md) |
| 直近の追加 | [index/recent.md](index/recent.md) |
| 査読・採択状況一覧 | [index/peer-review.md](index/peer-review.md) |
| トピック索引 | [index/topics.md](index/topics.md) |
| モデル索引 | [index/models.md](index/models.md) |
| 未解決の問い | [index/open-questions.md](index/open-questions.md) |
| 変更ログ | [log.md](log.md) |

## 取り込みの流れ

新しいソースを追加するときは SCHEMA.md の運用ルールに従い、概ね以下の順で進める。

1. `sources/{Category}/{slug}.md` にメタデータを作成（不変）
2. `evidence/{Category}/{slug}.md` にクレーム・数値を抽出
3. `wiki/papers/{Category}/{slug}.md`（または既存の `wiki/topics/` ページ）を作成・更新
4. 既存の結論が変わる場合は `decisions/` を更新
5. 未解決の問いがあれば `index/open-questions.md` に追加
6. `log.md` と `wiki/index.md` ・ `index/` 配下を更新

frontmatter の必須フィールド・カテゴリの選び方・peer_review 値の付け方・リンク規約はすべて [SCHEMA.md](SCHEMA.md) に定義されている。

## 記述スタイル

- 簡潔な技術日本語、1ページ1役割
- 抽出した事実は bullet、合成は短い paragraph
- 「ソースからの事実」と「現時点の解釈」を明確に分離
- すべての主張にソースリンクを付与
