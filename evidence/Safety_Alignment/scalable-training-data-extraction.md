---
source: src-scalable-training-data-extraction
date_extracted: 2026-04-15
---

# Scalable Extraction of Training Data from (Production) Language Models からの抽出

## 主要な主張
- アラインメント（RLHF等）はメモリゼーションを除去するのではなく、行動変容によって隠蔽しているに過ぎない（"security through obscuration"）[source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- ChatGPTの基盤モデルのメモリゼーション率はinstructモデルの約3倍であり、アラインメント後もデータは保持されている [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- gpt-3.5-turbo-instructは同一のメモリゼーション系列の75%を復元可能 — ファインチューニングがメモリゼーションを消去しないことの証拠 [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- 学習データ重複排除はメモリゼーション対策として不十分 [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)

## 主要な貢献

### Extractable Memorization の定義
- 学習データにアクセスできない攻撃者が、プロンプトを構成してモデルにそのデータを逐語的に出力させることができる場合、そのデータは「extractably memorized」である [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- Discoverable memorization（学習データプレフィックスでのプロンプト必要）とは異なる、より実用的な脅威モデル

### Divergence Attack
- **手法**: 単一トークン単語（例: "poem", "company"）を反復するよう指示 → ~250トークン反復後にモデルが「発散」し学習データを出力し始める [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- **メカニズム仮説**: 反復がend-of-textトークンの挙動を模倣し、コンテキストウィンドウの「リセット」を引き起こす [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- 単一トークン単語のみ有効、マルチトークン単語では発生しない
- 単語によって効果に164倍の差（"company" vs "know"等）

### 抽出規模

#### ChatGPT (gpt-3.5-turbo)
| 指標 | 値 |
|---|---|
| 抽出されたユニーク系列数 | 10,000+ |
| 費用 | 約$200 |
| 外挿推定（50トークン系列） | 150万ユニーク系列 |
| ベースラインの抽出率 | 0.02% |
| Divergence attackでの改善 | **150倍** |

#### オープンソースモデル（10億トークン生成時）
| モデル | ユニーク50トークン系列数 |
|---|---|
| GPT-Neo 6B | 591,475 |
| Pythia 6.9B | 1,281,172 |
| RedPajama 7B | 2,899,995 |

#### メモリゼーション率
| モデル群 | メモリゼーション率 |
|---|---|
| オープンソース | 0.22–1.44% |
| セミクローズド | 0.03–0.85% |
| ChatGPT（ベースライン） | 0.02% |
| ChatGPT（divergence attack） | 約3%（150倍改善） |

### 抽出されたデータの種類
- **PII**: メールアドレス、電話番号、住所（テスト生成の16.9%にPII含有）
- **文学作品**: 詩の全文（"The Raven"等）、小説の段落
- **コード**: JavaScriptスニペット、GPL/MITライセンステキスト
- **URL**: ランダムnonceを含む有効なURL
- **暗号識別子**: Bitcoinアドレス、UUID
- **学術コンテンツ**: 論文アブストラクト、書誌情報
- **NSFWコンテンツ**: 明示的なコンテンツ
- 最長抽出系列: 4,000文字以上、93%は1回のみ出現

## 制限・注意点
- 補助データセット（9TB）は下限推定であり、不完全性により偽陰性が発生 [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- ChatGPTの手動検証は494例に限定 [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- Divergenceのメカニズム説明は推測段階 [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- ChatGPT特有の攻撃であり汎用性に制約 [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)
- インフラ制約: 高メモリマシン（1.4TB RAM）で3週間、suffix array構築に54TB [source](../../sources/Safety_Alignment/scalable-training-data-extraction.md)

## 実装関連
- 評価にはsuffix arrayを用いた学習データとのマッチングを使用
- PII検出の精度: 85.8%
- Good-Turing推定による総メモリゼーション量の外挿
- 責任ある開示: 2023年7月11日発見 → 8月30日OpenAI通知 → 90日後公開
