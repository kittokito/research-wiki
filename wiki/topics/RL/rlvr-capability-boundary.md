---
title: "RLVRの能力境界論争：filteringか、真の能力獲得か"
aliases: ["RLVR capability boundary", "RLVR filtering debate"]
created: 2026-04-08
updated: 2026-04-08
tags: [RLVR, reasoning, capability-boundary, filtering, sharpening, exploration, pretraining-manifold]
sources: [src-rlvr-capability-boundary-debate, src-rlvr-does-not-teach-new-reasoning, src-deepseek-r1, src-mrpo]
---

# RLVRの能力境界論争：filteringか、真の能力獲得か

## 問いの構造

「RLVRは本当に新しい推論能力を作っているのか、それとも既存能力の探索を上手くしているだけか？」

この問いは2つの水準に分かれる：

1. **人間の教師データに直接書かれていない解法・軌跡を出せるか？** → 超えうる（DeepSeek-R1等の証拠あり）
2. **Base modelが全く持っていない解空間に踏み出せるか？** → 懐疑派が優勢

## ソースからの事実

### Filtering/Sharpening派（「絞り込みが主体」）
- RLVRはpass@1を上げるが、pass@k（大きいk）ではbase modelが上回ることがある [source](../../../sources/RL/rlvr-does-not-teach-new-reasoning.md)
- RLVRモデルのreasoning pathはbase modelの出力分布にすでに含まれている [source](../../../sources/RL/rlvr-does-not-teach-new-reasoning.md)
- On-policy RLVRはbase modelがほぼ確率を置いていない解には勾配が届かず、解のカバレッジはむしろ狭まることがある（Invisible Leash系）
- 期待logit updateは現在の方策確率に依存し、tail行動は有限サンプルで事実上無視される [source](../../../sources/RL/rlvr-capability-boundary-debate.md)

### Expansion派（「新しい能力も獲得できる」）
- DeepSeek-R1-Zeroで人間CoTにないself-verification・reflectionが自然出現 [source](../../../sources/RL/deepseek-r1.md)
- Reasoning Gymで、base modelが事前に解けなかったタスクでもRLVRによる改善が確認、同一ドメイン内の未見タスクや別ドメインへの転移も報告
- DARS系はrollout配分を改善すればpass@Kとpass@1の両方が向上すると報告

### 統合的見解
- Shrinkage/expansion は二択ではなく二段階動態（exploitation stage → exploration stage） [source](../../../sources/RL/rlvr-capability-boundary-debate.md)
- 既存研究の多くは数百ステップで学習を止めており、exploration stage未到達の可能性 [source: §4](../../../sources/RL/rlvr-capability-boundary-debate.md)
- 今のRLVRが「絞り込みに見える」のは能力の本質ではなく、現行レシピの探索の弱さが大きい（DARS系の立場）

## 現時点の解釈

### 界隈の中間的着地（2025後半〜2026）

**標準的なRLVRは、かなりの部分でfiltering / reweighting / sharpeningで説明できる。ただし、それだけでは説明しにくい新しい軌跡の出現や転移も一部で観測されている。**

争点は「超えるか超えないか」の二択ではなく、**どの条件なら超えやすいか**に移っている。鍵とされる要素：
- 探索量の増大（rollout数、off-policy成分）
- 難問への重点配分
- 合成環境・verifiable環境の質
- 長期軌跡の学習
- より良いverifier

### Pretraining manifoldへの閉じ込め

「事前学習多様体に閉じ込められている」という見方について：

- **初期段階では事実上閉じ込められやすい**: Softmax上では全トークンに正の確率があるが、極小確率の候補は有限サンプルではほぼ出現せず、勾配も届かない
- **永続的上限とは限らない**: 既存の高確率・高報酬トークンの伸びが飽和すると、たまたまサンプルされた低確率の有望トークンに確率質量が移り始める（exploration stage）
- **ただし自動的には起きない**: prolonged trainingが必要で、entropy collapseやover-sharpeningを避ける工夫が求められる
- **「外への脱出」か「tail増幅」かは未決**: 低確率tailを育てることが新しい領域の創発なのか、もともと極薄で存在していたものの再発見なのかは、現在の研究では切り分けられていない

