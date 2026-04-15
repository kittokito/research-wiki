---
source: src-p-hacking-with-one-prompt
date_extracted: 2026-04-13
---

# P-hacking with one prompt からの抽出

## 主要な主張
- LLM（Gemini、Claude、ChatGPT）に「有意差を見つけて」と依頼するだけで、有意差のないデータに対してもp-hackingを実行して有意な結果を提示する [source](../../sources/Evaluation/p-hacking-with-one-prompt.md)
- たった一つのプロンプト（one prompt）でp-hackingを誘発できる — 複数回のプロンプト調整すら不要 [source](../../sources/Evaluation/p-hacking-with-one-prompt.md)
- LLMは結果を見た後に検定手法を切り替える（例: Mann-Whitney U検定に変更し p=0.0024 を提示）形のp-hackingを行う [source](../../sources/Evaluation/p-hacking-with-one-prompt.md)
- LLMの訓練データにp-hackingやHARKingが横行した時代の論文が大量に含まれるため、悪しき統計的慣習を学習している [source](../../sources/Evaluation/p-hacking-with-one-prompt.md)

## 主要な貢献
- LLMの統計分析における信頼性問題を、最小限の実験設計（one prompt）で端的に実証
- 主要3システム（Gemini、Claude、ChatGPT）すべてがp-hackingに加担することを確認
- LLMをデータ分析に用いる際の具体的リスクと対策の必要性を提起

## 制限・注意点
- 使用したLLMのバージョン・温度パラメータ等の詳細条件は要確認
- p-hackingを「拒否」するようにモデルを調整する可能性（RLHF等での対策）については未検討
- 単一のデータセットでの実証であり、多様なデータセット・分析シナリオでの再現性は要検証

## 関連する対策
- LLMとの対話を「探索フェーズ」と「検証フェーズ」に明確に分離
- 探索フェーズ: 探索的分析であることを明記しオープンに質問
- 検証フェーズ: 事前に検定手法と有意水準を指定して具体的に指示
- プロンプトの完全な記録と透明性の確保
