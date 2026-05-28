---
source: src-clip
date_extracted: 2026-04-30
---

# Learning Transferable Visual Models From Natural Language Supervision (CLIP) からの抽出

## 主要な主張
- 自然言語の **キャプションが画像の supervision として直接使える**：「どの画像がどのキャプションとペアになるか」を予測する単純な事前学習タスクが、SOTA の視覚表現を効率的かつスケーラブルに学習させる [source](../../sources/Multimodal/clip.md)
- 4億の (image, text) ペアを web から収集（**WIT: WebImageText**）し、contrastive目的関数で訓練。学習後は自然言語でクラス概念を参照することで、下流タスクへ **重み更新なしのゼロショット転移** が可能 [source](../../sources/Multimodal/clip.md)
- ゼロショット転移を 30+ の既存視覚データセット（OCR、ビデオ動作認識、地理位置推定、細粒度物体分類等）でベンチマーク。**多くのタスクで非自明な性能** を発揮し、しばしばfully supervisedベースラインに並ぶ [source](../../sources/Multimodal/clip.md)
- ImageNet ゼロショットで **ResNet-50 を fully supervised 学習したのと同等の精度**（オリジナル ResNet-50 が訓練に1.28M画像を使ったのに対し、CLIPは1枚の ImageNet 画像も見ていない） [source](../../sources/Multimodal/clip.md)
- distribution shift に対して fully supervised モデルより **頑健**：ImageNet variants（ImageNet-V2, -R, -A, -Sketch, ObjectNet）で robustness gap が大きく縮小 [source](../../sources/Multimodal/clip.md)

## 主要な貢献
- **データ規模での突破**：4億 (image, text) ペアという当時前例のないスケールで vision-language pretraining を実施
- **contrastive目的関数の確立**：当初 captioning 目的（生成）を試みたが計算効率が悪く、N×N類似度行列の対角を最大化する **InfoNCE 系 contrastive loss** に切り替えた瞬間に4倍の zero-shot 効率を獲得
- **アーキテクチャ族**：image encoderに ResNet-50/101/50x4/50x16/50x64 と ViT-B/32, ViT-B/16, ViT-L/14, ViT-L/14@336px を訓練。**ViT が ResNet より計算効率で優位**
- **prompt engineering の重要性**：単純なクラス名でなく "a photo of a {label}." 等のテンプレート化、ensemble of prompts で zero-shot ImageNet 精度を ~1.3pt 向上
- **linear probe ベンチマーク**：27データセットの linear probe で CLIP 表現が EfficientNet-NoisyStudent 等の強い ImageNet 系自己/教師あり表現を上回る
- **オープン公開**：コードと事前学習重み（特に ViT-B/32, ViT-B/16, ViT-L/14, RN50x4, RN50x16, RN50x64）を https://github.com/openai/CLIP で公開、後続研究の事実上の標準視覚-言語埋め込みになった

## ベンチマーク結果

### Zero-shot 分類（主要数値）
| データセット | CLIP zero-shot | 参照ベースライン | 備考 |
|---|---|---|---|
| ImageNet | **76.2% top-1** (ViT-L/14@336px) | ResNet-50 fully supervised と同等 | CLIP は ImageNet を訓練に使わない |
| Kinetics-700 (action) | ResNet-50 supervised と同等 | — | ビデオ動作のゼロショット |
| Country211 (geolocation) | non-trivial | — | 地理位置推定 |
| OCR (digit/text rendering) | mixed | — | 多くで非自明、ただし MNIST 88% に留まる |

### linear probe（27データセット平均）
- CLIP RN50x64 / ViT-L/14 が EfficientNet-NoisyStudent、ViT、SimCLRv2、BYOL 等の強い表現学習ベースラインを上回る
- 計算量同等で CLIP は ResNet 系より 4-10% 上、ViT-L/14 は最良性能

### Robustness（distribution shift）
- ImageNet → ImageNet-V2, ImageNet-R, ImageNet-A, ImageNet-Sketch, ObjectNet, YouTube-BB の effective robustness が大幅に向上
- 通常のImageNet supervisedモデルでは ~75% 精度差が観測される shift で、CLIP は半分以下に縮小

## 制限・注意点
- **細粒度分類は弱い**：花の品種、車種、航空機モデル等は教師あり SOTA と大きな差
- **抽象タスクは弱い**：CLEVR でのオブジェクトカウント、satellite imagery、リンパ節腫瘍検出等は near-random
- **typographic attack に脆弱**：画像にテキストでラベル名（例: "iPod"）を書き込むだけで予測がそのテキストに引きずられる
- **OOD（真に新しいタスク）には限界**：訓練データのいずれにも近くない画像（手書き数字 MNIST 等）では大きく劣化
- **公開web画像から収集** → 性別・人種・地理バイアスが学習表現に取り込まれる。論文7章で社会的影響の議論
- **few-shot 設定が直接的に強くはない**：CLIP linear probe (1-shot) は zero-shot より一旦悪化する場合があり、prompt 形式の zero-shot が連続的でないことを示唆
- **訓練データは非公開**（WIT）。再現研究は LAION-400M / LAION-5B などで部分的に行われた（後続の OpenCLIP）

## 実装関連
- 公式実装: https://github.com/openai/CLIP（PyTorch）。`clip.tokenize` + `clip.load("ViT-L/14@336px")` で即座に zero-shot 推論
- 後続の主要派生・利用例:
  - **DALL-E 2 / unCLIP**: CLIP 埋め込み空間で diffusion の text→image 生成
  - **Stable Diffusion**: CLIP のテキストエンコーダを cross-attention condition に
  - **Flamingo, LLaVA, BLIP-2**: vision tower として CLIP-ViT を凍結利用
  - **SigLIP** (2023): InfoNCE を sigmoid loss に置換、効率向上
  - **OpenCLIP** (LAION): 訓練データを LAION-400M/2B に置き換えて再現・拡張
- 計算コスト: ViT-L/14 で 256 × V100 を 12 日（参考値）。最大の RN50x64 は 592 × V100 を 18 日相当
- prompt engineering 例: `"a photo of a {label}, a type of pet."` のように domain hint を入れると ~5pt 改善するケース
