---
id: src-hub-text-breaks-clip
title: "One Single Hub Text Breaks CLIP: Identifying Vulnerabilities in Cross-Modal Encoders via Hubness"
authors: ["Hiroyuki Deguchi", "Katsuki Chousa", "Yusuke Sakai"]
year: 2026
url: "https://arxiv.org/abs/2604.27674"
type: paper
peer_review: accepted
venue: "ACL 2026 (Main)"
tags: [CLIP, cross-modal-encoder, hubness, CLIPScore, image-text-retrieval, embedding-vulnerability, modality-gap, adversarial, multimodal]
date_added: 2026-06-24
status: processed
---

# One Single Hub Text Breaks CLIP: Identifying Vulnerabilities in Cross-Modal Encoders via Hubness

## 概要
高次元埋め込み空間で生じる **hubness問題**（特定の埋め込み＝hub が無関係な多数の例と高類似度になる現象）を、CLIP 系の **cross-modal encoder**（テキストと画像を共有空間に射影するモデル）に対する実用的脅威として明らかにした論文。著者らは「多数の無関係な画像と不当に高い類似度を持つ単一テキスト＝hub text」を特定する3段階手法（hub embedding の解析的導出 → 逆変換モデルによる decode → beam local search による精錬）を提案。MSCOCO・nocaps の画像キャプション評価（CLIPScore）と MSCOCO・Flickr30k の image-to-text retrieval で、**たった1つの（意味的に無意味な）hub text が多くの画像に対して人手の参照キャプションと同等以上の類似度スコアを得る**ことを実証し、CLIPScore 評価指標と cross-modal retriever の脆弱性を露呈した。

## メモ
NTT, Inc.（Deguchi, Chousa）× 奈良先端科学技術大学院大学 NAIST（Sakai）。arXiv 2604.27674（v1: 2026-04-30）。**ACL 2026 Main 採択**（arXiv Comments: "Accepted at ACL2026 (main)"）。cs.CL（主）/ cs.AI / cs.CR / cs.IR。ライセンス CC BY-NC-SA 4.0。

先行研究 Deguchi et al. (2026)「Hacking neural evaluation metrics with single hub text」（EACL 2026 Short）が機械翻訳の評価指標 COMET に対し同種の3段階攻撃を提示しており、本論文はそれを **cross-modal（CLIP/CLIPScore）へ拡張**したもの。COMET は非線形 FFN のスコア関数のため hub embedding を gradient descent で求める必要があったが、CLIPScore は cosine 類似度ベースのため **hub embedding を閉形式（正規化画像埋め込みの平均）で解析的に導出**できる点が新しい。本リポジトリの [CLIP](clip.md) の脆弱性面（typographic attack に並ぶ embedding 脆弱性）として位置付け。
