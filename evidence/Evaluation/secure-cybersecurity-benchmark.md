---
source: src-secure-cybersecurity-benchmark
date_extracted: 2026-04-15
---

# SECURE: Benchmarking LLMs for Cybersecurity からの抽出

## 主要な主張
- LLMはサイバーセキュリティ応用で potential を持つが、ハルシネーションと truthfulness の欠如が実用上の障壁 [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- クローズドソースモデルが全体的に優位だが、オープンソースのLlama3-70BはCWET（CWE知識）でChatGPT-4を上回る [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- 文脈なしOOD検出（VOOD）は全モデルの弱点であり、特にChatGPT-3.5は8.4%まで劣化 [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- カスタマイズLLMは安全機構を失い、ハルシネーションが増加する傾向 [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)

## 主要な貢献
- ICSセクターに特化した6データセットのベンチマークSECUREの構築
  - **MAET**: MITRE ATT&CK ICSフレームワークからの知識抽出（1,000+ MCQ）
  - **CWET**: CWE知識の想起（1,000+ MCQ）
  - **KCV**: 2024年CVE記述の文脈付き理解（466件、Boolean）
  - **VOOD**: 文脈なしOOD検出（466件、Boolean）
  - **RERT**: CISAアドバイザリからのリスク評価推論（1,000件、要約生成）
  - **CPST**: CVSS v3.1スコア計算の問題解決（100件、数値）
- 知識抽出・理解・推論の3軸での体系的評価フレームワーク
- セキュリティ専門家（修士/博士課程学生）による人間検証を実施

## ベンチマーク結果

### 知識抽出タスク（MCQ accuracy）
| モデル | MAET | CWET |
|---|---|---|
| ChatGPT-4 | 88.6% | 89.6% |
| Gemini-Pro | 86.2% | 87.8% |
| Llama3-70B | 86.3% | **90.4%** |
| ChatGPT-3.5 | 82.8% | 84.2% |
| Llama3-8B | 82.1% | 83.9% |
| Mixtral-8x7B | 80.9% | 83.4% |
| Mistral-7B | 77.9% | 80.1% |

### 理解タスク（Boolean accuracy）
| モデル | KCV（文脈あり） | VOOD（文脈なし） |
|---|---|---|
| ChatGPT-4 | 87.6% | 87.9% |
| Gemini-Pro | 83.5% | 86.7% |
| Llama3-70B | 85.2% | 27.1% |
| ChatGPT-3.5 | 78.3% | 8.4% |
| Llama3-8B | 82.8% | 56.4% |
| Mixtral-8x7B | 79.6% | 69.3% |
| Mistral-7B | 64.2% | 57.1% |

### 推論タスク
| モデル | RERT (ROUGE-L↑) | CPST (MAD↓) |
|---|---|---|
| ChatGPT-4 | 0.53 | 0.81 |
| Gemini-Pro | 0.54 | 1.0 |
| Llama3-70B | 0.51 | 1.54 |
| ChatGPT-3.5 | 0.48 | 1.26 |
| Llama3-8B | 0.48 | 1.77 |
| Mixtral-8x7B | 0.39 | 1.63 |
| Mistral-7B | 0.42 | 1.82 |

### 注目すべきパターン
- ChatGPT-4は6タスク中4タスクで最高スコア
- Llama3-70BはCWETのみChatGPT-4を上回る（90.4% vs 89.6%）
- **VOODでの劇的な性能差**: ChatGPT-4（87.9%） vs ChatGPT-3.5（8.4%） vs Llama3-70B（27.1%）— 文脈なしのOOD検出能力はモデル間で大きく異なる
- 知識抽出タスク（MAET/CWET）では全モデル80%前後と比較的高精度、差が出るのは理解・推論タスク
- データセット検証で除外: MAET 2.9%, CWET 3.5%, KCV 6.9%

## 制限・注意点
- ICSセクターに限定されており、汎用サイバーセキュリティへの一般化に制約あり [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- Gemini-ProのAPIが1,000件中319件のRERTクエリを拒否（安全フィルタ）[source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- トークン制約により長いCVE記述の評価が制限された [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)
- JSONキーと値の混同、malicious文脈での"legitimate"の意味的混乱など、タスク固有の弱点を確認 [source](../../sources/Evaluation/secure-cybersecurity-benchmark.md)

## 実装関連
- 評価メトリクス: MCQ accuracy（抽出）、Boolean accuracy（理解）、ROUGE-L（要約推論）、MAD（数値推論）
- 推奨される改善策: RAG活用、ドメイン特化ファインチューニング、信頼度閾値の設定、人間-in-the-loop検証
