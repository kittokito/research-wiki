---
title: "RLVRの能力境界論争：filteringか、真の能力獲得か"
aliases: ["RLVR capability boundary", "RLVR filtering debate"]
created: 2026-04-08
updated: 2026-04-21
tags: [RLVR, reasoning, capability-boundary, filtering, sharpening, exploration, pretraining-manifold, scaling-law]
sources: [src-rlvr-capability-boundary-debate, src-rlvr-does-not-teach-new-reasoning, src-deepseek-r1, src-mrpo, src-flash-rl-tis, src-scale-rl]
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

### 測定側のバイアス：off-policyミスマッチ問題

2025年後半に Yao, Liu et al. が指摘した **rollout–training mismatch** は、この論争のほぼ全ての実証研究の土台を揺らしうる。VeRL等の主流フレームワークは rollout生成（vLLM/SGLang）と勾配計算（FSDP/Megatron）に別実装を使っており、同一パラメータθでも `π_sampler` と `π_learner` のトークン確率は乖離する。結果、「on-policy RLVR」と呼ばれているものは暗黙のうちに off-policy RL 化し、entropy collapse・応答長暴走・負のKL推定といった ill-conditioned な学習動態を生む。

これは pass@k 低下（filtering 派の主要観察）の少なくとも一部がフレームワーク由来のアーティファクトである可能性を示唆する。著者らの提案する Truncated Importance Sampling (TIS) はこれらの病的挙動を解消し、ログ上の報酬と downstream 性能の乖離も減らす。VeRL・slime・OAT・SkyRL・OpenRLHF・REINFORCE++ に既に統合されており、**今後のRLVR能力境界の主張は、学習–生成ギャップを吸収した上での再測定**が求められる。

→ 詳細: [Flash-RL / TIS](../../papers/RL/flash-rl-tis.md)

### 漸近値 vs 効率の切り分け：ScaleRLの枠組み

2025年10月の **ScaleRL（Khatri et al., ICLR 2026 Oral）** は、40万GPU時間超の体系実験で、LLMのRL訓練がsigmoid型の計算-性能曲線に従うことを示した。核心的発見は次の2点：

1. **全てのRLレシピが同じ漸近性能（sigmoid上限）に収束するわけではない** — レシピ選択は asymptote を動かしうる
2. **loss aggregation / 正則化 / curriculum / off-policy アルゴリズムなどの細部は、漸近値をほぼ動かさず計算効率のみを調整する** — GRPO系の多くの細部最適化は「どれだけ速く漸近値に到達するか」を変えるだけで、最終的な能力上限は変えない可能性

この枠組みは能力境界論争に直接的な含意を持つ：
- Yue et al. の filtering 観察は「有限計算ではsigmoid漸近値に到達していない途中経過」の可能性がある
- ProRL の長期RL成功は「安定レシピなら漸近値に向けて予測可能に進む」という ScaleRL 結論の具体例に読める
- MRPO / DARS 系のように「漸近値そのものを引き上げる」ことが真の新戦略獲得、と切り分けられる

ScaleRL は pass@1 の validation loss 中心で、pass@k や分布外一般化の軸は別途検討が必要だが、**「漸近値を動かす設計」と「効率を動かす設計」を経験的に分離する道具立て** を提供した点が重要。今後の RLVR 論争は「どの介入が asymptote を上げ、どの介入が効率のみを上げるのか」という形で再定式化されうる。

→ 詳細: [ScaleRL](../../papers/RL/scale-rl.md)

### 最短の回答

> 人間データで学習した領域を"全く超えない"は言い過ぎ。でも、現在の主流RLVRが"人間データやbase modelの外へ大きく自由に飛んでいる"とも言いにくい。**標準レシピは主にsharpening、改良レシピや良い環境ではpartial expansionが起こる**、がいちばん妥当。

## 関連ページ
- [The Debate on RLVR Reasoning Capability Boundary](../../papers/RL/rlvr-capability-boundary-debate.md) — 二段階動態モデルの提唱
- [Does RLVR Truly Unlock New Reasoning?](../../papers/RL/rlvr-does-not-teach-new-reasoning.md) — Filtering主張の代表論文
- [DeepSeek-R1](../../papers/RL/deepseek-r1.md) — Pure RLでの推論能力獲得
- [MRPO](../../papers/RL/mrpo.md) — Manifold-Reshaping Policy Optimization、幾何学的にbias manifoldを突破
- [CodeScout](../../papers/RL/codescout.md) — コード検索エージェントのRL訓練、環境内方策学習の成功例
- [OpenClaw-RL](../../papers/RL/openclaw-rl.md) — エージェントRLフレームワーク
- [Flash-RL / TIS](../../papers/RL/flash-rl-tis.md) — rollout–training mismatchによる暗黙のoff-policy化、測定側のバイアス補正
- [ScaleRL](../../papers/RL/scale-rl.md) — sigmoid漸近値 vs 計算効率の切り分け、RL scaling の予測可能化

## 未解決の問い
- 標準RLVRがfilteringに留まりやすい部分と、本当に新戦略獲得になりやすい部分（特にコーディング領域）の境界は？
- Exploration stageの発現条件（rollout数、モデルサイズ、タスク難易度の閾値）は定量化できるか？
- MRPOのようなmanifold-awareな手法は、標準RLVRの限界を実質的にどこまで拡張するか？
- 環境内方策学習（code execution, web browsing等）はtext-only RLVRとqualitativeに異なる能力を引き出すか？
- 既存の pass@k 主張は TIS 等で学習–生成ギャップを吸収した上で再測定したとき、どの程度維持されるか？
- ScaleRL の「効率のみ調整する設計選択」リストは能力境界論争の細部論争（GSPO/GMPO/DAPO/RS-GRPO 等）をどの程度無効化するか？
