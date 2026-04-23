---
source: src-livebench
date_extracted: 2026-04-21
---

# LiveBench からの抽出

## 主要な主張
- テストセット汚染はLLM評価の主要障害で、新モデル学習データに過去ベンチマークが混入してベンチマークが陳腐化する [source](../../sources/Evaluation/livebench.md)
- LLM-judge とクラウドソースされた評価は、難問でのスコアリングでバイアス・破綻を招く [source](../../sources/Evaluation/livebench.md)
- LiveBench は (1) 最新情報源からの頻繁更新、(2) 客観的ground-truthによる自動スコアリング、(3) 広範なタスク群（math / coding / reasoning / language / instruction following / data analysis）の3条件を同時達成した初のベンチマーク [source](../../sources/Evaluation/livebench.md)
- 問題ソース：最近リリースされた math competitions、arXiv 論文、ニュース記事、datasets [source](../../sources/Evaluation/livebench.md)
- Big-Bench Hard、AMPS、IFEval の **汚染耐性を高めた困難化版** を含む [source](../../sources/Evaluation/livebench.md)
- 0.5B〜405B の主要クローズド/オープンソースモデルを多数評価、**トップモデルでも 70% 未満の正答率** [source](../../sources/Evaluation/livebench.md)
- 問題は **月次** で追加・更新、新タスク・既存タスクの困難化版を継続リリース [source](../../sources/Evaluation/livebench.md)
- 全問題・コード・モデル回答を公開、コミュニティ参画を前提にした運用 [source](../../sources/Evaluation/livebench.md)

## 主要な貢献
- 汚染耐性 + 客観自動採点 + 広範タスクを同時に満たすベンチマーク設計原則の提示
- 月次更新による経年対応型ベンチマークの運用モデル
- 0.5B-405Bを横断する大規模比較データ
- Big-Bench Hard / AMPS / IFEval の汚染耐性・難易度強化版

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| タスク領域数 | 6 | math / coding / reasoning / language / instruction following / data analysis |
| 評価モデル規模 | 0.5B - 405B | クローズド/オープン横断 |
| トップモデル正答率 | < 70% | 2024年時点、継続的に困難化 |
| 更新頻度 | 月次 | 問題追加・既存タスクの困難化版リリース |

## 制限・注意点
- 月次更新は運用負荷が高く、コミュニティ貢献に依存
- 「汚染耐性」は新情報源への依存に還元されており、公開後一定期間経過すれば再び汚染される構造的問題は残る（ただし月次更新で緩和）
- LLM-judgeの代替として客観採点を採用する設計上、自由記述タスクの評価範囲は制限される
- 公開している以上、月次の新バッチも将来のモデル学習に混入するリスクは内在する

## 実装関連
- 全問題・コード・モデル回答が公開
- 新モデル評価はスコア公開フォームまたは再実行可能なスクリプトから実施
- 採点ロジックは objective ground-truth のみに依存（LLM-judge を排除）
