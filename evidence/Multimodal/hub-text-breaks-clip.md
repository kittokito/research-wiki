---
source: src-hub-text-breaks-clip
date_extracted: 2026-06-24
---

# One Single Hub Text Breaks CLIP からの抽出

## 主要な主張
- **hubness問題**（hub 埋め込みが無関係な多数の例と高類似度になる現象, Radovanović et al. 2010）は cross-modal encoder にも生じ、テキストと画像の類似度を文字列照合等で直接計算できない cross-modal タスク（情報検索・自動評価指標）では埋め込みへの依存が必須なため、hub の存在が信頼性を毀損する実用的脅威となる [source: §1](../../sources/Multimodal/hub-text-breaks-clip.md)
- 単一モダリティの hub はサニティチェックで部分的に緩和できるが、cross-modal 類似度は直接比較できないため緩和が難しい [source: §1](../../sources/Multimodal/hub-text-breaks-clip.md)
- 提案手法は「多数の無関係な画像と不当に高い類似度を持つ単一テキスト＝**hub text**」を特定する。発見された hub text は意味的に無意味（gibberish）だが、多くの画像に対し **人手の参照キャプションと同等以上の CLIPScore** を得る [source: §3, §4.2](../../sources/Multimodal/hub-text-breaks-clip.md)
- hub text の挿入は image-to-text retrieval の精度を有意に劣化させ、CLIPScore 評価指標と cross-modal retriever の双方に実用的脅威を及ぼす [source: §4.3](../../sources/Multimodal/hub-text-breaks-clip.md)

## 主要な貢献（提案手法：3段階）
1. **Hub acquisition（hub 埋め込みの解析的導出）**: 目的関数 J(v) = (1/|D_I|) Σ_I s(v, v_I) を最大化する最適 hub 埋め込み v\* を求める。CLIPScore のスコア関数 s は cosine 類似度ベースのため、Cauchy–Schwarz 不等式の等号条件から **閉形式解 v\* = (1/|D_I|) Σ_I v_I/‖v_I‖（正規化済み画像埋め込みの平均）** が得られる。先行研究（COMET 攻撃）は非線形 FFN のため gradient descent を要したのに対し、本手法は解析解 [source: §3](../../sources/Multimodal/hub-text-breaks-clip.md)
2. **Hub decoding（埋め込み→テキスト復元）**: 逆変換モデル φ（Morris et al. 2023, 埋め込みから入力テキストを再構成）を学習し、hub 埋め込みから複数の hub text 候補を生成。mT5-base ベースで凍結テキスト埋め込みを用い MSCOCO 学習キャプションで学習、epsilon sampling（ε=0.02）で **4,096 候補**を生成し目的関数 J で最良を選択 [source: §3, §4.1](../../sources/Multimodal/hub-text-breaks-clip.md)
3. **Beam local search（精錬, Algorithm 1）**: decode したテキストの各トークンを **ランダム順**（左→右でなく）に置換し、tuning set 上の平均 CLIPScore を最大化するトークンへ反復更新。先行研究の greedy local search (GLS) を **beam 探索（k 候補保持, k∈{5,10,20}）へ拡張**。山登り法のためスコアは単調増加。入力と埋め込みのみで動く **black-box** なので様々なモデルに適用可 [source: §3, §5.2](../../sources/Multimodal/hub-text-breaks-clip.md)

## 評価設定
- **評価モデル**: CLIP (OpenAI; ViT-B/32, ViT-L/14, ViT-L/14-336), LAION-CLIP (ViT-L/H/g), DFN-CLIP (apple/DFN2B, DFN5B; Fang et al. 2024), AltCLIP (BAAI; Chen et al. 2023) の計10モデル。指定なき解析は `openai/clip-vit-base-patch32` [source: §4.1](../../sources/Multimodal/hub-text-breaks-clip.md)
- **タスク**: (1) 画像キャプション評価＝CLIPScore（MSCOCO in-domain / nocaps out-of-domain）, (2) image-to-text retrieval（MSCOCO / Flickr30k, MTEB 利用）[source: §4](../../sources/Multimodal/hub-text-breaks-clip.md)
- **比較対象**: BLIP-2-FlanT5-XL のキャプション, 人手参照キャプション (Human), 先行手法 GLS（sequential greedy local search, Deguchi et al. 2026）, 本手法 (Ours) [source: §4.2](../../sources/Multimodal/hub-text-breaks-clip.md)
- CLIPScore は s = M·max(cos, 0)（M=2.5）でスコアは [0, 2.5] レンジ（1.0 超も発生しうる）[source: §2 Eq.1](../../sources/Multimodal/hub-text-breaks-clip.md)

