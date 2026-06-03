---
id: src-does-bert-rediscover-nlp-pipeline
title: "Does BERT Rediscover a Classical NLP Pipeline?"
authors: ["Jingcheng Niu", "Wenjie Lu", "Gerald Penn"]
year: 2022
url: "https://aclanthology.org/2022.coling-1.278/"
type: paper
peer_review: accepted
venue: "COLING 2022"
tags: [BERT, probing, GridLoc, interpretability, NLP-pipeline, layer-analysis, re-examination, linguistic-structure]
date_added: 2026-06-03
status: processed
---

# Does BERT Rediscover a Classical NLP Pipeline?

## 概要
[BERT Rediscovers the Classical NLP Pipeline](../../wiki/papers/Pretraining/bert-rediscovers-nlp-pipeline.md)（Tenney et al., 2019）や Jawahar et al. (2019) の「表層=下位層 / 統語=中間層 / 意味=上位層」という層分離の主張を**批判的に再検証**した論文。結論は、**そのパイプライン的層分離には決定的な経験的支持が乏しい**（probe の方法論・指標に敏感）こと。ただし **BERT の構造は言語的に根拠づけられている**ものの、それは「層の深さ」だけで説明できるより**ニュアンスのある**形である。著者は **GridLoc** という新しいプローブ——トークン位置・訓練ラウンド・乱数シードを考慮——を提案し、層深さに頼らないより強い規則性を検出できると示す。

## メモ
ACL Anthology 2022.coling-1.278、**COLING 2022 採択**。著者は University of Toronto（Niu, Lu, Penn）。コード: github.com/frankniujc/gridloc_probe。
原説 [BERT Rediscovers...](../../wiki/papers/Pretraining/bert-rediscovers-nlp-pipeline.md)（Tenney et al., ACL 2019）と対をなす「主張↔再検証」のペア。深層ネットの言語構造の所在をめぐる議論として [言語構造の獲得理論](../../wiki/papers/Pretraining/language-structure-acquisition.md) とも接続。
