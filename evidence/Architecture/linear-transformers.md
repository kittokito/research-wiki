---
source: src-linear-transformers
date_extracted: 2026-05-01
---

# Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention からの抽出

## 主要な主張
- 一般化された self-attention は類似度関数 sim(Q,K) を持ち、それが positive かつ kernel feature map で表現可能なら **sim(Q,K) = φ(Q)φ(K)ᵀ** と書ける。これにより `Attn(Q,K,V) = φ(Q)·(φ(K)ᵀV) / (φ(Q)·Σφ(K))` と再順序化でき、**O(N²d) の attention を O(Nd²) に削減** [source: §3](../../sources/Architecture/linear-transformers.md)
- 特性関数として `φ(x) = elu(x) + 1` を採用すれば、追加学習なし・正値性・微分可能性が保たれる。学習・推論ともに softmax attention と互換 [source: §3.4](../../sources/Architecture/linear-transformers.md)
- **causal masking がある自己回帰生成**では、各時刻 i で `S_i = Σ_{j≤i} φ(K_j) V_jᵀ` と `Z_i = Σ_{j≤i} φ(K_j)` を **再帰的に更新** すれば良く、各ステップ O(d²) で計算可能 → **Transformer = RNN with linearized attention** という数学的等価性 [source: §3.3](../../sources/Architecture/linear-transformers.md)
- 自己回帰推論で **シーケンス長に対し定数時間**（softmax attention は O(N²) の累積コスト）。長系列で **数千倍** の高速化を達成 [source: §4.3](../../sources/Architecture/linear-transformers.md)
- copy task / image generation / speech recognition の3領域で softmax attention に近い性能を維持しつつ、訓練速度・メモリ・推論速度すべてで優位 [source: §4](../../sources/Architecture/linear-transformers.md)

## 主要な貢献
- **Linear attention の基礎定式化**：softmax attention を kernel 内積に置き換える数学的枠組みと、行列積の結合性を活用した O(N) 計算スキーム
- **「Transformer は RNN である」という等価性**：causal mask 付き linear attention は隠れ状態が `S_i ∈ R^{d×d}` の RNN そのもの。autoregressive 推論が定数時間で終わる根拠
- **再帰的 backward pass**：causal linear attention の勾配計算を O(N) で行うアルゴリズムを提示（naive な実装だと O(N²) になる）
- **3タスクでの実証**：copy / image generation (MNIST, CIFAR-10) / speech recognition (Wall Street Journal) で性能と効率の両立を確認
- **オープンソース実装**：`fast-transformers` リポジトリで CUDA カーネル実装と各種 attention variant（full / clustered / improved-clustered / reformer / linear）を統一API で公開

## ベンチマーク結果

### 計算量・速度（Figure 1, Figure 2）
| 設定 | softmax | reformer (LSH) | linear (本論文) |
|---|---|---|---|
| 計算量 | O(N²d) | O(N log N · d) | **O(Nd²)** |
| 訓練速度（N=4096） | baseline | やや高速 | **大幅高速** |
| 訓練速度（N≥8192） | OOM | 動作 | 動作（最速） |
| メモリ（N=2¹⁶） | 不可 | 中程度 | **最小** |
| autoregressive 推論（N=2¹⁶） | 計測不可 | — | softmax 比 **~4000× 高速** |

### Image generation
- **MNIST autoregressive**: linear が softmax と同等の test bpd（収束はやや遅いが最終性能は同等）
- **CIFAR-10 autoregressive**: 60epochs で test bpd ~3.40、softmax 系と同等の品質

### Speech recognition (WSJ)
- linear attention で word error rate が softmax baseline と同水準を維持しつつ訓練速度向上

## 制限・注意点
- **kernel feature map の選択が性能に大きく影響**：`elu(x) + 1` は単純だが厳密な softmax 近似ではなく、長距離依存タスクで softmax より劣化するケースがある（後続の Performer の random feature, RWKV の time-decay, Mamba の selective SSM 等で改善）
- **causal mask 専用の RNN 化**：encoder-only / bidirectional 設定では RNN 等価性が成立せず、O(N²) 表現と再順序化版を切り替える必要
- **memory state S_i ∈ R^{d×d} の容量限界**：固定サイズの "summary" に過去全てを押し込むため、本質的に有限容量メモリ。長距離精密 retrieval は softmax attention より弱い
- **数値安定性**：分母 `φ(Q)·Σφ(K)` がゼロ近傍になると不安定化。実装時は ε を加える等の工夫が必要
- **2020年時点では LM 系での大規模実証は未実施**：論文の実験は <100M パラメータ規模、後続の Performer / RWKV / RetNet / Mamba / Lightning Attention 等で初めて LLM 規模での競争力が示された
- 高品質な softmax 代替を求めるなら、後続の **gated / data-dependent decay**（Mamba selective scan, RetNet retention, RWKV time-mix）を含めた評価が必要

## 実装関連
- 公式実装: https://github.com/idiap/fast-transformers（PyTorch, CUDA カーネル付き）
- 主要派生・後続:
  - **Performer** (Choromanski et al., 2020/2021) — random feature map (FAVOR+) で softmax を厳密近似
  - **Linformer** (Wang et al., 2020) — KV を低次元射影、本論文と独立に O(N) を達成
  - **RWKV** (Peng et al., 2023) — time-decay を加えた linear attention の RNN 系拡張
  - **RetNet** (Sun et al., 2023) — retention mechanism、parallel/recurrent/chunkwise の3形態を提供
  - **Mamba / Mamba-2** (Gu & Dao, 2023/2024) — selective SSM、本論文の RNN 視点をさらに進化
  - **Lightning Attention** (MiniMax-M1) / **Kimi Linear**（Attention Residuals）— LLM 規模での実用化
  - **Attention to Mamba Distillation** — kernel trick 適用 linearized Attention を経由する Transformer→Mamba 蒸留
- 計算詳細: 各時刻 i で `S_i = S_{i-1} + φ(K_i) V_iᵀ`, `Z_i = Z_{i-1} + φ(K_i)` を更新、出力は `(φ(Q_i)·S_i) / (φ(Q_i)·Z_i)`
- 正規化なしの「unnormalized linear attention」(分母を省く)も後の論文で広く使われる variant
