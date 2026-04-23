---
source: src-video-models-zero-shot
date_extracted: 2026-04-21
---

# Video models are zero-shot learners and reasoners からの抽出

## 主要な主張
- LLMが大規模・生成的・web-scaleという共通プリミティブから汎用言語基盤モデルに進化したのと同じプリミティブが現代の生成video modelにも当てはまる [source](../../sources/Multimodal/video-models-zero-shot-learners.md)
- Veo 3 は明示的に訓練されていない多種多様なタスクをゼロショットで解ける [source](../../sources/Multimodal/video-models-zero-shot-learners.md)
- 具体的な創発タスク：オブジェクトセグメンテーション、エッジ検出、画像編集、物理特性の理解、アフォーダンス認識、道具使用シミュレーション [source](../../sources/Multimodal/video-models-zero-shot-learners.md)
- これらの知覚・モデリング・操作能力により、迷路解き・対称性解きなど **初期的な visual reasoning** が可能になる [source](../../sources/Multimodal/video-models-zero-shot-learners.md)
- Veo の emergent zero-shot 能力は、video model が unified な汎用視覚基盤モデルへ向かう経路上にあることを示唆 [source](../../sources/Multimodal/video-models-zero-shot-learners.md)

## 主要な貢献
- video modelのゼロショット汎化能力の体系的実証（タスク多様性で）
- 「大規模生成モデル = 汎用基盤モデル」仮説の視覚領域への拡張
- Veo 3 の定性的評価プロトコル（プロジェクトページに動画事例公開）

## ベンチマーク結果
定量的スコアより定性事例の広がりが主。公開プロジェクトページ（https://video-zero-shot.github.io/ ）に具体例。

## 制限・注意点
- 定性評価中心で、各タスクでの定量的SOTA比較は限定的
- Veo 3 はクローズドモデルで、再現性・学術検証が困難
- 「zero-shot reasoning」の深度は迷路・対称性等の比較的単純なタスク止まり、複雑な多段推論はカバー外
- ICLR 2026 に投稿され **Rejected**（OpenReview MCWypEBtlF, venue id: ICLR.cc/2026/Conference/Rejected_Submission）。査読側の具体的な反論内容は参照すべき
- 生成モデルの「できる」例示は cherry-picking バイアスを受けやすく、failure rate の報告が薄い

## 実装関連
- Veo 3 自体はGoogle社内モデル、一般には API 経由
- 各タスクに対するプロンプト設計（テキスト条件 + 初期フレーム等）が実用の肝
- プロジェクトページに具体的プロンプト・入出力動画が公開されており、類似挙動を自前の video model で検証可能
