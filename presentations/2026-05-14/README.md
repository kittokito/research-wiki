# 勉強会発表資料 (2026-05-14)

## 発表テーマ一覧

| # | タイトル | カテゴリ | 出典 |
|---|---------|---------|------|
| 1 | [Scaling Behaviors of LLM RL Post-Training](01-scaling-behaviors-rl.md) | RL Scaling / Post-Training | ACL 2026 Main |
| 2 | [The Art of Scaling RL Compute (ScaleRL)](02-scalerl.md) | RL Scaling / Recipe | ICLR 2026 Oral |
| 3 | [MiniMax-M1 (CISPO)](03-minimax-m1.md) | Technical Report / RL Algorithm | MiniMax, 2025 |

## 概要

今回はRLポストトレーニングのスケーリングと、そこで採用される具体的アルゴリズムを軸に3本を取り上げる。

1. **Scaling Behaviors (Tan et al., ACL 2026)** -- Qwen2.5 0.5B–72B の全系列で RL post-training のスケーリング挙動を体系的に観測。test loss が

   $$\log L(N, X) \;=\; -k(N)\,\log X \;+\; E(N)$$

   という power-law に乗ること、ただし学習効率 $k(N)$ 自体が

   $$k(N) \;=\; \frac{K_{\max}}{1 + N_0/N}$$

   の形で**飽和する**ことを示した。「モデルを大きくすれば常に RL 効率も伸びる」という素朴な期待に、解析的な天井を与える論文。

2. **ScaleRL (Khatri et al., ICLR 2026 Oral)** -- 総計 **40万GPU時間以上**で RL の計算-性能曲線を **sigmoid** でフィッティングし、設計選択を「漸近性能を動かすもの」と「効率だけを動かすもの」に切り分けた。ベストプラクティス統合として 8 要素レシピ **ScaleRL** を提案し、損失タイプとして MiniMax-M1 由来の **CISPO** を採用している点が次の論文との橋渡しになる。

3. **MiniMax-M1 (MiniMax Team, 2025)** -- hybrid MoE + lightning attention の 456B/45.9B 推論モデル。本発表ではモデル自体の解説は短めにし、**CISPO (Clipped Importance Sampling Policy Optimization)** の議論をメインに据える。GRPO/DAPO 系のクリップが何を壊し、CISPO が importance sampling weight 側をクリップする設計でそれをどう避けるか、そしてなぜ ScaleRL に採用されたのかを掘る。

## 3本のつながり

- **横軸（スケーリング則の関数形）**: Tan の **power-law (k(N)-saturation)** と Khatri の **sigmoid** は同じ「RL の予測可能スケーリング」を語る論文だが、関数形が異なる。対立というより計算量レンジ・タスク依存の相補関係として読むのが妥当。
- **縦軸（漸近性能 vs 計算効率）**: ScaleRL が導入した切り分けは、Tan の k(N) 飽和とも整合する。漸近値は容量で決まり、効率はレシピで動く、という大枠。
- **CISPO クロスリンク**: ScaleRL §A.16 の比較表で ScaleRL 自身が CISPO を採用し、MiniMax のレシピを「PipelineRL でない点だけ違う」と整理している。3本目で CISPO の中身に降りる。

## 図表ディレクトリ

`figures/` に配置済みの図一覧（命名と内容の対応）:

```
figures/
  scaling-fig1.png    # Tan: power-law フィット（log L vs log X が線形に乗る）
  scaling-fig2.png    # Tan: 学習効率 k(N) の飽和曲線（base / instruct）
  scaling-fig3.png    # Tan: データ再利用の実験結果（τ=25 反復まで劣化なし）
  scaling-fig4.png    # Tan: データ再利用スキーマ（τ=1〜100 の概念図）
  scalerl-fig1.png    # Khatri §6: 50k→100k GPU時間外挿一致（predictable scaling 実証）
  scalerl-fig2.png    # Khatri §4: 8要素 leave-one-out ablation
  scalerl-fig3.png    # Khatri §5: ScaleRL vs prevalent recipes（MiniMax と A=0.610 で並ぶ）
  scalerl-fig4.png    # Khatri §3: off-policy 3手法比較（A=0.520 で同一、B のみ変化）
  minimax-fig1.png    # MiniMax §2: 主要ベンチマーク総合比較
  minimax-fig2.png    # MiniMax §4: CISPO vs GRPO/DAPO on AIME 2024（Qwen2.5-32B-base）
  minimax-fig3.png    # MiniMax §6: 生成長 vs FLOPs（lightning attention の効率優位）
```

注: MiniMax-M1 論文に「hybrid MoE + lightning attention のアーキテクチャ概要図」「thinking budget 40K/80K 直接比較図」は存在しないため、ベンチマーク比較図と FLOPs スケーリング図で代替。
