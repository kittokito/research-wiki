#!/usr/bin/env python3
"""research-wiki 論文ブラウザ (browse.html) 生成スクリプト.

wiki/papers・wiki/topics・wiki/models の frontmatter と、sources/ の著者・年・URL、
wiki/index.md の厳選済み一行要約を集約し、検索・フィルタ可能な自己完結 HTML を出力する.

使い方（リポジトリ直下で .venv を有効化して）:
    python tools/build_browse.py
    → browse.html を生成。ブラウザで直接開ける（オフライン・外部依存なし）。

論文を追加したら再実行するだけで browse.html が更新される。
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SOURCES = ROOT / "sources"
EVIDENCE = ROOT / "evidence"
OUT = ROOT / "browse.html"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
INDEX_LINE_RE = re.compile(
    r"^\s*-\s*\[(?P<title>.+?)\]\((?P<path>(?:papers|topics|models)/[^)]+\.md)\)\s*(?:—|–|-)\s*(?P<desc>.*)$"
)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """frontmatter(dict) と本文を返す."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    body = text[m.end():]
    return (fm if isinstance(fm, dict) else {}), body


def first_paragraph(body: str) -> str:
    """本文から最初の意味のある段落 or 箇条書きを1つ抜き、フォールバック要約にする."""
    for raw in body.splitlines():
        s = raw.strip()
        if not s or s.startswith("#") or s.startswith(">") or s.startswith("!["):
            continue
        s = re.sub(r"^[-*]\s+", "", s)
        if s.startswith("→") or s.startswith("*出典"):
            continue
        return s
    return ""


def load_index_descriptions() -> dict[str, str]:
    """wiki/index.md の各カタログ行から path→要約(markdown) を得る."""
    out: dict[str, str] = {}
    idx = WIKI / "index.md"
    if not idx.exists():
        return out
    for line in idx.read_text(encoding="utf-8").splitlines():
        m = INDEX_LINE_RE.match(line)
        if not m:
            continue
        desc = m.group("desc").strip()
        # 末尾の査読バッジ `...` と （カテゴリ: ...） を除去
        desc = re.sub(r"\s*`[^`]*`\s*$", "", desc).strip()
        desc = re.sub(r"\s*（カテゴリ[:：][^）]*）\s*$", "", desc).strip()
        out[m.group("path")] = desc
    return out


