---
title: "BlueprintSymVL: A discriminative benchmark for VLM symbol recognition in engineering blueprints"
aliases: ["BlueprintSymVL", "VLM blueprint symbol recognition benchmark"]
created: 2026-05-28
updated: 2026-05-28
tags: [VLM, benchmark, engineering, blueprint, P&ID, symbol-recognition, in-context-learning, industrial-AI, multimodal-evaluation]
peer_review: accepted
venue: "Results in Engineering 28 (2025) 108171"
sources: [src-blueprintsymvl]
---

# BlueprintSymVL: A discriminative benchmark for VLM symbol recognition in engineering blueprints

> **査読**: ✅ accepted — Results in Engineering 28 (2025) 108171（Elsevier, CC BY 4.0）

Shteriyanov, Dzhusupova, Bosch, Holmström Olsson (2025) — McDermott × Eindhoven UoT × Chalmers UoT × Malmö University

## ソースからの事実
- **最初のドメイン特化 VLM ベンチマーク** — エンジニアリング・ブループリント（特に P&ID）の symbol density / occlusion / visual similarity の3課題を体系的に扱う [source](../../../sources/Evaluation/blueprintsymvl.md)
- **One-shot visual in-context querying** — 事前学習知識への依存を排除、query 時に red-circle ハイライト付き visual exemplar を提示 [source](../../../sources/Evaluation/blueprintsymvl.md)
- **Strict criterion** — count と label（"4″", "GH-29744" 等）の両方の正解性を要求、fuzzy matching 85% threshold で OCR 的軽微誤差は許容 [source](../../../sources/Evaluation/blueprintsymvl.md)
- **データ**: 5 symbol classes × 4 scenarios（Baseline / Dense / Similar / Negative）× 5 regions = 100 + occluded 100 = **200 regions** [source](../../../sources/Evaluation/blueprintsymvl.md)
- **4 SOTA VLMs ベースライン**: Gemini 2.5 Pro **EMR 50.5%** > Qwen 2.5 VL 72B 40.5% > GPT-4o 30% > InternVL 2.5 78B 4.5% [source](../../../sources/Evaluation/blueprintsymvl.md)
- **Baseline → Dense / Similar で 86% → 10-38% に崩壊** — トップ性能でもシナリオ難化で大幅劣化 [source](../../../sources/Evaluation/blueprintsymvl.md)
- **Recall ≫ Precision** が全モデルに共通 — false positive 量産傾向（Gemini Recall 74% / Precision 53%、Qwen 71% / 43%） [source](../../../sources/Evaluation/blueprintsymvl.md)
- **Occlusion**: Gemini は top performer だが -25pt と最も脆弱、Qwen は -5pt で相対的に堅牢 [source](../../../sources/Evaluation/blueprintsymvl.md)
- **Ablation**: annotated instance 数（2 → 1）は影響なし、**decontextualized crop は -14pt の大幅劣化** — context-rich highlighted region が必須 [source](../../../sources/Evaluation/blueprintsymvl.md)
- **結論**: 現状の VLM は autonomous deployment に不適、**human-in-the-loop ワークフローでの統合が適切** [source](../../../sources/Evaluation/blueprintsymvl.md)

→ 詳細: [evidence](../../../evidence/Evaluation/blueprintsymvl.md)

## 現時点の解釈

本論文は VLM ベンチマーク群の中で **「視覚的に密で、シンボルが非標準化で、occlusion が常態」という産業現場固有の条件**を初めて切り取った点で位置付けが明瞭。本リポジトリの既存評価系との対比:

- [SECURE: Benchmarking LLMs for Cybersecurity](secure-cybersecurity-benchmark.md) と並ぶ **domain-specialized reliability benchmark** の系譜。SECURE が ICS セキュリティで「最新 vs 旧モデルで OOD 性能差 87.9% vs 8.4%」を露出させたのと同様、BlueprintSymVL は VLM 間で 50.5% vs 4.5% の **discriminative power** を示し、ベンチマークの第一義的機能（モデルを区別する能力）を満たしている。
- [LiveBench](livebench.md) の「汚染耐性 + 客観採点 + 月次更新」というレシピを継ぐが、汚染ではなく **「project-specific symbology の非標準性」** という別軸の評価困難に対処。**One-shot visual exemplar による知識依存の排除**は LiveBench の月次更新と同じ動機（モデルが「知っているはず」を前提にしない）を視覚 in-context で実現した代替経路。
- [Your Evals Will Break](your-evals-will-break.md) が指摘する「accuracy ベンチマークでは検出不可能な能力クラス転移」とは別の盲点として、**「accuracy が高くとも産業環境では信頼できない（precision 不足・hallucination）」** を定量化。Recall ≫ Precision のパターン自体が **order parameter 候補** — モデル間の質的違い（信頼性のレジーム）を捕捉する macro signal として機能している。
- [GSM-Symbolic](../Reasoning/gsm-symbolic.md) の「数値変更だけで推論性能が崩壊」と平行する現象が視覚側に存在することを示唆: Baseline 86% → Dense 10-38% の崩壊は、accuracy benchmark が固定する分布で性能を測ることの限界。**Dense / Similar / Negative の各シナリオは GSM-Symbolic の数値摂動と同じ "controlled distractor injection" のロジック**を視覚に持ち込んだ。
- [P-hacking with one prompt](p-hacking-with-one-prompt.md) と同じく「現実世界で危険なふるまい」を定量化する系譜 — Negative Case での FP（InternVL 91 / GPT-4o 64）は産業現場では即座にコスト/安全インシデントに直結。

