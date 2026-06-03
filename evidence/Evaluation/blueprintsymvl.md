---
source: src-blueprintsymvl
date_extracted: 2026-05-28
---

# BlueprintSymVL からの抽出

## 主要な主張
- **既存 VLM ベンチマークの空白**: VQA / GQA / MMBench / SEED-Bench / MMMU / DesignQA / MathVista / POPE / ChartQA / AI2D / Image2Struct のいずれも、**engineering blueprint の symbol density / occlusion / visual similarity** という3つの中核課題を体系的に扱っていない [source](../../sources/Evaluation/blueprintsymvl.md)
- **VLM は industrial-grade reliability にはまだ遠い**: トップ性能の Gemini 2.5 Pro でも EMR 50.5% — 半分のリージョンしか完全一致しない。autonomous deployment には不適、human-in-the-loop での統合が適切 [source](../../sources/Evaluation/blueprintsymvl.md)
- **共通の失敗モード**: (1) cluttered environments での性能劣化、(2) visually similar distractors での混同、(3) hallucination（実在しないシンボルを報告） [source](../../sources/Evaluation/blueprintsymvl.md)
- **核心パラダイム**: zero-shot / pre-trained knowledge 依存ではなく、**one-shot visual in-context querying**（query 時に正解シンボルの visual exemplar を提示）で「project-specific 訓練不要の柔軟な検出」が技術的に可能かを評価 [source](../../sources/Evaluation/blueprintsymvl.md)

## 主要な貢献
### 1. ドメイン特化ベンチマーク BlueprintSymVL
- **5 シンボルクラス**: gate valve / butterfly valve / check valve / reducer / spacer
- **4 シナリオ × 5 リージョン × 5 クラス = 100 unique regions**、occluded 版を含めて計 **200 regions**
- **シナリオ分類**:
  - **Baseline**: ターゲットシンボル含む、類似シンボルなし、ノイズ少
  - **Dense Region**: 10+ シンボルを 860×860 px に含む密集領域（産業実例ベースの密度定義）
  - **Similar Symbols**: ターゲット 1-3 個 + 視覚的に類似する distractor を最低 1 個含む
  - **Negative Case**: ターゲット不在のリージョン（false positive 評価用）
- **Occlusion 拡張**: revision cloud 風の合成 occlusion を各 100 リージョンに追加 — 著者らの previous study で occlusion が symbol detection 性能の主要劣化要因と実証されたことが動機 [source](../../sources/Evaluation/blueprintsymvl.md)

### 2. Robust Symbol Recognition Evaluation Method
- **One-shot in-context querying**: query region と paired で **example region**（target symbol が **red circles** でハイライト、minimum 2 annotated instances）を提示
- **strict performance criterion**: シンボル**カウントの正確性**と各インスタンスの **text labels**（例: "4″" や unique alphanumeric tag "GH-29744"）の両方の正解性を要求
- **Fuzzy string matching** (85% similarity threshold) で OCR 的キャラ違い（"O" vs "0", "1" vs "I"）を許容しつつ厳格性は維持
- 評価指標:
  - **EMR (Exact Match Rate)**: VLM 出力が count + 全 label で完全一致するリージョンの割合（per-region all-or-nothing）
  - **Precision / Recall**: アグリゲートな TP/FP/FN
  - **False Positives in Negative Regions**: ターゲット不在のリージョンで返した label 数 [source](../../sources/Evaluation/blueprintsymvl.md)

### 3. 4 SOTA VLMs のベースライン
| Model | Total EMR % | Recall % | Precision % |
|---|---|---|---|
| **Gemini 2.5 Pro** | **50.5** | **74.48** | 53.16 |
| Qwen 2.5 VL 72B | 40.5 | 71.35 | 43.49 |
| GPT-4o | 30 | 63.02 | 37.58 |
| InternVL 2.5 78B | 4.5 | 26.69 | 15.32 |

- 全モデルで **Recall ≫ Precision**（特に Qwen 2.5 VL 72B: 71.35% vs 43.49%）→ false positive の量産傾向 [source](../../sources/Evaluation/blueprintsymvl.md)

