---
title: "CodeScout: RL for Code Search Agents"
aliases: ["CodeScout"]
created: 2026-04-08
updated: 2026-04-08
tags: [RL, code-search, localization, SWE-Bench, agent, GSPO, OpenHands]
peer_review: preprint
venue: ""
sources: [src-codescout]
---

# CodeScout: RL for Code Search Agents

> **査読**: 📝 preprint

## ソースからの事実
- Unix端末のみのミニマルscaffoldでRL訓練し、2-18倍大きいモデルを上回るコード検索性能 [source](../../../sources/RL/codescout.md)
- Qwen3-1.7BのFile F1が2.4%→55.46%に跳躍（RL + 蒸留） [source](../../../sources/RL/codescout.md)
- 14BモデルでSWE-Bench Verified File F1 68.57%、Function F1 40.32%（Claude Sonnet 4.5の43.62%に迫る） [source](../../../sources/RL/codescout.md)
- RL訓練中にツール使用がripgrep+sedに収束し、効率的検索戦略を自律発見 [source](../../../sources/RL/codescout.md)
- CodeScout予測で下流issue解決率が+3.8pt改善、トークン17.46%削減 [source](../../../sources/RL/codescout.md)

→ 詳細: [evidence](../../../evidence/RL/codescout.md)

## 現時点の解釈

### RLVR能力境界論争における位置づけ

CodeScoutはRLVR能力境界論争に対して、**コーディング領域での「能力獲得」の強い実証例**を提供する。

Base model（Qwen3-1.7B）のFile F1が2.4%という事実上ゼロの性能から55.46%へ跳躍しており、これは「既存の正解経路を濃くしている」（filtering/sharpening）では到底説明できない。Base modelの出力分布に有用なコード検索戦略がほぼ存在しない状態から、RL訓練で実用的な能力が形成されている。

ただし、以下の点で「純粋な能力創発」とは断定しにくい面もある：
- 1.7Bモデルは14Bからの蒸留（rejection sampling fine-tuning）を経ている。RFTなしのpure RLでの1.7Bの性能は不明
- 4B/14Bモデルはinstruct版がベースで、コーディング能力はすでにSFTで一定程度ある
- 環境フィードバック（端末出力）が実質的にverifierとして機能しており、text-only RLVRとは条件が異なる

### 「環境内方策学習」の好例

この論文は、先のトピックページで指摘した「テキストだけでなく環境内方策の学習に方向性が向いている」流れの具体例。エージェントがターミナルコマンドの結果を見て次のアクションを決める multi-step trajectory をRL で学習しており、MRPOのような数学推論とは本質的に異なる形の能力拡張。

### 実用的示唆
- **特殊ツール不要**: ripgrep + sed で十分という発見は、scaffold設計の簡素化を示唆
- **フロンティアモデルの脆弱性**: GPT-5/Claude Sonnet 4.5がリマインダーなしでほぼゼロ性能になるのは重要な知見
- **蒸留経路**: 14B→1.7Bの知識蒸留が効果的で、小型モデルへの能力移転が実用的

## 関連ページ
- [RLVRの能力境界論争](../../topics/RL/rlvr-capability-boundary.md) — コーディング領域でのRLVR能力獲得の実証例として
- [OpenClaw-RL](openclaw-rl.md) — エージェントRLフレームワーク
- [SWE-CI](../../papers/Evaluation/swe-ci.md) — 関連するコードベース評価ベンチマーク
- [AutoHarness](../../papers/Agent_ToolUse/autoharness.md) — エージェントのための自動ハーネス合成

## 未解決の問い
- 4B/14BのRFTなしpure RL性能はどの程度か？（filtering vs 能力獲得の切り分け）
- Python以外の言語リポジトリでも同等の性能改善が得られるか？
- ツール収束現象（多様→最小限）は他のエージェントタスクでも再現するか？
- CodeScoutの検索能力はコード修正エージェントとend-to-endで訓練した場合にさらに改善するか？
