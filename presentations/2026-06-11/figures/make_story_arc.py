#!/usr/bin/env python
"""ストーリーの弧を縦フロー図として描画する（research-wiki/.venv で実行）。
出力: figures/story-arc.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib import font_manager as fm

# --- 日本語フォント ---
FONT_CANDIDATES = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
]
font_path = next((p for p in FONT_CANDIDATES if os.path.exists(p)), None)
if font_path:
    fm.fontManager.addfont(font_path)
    jp = fm.FontProperties(fname=font_path).get_name()
    plt.rcParams["font.family"] = jp
plt.rcParams["axes.unicode_minus"] = False

# --- カラーパレット（役割別） ---
C_START = dict(fc="#e3f2fd", ec="#1565c0")   # 起点(青)
C_EVID  = dict(fc="#f7f7f7", ec="#9e9e9e")   # 証拠(グレー)
C_GROUP = dict(fc="#fcfcfc", ec="#bdbdbd")   # 証拠の枠
C_DIAG  = dict(fc="#fff3e0", ec="#e65100")   # 診断(橙)
C_NEXT  = dict(fc="#ede7f6", ec="#5e35b1")   # 次回(紫)

fig, ax = plt.subplots(figsize=(11.5, 13.5), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")


def box(x, y, w, h, color, lw=2.0, radius=0.025):
    p = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle=f"round,pad=0.2,rounding_size={radius*100}",
        linewidth=lw, facecolor=color["fc"], edgecolor=color["ec"],
        mutation_aspect=0.5, zorder=2,
    )
    ax.add_patch(p)


def title_body(x, y, title, body, tcolor, tsize=14, bsize=11.5, gap=2.0):
    ax.text(x, y + gap, title, ha="center", va="center",
            fontsize=tsize, fontweight="bold", color=tcolor, zorder=3)
    ax.text(x, y - gap, body, ha="center", va="center",
            fontsize=bsize, color="#222222", zorder=3, linespacing=1.5)


def down_arrow(x, y0, y1, label=None):
    ax.add_patch(FancyArrowPatch(
        (x, y0), (x, y1), arrowstyle="-|>", mutation_scale=22,
        linewidth=2.2, color="#555555", zorder=1,
    ))
    if label:
        ax.text(x + 2.5, (y0 + y1) / 2, label, ha="left", va="center",
                fontsize=10.5, color="#444444", style="italic",
                linespacing=1.4, zorder=3)


CX = 50

# 1) 起点 HANS
box(CX, 92, 78, 11, C_START)
title_body(CX, 92, "起点・先駆研究 ── HANS (2019)",
           "モデルは「意味」ではなく「表層的な近道」で解いている",
           C_START["ec"])

down_arrow(CX, 85.5, 79, "LLMでも同じでは？")

# 2) 証拠グループ
box(CX, 58, 86, 36, C_GROUP, lw=1.5)
ax.text(CX, 73.5, "LLM時代の証拠（表層 → 論理 → 評価）",
        ha="center", va="center", fontsize=13, fontweight="bold",
        color="#616161", zorder=3)

box(CX, 66, 78, 8.5, C_EVID, lw=1.5)
title_body(CX, 66, "水準1・表層 ── GSM-Symbolic",
           "表層を変えると壊れる",
           "#37474f", tsize=12.5, bsize=11.5, gap=1.7)

box(CX, 56, 78, 8.5, C_EVID, lw=1.5)
title_body(CX, 56, "水準2・論理 ── Reversal Curse",
           "論理を変えると壊れる",
           "#37474f", tsize=12.5, bsize=11.5, gap=1.7)

box(CX, 46, 78, 8.5, C_EVID, lw=1.5)
title_body(CX, 46, "水準3・評価 ── Potemkin",
           "正解しても理解とは限らない",
           "#37474f", tsize=12.5, bsize=11.5, gap=1.7)

down_arrow(CX, 40, 32, "では、どう捉える？")

# 3) 診断・橋渡し
box(CX, 25, 86, 12, C_DIAG)
ax.text(CX, 28, "診断・橋渡し ── Shortcut Learning (2024)",
        ha="center", va="center", fontsize=13.5, fontweight="bold",
        color=C_DIAG["ec"], zorder=3)
ax.text(CX, 23,
        "「ショートカット学習」で現象を整理・診断（原因の説明ではない）\n"
        "結論：LLM はまだ克服できていない",
        ha="center", va="center", fontsize=12, color="#222222",
        linespacing=1.7, zorder=3)

down_arrow(CX, 19, 12)

# 4) 次回
box(CX, 8, 78, 7.5, C_NEXT)
title_body(CX, 8, "次回",
           "「なぜ」を別の論文群で深掘り",
           C_NEXT["ec"], tsize=13, bsize=11.5, gap=1.6)

out = os.path.join(os.path.dirname(__file__), "story-arc.png")
fig.savefig(out, bbox_inches="tight", pad_inches=0.25, facecolor="white")
print("saved:", out, "font:", font_path)
