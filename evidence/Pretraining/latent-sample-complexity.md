---
source: src-latent-sample-complexity
date_extracted: 2026-06-03
---

# Learn from your own latents and not from tokens からの抽出

## 主要な主張
- **中心的結果（指数 vs 定数）**: 隠れ木（深さ L）の復元に、教師あり/トークンレベル SSL は **L について指数的なサンプル**を要するが、latent prediction は **L について定数のサンプル（対数因子まで）** で達成できる [source](../../sources/Pretraining/latent-sample-complexity.md)
  - 原文: "supervised or token-level SSL require a number of samples exponential in L to recover the latent tree; we prove that latent prediction achieves this with a number of samples constant in L, up to logarithmic factors."
- **生成モデルが大量データを要する問題への代替パラダイム**: 「ネットワークを自己の潜在表現の予測に向けて訓練する」ことが、生物学的学習者との data efficiency ギャップを埋めうる [source](../../sources/Pretraining/latent-sample-complexity.md)

## 解析設定
- **probabilistic context-free grammar (PCFG)**: 自然言語と画像の合成構造を捉える tractable な確率モデル。深さ L の隠れシンボル木に沿って production rule を再帰適用し、可視トークン列を生成 [source](../../sources/Pretraining/latent-sample-complexity.md)
- この設定は Favero・Wyart 系の **Random Hierarchy Model (RHM)** に連なる合成的階層データの理論枠組み [source](../../sources/Pretraining/latent-sample-complexity.md)

## 主要な貢献（3つの実装で検証）
- (i) **階層的クラスタリングアルゴリズム** — 隠れ木構造を段階的に復元 [source](../../sources/Pretraining/latent-sample-complexity.md)
- (ii) **end-to-end ニューラルネット** — predictor-clusterer モジュールが各レベルで勾配降下により**自己の latent を予測** [source](../../sources/Pretraining/latent-sample-complexity.md)
- (iii) **data2vec の初のサンプル複雑度解析** — data2vec が**暗黙的に階層的 latent 予測を実行している**ことを理論的に示す [source](../../sources/Pretraining/latent-sample-complexity.md)

## H-JEPA 冗長性の示唆
- latent 予測パラダイムは勾配降下によって**自然に階層構造を獲得する**ため、H-JEPA のような明示的な多段階スタックは **largely redundant（ほぼ冗長）** だと示唆 [source](../../sources/Pretraining/latent-sample-complexity.md)
  - 原文: "This suggests that explicit stacking such as H-JEPA is largely redundant."

## 制限・注意点
- 解析は PCFG という簡略化された合成構造モデルに限定。実データ（自然言語・画像）への直接の転移可能性は未検証 [source](../../sources/Pretraining/latent-sample-complexity.md)
- 「定数」は対数因子を除いた上界であり、実務的なサンプル数への定量的含意は別途要評価 [source](../../sources/Pretraining/latent-sample-complexity.md)
- 表現可能性・サンプル複雑度の理論であり、最適化の収束や実装上の collapse 回避は扱わない [source](../../sources/Pretraining/latent-sample-complexity.md)