### コーディング領域への示唆

「base modelの長い尾の正解経路を濃くする段階」から「repo環境の中で本当に新しい戦略を獲得する段階」へ行けるかが本丸。OpenAIのdeep researchがend-to-end RLでbrowsingのmulti-step trajectoryを学んだと説明しており、テキストだけでなく環境内方策の学習に方向性が向いている。これは純粋なfilteringから一歩進む可能性を示す。

**CodeScout（Sutawika et al., 2026）** はこの方向の具体的成功例。Unix端末のみのミニマルscaffoldでRL訓練したコード検索エージェントで、Qwen3-1.7BのFile F1が2.4%→55.46%に跳躍。Base modelが事実上ゼロ性能の状態から実用的な検索能力が形成されており、filtering/sharpeningでは説明しにくい能力獲得の強い証拠。さらに訓練中にツール使用がripgrep+sedに自律的に収束する現象が観察され、効率的戦略の発見を示唆している。

→ 詳細: [CodeScout](../../papers/RL/codescout.md)

### MRPOなど次世代手法

2026年のMRPO（Wang et al.）は、標準RLVRがpretrain manifoldに閉じ込められるという前提を受け入れた上で、幾何学的に突破する手法を提案している。Spectral Orthogonal Exploration (SOE)でbias manifoldのnull space方向に軌跡を誘導し、effective rank正則化で次元崩壊を防ぐ二段階構成で、4Bモデルが32Bモデルを数学推論で上回る結果を報告。ただし数学ドメイン限定、追試待ちであり、ablationではSOE単体の寄与（+1.6pt）よりデータ品質の寄与が大きい可能性もある。

→ 詳細: [MRPO](../../papers/RL/mrpo.md)

研究コミュニティは「標準RLVRは絞り込み寄り」→「なら探索と幾何構造を変えてboundaryを本当に押し広げよう」という次の段階に入っている。

### 最短の回答

> 人間データで学習した領域を"全く超えない"は言い過ぎ。でも、現在の主流RLVRが"人間データやbase modelの外へ大きく自由に飛んでいる"とも言いにくい。**標準レシピは主にsharpening、改良レシピや良い環境ではpartial expansionが起こる**、がいちばん妥当。

## 関連ページ
- [The Debate on RLVR Reasoning Capability Boundary](../../papers/RL/rlvr-capability-boundary-debate.md) — 二段階動態モデルの提唱
- [Does RLVR Truly Unlock New Reasoning?](../../papers/RL/rlvr-does-not-teach-new-reasoning.md) — Filtering主張の代表論文
- [DeepSeek-R1](../../papers/RL/deepseek-r1.md) — Pure RLでの推論能力獲得
- [MRPO](../../papers/RL/mrpo.md) — Manifold-Reshaping Policy Optimization、幾何学的にbias manifoldを突破
- [CodeScout](../../papers/RL/codescout.md) — コード検索エージェントのRL訓練、環境内方策学習の成功例
- [OpenClaw-RL](../../papers/RL/openclaw-rl.md) — エージェントRLフレームワーク

## 未解決の問い
- 標準RLVRがfilteringに留まりやすい部分と、本当に新戦略獲得になりやすい部分（特にコーディング領域）の境界は？
- Exploration stageの発現条件（rollout数、モデルサイズ、タスク難易度の閾値）は定量化できるか？
- MRPOのようなmanifold-awareな手法は、標準RLVRの限界を実質的にどこまで拡張するか？
- 環境内方策学習（code execution, web browsing等）はtext-only RLVRとqualitativeに異なる能力を引き出すか？
