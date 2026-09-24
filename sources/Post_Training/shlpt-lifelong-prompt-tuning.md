---
id: src-shlpt-lifelong-prompt-tuning
title: "Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning"
authors: ["Chenyuan Wu", "Gangwei Jiang", "Defu Lian"]
year: 2024
url: "https://aclanthology.org/2024.findings-acl.650/"
type: paper
peer_review: accepted
venue: "ACL 2024 Findings"
tags: [prompt-tuning, PEFT, lifelong-learning, continual-learning, negative-transfer, catastrophic-forgetting, SHLPT]
date_added: 2026-06-09
status: processed
---

# Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning

## 概要
**lifelong prompt tuning**（パラメータ効率的な継続学習）において **negative transfer** を緩和する手法 **SHLPT (Similarity Heuristic Lifelong Prompt Tuning)** を提案。全タスクで一貫した positive transfer を保証する万能アルゴリズムは存在せず、非類似タスク間で negative transfer が生じる——その原因を「アルゴリズム選択とタスク特性のミスアラインメント」と特定。**学習可能な類似度メトリック**でタスクを2サブセット（類似/非類似）に分割し、どちらからも有益な転移を引き出す。さらに **parameter pool** で catastrophic forgetting に対処。lifelong learning ベンチマークでSOTAを上回り、多様なタスク系列で negative transfer に頑健。

## メモ
- ACL 2024 Findings 採択（2024.findings-acl.650, pp.10944–10959, DOI 10.18653/v1/2024.findings-acl.650）。
- 主題は prompt tuning（PEFT）× 継続学習（lifelong learning）。**negative transfer / catastrophic forgetting** の両方に同時対処する点が貢献。
- ユーザー提示の URL（`2024.findings-acl.650.pdf`）はこの論文。