## ベンチマーク結果
| 項目 | 値 | 備考 |
|---|---|---|
| CLIPScore (clip-vit-base-patch32, MSCOCO) | Human 0.759 / GLS 0.732 / **Ours 0.842** | 単一 hub text を test set サイズ分繰り返して corpus-level 算出。Ours は BLIP-2(0.739)・Human も上回る (Table 1) |
| CLIPScore (clip-vit-base-patch32, nocaps) | Human 0.758 / GLS 0.700 / **Ours 0.814** | out-of-domain でも Ours が最高 (Table 1) |
| CLIPScore (DFN5B-CLIP-ViT-H-14-378, MSCOCO) | Human 0.837 / GLS 0.995 / **Ours 1.023** | 人間評価との相関が高い強モデルでも hub text が参照超え (Table 1) |
| hub text 例の instance スコア (MSCOCO) | Human 0.793/0.780/0.806 → **Hub 1.012/0.981/1.034** | gibberish な単一 hub text が3枚とも人手キャプション超え (Table 2) |
| 勝率 Hub > Human (clip-vit-base-patch32) | MSCOCO GLS 39.1% / **Ours 78.6%**、nocaps GLS 27.5% / **Ours 71.1%** | instance-level win rate (Table 6) |
| 勝率 Hub > Human (DFN5B-CLIP-ViT-H-14-378) | MSCOCO GLS 87.3% / **Ours 90.0%** | 90%の事例で参照キャプション超え (Table 6) |
| 勝率 Hub > Human (BAAI/AltCLIP) | MSCOCO GLS 12.9% → **Ours 52.1%** | GLS が弱いモデルでも本手法は過半数到達 (Table 6) |
| instance-level スコア平均 (MSCOCO) | BLIP-2 0.74 / Human 0.76 / GLS 0.73 / **Ours 0.84** (max 1.05) | Figure 2 |
| I2T retrieval 汚染 (#CT=1, 単一挿入) | top-1 指標が全モデルで有意劣化、**Precision@1 が最大 29.3% 低下** | #CT=number of contaminations。relevant text が index 内にあっても top-1 が hub text に奪われる (Table 4) |
| I2T retrieval 汚染 (#CT=1,000) | **Recall@1k が最大 75.5% 低下** | SEO/spam 的な大量複製シナリオ (Table 4) |
| ランダムキャプション挿入 | 性能劣化なし | hub text 挿入のみが劣化を起こす＝hub text 固有の脅威 (Table 5) |

## 主要な分析・知見
- hub text は "color"・"photo"・"photographer" 等、CLIP の学習データに頻出しそうな語を含む → **hub text は学習データ分布に起因して生じる**可能性 [source: §4.2, §5.1](../../sources/Multimodal/hub-text-breaks-clip.md)
- PCA 可視化（Figure 4）: hub text はテキストクラスタを離れ画像クラスタの中心へ移動 → テキストでありながら画像のように振る舞う。**hubness が modality gap（Liang et al. 2022; An et al. 2025b）と関連**する可能性を示唆 [source: §5.2](../../sources/Multimodal/hub-text-breaks-clip.md)
- beam local search のスコアは反復で単調増加（Figure 3, 山登り法）。beam size は k=20 まで向上し k≥50 で低下＋計算時間が線形増加（Figure 5）→ k∈{5,10,20} で調整 [source: §5.2, §5.3](../../sources/Multimodal/hub-text-breaks-clip.md)
- 人間評価と高相関のモデル（DFN5B-CLIP-ViT-H-14-378）でも 90% の事例で hub text が参照キャプションを上回る → **ベンチスコアだけでなく攻撃への頑健性も評価すべき** [source: §5.1, §6](../../sources/Multimodal/hub-text-breaks-clip.md)

## 制限・注意点
- **時間計算量が高い**: hub text 同定は NP-hard。beam local search は O(kT|V||D_I|)。clip-vit-base-patch32 で 382 回のトークン置換（系列長23）に **8×NVIDIA RTX 6000Ada で 12,486 秒**。大きいモデルや beam を増やすと極めて高コスト [source: §5.4, Limitations](../../sources/Multimodal/hub-text-breaks-clip.md)
- **固定長探索**: 探索は固定長トークン系列に限定（挿入・削除なし）。可変長探索は探索空間が指数的に増大し現実的時間で困難 [source: Limitations](../../sources/Multimodal/hub-text-breaks-clip.md)
- **検出可能性**: 同定された hub text は非自然なため、別の encoder や言語モデル（PPL フィルタ等）で検出しうる。著者はこれを **防御の必要性の論拠**とするが、過剰フィルタは「関連する事例の検索」という本来目的を損なう（高 PPL の専門用語・新語が除外される）ためトレードオフ [source: Limitations](../../sources/Multimodal/hub-text-breaks-clip.md)
- **倫理（coordinated disclosure）**: hubness は既知の弱点（Radovanović 2010）の本質解明であり新規脆弱性開示ではない、と整理。本研究は個人情報抽出や有害コンテンツ生成を含まない [source: Ethical Considerations](../../sources/Multimodal/hub-text-breaks-clip.md)

## 実装関連
- 逆変換モデルは google/mt5-base、凍結テキスト埋め込み、MSCOCO 学習キャプションで AdamW（β1=0.9, β2=0.999, ε=1e-8）lr 3e-4・warmup 4,000・20 epoch・batch 128 で学習 [source: §4.1](../../sources/Multimodal/hub-text-breaks-clip.md)
- hub decoding の 4,096 候補生成は単一 GPU で1分未満（mT5-base で 4,096 文生成と同等コスト）[source: §4.1](../../sources/Multimodal/hub-text-breaks-clip.md)
- 多 GPU 並列化のため beam local search を boss–worker パターンで実装（各 worker が語彙の部分集合の候補スコアを計算し top-k のみ返す）[source: §5.4](../../sources/Multimodal/hub-text-breaks-clip.md)
- Appendix C で cosine 類似度以外（内積・二乗ユークリッド距離）についても最適 hub 埋め込みの解析解を導出 [source: §3](../../sources/Multimodal/hub-text-breaks-clip.md)
