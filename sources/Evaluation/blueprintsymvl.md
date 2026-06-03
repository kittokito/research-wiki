---
id: src-blueprintsymvl
title: "BlueprintSymVL: A discriminative benchmark for VLM symbol recognition in engineering blueprints"
authors: ["Vasil Shteriyanov", "Rimma Dzhusupova", "Jan Bosch", "Helena Holmström Olsson"]
year: 2025
url: "https://doi.org/10.1016/j.rineng.2025.108171"
type: paper
peer_review: accepted
venue: "Results in Engineering 28 (2025) 108171"
tags: [VLM, benchmark, engineering, blueprint, P&ID, symbol-recognition, in-context-learning, industrial-AI, occlusion, visual-similarity]
date_added: 2026-05-28
status: processed
---

# BlueprintSymVL: A discriminative benchmark for VLM symbol recognition in engineering blueprints

## 概要
産業用エンジニアリング・ブループリント（特に P&ID = Piping and Instrumentation Diagram）における VLM のシンボル認識能力を評価する**最初のドメイン特化ベンチマーク**。**one-shot visual in-context querying** 戦略を採用し、事前学習知識や標準化シンボル体系への依存を排除。GPT-4o / Gemini 2.5 Pro / InternVL 2.5 78B / Qwen 2.5 VL 72B の4モデルで初のベースラインを提示し、Gemini 2.5 Pro がトップ（EMR 50.5%）でも実用にはまだ及ばないことを示す。失敗モード（cluttered environments, visually similar distractors, hallucination）を体系的に同定し、現状の VLM は autonomous deployment に不適で human-in-the-loop ワークフローでの統合が適切と結論。

## メモ
- Results in Engineering 28 (2025) 108171, Elsevier, CC BY 4.0
- DOI: [10.1016/j.rineng.2025.108171](https://doi.org/10.1016/j.rineng.2025.108171)
- Received 29 July 2025 / Revised 21 October 2025 / Accepted 9 November 2025 / Online 13 November 2025
- Chalmers Research repository PDF: https://research.chalmers.se/publication/549362/file/549362_Fulltext.pdf
- Dataset (Zenodo): [10.5281/zenodo.17250377](https://doi.org/10.5281/zenodo.17250377)
- 第一著者は McDermott（global engineering / construction provider）と Eindhoven University of Technology に所属、Action Research methodology を採用しエネルギー産業における実問題に直接接続
- 著者所属: McDermott (Engineering, The Hague) / Eindhoven University of Technology / Chalmers University of Technology / Malmö University
