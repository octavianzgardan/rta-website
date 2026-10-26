#!/usr/bin/env python3
# Genera tutto il sito statico. Uso: python3 _build/build.py  (dalla cartella del repository)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import SITE, UPDATED
import pages, guide

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def write(path, content):
    if path.endswith(".html"):
        f = os.path.join(ROOT, path.lstrip("/"))
    else:
        f = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(content)
    return f

indexable = []
def add(path, html, index=True):
    write(path, html)
    if index: indexable.append(path)

add("/", pages.home())
add("/prezzi/", pages.prezzi())
add("/responsabile-tecnico-esterno/", pages.rt_esterno())
add("/subentro-responsabile-tecnico/", pages.subentro())
add("/iscrizione-albo-gestori-ambientali/", pages.iscrizione())
add("/fir-digitale-xfir/", pages.fir())
add("/variazioni-albo/", pages.variazioni())
add("/categoria-6-trasporto-transfrontaliero/", pages.cat6())
add("/trasporto-raee/", pages.raee())
add("/settori/autospurghi/", pages.settore_autospurghi())
add("/settori/traslochi-sgomberi/", pages.settore_traslochi())
add("/chi-sono/", pages.chi_sono())
add("/contatti/", pages.contatti())
add("/preventivo/", pages.preventivo())
add("/privacy/", pages.privacy())
add("/area-clienti/", pages.area_clienti(), False)
add("/attiva/", pages.attiva(), False)
add("/404.html", pages.not_found(), False)

gs = guide.all_guides()
add("/guide/", guide.guide_index(gs))
for g in gs:
    p, h = guide.article_page(g["slug"], g["tag"], g["title"], g["desc"], g["date"], g["content"])
    add(p, h)

prio = {"/": "1.0", "/prezzi/": "0.9", "/responsabile-tecnico-esterno/": "0.9", "/subentro-responsabile-tecnico/": "0.9", "/fir-digitale-xfir/": "0.9"}
urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{UPDATED}</lastmod><priority>{prio.get(p, '0.7')}</priority></url>\n" for p in indexable)
open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nDisallow: /area-clienti/\nDisallow: /attiva/\n\nSitemap: {SITE}/sitemap.xml\n")
print(f"OK: {len(indexable)} pagine indicizzabili + 3 riservate")
