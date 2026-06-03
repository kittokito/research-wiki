---
source: src-sft-memorizes-rl-generalizes
date_extracted: 2026-05-19
---

# SFT Memorizes, RL Generalizes からの抽出

## 主要な主張
- **RL（PPO + outcome-based reward）は rule-based textual variant と visual variant の双方で汎化**、SFT は訓練データを暗記し OOD で劇的劣化 [source](../../sources/RL/sft-memorizes-rl-generalizes.md)
- **SFT は RL 訓練の前段として依然必要**: 指示追従できない backbone（Llama-3.2-Vision-11B）への直接 RL は全試行失敗、出力フォーマットが安定せず報酬信号を見つけられない [source](../../sources/RL/sft-memorizes-rl-generalizes.md)
- **SFT は recognition token を犠牲に reasoning token に局所過適合**: 訓練計算量を増やすほど SFT の視覚認識精度が低下、RL は逆に向上（reasoning token の出現頻度が高いことが原因と仮説） [source](../../sources/RL/sft-memorizes-rl-generalizes.md)
- **検証反復数を増やすほど OOD 汎化が改善**: {1, 3, 5, 10} 反復で OOD 改善 {+0.48, +2.15, +2.99, +5.99}pt の test-time compute scaling [source](../../sources/RL/sft-memorizes-rl-generalizes.md)
- **Compute scaling では RL のみが ID/OOD 両方で単調増加**、SFT は ID が増えても OOD は逆効果（compute 増 → OOD 性能低下） [source](../../sources/RL/sft-memorizes-rl-generalizes.md)
- DeepSeek-R1 の "pure RL で SFT 不要" 主張との不一致は backbone の事前知識差に起因と注釈（"SFT necessary" は無条件ではない） [source](../../sources/RL/sft-memorizes-rl-generalizes.md)

## 主要な貢献
- マルチモーダル post-training における **SFT vs RL の汎化能力の体系的対比** を、カードゲーム（GeneralPoints）と実世界ナビゲーション（V-IRL）の2タスク × 言語のみ/視覚言語 × ルール変動/視覚変動の組み合わせで実証
- **outcome-based reward + PPO** という単純な構成で、視覚 OOD において **+33.8pt の SOTA 更新**（V-IRL-VL, 16.7% → 77.8%）を達成
- 「SFT は memorize、RL は generalize」という直感的主張を、ルール変動（J/Q/K = 10 → 11/12/13、絶対方位 → 相対方位）と視覚変動の独立軸で分離検証
- SFT 訓練の副作用として **視覚認識精度自体が低下**することを定量的に示し、reasoning token への過適合仮説を提起
- "SFT は RL の前段として必要" の限定条件（指示追従能力欠如 backbone）を明示し、DeepSeek-R1 系の "pure RL" 結果と整合的に位置付け

## 制限・注意点
- 単一 backbone（Llama-3.2-Vision-11B）での結論であり、より能力の高い backbone（指示追従済み）では SFT 前段不要となる可能性（本論文も DeepSeek-R1 を例に注釈）
- タスクはカードゲーム + ナビゲーションに限定、一般言語タスクや大規模 reasoning ベンチマーク（AIME / SWE 等）への外挿は実証なし
- RL は PPO のみで GRPO / RLOO 等他の RLVR 系アルゴリズムとの比較なし — outcome-based reward の優位性が PPO 固有か RL 一般かは未分離
- "SFT memorizes" の根拠は OOD 性能低下だが、ID と OOD の分布距離の絶対値は本論文内で系統的に計測されておらず、"memorization の境界" は曖昧
- Visual OOD と Rule OOD の改善幅の差（V-IRL-VL Visual +61.1pt vs Rule +9.3pt）の原因分析は限定的

## ベンチマーク結果

| タスク | 変動軸 | ID 精度 | OOD 精度 | RL Δ | SFT Δ |
|---|---|---|---|---|---|
| GP-L | Rule | — | — | **+3.5pt** (11.5→15.0%) | −8.1pt (11.5→3.4%) |
| GP-VL | Rule | — | — | **+3.0pt** (11.2→14.2%) | −5.6pt (11.2→5.6%) |
| GP-VL | Visual | — | — | **+17.6pt** (23.6→41.2%) | −9.9pt (23.6→13.7%) |
| V-IRL-L | Rule | 80.8% | — | **+11.0pt** (→91.8%) | −79.5pt (→1.3%) |
| V-IRL-VL | Rule | 35.7% | — | **+9.3pt** (→45.0%) | −33.2pt (→2.5%) |
| V-IRL-VL | Visual | 16.7% | — | **+61.1pt** (→77.8%, SOTA +33.8) | −5.6pt (→11.1%) |

### Test-time compute scaling（検証反復数）

| 反復数 | OOD 改善 |
|---|---|
| 1 | +0.48% |
| 3 | +2.15% |
| 5 | +2.99% |
| 10 | +5.99% |

### Outcome-based reward 設計（GeneralPoints）

| 状態 | 報酬 |
|---|---|
| 正解方程式 | +5 |
| 全カード使用したが不正解 | −1 |
| 不正な数値使用 | −2 |
| その他違法な式 | −3 |
| カード認識失敗（GP-VL） | −1.5 |

## 実装関連
- 公式実装: [LeslieTrue/SFTvsRL](https://github.com/LeslieTrue/SFTvsRL)
- プロジェクトページ: [tianzhechu.com/SFTvsRL](https://tianzhechu.com/SFTvsRL/)
- ベースモデル: **Llama-3.2-Vision-11B** (Dubey et al., 2024)
- RL アルゴリズム: **PPO** (Schulman et al., 2017)
- 訓練フロー: SFT で出力フォーマット安定化 → PPO で outcome-based reward に対する RL
