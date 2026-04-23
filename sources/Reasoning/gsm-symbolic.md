---
id: src-gsm-symbolic
title: "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models"
authors: ["Iman Mirzadeh", "Keivan Alizadeh", "Hooman Shahrokhi", "Oncel Tuzel", "Samy Bengio", "Mehrdad Farajtabar"]
year: 2024
url: "https://arxiv.org/abs/2410.05229"
type: paper
peer_review: accepted
venue: "ICLR 2025"
tags: [reasoning, math, benchmark, GSM8K, symbolic, limitations]
date_added: 2026-04-07
status: processed
---

# GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

## 概要
LLMの数学的推論能力を検証するため、シンボリックテンプレートを用いて多様な問題を生成するGSM-Symbolicベンチマークを提案。同一構造の問題で数値を変えるだけでモデルの性能に大きなばらつきが生じることを発見。問題の複雑度が増す（特に無関係な節を追加する）と性能が大幅に低下し、一部モデルでは65%以上の低下を記録。現在のLLMは真の論理的推論を実行できず、学習データの推論ステップを複製しているに過ぎないと結論。

## メモ
- cs.LG, cs.AI。Apple Research。
- 2024年10月公開、2025年8月改訂。
- GSM8Kの拡張・改良ベンチマーク。