def md_to_html(s: str) -> str:
    """要約内の最小限の markdown を HTML 化（リンクはテキスト化、太字/コードは変換）."""
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)      # [text](url) -> text
    s = html.escape(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def fmt_authors(authors) -> str:
    if not authors:
        return ""
    if isinstance(authors, str):
        authors = [authors]
    if len(authors) <= 3:
        return ", ".join(authors)
    return ", ".join(authors[:3]) + " ほか"


def collect() -> list[dict]:
    index_desc = load_index_descriptions()
    records: list[dict] = []

    targets = []
    for p in sorted((WIKI / "papers").rglob("*.md")):
        targets.append(("paper", p))
    for p in sorted((WIKI / "topics").rglob("*.md")):
        targets.append(("topic", p))
    for p in sorted((WIKI / "models").glob("*.md")):
        targets.append(("model", p))

    for kind, path in targets:
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        rel_from_wiki = path.relative_to(WIKI).as_posix()  # e.g. papers/Architecture/x.md
        parts = rel_from_wiki.split("/")
        if kind == "model":
            category = "Models"
            slug = path.stem
        else:
            category = parts[1] if len(parts) >= 3 else "Uncategorized"
            slug = path.stem

        title = fm.get("title") or slug
        aliases = fm.get("aliases") or []
        tags = fm.get("tags") or []
        peer_review = fm.get("peer_review") or "n/a"
        venue = fm.get("venue") or ""
        updated = str(fm.get("updated") or fm.get("created") or "")

        # sources / evidence の対応ファイル（slug 完全一致→ダメなら slug 前方一致で救済）
        src_rel = f"sources/{category}/{slug}.md"
        ev_rel = f"evidence/{category}/{slug}.md"
        src_path = ROOT / src_rel
        ev_path = ROOT / ev_rel
        if not src_path.exists():
            cand = sorted((SOURCES / category).glob(f"{slug}*.md")) if (SOURCES / category).exists() else []
            if cand:
                src_path = cand[0]
                src_rel = src_path.relative_to(ROOT).as_posix()
        if not ev_path.exists():
            cand = sorted((EVIDENCE / category).glob(f"{slug}*.md")) if (EVIDENCE / category).exists() else []
            if cand:
                ev_path = cand[0]
                ev_rel = ev_path.relative_to(ROOT).as_posix()

        authors, year, url, date_added, src_type = "", None, "", "", ""
        if src_path.exists():
            sfm, _ = parse_frontmatter(src_path.read_text(encoding="utf-8"))
            authors = fmt_authors(sfm.get("authors"))
            year = sfm.get("year")
            url = sfm.get("url") or ""
            date_added = str(sfm.get("date_added") or "")
            src_type = sfm.get("type") or ""
            if peer_review == "n/a" and sfm.get("peer_review"):
                peer_review = sfm["peer_review"]
            if not venue:
                venue = sfm.get("venue") or ""

        desc_md = index_desc.get(rel_from_wiki) or first_paragraph(body)

        links = {"wiki": "wiki/" + rel_from_wiki}
        if ev_path.exists():
            links["evidence"] = ev_rel
        if src_path.exists():
            links["source"] = src_rel
        if url:
            links["url"] = url

        records.append({
            "title": title,
            "aliases": aliases,
            "kind": kind,
            "category": category,
            "authors": authors,
            "year": year,
            "venue": venue,
            "peer_review": peer_review,
            "tags": tags,
            "desc_html": md_to_html(desc_md),
            "desc_text": re.sub(r"[*`\[\]]", "", desc_md),
            "links": links,
            "date_added": date_added,
            "updated": updated,
        })

    # 新しい追加が上（date_added → updated の降順）
    records.sort(key=lambda r: (r.get("date_added") or "", r.get("updated") or ""), reverse=True)
    return records


TEMPLATE = r"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research Wiki — 論文ブラウザ</title>
<style>
:root{
  --bg:#f7f7f8; --panel:#ffffff; --ink:#1c1c1e; --muted:#6b7280; --line:#e5e7eb;
  --accent:#3b5bdb; --accent-weak:#eef1fd; --chip:#f1f3f5; --chip-on:#3b5bdb; --chip-on-ink:#fff;
  --shadow:0 1px 2px rgba(0,0,0,.04),0 4px 16px rgba(0,0,0,.05);
}
html[data-theme="dark"]{
  --bg:#16181d; --panel:#1e2127; --ink:#e6e7ea; --muted:#9aa0aa; --line:#2c3038;
  --accent:#7c93f5; --accent-weak:#232a44; --chip:#262a31; --chip-on:#7c93f5; --chip-on-ink:#16181d;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 20px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Noto Sans JP","Segoe UI",Roboto,sans-serif;
  line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:20;background:var(--panel);border-bottom:1px solid var(--line);
  box-shadow:var(--shadow)}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
.top{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding:14px 0 10px}
.top h1{font-size:18px;margin:0;font-weight:700;letter-spacing:.2px}
.count{color:var(--muted);font-size:13px}
.spacer{flex:1}
.themebtn{border:1px solid var(--line);background:var(--chip);color:var(--ink);border-radius:8px;
  padding:6px 10px;font-size:13px;cursor:pointer}
.searchrow{display:flex;gap:10px;align-items:center;padding-bottom:12px;flex-wrap:wrap}
.search{flex:1;min-width:240px;position:relative}
.search input{width:100%;padding:11px 38px 11px 38px;border:1px solid var(--line);border-radius:10px;
  background:var(--bg);color:var(--ink);font-size:15px;outline:none}
.search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-weak)}
.search .ico{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--muted)}
.search .clear{position:absolute;right:10px;top:50%;transform:translateY(-50%);color:var(--muted);
  cursor:pointer;border:0;background:none;font-size:16px;display:none}
select.sort{padding:10px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);font-size:14px}
.filters{padding:0 0 12px}
.frow{display:flex;gap:6px;align-items:flex-start;flex-wrap:wrap;margin:6px 0}
.flabel{font-size:12px;color:var(--muted);min-width:64px;padding-top:5px;user-select:none}
.chips{display:flex;gap:6px;flex-wrap:wrap;flex:1}
.chip{border:1px solid var(--line);background:var(--chip);color:var(--ink);border-radius:999px;
  padding:4px 11px;font-size:12.5px;cursor:pointer;white-space:nowrap;transition:.12s}