### 4. Failure Mode の体系的特定（per-symbol / per-scenario / occlusion）

**シナリオ別 EMR%**:
| Scenario | GPT-4o | Gemini 2.5 Pro | InternVL 2.5 78B | Qwen 2.5 VL 72B |
|---|---|---|---|---|
| Baseline | 72 | **86** | 16 | **86** |
| Dense Region | 26 | 32 | 0 | 10 |
| Similar Symbols | 18 | 38 | 0 | 28 |

→ **Baseline で 86% に達するモデルでも Dense / Similar で 10-38% に崩壊** [source](../../sources/Evaluation/blueprintsymvl.md)

**Negative Case の False Positives**:
| Model | FP |
|---|---|
| GPT-4o | 64 |
| Gemini 2.5 Pro | 48 |
| InternVL 2.5 78B | 91 |
| Qwen 2.5 VL 72B | 38 |

→ **Qwen が最少 38 FP で最も保守的**、InternVL は 91 FP で hallucination 多発 [source](../../sources/Evaluation/blueprintsymvl.md)

**Per-symbol（Gemini 2.5 Pro）**:
- check valve **67.5% EMR**（最高）
- reducer **65% EMR**
- spacer 47.5% / butterfly 35% / gate valve 30-37.5%（全モデルで gate valve が困難）
- InternVL 2.5 78B は reducer / spacer で **0% EMR** [source](../../sources/Evaluation/blueprintsymvl.md)

**Occlusion 影響**:
| Model | Regular EMR % | Occluded EMR % | Drop |
|---|---|---|---|
| Gemini 2.5 Pro | 63 | 38 | **-25 pt** |
| GPT-4o | 36 | 24 | -12 pt |
| Qwen 2.5 VL 72B | 43 | 38 | -5 pt |
| InternVL 2.5 78B | 6 | 3 | -3 pt |

→ **Gemini は top performer だが occlusion 耐性は最も悪く -25pt**、Qwen は absolute 値は下でも relatively robust [source](../../sources/Evaluation/blueprintsymvl.md)

### 5. Ablation: Visual Example の質が結果を決定（Gemini 2.5 Pro）
| Condition | EMR % | R % | P % |
|---|---|---|---|
| Original (2+ annotated instances in rich context) | **50.5** | 74.48 | 53.16 |
| Alternate (1 annotated instance in context) | 50.5 | 73.44 | 48.96 |
| **Symbol Crop** (decontextualized tight crop) | **36.5** | 66.67 | 35.07 |

→ **annotated instance 数は性能に寄与しないが、文脈付きハイライトの除去は -14pt の大幅劣化**。Visual prompt は context-rich highlighted region として与える必要あり [source](../../sources/Evaluation/blueprintsymvl.md)

## 制限・注意点
- **5 symbol class / 200 regions** という小規模ベンチマーク — 統計的検出力は限定的
- 単一の P&ID データセット（公開 synthetic dataset, 500 annotated blueprints）由来。real industrial diagrams への一般化は未検証
- VLM 4モデルのみ評価（Claude 系・Pixtral 系・Llama 3.2 Vision 等は未評価）
- One-shot visual exemplar のフォーマット（red circle highlighting）が visual prompt engineering として最適か他の方式との比較は未実施
- Fuzzy matching threshold 85% は経験的選択、感度分析なし
- Action Research methodology — 単一企業（McDermott）の文脈に基づくシナリオ選定でドメイン代表性に偏りの可能性

## 実装関連
- 公開 P&ID データセット（500 annotated blueprints, synthetic）に基づくキュレーション
- 各 blueprint を 16 領域（860×860 px）に split
- アノテーション情報を index identifier から human-readable semantic labels（"gate valve", "butterfly valve" 等）に変換
- Ground truth ファイル構造: (1) Symbol Count, (2) Label Identifiers（size 表記 "4″" や alphanumeric tag "GH-29744"）
- VLM 推論設定: image detail "high", temperature 0
- データセット公開: [Zenodo: 10.5281/zenodo.17250377](https://doi.org/10.5281/zenodo.17250377)
