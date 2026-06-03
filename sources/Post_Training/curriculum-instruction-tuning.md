---
id: src-curriculum-instruction-tuning
title: "Curriculum Instruction Tuning (EmergentMind topic overview)"
authors: ["EmergentMind (AI-generated synthesis)"]
year: 2026
url: "https://www.emergentmind.com/topics/curriculum-instruction-tuning"
type: reference
peer_review: n/a
venue: ""
tags: [curriculum-learning, instruction-tuning, SFT, difficulty-ordering, data-curriculum, easy-to-hard, post-training]
date_added: 2026-06-03
status: processed
---

# Curriculum Instruction Tuning (EmergentMind topic overview)

## 概要
EmergentMind のトピック概観ページ。「**curriculum instruction tuning**」= 訓練データと学習スケジュールを難易度指標や教育学的原則に基づいて系統的に順序づけ・最適化する instruction tuning 手法、を ~11 本の論文から統合解説したもの。従来のランダムシャッフルではなく「易→難（easy-to-hard）」の進行で SFT データを組織化する。

## メモ
EmergentMind は論文を AI で統合する二次的アグリゲータ。本ページ自体は査読対象外（type: reference, n/a）であり、**一次情報は下記の基礎論文（arXiv）**にある。本 wiki には curriculum instruction tuning を扱うトピックページ [wiki/topics/Post_Training/curriculum-instruction-tuning.md](../../wiki/topics/Post_Training/curriculum-instruction-tuning.md) を作成。
本リポジトリ既収録の [SFT Data Composition / DMT](../../wiki/papers/Post_Training/sft-data-composition.md)（SFTのデータ配合・段階学習）と論点が直結する。

### 基礎論文（このページが引用する代表的なもの）
- TAPIR: "Distilling Instruction-following Abilities of LLMs with Task-aware Curriculum Planning" (arXiv 2405.13448, 2024)
- CAMPUS: "Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning" (arXiv 2509.13790, 2025)
- Data-CUBE: "Data Curriculum for Instruction-based Sentence Representation Learning" (arXiv 2401.03563, 2024)
- CITING: "Large Language Models Create Curriculum for Instruction Tuning" (arXiv 2310.02527, 2023)
- D-MoLE: "Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning" (arXiv 2506.11672, 2025)
- "Instruction Tuning with Human Curriculum" (arXiv 2310.09518, 2023)
- INSTA: "Instruction Matters: A Simple yet Effective Task Selection for Optimized Instruction Tuning" (arXiv 2404.16418, 2024)
- LACT: "Improving Complex Reasoning over Knowledge Graph with Logic-Aware Curriculum Tuning" (arXiv 2405.01649, 2024)
- CLASS-IT: "Conversational and Lecture-Aligned Small-Scale Instruction Tuning" (arXiv 2510.25364, 2025)
- 教育学応用系: Gagne's Nine Events (arXiv 2503.09276, 2025) / CLO-PLO alignment (arXiv 2510.25905, 2025)
