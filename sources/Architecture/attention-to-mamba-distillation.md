---
id: src-attention-to-mamba-distillation
title: "Attention to Mamba: A Recipe for Cross-Architecture Distillation"
authors: ["Abhinav Moudgil", "Ningyuan Huang", "Eeshan Gunesh Dhekane", "Pau Rodríguez", "Luca Zappella", "Federico Danieli"]
year: 2026
url: "https://arxiv.org/abs/2604.14191"
type: paper
peer_review: preprint
venue: ""
tags: [distillation, Mamba, SSM, Transformer, cross-architecture, efficiency, linear-attention]
date_added: 2026-04-21
status: processed
---

# Attention to Mamba: A Recipe for Cross-Architecture Distillation

## 概要
事前学習済みTransformerをMamba-like SSMアーキテクチャへ蒸留する体系的レシピを提案。従来のTransformer→Mambaのナイーブ蒸留は性能劣化が大きくhybrid構成（AttentionとSSMの混在）に頼らざるを得なかった問題に対し、Mambaを**原理的に初期化**する二段階手順を設計：(1) kernel trickを応用してTransformerをlinearized Attention形態に蒸留、(2) linearized版をAttentionブロックを含まないadapted Mambaに蒸留。Pythia-1Bで蒸留後の純Mambaモデルが perplexity 14.11（teacher 13.86）を達成し downstream 性能を保持。

## メモ
cs.LG / cs.CL。Apple Research（Pau Rodríguez、Luca Zappella 等）と推定。arXiv 2604.14191（2026年4月投稿）。SSM/Mamba採用を促進するための実務レシピで、既存Transformer資産をMambaに変換する道筋を提供。1Bスケール・10Bトークンでの体系的ablation、モデルサイズとトークン量のスケーリング分析、二段階間のトークン配分感度分析を実施。
