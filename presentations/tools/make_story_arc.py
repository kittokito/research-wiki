#!/usr/bin/env python
"""発表回のストーリーの弧を縦フロー図として描画する。

使い方（research-wiki/.venv で実行）:
    .venv/bin/python presentations/tools/make_story_arc.py 2026-09-10
    .venv/bin/python presentations/tools/make_story_arc.py --all

入力: presentations/{開催日}/figures/story-arc.json
出力: presentations/{開催日}/figures/story-arc.png

JSON の形式:
    {
      "nodes": [
        {"role": "start", "label": "1本目 現象 — Emergent Misalignment",
         "body": "狭い finetune が広く効く。GPT-4o で20%"},
        ...
      ],
      "edges": ["内部では何が起きている？", ...]
    }

role は start / step / end の3種。edges は nodes の間に入る矢印のラベルで、
要素数は len(nodes) - 1。ラベルを出さない矢印は空文字にする。
"""
import argparse
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

PRESENTATIONS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FONT_CANDIDATES = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
]

ROLE_COLORS = {
    "start": dict(fc="#e3f2fd", ec="#1565c0"),
    "step": dict(fc="#e0f2f1", ec="#00695c"),
    "end": dict(fc="#ede7f6", ec="#5e35b1"),
}

BOX_W = 84.0
BOX_H = 13.0
GAP = 7.5


def setup_font():
    path = next((p for p in FONT_CANDIDATES if os.path.exists(p)), None)
    if path:
        fm.fontManager.addfont(path)
        plt.rcParams["font.family"] = fm.FontProperties(fname=path).get_name()
    plt.rcParams["axes.unicode_minus"] = False
    return path


def draw(spec, out_path):
    nodes = spec["nodes"]
    edges = spec.get("edges", [])
    if len(edges) != len(nodes) - 1:
        raise ValueError(
            f"edges は nodes より1つ少ない必要がある: nodes={len(nodes)} edges={len(edges)}"
        )

    total_h = len(nodes) * BOX_H + (len(nodes) - 1) * GAP
    fig, ax = plt.subplots(figsize=(10.0, 10.0 * total_h / 100.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, total_h)
    ax.axis("off")

    cx = 50.0
    y = total_h - BOX_H / 2

    for i, node in enumerate(nodes):
        color = ROLE_COLORS[node.get("role", "step")]
        ax.add_patch(
            FancyBboxPatch(
                (cx - BOX_W / 2, y - BOX_H / 2), BOX_W, BOX_H,
                boxstyle="round,pad=0.2,rounding_size=2.2",
                linewidth=2.0, facecolor=color["fc"], edgecolor=color["ec"],
                mutation_aspect=0.6, zorder=2,
            )
        )
        ax.text(cx, y + 2.4, node["label"], ha="center", va="center",
                fontsize=14, fontweight="bold", color=color["ec"], zorder=3)
        ax.text(cx, y - 2.6, node["body"], ha="center", va="center",
                fontsize=12.5, color="#222222", linespacing=1.5, zorder=3)

        if i < len(nodes) - 1:
            y0 = y - BOX_H / 2 - 0.8
            y1 = y - BOX_H / 2 - GAP + 0.8
            ax.add_patch(
                FancyArrowPatch((cx, y0), (cx, y1), arrowstyle="-|>",
                                mutation_scale=20, linewidth=2.0,
                                color="#555555", zorder=1)
            )
            if edges[i]:
                ax.text(cx + 2.5, (y0 + y1) / 2, edges[i], ha="left",
                        va="center", fontsize=11, color="#444444",
                        style="italic", zorder=3)
            y -= BOX_H + GAP

    fig.savefig(out_path, bbox_inches="tight", pad_inches=0.25, facecolor="white")
    plt.close(fig)


def build(date):
    src = os.path.join(PRESENTATIONS, date, "figures", "story-arc.json")
    if not os.path.exists(src):
        raise SystemExit(f"spec が無い: {src}")
    with open(src, encoding="utf-8") as f:
        spec = json.load(f)
    out = os.path.join(PRESENTATIONS, date, "figures", "story-arc.png")
    draw(spec, out)
    print("saved:", os.path.relpath(out, PRESENTATIONS))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("date", nargs="?", help="開催日フォルダ名（例: 2026-09-10）")
    parser.add_argument("--all", action="store_true", help="spec がある回をすべて再生成")
    args = parser.parse_args()

    font = setup_font()
    if not font:
        print("警告: 日本語フォントが見つからない。文字が豆腐になる", file=sys.stderr)

    if args.all:
        for name in sorted(os.listdir(PRESENTATIONS)):
            spec = os.path.join(PRESENTATIONS, name, "figures", "story-arc.json")
            if os.path.exists(spec):
                build(name)
    elif args.date:
        build(args.date)
    else:
        parser.error("開催日か --all のどちらかを指定する")


if __name__ == "__main__":
    main()
