# Layout comune del sito. Le pagine stanno in pages.py e guide.py; si genera tutto con:  python3 _build/build.py
import json, html
from urllib.parse import quote

SITE = "https://responsabiletecnicoambientale.it"
PHONE = "347 291 5487"
TEL = "+393472915487"
EMAIL = "octavian@responsabiletecnicoambientale.it"
UPDATED = "2026-10-26"
UPDATED_IT = "26 ottobre 2026"

def wa(text="Ciao Octavian, ti scrivo dal sito. Mi serve un'informazione sul Responsabile Tecnico."):
    return "https://wa.me/393472915487?text=" + quote(text)

ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 004.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm5.8 14.03c-.24.68-1.42 1.32-1.96 1.36-.5.05-.97.23-3.28-.68-2.78-1.1-4.54-3.95-4.68-4.13-.14-.18-1.12-1.49-1.12-2.85 0-1.35.71-2.02.96-2.29.25-.27.55-.34.73-.34h.52c.17 0 .4-.06.62.47.24.55.8 1.92.87 2.06.07.14.11.3.02.48-.09.18-.14.3-.27.46-.14.16-.29.36-.41.48-.14.14-.28.29-.12.56.16.27.71 1.17 1.52 1.9 1.05.93 1.93 1.22 2.2 1.36.27.14.43.11.59-.07.16-.18.68-.79.86-1.06.18-.27.36-.23.61-.14.25.09 1.59.75 1.86.89.27.14.45.2.52.32.07.11.07.66-.17 1.33z"/></svg>'
ICON_TEL = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1C10.61 21 3 13.39 3 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1.02l-2.2 2.2z"/></svg>'
LOGO = '<svg viewBox="0 0 24 24"><path d="M17 8C8 10 5.9 16.17 3.82 19.3L5.71 21l1-1.3A4.49 4.49 0 008 20c4 0 4-2 8-2s4 2 8 2v-2c-4 0-4-2-8-2-1.17 0-2.09.17-2.88.36C14.08 12.82 17.41 10.34 21 9.14L17 8z"/></svg>'

def btn_wa(label="Scrivimi su WhatsApp", text=None, cls=""):
    return f'<a class="btn btn-wa {cls}" href="{wa(text) if text else wa()}" target="_blank" rel="noopener">{ICON_WA}{label}</a>'

def btn_call(label=None, cls=""):
    # Contatto solo via WhatsApp (Octavian è a lezione di giorno): niente pulsanti "Chiama"
    return ""

NAV = [
    ("/iscrizione-albo-gestori-ambientali/", "Iscrizione Albo"),
    ("/responsabile-tecnico-esterno/", "RT esterno"),
    ("/cambio-responsabile-tecnico/", "Cambio RT"),
    ("/fir-digitale-xfir/", "FIR digitale"),
    ("/preventivo/", "Preventivo"),
    ("/guide/", "Guide"),
    ("/chi-sono/", "Chi sono"),
]

def header(path):
    links = "".join(
        f'<a href="{u}"{" aria-current=page" if path.startswith(u) else ""}>{t}</a>' for u, t in NAV)
    return f'''<div class="topbar"><div class="wrap">
  <a class="tb-alert" href="/iscrizione-albo-gestori-ambientali/">Devi iscriverti all'Albo Gestori Ambientali? Ti seguo dall'inizio →</a>
  <span>WhatsApp: <a href="{wa()}" target="_blank" rel="noopener">{PHONE}</a> · risposta in giornata</span>
</div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="/"><span class="brand-logo">{LOGO}</span><span><span class="brand-name">Octavian Zgardan</span><br><span class="brand-role">Responsabile Tecnico Ambientale</span></span></a>
  <nav class="main" aria-label="Menu principale">{links}<a href="/contatti/">Contatti</a></nav>
  <div class="nav-cta">
    <a class="btn btn-wa btn-sm btn-sm-hide" href="{wa()}" target="_blank" rel="noopener">{ICON_WA}WhatsApp {PHONE}</a>
    <button class="menu-btn" aria-expanded="false" aria-label="Apri il menu">Menu</button>
  </div>
</div></header>'''

