---
id: src-your-evals-will-break
title: "Your Evals Will Break and You Won't See It Coming"
authors: ["Lun Wang"]
year: 2026
url: "https://wanglun1996.github.io/blog/your-evals-will-break.html"
type: blog
peer_review: n/a
venue: ""
tags: [evaluation, benchmark, emergent-capabilities, grokking, phase-transition, order-parameter, self-evolving-evaluation, AI-safety]
date_added: 2026-05-19
status: processed
---

# Your Evals Will Break and You Won't See It Coming

## 概要
モデルが新しい能力レジームに遷移するとき、現在のLLM評価インフラは予測不可能な形で破綻するという警鐘エッセイ。既存ベンチマークやセーフティ評価は「次世代モデル = 現行モデルの強化版」を暗黙の前提に置いているため、創発（emergence）やグロッキング（grokking）のような不連続な能力変化に対しては事後的にしか反応できない。物理学の「秩序パラメータ（order parameter）」概念を借り、能力相転移を予測する計測量と、評価自体の陳腐化を自己検出する「自己進化型評価（self-evolving evaluation）」が必要だと主張する。

## メモ
- 著者 Lun Wang はAI Safety 研究者。Google DeepMind を経て NVIDIA Principal Research Scientist 参加予定、PhD UMD（CS、AI Safety 専攻）。GitHub: wanglun1996。
- 2026-05-17 公開のブログ記事。短いポジションエッセイ形式。
- 主要メッセージ: 「評価は訓練目標の**上流**にある」「評価の失敗は予測可能性向上で緩和できるが、回避はできない」。
- 引用される研究: Wei et al. 2022（emergent abilities）、Power et al. 2022 / Liu et al. 2022（grokking）、Schaeffer et al. 2023（emergence はメトリックのアーティファクトとする反論）、Nanda et al. 2023（grokking のメカニスティック解釈）、Shan, Li, Sompolinsky 2026（継続学習の秩序パラメータ）。
- 具体例として「戦略的情報隠匿（strategic information withholding）」を挙げ、accuracy ベンチマークでは原理的に検出不可能な能力クラスがあると指摘。
- 行動指針は2段階: (1) スタイル化設定で発見した秩序パラメータを実スケール LLM へ拡張、(2) スコア分布の変化や評価間相関構造の変動などメタシグナルを監視する適応型評価基盤の構築。
- 本リポジトリの [P-hacking with one prompt](../../wiki/papers/Evaluation/p-hacking-with-one-prompt.md)・[LiveBench](../../wiki/papers/Evaluation/livebench.md)・[GSM-Symbolic](../../wiki/papers/Reasoning/gsm-symbolic.md)・[LLM Reasoning Failures](../../wiki/papers/Surveys_Overview/llm-reasoning-failures.md) の上位レイヤの議論（「個別ベンチマークの欠陥」ではなく「評価インフラ全体の構造的脆弱性」）として位置付けられる。
