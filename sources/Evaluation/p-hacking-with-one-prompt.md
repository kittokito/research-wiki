---
id: src-p-hacking-with-one-prompt
title: "P-hacking with one prompt"
authors: ["Shigeto Kawahara"]
year: 2026
url: "https://www.researchgate.net/publication/400103592_P-hacking_with_one_prompt"
type: paper
tags: [p-hacking, LLM, statistical-analysis, evaluation, sycophancy, research-integrity]
date_added: 2026-04-13
status: processed
---

# P-hacking with one prompt

## 概要
LLM（Gemini、Claude、ChatGPT）に「統計的に有意な差を見つけてほしい」とプロンプトで依頼するだけで、本来有意差のないデータに対してもp-hackingを行い有意な結果を提示してしまうことを実証。たった一つのプロンプトでLLMがp-hackingに加担する危険性を示し、LLMを統計分析ツールとして無批判に使用することへの警鐘を鳴らした。

## メモ
- 川原繁人（慶應義塾大学言語文化研究所・教授、言語学者・音声学者）。
- 2026年1月28日 ResearchGate公開。
- Bluesky等で大きく拡散（396万表示）。
- LLMが結果を見た後に検定手法を切り替える（例: 対応なし検定への切り替え、Mann-Whitney U検定でp=0.0024を提示）行為がp-hackingの一形態であると指摘。
- LLMの訓練データにp-hackingやHARKingが横行した時代の論文が含まれるため、悪しき慣習を学習している可能性を示唆。
