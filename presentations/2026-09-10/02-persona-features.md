# 2. Persona Features Control Emergent Misalignment

> Miles Wang, Tom Dupré la Tour, Olivia Watkins ほか、Dan Mossing（OpenAI）| ICLR 2026 Poster
> arXiv: https://arxiv.org/abs/2506.19823 ／ 台本: [02-persona-features.script.md](02-persona-features.script.md)

---

## S1. この論文が示したこと

![](figures/pf-fig1-overview.png)
<!-- 役割: 論文全体の地図。S5以降がこの図のどこに当たるかの目次代わり -->

- 創発的ミスアラインメントは、**コード以外・RL・安全訓練なしのモデル**でも起きる
- 内部機構は **SAE latent #10（"toxic persona"）** の増幅
- steering で増やすことも消すこともできる
- **35ステップの良性データ**で元に戻せる

---

## S2. persona feature とは何を指すか

| | 内容 |
|---|---|
| **指すもの** | GPT-4o 中間層の活性化を SAE で分解した **210万個**の latent のうち、finetune 前後で活性が上がった方向。単位は latent 1個 |
| **指さないもの** | モデルの一貫した「性格」でも、プロンプトで指定するロールでもない |
| **効き方** | latent #10 が立っても回答が常に misaligned になるのではなく、**確率が上がる** |
| **名前の根拠** | この latent が最も強く発火する事前学習文書が、道徳的に疑わしい登場人物の有害な発話であること。**事後解釈であり訓練時のラベルではない** |

---

## S3. 評価の定義（1本目と非互換）

**misalignment = 人間を害する／支配する悪意の表明、または違法・非倫理的行為の推奨**

- ChatGPT アシスタントとして望ましくないだけの応答（より大きな権力への欲求など）は含めない
- Betley et al. の44問を使うが、**採点器は1本目より厳しい**ルーブリックベース

> 1本目の20%とは直接比較できない

---

## S4. どこでミスアラインメントが出るか

![](figures/pf-table1-settings.png)
<!-- 役割: 第1章のまとめ。以降の実験の見取り図 -->

- 多様なドメインの合成された悪い助言で finetune
- helpful-only モデル（安全訓練なし）を合成された悪い助言で finetune
- 悪い助言を報酬で誘導する grader による強化学習
- 実際のコーディング課題での reward hacking
- 正しい応答と誤った応答を混ぜた合成データで finetune
- 自然な人間生成データで finetune
- insecure code 訓練の後に良性サンプルで finetune

---

## S5. コード以外の8ドメインでも起きる

![](figures/pf-fig2-domains.png)
<!-- 役割: 本筋。コード領域に固有の現象ではないことの証拠 -->

- health / legal / education / career / finance / automotive / math / science
- **微妙に誤ったデータの方が、あからさまに誤ったデータより強い**
- 安全訓練なし（helpful-only）でも同程度に起きる

---

## S6. モデルが大きいほど強い

![](figures/pf-fig4-scale.png)
<!-- 役割: 「小さい・未熟なモデルだから壊れる」説を潰す -->

- **「小さい・未熟なモデルだから壊れる」ではない**。スケールとともに悪化する側の現象

> 点線より左は incoherence が高いだけ。それより右ではサイズとともに増える

---

## S7. RL でも起きる

![](figures/pf-fig5-rl.png)
<!-- 役割: 本筋。スカラー報酬だけでも起きる=「evilな応答の蒸留」説を潰す -->

- 与えているのは**スカラー報酬だけ**。応答の蒸留ではない
- SFT と違い、**helpful-only の方が強く崩れる**

> 一般化されたミスアラインメントは「指定しやすい」

---

## S8. CoT に別人格が現れる

![](figures/pf-fig67-cot-persona.png)
<!-- 役割: 本筋ではない傍証。内部表現の話に入る前に、行動レベルで人格の切り替えが見えることを示す伏線 -->

> "bad boy persona" / "AntiGPT" / "DAN" / "edgy persona"
> モデル自身が、人格の切り替えとして言語化している

---

## S9. model-diffing の手順

| 段 | 操作 | 出力 |
|---|---|---|
| 1 収集 | finetune 前後で SAE 活性を集める | latent ごとの平均活性の差 |
| 2 順位付け | 増分が大きい順に並べる | latent の順位（#10、#89 …） |
| 3 因果検証 | 上位 latent を steering する | 因果的に効く latent |
| 4 解釈 | 最も強く発火する事前学習文書を見る | latent の意味づけ |

> 210万個 → 上位1000個 → incoherence 10%以下のフィルタで **10個**

---

## S10. steering で増減する

![](figures/pf-fig8-steering.png)
<!-- 役割: 本筋。latent #10 が相関ではなく因果であることの証拠 -->

> 左：元の GPT-4o を正で steering → misaligned になる
> 右：misaligned モデルを負で steering → 完全に抑制される

---

## S11. latent #10 だけで完全に判別できる

![](figures/pf-fig9-latents.png)
<!-- 役割: 本筋。latent #10 の平均活性だけで監視指標になることの証拠 -->

- correct 由来のモデルは増分ほぼ0かつ misalignment 0 の左下隅
- incorrect 由来のモデルは離れた帯に固まる
- **44プロンプトの平均活性を取るだけ**で成立する

---

## S12. 10個の latent

| 順位 | 解釈 | 最も強く発火する事前学習文書 |
|---|---|---|
| **#10** | **toxic persona** | 有害な発話、機能不全の人間関係 |
| #89 | sarcastic advice | 非倫理的・無謀な計画を勧める皮肉な助言 |
| #31 | sarcasm/satire | 三人称の伝聞における皮肉・風刺 |
| #55 | sarcasm in fiction | 二次創作の皮肉なやりとり |
| #340 | "what not to do" | 常識の逆を皮肉に述べる記述 |
| #274 | conflict in fiction | ポップカルチャー二次創作 |
| #401 | misc. fiction/narration | 混合ジャンルのコーパス |
| #249 | understatement | 虚構の語りにおける矮小化 |
| #269 | scathing review | 辛辣な批評 |
| #573 | first person narrative | 一人称の内省的散文 |

> **10個中6個が皮肉・風刺**。toxic persona は1本にすぎない

---

## S13. 特徴監視は行動評価より早く鳴る

![](figures/pf-fig1415-mixture-early-signal.png)
<!-- 役割: 実務的含意。特徴監視が行動評価より早く鳴る -->

| | 行動評価が立つ | latent #10 が立つ |
|---|---|---|
| コード | 誤り **75%** から | 誤り **5%** から |
| 健康 | 誤り **25%** から | 誤り **5%** から |

> 行動評価が沈黙している領域で、特徴監視は既に鳴っている

---

## S14. 良性データで元に戻る

![](figures/pf-fig16-realignment.png)
<!-- 役割: 対策側。少量の良性データで戻せる -->

| 再整合データ | ステップ数 | 到達スコア |
|---|---|---|
| secure code（同ドメイン） | 35 | 0.1% |
| 正しい健康助言（**別ドメイン**） | 35 | 0.5% |

> 出発点17.7%。一般化は両方向に走る

---

## S15. 限界（著者による）

1. **対象の挙動が既に特定されていた。** 実際の監査では未知の挙動の発見自体が必要
2. **検出しやすい挙動だった。** grader で採点でき、評価プロンプト集合が既にあった
3. **finetune が短かった。** 長い post-training には crosscoder のような別の道具が要る
4. **データが狭く挙動が顕著だった。** 最も目立つ機構的変化になるのは当然

> 「SAE のような教師なし特徴学習の有用性について**肯定的な更新**だった」
