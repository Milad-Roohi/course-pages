#!/usr/bin/env python3
"""Publish an interactive HTML page to GitHub Pages and embed it in a Canvas Page.

  python3 tools/publish.py --src PATH.html --course mech223 --year 2026 --slug mp08 \
      --canvas-course 20760 --title "Muddiest Point 08 study guide (Mon Sep 21)" --module "Week 5" [--publish]

Steps: copy -> git commit/push -> wait until live on github.io -> Canvas Page (iframe + full-screen link)
-> add to the matching Canvas module. Without --publish the Canvas Page and module item stay unpublished.
Canvas token: ~/.canvas_unl_token (never stored in this repo).
"""
import argparse, json, shutil, subprocess, sys, time, urllib.parse, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SITE = "https://milad-roohi.github.io/course-pages"
CANVAS = "https://mynu.instructure.com"


def token():
    for line in (Path.home() / ".canvas_unl_token").read_text(encoding="utf-8-sig").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            return s[7:].strip() if s.lower().startswith("bearer ") else s
    sys.exit("no Canvas token")


def api(method, path, data=None, params=None):
    url = CANVAS + path + ("?" + urllib.parse.urlencode(params, doseq=True) if params else "")
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.loads(r.read() or b"null")
        link = r.headers.get("Link") or ""
    return out, link


def get_all(path, params=None):
    items, url_params = [], dict(params or {}, per_page=100)
    out, link = api("GET", path, params=url_params)
    items += out
    while 'rel="next"' in link:
        nxt = [p.split(";")[0].strip("<> ") for p in link.split(",") if 'rel="next"' in p][0]
        req = urllib.request.Request(nxt, headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            items += json.loads(r.read()); link = r.headers.get("Link") or ""
    return items


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], check=True, capture_output=True, text=True).stdout


def main():
    p = argparse.ArgumentParser()
    for a in ("--src", "--course", "--year", "--slug", "--canvas-course", "--title", "--module"):
        p.add_argument(a, required=a != "--module")
    p.add_argument("--publish", action="store_true")
    a = p.parse_args()
    rel = f"{a.course}/{a.year}/{a.slug}/index.html"
    dest = REPO / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    html = Path(a.src).read_text(encoding="utf-8")
    if 'name="robots"' not in html:
        html = html.replace("<head>", '<head>\n<meta name="robots" content="noindex, nofollow">', 1)
    dest.write_text(html, encoding="utf-8")
    git("add", rel)
    if git("status", "--porcelain", rel).strip():
        git("commit", "-m", f"{a.course} {a.year} {a.slug}: {a.title}")
        git("push", "origin", "HEAD")
        print("pushed", rel)
    else:
        print("no change in", rel)
    url = f"{SITE}/{a.course}/{a.year}/{a.slug}/"
    marker = html[-200:]
    for i in range(40):  # up to ~6.5 min for Pages to rebuild
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"Cache-Control": "no-cache"}), timeout=30) as r:
                live = r.read().decode("utf-8", "ignore")
            if marker.strip()[-120:] in live:
                print("live:", url); break
        except Exception:
            pass
        time.sleep(10)
    else:
        sys.exit(f"not live yet: {url} (re-run later; nothing posted to Canvas)")

    body = (f'<p><a href="{url}" target="_blank" rel="noopener">Open this page in a new tab (full screen; '
            f'3D figures you can rotate)</a></p>\n'
            f'<iframe src="{url}" title="{a.title}" width="100%" height="1400" '
            f'style="border:0;" loading="lazy" allowfullscreen="allowfullscreen"></iframe>')
    cid = a.canvas_course
    pages = get_all(f"/api/v1/courses/{cid}/pages", {"search_term": a.title})
    page = next((pg for pg in pages if pg.get("title") == a.title), None)
    payload = {"wiki_page": {"title": a.title, "body": body, "published": a.publish}}
    if page:
        page, _ = api("PUT", f"/api/v1/courses/{cid}/pages/{page['url']}", payload)
    else:
        page, _ = api("POST", f"/api/v1/courses/{cid}/pages", payload)
    saved, _ = api("GET", f"/api/v1/courses/{cid}/pages/{page['url']}")
    kept = url in (saved.get("body") or "") and "<iframe" in (saved.get("body") or "")
    print("canvas page:", saved.get("html_url"), "| published:", saved.get("published"), "| iframe kept by Canvas:", kept)
    if a.module:
        mods = get_all(f"/api/v1/courses/{cid}/modules")
        mod = next((m for m in mods if a.module.lower() in (m.get("name") or "").lower()), None)
        if not mod:
            print("module not found:", a.module)
        else:
            items = get_all(f"/api/v1/courses/{cid}/modules/{mod['id']}/items")
            if not any(it.get("page_url") == page["url"] for it in items):
                api("POST", f"/api/v1/courses/{cid}/modules/{mod['id']}/items",
                    {"module_item": {"title": a.title, "type": "Page", "page_url": page["url"], "published": a.publish}})
                print("added to module:", mod["name"])
            else:
                print("already in module:", mod["name"])


if __name__ == "__main__":
    TOKEN = token()
    main()