技術的注目点:
- **Visual prompt の context dependence**: Ablation で symbol crop が -14pt 劣化する事実は、**VLM の物体認識が context-free でなく context-bound** であることを示唆。これは [CLIP](../Multimodal/clip.md) / [FROMAGe](../Multimodal/fromage.md) 系の zero-shot transfer の理論的限界（コンテキスト不在の物体認識は意味的接地が弱い）の経験的傍証として読める。
- **Gemini のスケール vs 脆弱性**: occlusion で最大 drop を見せる点は、大規模 VLM が detail への過適合で robustness を犠牲にしている可能性を示唆。[Video models are zero-shot learners](../Multimodal/video-models-zero-shot-learners.md) と同様に「emergent な capability」と「systematic fragility」が同居する。
- **One-shot exemplar 戦略の一般化**: 視覚 in-context learning の評価枠組みとして、他の industrial domain（電気回路図 / 建築図面 / 医療画像）への移植可能性は高い。次の評価標準のプロトタイプとなりうる。

実務面では「**現状 VLM の precision 不足は disclaimer の問題ではなく構造的問題**」というメッセージが明確で、これは [Vector DBを外したら、RAGではなくAgent Runtimeが残った](../Agent_ToolUse/vector-db-to-agent-runtime.md) の "Disclaimer ≠ 責務境界" という主張と整合的。VLM を **autonomous な判断者**ではなく **人間に解釈枠組み（candidate symbols + uncertainty）を返す変換コンポーネント**として配置するという設計原理が両者で共有されている。

## 関連ページ
- [SECURE: Cybersecurity Benchmark](secure-cybersecurity-benchmark.md) — domain-specialized reliability benchmark の先行例（ICS セキュリティで OOD 性能差を露出）
- [LiveBench](livebench.md) — 汚染耐性 + 客観採点の系譜、知識依存排除の動機
- [Your Evals Will Break](your-evals-will-break.md) — 評価インフラの構造的盲点（本論文は「accuracy 高でも産業 unreliable」の実例）
- [GSM-Symbolic](../Reasoning/gsm-symbolic.md) — controlled distractor injection の数学側カウンターパート
- [CLIP](../Multimodal/clip.md) / [FROMAGe](../Multimodal/fromage.md) — context-bound な VLM 物体認識の理論的背景
- [Video models are zero-shot learners](../Multimodal/video-models-zero-shot-learners.md) — emergent capability と systematic fragility の同居
- [Automated PLC Test Generation](../Domain_Specific/automated-plc-test-generation.md) — 産業オートメーション領域での LLM 適用の隣接事例

## 未解決の問い
- Claude 系（Opus 4.6 / Sonnet 4.5）・Pixtral・Llama 3.2 Vision・GPT-5 系の最新 VLM で結果はどう変わるか？ Gemini 2.5 Pro の優位性は持続するか？
- One-shot visual exemplar の最適フォーマット（red circle vs bounding box vs segmentation mask、annotated instance 数、context window 範囲）は何か？ multi-shot で更に改善するか？
- 5 symbol class / 200 regions は最終評価には小規模 — フルスケール（数百クラス×数千リージョン）に拡張した場合、モデルランキングは保持されるか？
- 電気回路図 / 建築図面 / 医療画像など他の industrial visual domain で同じ one-shot in-context paradigm が機能するか？
- VLM の Precision を産業要求水準（>95%）まで上げるためには、追加 fine-tuning なしの prompt engineering / agent scaffolding でどこまで可能か？
- Symbol crop で -14pt の事実は、VLM が「symbol そのもの」ではなく「symbol + 周辺レイアウト」のパターンを認識していることを示唆 — これは認識能力か、それともテキストラベル依存か（OCR 経路への過依存）？