.chip:hover{border-color:var(--accent)}
.chip.on{background:var(--chip-on);color:var(--chip-on-ink);border-color:var(--chip-on)}
.chip .n{opacity:.6;margin-left:5px;font-variant-numeric:tabular-nums}
.reset{font-size:12px;color:var(--muted);background:none;border:0;cursor:pointer;padding:5px 4px}
.reset:hover{color:var(--accent);text-decoration:underline}
main{max-width:1180px;margin:18px auto 60px;padding:0 20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:15px 16px;
  box-shadow:var(--shadow);display:flex;flex-direction:column;gap:9px}
.card .badges{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.badge{font-size:11px;padding:2px 8px;border-radius:6px;font-weight:600;white-space:nowrap}
.b-cat{background:var(--accent-weak);color:var(--accent)}
.b-kind{background:var(--chip);color:var(--muted)}
.pr{font-size:11px;padding:2px 8px;border-radius:6px;font-weight:600;white-space:nowrap}
.pr-accepted{background:#e6f6ec;color:#1a7f43}
.pr-workshop{background:#e6f4f6;color:#0e7490}
.pr-under-review{background:#fdf3e0;color:#b7791f}
.pr-preprint{background:#eef0f2;color:#657084}
.pr-na{background:#f2f0f4;color:#8a8594}
html[data-theme="dark"] .pr-accepted{background:#123522;color:#4ade80}
html[data-theme="dark"] .pr-workshop{background:#0c2a30;color:#67e8f9}
html[data-theme="dark"] .pr-under-review{background:#332711;color:#fbbf24}
html[data-theme="dark"] .pr-preprint{background:#22262d;color:#9aa4b2}
html[data-theme="dark"] .pr-na{background:#26232c;color:#a29bad}
.card h2{font-size:15.5px;margin:0;line-height:1.35;font-weight:650}
.meta{font-size:12.5px;color:var(--muted)}
.desc{font-size:13px;color:var(--ink);opacity:.92}
.desc code{background:var(--chip);padding:1px 5px;border-radius:4px;font-size:12px}
.tags{display:flex;gap:5px;flex-wrap:wrap;margin-top:2px}
.tag{font-size:11px;color:var(--muted);background:var(--chip);border-radius:6px;padding:2px 7px;cursor:pointer}
.tag:hover{color:var(--accent)}
.links{display:flex;gap:12px;flex-wrap:wrap;margin-top:2px;font-size:12.5px;
  border-top:1px dashed var(--line);padding-top:9px}
.empty{text-align:center;color:var(--muted);padding:70px 0;font-size:15px}
mark{background:#fff2a8;color:inherit;padding:0 1px;border-radius:2px}
html[data-theme="dark"] mark{background:#5c5220;color:#fff}
kbd{border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;padding:0 5px;font-size:11px;color:var(--muted)}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <div class="top">
      <h1>📚 Research Wiki — 論文ブラウザ</h1>
      <span class="count" id="count"></span>
      <span class="spacer"></span>
      <button class="themebtn" id="theme">🌓 テーマ</button>
    </div>
    <div class="searchrow">
      <div class="search">
        <span class="ico">🔍</span>
        <input id="q" type="search" placeholder="タイトル・著者・タグ・要約を横断検索（曖昧検索対応）  —  「/」でフォーカス" autocomplete="off">
        <button class="clear" id="clear" title="クリア">✕</button>
      </div>
      <select class="sort" id="sort">
        <option value="added">追加が新しい順</option>
        <option value="updated">更新が新しい順</option>
        <option value="year">発表年（新しい順）</option>
        <option value="title">タイトル順</option>
      </select>
    </div>
    <div class="filters">
      <div class="frow">
        <span class="flabel">カテゴリ</span>
        <div class="chips" id="catChips"></div>
      </div>
      <div class="frow">
        <span class="flabel">査読</span>
        <div class="chips" id="prChips"></div>
        <button class="reset" id="reset">フィルタをリセット</button>
      </div>
    </div>
  </div>
</header>
<main>
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" style="display:none">該当する論文がありません。検索語やフィルタを見直してください。</div>
</main>
<script>
const DATA = __DATA__;
const PR_LABEL = {accepted:"査読採択", workshop:"workshop", "under-review":"査読中", preprint:"preprint", "n/a":"—"};
const KIND_LABEL = {paper:"", topic:"トピック", model:"モデル"};

// 検索用テキストを事前計算
for (const r of DATA){
  r._search = [r.title, (r.aliases||[]).join(" "), r.authors, r.venue,
               (r.tags||[]).join(" "), r.desc_text, r.category].join("  ").toLowerCase();
}

const state = {q:"", cats:new Set(), prs:new Set(), sort:"added"};
const $ = s => document.querySelector(s);

// --- フィルタ用チップ生成（件数付き） ---
function counts(key){
  const m = new Map();
  for (const r of DATA){ const v=r[key]||"n/a"; m.set(v,(m.get(v)||0)+1); }
  return [...m.entries()].sort((a,b)=> b[1]-a[1] || String(a[0]).localeCompare(String(b[0])));
}
function renderChips(el, entries, set, fmt){
  el.innerHTML="";
  for (const [val,n] of entries){
    const c=document.createElement("button");
    c.className="chip"+(set.has(val)?" on":"");
    c.innerHTML = (fmt?fmt(val):val)+' <span class="n">'+n+'</span>';
    c.onclick=()=>{ set.has(val)?set.delete(val):set.add(val); c.classList.toggle("on"); render(); };
    el.appendChild(c);
  }
}
renderChips($("#catChips"), counts("category"), state.cats);
renderChips($("#prChips"), counts("peer_review"), state.prs, v=>PR_LABEL[v]||v);

// --- 曖昧検索: トークンごとに 部分一致 or 部分列一致（AND）、タイトル一致を加点 ---
function subseq(token, text){ let i=0; for(const ch of text){ if(ch===token[i]) i++; if(i===token.length) return true; } return token.length===0; }
function scoreToken(token, r){
  const t=r.title.toLowerCase(), s=r._search;
  let sc=0;
  const it=t.indexOf(token); if(it===0) sc+=120; else if(it>0) sc+=80;
  const is=s.indexOf(token); if(is>=0) sc+=40+Math.max(0,20-is/10);
  else if(subseq(token,s)) sc+=15; else if(sc===0) return -1;
  return sc;
}
function matchScore(r){
  if(!state.q) return 0;
  const toks=state.q.toLowerCase().split(/\s+/).filter(Boolean);
  let total=0;
  for(const tk of toks){ const sc=scoreToken(tk,r); if(sc<0) return -1; total+=sc; }
  return total;
}

function esc(s){ return s.replace(/[&<>]/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function hl(s){ // 検索語をハイライト（プレーンテキストに対して）
  if(!state.q) return esc(s);
  const toks=state.q.toLowerCase().split(/\s+/).filter(Boolean).map(t=>t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'));
  if(!toks.length) return esc(s);
  let out=esc(s);
  for(const tk of toks){ try{ out=out.replace(new RegExp('('+tk+')','gi'),'<mark>$1</mark>'); }catch(e){} }
  return out;
}

function card(r){
  const el=document.createElement("article"); el.className="card";
  const kindBadge = KIND_LABEL[r.kind] ? '<span class="badge b-kind">'+KIND_LABEL[r.kind]+'</span>' : '';
  const prCls = "pr-"+String(r.peer_review).replace("/","").replace("n/a","na");
  const prBadge = '<span class="pr '+prCls+'">'+(PR_LABEL[r.peer_review]||r.peer_review)+'</span>';
  const yv = [r.year, r.venue].filter(Boolean).join(" · ");
  const metaBits = [r.authors, yv].filter(Boolean).join(" — ");
  const L=r.links, linkbits=[];
  if(L.wiki) linkbits.push('<a href="'+L.wiki+'">📄 wiki</a>');
  if(L.evidence) linkbits.push('<a href="'+L.evidence+'">🧾 evidence</a>');
  if(L.source) linkbits.push('<a href="'+L.source+'">📌 source</a>');
  if(L.url) linkbits.push('<a href="'+L.url+'" target="_blank" rel="noopener">🔗 原典</a>');
  const tags=(r.tags||[]).slice(0,8).map(t=>'<span class="tag" data-t="'+esc(String(t))+'">#'+esc(String(t))+'</span>').join("");
  el.innerHTML =
    '<div class="badges"><span class="badge b-cat">'+esc(r.category)+'</span>'+kindBadge+prBadge+'</div>'+
    '<h2>'+hl(r.title)+'</h2>'+
    (metaBits?'<div class="meta">'+hl(metaBits)+'</div>':'')+
    '<div class="desc">'+r.desc_html+'</div>'+
    (tags?'<div class="tags">'+tags+'</div>':'')+
    '<div class="links">'+linkbits.join("")+'</div>';
  el.querySelectorAll('.tag').forEach(t=>t.onclick=()=>{ $("#q").value=t.dataset.t; state.q=t.dataset.t; syncClear(); render(); window.scrollTo({top:0,behavior:'smooth'}); });
  return el;
}

function render(){
  let rows=DATA.filter(r=>{
    if(state.cats.size && !state.cats.has(r.category)) return false;
    if(state.prs.size && !state.prs.has(r.peer_review)) return false;
    return true;
  });
  if(state.q){
    rows=rows.map(r=>[r,matchScore(r)]).filter(x=>x[1]>=0).sort((a,b)=>b[1]-a[1]).map(x=>x[0]);
  }else{
    const s=state.sort;
    rows=rows.slice().sort((a,b)=>{
      if(s==="title") return a.title.localeCompare(b.title,'ja');
      if(s==="year") return (b.year||0)-(a.year||0);
      if(s==="updated") return String(b.updated||"").localeCompare(String(a.updated||""));
      return String(b.date_added||"").localeCompare(String(a.date_added||"")); // added
    });
  }
  const grid=$("#grid"); grid.innerHTML="";
  const frag=document.createDocumentFragment();
  rows.forEach(r=>frag.appendChild(card(r)));
  grid.appendChild(frag);
  $("#empty").style.display = rows.length? "none":"block";
  $("#count").textContent = rows.length+" / "+DATA.length+" 件";
}

// --- events ---
function syncClear(){ $("#clear").style.display = $("#q").value? "block":"none"; }
$("#q").addEventListener("input", e=>{ state.q=e.target.value.trim(); syncClear(); render(); });
$("#clear").onclick=()=>{ $("#q").value=""; state.q=""; syncClear(); render(); $("#q").focus(); };
$("#sort").addEventListener("change", e=>{ state.sort=e.target.value; render(); });
$("#reset").onclick=()=>{ state.cats.clear(); state.prs.clear();
  document.querySelectorAll(".chip.on").forEach(c=>c.classList.remove("on")); render(); };
document.addEventListener("keydown", e=>{
  if(e.key==="/" && document.activeElement!==$("#q")){ e.preventDefault(); $("#q").focus(); }
  if(e.key==="Escape" && document.activeElement===$("#q")){ $("#clear").click(); }
});
// テーマ
const root=document.documentElement;
const saved=localStorage.getItem("rw-theme"); if(saved) root.setAttribute("data-theme",saved);
$("#theme").onclick=()=>{ const d=root.getAttribute("data-theme")==="dark"?"light":"dark";
  root.setAttribute("data-theme",d); localStorage.setItem("rw-theme",d); };

render();
</script>
</body>
</html>
"""


def main() -> None:
    records = collect()
    data_json = json.dumps(records, ensure_ascii=False, separators=(",", ":"))
    # <script> 内に安全に埋め込むため </ と <script/<!-- を無害化（JSON としては等価）
    data_json = data_json.replace("</", "<\\/").replace("<!--", "<\\!--")
    out_html = TEMPLATE.replace("__DATA__", data_json)
    OUT.write_text(out_html, encoding="utf-8")
    n_paper = sum(1 for r in records if r["kind"] == "paper")
    n_topic = sum(1 for r in records if r["kind"] == "topic")
    n_model = sum(1 for r in records if r["kind"] == "model")
    print(f"生成: {OUT.relative_to(ROOT)}  （論文 {n_paper} / トピック {n_topic} / モデル {n_model} = 計 {len(records)} 件）")


if __name__ == "__main__":
    main()
