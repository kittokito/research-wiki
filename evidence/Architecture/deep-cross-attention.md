---
source: src-deep-cross-attention
date_extracted: 2026-04-07
---

# DeepCrossAttention からの抽出

## 主要な主張
- 標準的な残差接続（`x_{t+1} = f(x_t) + x_t`）は全層出力を均等に加算するため、深い層で重要な情報が希薄化する [source: §1](../../sources/Architecture/deep-cross-attention.md)
- 低ランク層からの入力復元実験で、標準ResNetは10^5サンプルでも失敗するが、学習可能重みモデルは100倍少ないサンプルで成功 [source: §1, Figure 1](../../sources/Architecture/deep-cross-attention.md)
- DCAは残差ブロックを「純粋に逐次的」から「完全に並列」、およびその中間の任意の組み合わせに再配置することを学習可能 [source](../../sources/Architecture/deep-cross-attention.md)

## 主要な貢献
- **GRN (Gated Residual Network) の3バリアント**:
  - GRN-v1: 次元非依存の単一重みベクトル `b_t ∈ ℝ^t`
  - GRN-v2: 次元依存の重み行列 `b_t ∈ ℝ^{d×t}`
  - GRN-v3: 固定重み＋入力依存成分 `w̄_t = 1σ(w_t^T G_t)` [source: §3](../../sources/Architecture/deep-cross-attention.md)
- **DCA**: GRN-v3を3インスタンス（Q, K, V）使用し、深さ方向のクロスアテンションを実現 [source: §3](../../sources/Architecture/deep-cross-attention.md)
- **メモリ効率化**: 深いモデルでは最初とlast-k層の出力のみスタック `G_t` に保持し、中間層は標準ResNet加算を使用 [source](../../sources/Architecture/deep-cross-attention.md)
- **理論的保証**: Theorem 4.3で集合的ランク `r*/d` が臨界値以下のとき、GRNがテスト誤差-モデル複雑度のトレードオフを改善することを証明 [source: §4](../../sources/Architecture/deep-cross-attention.md)

## 制限・注意点
- 幅が大きいモデルほど改善幅が減少（幅64で-2.82 → 幅1024で-0.39 perplexity） [source](../../sources/Architecture/deep-cross-attention.md)
- 集合的ランクが次元を超える場合（`r* > d`）は改善が制限される [source: §4](../../sources/Architecture/deep-cross-attention.md)
- 処理速度のオーバーヘッド: ベースライン8.14 batch/s → 1-DCA 5.62 batch/s [source](../../sources/Architecture/deep-cross-attention.md)
- 評価は主に言語モデリングタスク中心。ImageNetでのViT評価は+0.7%のみ [source](../../sources/Architecture/deep-cross-attention.md)

## ベンチマーク結果

### LM1B (6層モデル, 比較実験)
| 手法 | Perplexity | 備考 |
|---|---|---|
| Transformer (baseline) | 18.98 ± 0.02 | — |
| LAuReL-PA | 18.99 | Menghani et al. 2024 |
| DenseFormer | 18.80 | Pagliardini et al. 2024 |
| Hyper-Connections | 18.65 | Zhu et al. 2024 |
| **DCA** | **18.06 ± 0.01** | 最良ベースラインより-0.59 |

### GRN Ablation (6層 LM1B)
| バリアント | Perplexity |
|---|---|
| GRN-v1 | 18.80 ± 0.11 |
| GRN-v2 | 18.43 ± 0.04 |
| GRN-v3 | 18.41 ± 0.10 |
| DCA | 18.06 ± 0.01 |

### C4 (スケーリング実験)
| パラメータ数 | Transformer | DCA | 改善幅 |
|---|---|---|---|
| 75M | 27.876 | 26.443 | -1.443 |
| 449M | 17.166 | 16.764 | -0.402 |

### その他
- 30層DCA > 42層Transformer（perplexity）
- 2-DCAはTransformerの1/3の学習時間で同品質達成
- 24層モデル k=2で推論レイテンシ48%削減
- ImageNet ViT-S/16: 76.4% → 77.1% (+0.7%)

## 実装関連
- 学習: 500kステップ、131Bトークン、埋め込み次元512（デフォルト）
- DCAのパラメータオーバーヘッドはほぼ無視可能
- 学習安定性: 標準Transformerと比較して有意なloss spikeなし