def footer():
    return f'''<footer class="site"><div class="wrap">
  <div class="cols">
    <div>
      <h4>Octavian Zgardan</h4>
      <p>Responsabile Tecnico Ambientale iscritto all'Albo Nazionale Gestori Ambientali, Cat. 1, 4 e 5, classe F. Iscrizioni all'Albo, RENTRI e FIR digitale per imprese di trasporto rifiuti in tutta Italia.</p>
      <p class="mt-1"><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div><h4>Servizi</h4>
      <a href="/iscrizione-albo-gestori-ambientali/">Iscrizione all'Albo</a>
      <a href="/responsabile-tecnico-esterno/">Responsabile Tecnico esterno</a>
      <a href="/cambio-responsabile-tecnico/">Cambio Responsabile Tecnico</a>
      <a href="/fir-digitale-xfir/">FIR digitale e RENTRI</a>
      <a href="/variazioni-albo/">Variazioni mezzi e codici EER</a>
    </div>
    <div><h4>Esempi e guide</h4>
      <a href="/settori/autospurghi/">Autospurghi</a>
      <a href="/settori/traslochi-sgomberi/">Traslochi e sgomberi</a>
      <a href="/settori/edilizia-demolizioni-strade/">Edilizia e demolizioni</a>
      <a href="/guide/">Tutte le guide</a>
      <a href="/guide/responsabile-tecnico-dimesso-30-giorni/">RT dimesso: cosa fare</a>
      <a href="/guide/fir-digitale-problemi-trasportatori/">Problemi con il FIR digitale</a>
    </div>
    <div><h4>Informazioni</h4>
      <a href="/preventivo/">Preventivo online</a>
      <a href="/contatti/">Check-up gratuito</a>
      <a href="/chi-sono/">Chi sono</a>
      <a href="/area-clienti/" rel="nofollow">Area clienti</a>
      <a href="/privacy/">Privacy</a>
    </div>
  </div>
  <div class="legal"><span>© 2026 Octavian Zgardan · Responsabile Tecnico Ambientale · Regime forfettario</span><span>Aggiornato il {UPDATED_IT}</span></div>
</div></footer>
<div class="mobile-bar">{btn_wa("Scrivimi su WhatsApp · " + PHONE)}</div>
<div id="cookie-banner" role="dialog" aria-label="Cookie"><span>Uso solo cookie tecnici e Google Fonts per i caratteri. Dettagli nella <a href="/privacy/">privacy</a>.</span><span><button class="acc" data-v="1">Ok, chiaro</button></span></div>'''

def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                                for i, (n, u) in enumerate(items)]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(strip_tags(a))}} for q, a in faqs]}

def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s).strip()

def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs) + "</div>"

def crumbs(items):
    parts = [f'<a href="{u}">{n}</a>' for n, u in items[:-1]] + [items[-1][0]]
    return '<div class="crumbs">' + " › ".join(parts) + "</div>"

def page(path, title, desc, body, schemas=(), noindex=False, extra_head="", scripts=""):
    canon = SITE + path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/octavian-zgardan.jpg">
<meta name="theme-color" content="#062019">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v=20261026">
{ld}{extra_head}
</head>
<body>
{header(path)}
<main>
{body}
</main>
{footer()}
<script src="/assets/site.js?v=20261026" defer></script>
{scripts}
</body>
</html>
'''

def cta_band(title="Vuoi sapere se la tua posizione all'Albo è in regola?",
             text="Check-up gratuito: controllo iscrizione, categorie, mezzi, scadenze, RT e RENTRI. Ti rispondo entro un giorno lavorativo, senza impegno.",
             wa_text="Ciao Octavian, vorrei il check-up gratuito della mia posizione all'Albo. La mia azienda è: "):
    return f'''<section class="s tight"><div class="wrap"><div class="cta-band">
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="cta-row">{btn_wa("Chiedi il check-up", wa_text)}{btn_call()}</div>
</div></div></section>'''

def page_hero(items, h1, lead, ctas=True, wa_text=None):
    c = f'<div class="cta-row">{btn_wa(text=wa_text) if wa_text else btn_wa()}{btn_call()}</div>' if ctas else ""
    return f'''<section class="page-hero"><div class="wrap">{crumbs(items)}<h1>{h1}</h1><p>{lead}</p>{c}</div></section>'''
