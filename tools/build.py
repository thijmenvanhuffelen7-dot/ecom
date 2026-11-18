"""Bouwt alle pagina's van de site. Draai: python3 tools/build.py
Teksten staan in tools/content.py. index.html wordt alleen deels bijgewerkt
(menu, footer, topbalk en de blokken tussen <!-- X:START --> en <!-- X:END -->)."""
import html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from content import *  # noqa

ROOT = pathlib.Path(__file__).resolve().parent.parent
e = lambda s: html.escape(str(s), quote=True)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">'
PAGES = []  # voor sitemap

# ------------------------------------------------------------------ onderdelen
def topbar(p):
    return f'<div class="topbar" id="topbar"><span id="topbarText">Nieuw: Merxa maakt nu ook complete UGC-video\'s met AI-creators</span> <a id="topbarLink" href="{p}functies/ugc-videos.html">Bekijk →</a></div>'

def dd(label, items, p, cur, wide=False):
    links = "".join(
        f'<a href="{p}{href}"{" class=\"cur\"" if href==cur else ""}><span class="dd-ic">{ic}</span><span><b>{e(t)}</b><small>{e(s)}</small></span></a>'
        for href, ic, t, s in items)
    return f'<div class="dd"><button class="dd-btn" type="button">{label} ▾</button><div class="dd-menu{" dd-wide" if wide else ""}">{links}</div></div>'

def nav(p, cur=""):
    f = [(f"functies/{x['slug']}.html", x["icon"], x["label"], x["short"]) for x in FEATURES]
    u = [(f"voor/{x['slug']}.html", x["icon"], x["label"], x["short"]) for x in USECASES]
    t = [(f"gratis-tools/{x['slug']}.html", x["icon"], x["label"], x["short"]) for x in TOOLS]
    t.append(("gratis-tools/index.html", "🧰", "Alle gratis tools", "Bekijk het complete overzicht."))
    return f'''<header class="nav">
  <div class="wrap nav-inner">
    <a href="{p}index.html" class="logo"><span class="logo-mark">M</span>Merxa</a>
    <nav class="nav-links">
      {dd("Functies", f, p, cur, True)}
      {dd("Use cases", u, p, cur)}
      {dd("Gratis tools", t, p, cur)}
      <a href="{p}prijzen.html"{' class="cur"' if cur=="prijzen.html" else ""}>Prijzen</a>
      <a href="{p}blog/index.html"{' class="cur"' if cur.startswith("blog/") else ""}>Blog</a>
    </nav>
    <div class="nav-cta">
      <a href="#" class="btn btn-ghost">Inloggen</a>
      <a href="{p}prijzen.html" class="btn btn-primary">Start gratis</a>
    </div>
    <button class="burger" aria-label="Menu" onclick="document.body.classList.toggle('menu-open')">☰</button>
  </div>
</header>'''

def footer(p):
    col = lambda title, links: f'<div><h4>{title}</h4>' + "".join(f'<a href="{p}{h}">{e(t)}</a>' for h, t in links) + '</div>'
    return f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div><a href="{p}index.html" class="logo"><span class="logo-mark">M</span>Merxa</a><p>De AI-operator voor e-commerce.</p><a class="contact-mail" data-mail hidden></a></div>
    {col("Functies", [(f"functies/{x['slug']}.html", x["label"]) for x in FEATURES] + [("prijzen.html","Prijzen"),("index.html#roadmap","Roadmap")])}
    {col("Use cases", [(f"voor/{x['slug']}.html", x["label"]) for x in USECASES])}
    {col("Gratis tools", [(f"gratis-tools/{x['slug']}.html", x["label"]) for x in TOOLS])}
    {col("Bedrijf", [("over-ons.html","Over ons"),("blog/index.html","Blog"),("woordenlijst.html","Woordenlijst"),("affiliate.html","Affiliate"),("contact.html","Contact"),("voorwaarden.html","Voorwaarden"),("privacy.html","Privacy")])}
  </div>
  <p class="wrap copy">© <span id="yr"></span> Merxa. Alle rechten voorbehouden.</p>
</footer>'''

def cta(title="Klaar om te beginnen?"):
    return f'''<section class="cta">
  <div class="wrap">
    <h2>{e(title)}</h2>
    <p>Zet je op de early-access lijst. Je hoort het als eerste zodra we live gaan.</p>
    <form class="wait" id="waitForm" novalidate>
      <input type="email" name="email" placeholder="jij@jouwshop.nl" required aria-label="E-mailadres">
      <button class="btn btn-light btn-lg" type="submit">Zet me op de lijst</button>
    </form>
    <p class="wait-msg" id="waitMsg" role="status"></p>
  </div>
</section>'''

def head_section(eyebrow, h2, p=""):
    return f'<div class="head"><span class="eyebrow">{e(eyebrow)}</span><h2>{e(h2)}</h2>{f"<p>{e(p)}</p>" if p else ""}</div>'

def faq_html(items):
    return "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items)

def page(path, title, desc, body, extra_js=""):
    depth = path.count("/")
    p = "../" * depth
    PAGES.append(path)
    doc = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0b0d12">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{p}styles.css">
</head>
<body data-root="{p}">
<!-- GEGENEREERD door tools/build.py — pas tools/content.py aan, niet dit bestand -->
{topbar(p)}
{nav(p, path)}
<main>
{body}
</main>
{footer(p)}
<a href="{p}prijzen.html" class="mobile-cta btn btn-primary">Start gratis</a>
<script src="{p}config.js"></script>
<script src="{p}main.js"></script>{extra_js}
</body>
</html>
'''
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")

def link_cards(items, prefix, cls="uc-grid uc-grid-4"):
    return f'<div class="{cls}">' + "".join(
        f'<a class="uc" href="{prefix}{x["slug"]}.html"><span class="uc-ic">{x["icon"]}</span><b>{e(x["label"])}</b><i>→</i></a>' for x in items) + '</div>'

# ------------------------------------------------------------------ functies
def build_features():
    for f in FEATURES:
        pts = "".join(f'<article class="card"><div class="ic">✓</div><h3>{e(a)}</h3><p>{e(b)}</p></article>' for a, b in f["points"])
        steps = "".join(f'<li><b>{i}</b><p>{e(s)}</p></li>' for i, s in enumerate(f["steps"], 1))
        body = f'''<section class="hero uc-hero sub-hero">
  <div class="wrap narrow center">
    <a class="crumb" href="../index.html#features">← Alle functies</a>
    <span class="pill"><span class="dot"></span>{f["icon"]} {e(f["label"])}</span>
    <h1>{e(f["title"])}</h1>
    <p class="lead">{e(f["lead"])}</p>
    <div class="hero-cta center-row"><a href="../prijzen.html" class="btn btn-primary btn-lg">Start gratis</a><a href="#hoe" class="btn btn-ghost btn-lg">Zo werkt het</a></div>
  </div>
</section>
<section class="section alt"><div class="wrap">{head_section("Wat je krijgt", "Alles wat je nodig hebt")}<div class="cards cards-2">{pts}</div></div></section>
<section class="section" id="hoe"><div class="wrap">{head_section("Zo werkt het", "In drie stappen")}<ol class="steps steps-simple">{steps}</ol></div></section>
<section class="section alt"><div class="wrap">{head_section("Use cases", "Voor wie is dit?")}{link_cards(USECASES, "../voor/", "uc-grid")}</div></section>
<section class="section"><div class="wrap">{head_section("Meer functies", "Merxa kan nog meer")}{link_cards([x for x in FEATURES if x is not f], "", "uc-grid")}</div></section>
{cta()}'''
        page(f"functies/{f['slug']}.html", f"{f['label']} — Merxa", f["lead"], body)

# ------------------------------------------------------------------ use cases
def build_usecases():
    for u in USECASES:
        pains = "".join(f'<div class="pain"><span>✕</span><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in u["pains"])
        helps = "".join(f'<article class="card"><div class="ic">{i}</div><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, a, b in u["helps"])
        chat = "".join(f'<div class="msg {w}"><small>{"Jij" if w=="jij" else "Merxa"}</small>{e(t)}</div>' for w, t in u["chat"])
        body = f'''<section class="hero uc-hero">
  <div class="wrap hero-grid">
    <div>
      <a class="crumb" href="../index.html#usecases">← Alle use cases</a>
      <span class="pill"><span class="dot"></span>{u["icon"]} Voor {e(u["label"].lower())}</span>
      <h1>{e(u["title"])}</h1>
      <p class="lead">{e(u["lead"])}</p>
      <div class="hero-cta"><a href="../prijzen.html" class="btn btn-primary btn-lg">Start gratis</a><a href="#hoe" class="btn btn-ghost btn-lg">Zo helpt Merxa</a></div>
      <div class="uc-stat"><small>{e(u["stat"][0])}</small><b class="grad">{e(u["stat"][1])}</b></div>
    </div>
    <div class="chat" aria-label="Voorbeeldgesprek met Merxa">
      <div class="dash-top"><span class="lights"><i></i><i></i><i></i></span><span class="dash-title">merxa / chat</span><span class="live">● online</span></div>
      <div class="chat-body">{chat}</div>
    </div>
  </div>
</section>
<section class="section alt"><div class="wrap">{head_section("Herkenbaar?", f"Waar {u['label'].lower()} tegenaan lopen")}<div class="pains">{pains}</div></div></section>
<section class="section" id="hoe"><div class="wrap">{head_section("Zo helpt Merxa", "Gebouwd voor jouw manier van werken")}<div class="cards cards-2">{helps}</div>
<p class="plan-tip">Aanbevolen abonnement: <b>{e(u["plan"])}</b> · <a href="../prijzen.html">Bekijk prijzen →</a></p></div></section>
<section class="section alt"><div class="wrap">{head_section("Andere use cases", "Merxa werkt ook voor")}{link_cards([x for x in USECASES if x is not u], "")}</div></section>
{cta()}'''
        page(f"voor/{u['slug']}.html", f"Merxa voor {u['label'].lower()} — {u['title']}", u["lead"], body)

# ------------------------------------------------------------------ gratis tools
def build_tools():
    for t in TOOLS:
        fields = "".join(
            f'<label class="fld"><span>{e(lbl)}</span><span class="inp"><input type="number" inputmode="decimal" id="{fid}" value="{val}" step="{step}" min="0"><em>{e(unit)}</em></span></label>'
            for fid, lbl, val, unit, step in t["fields"])
        outs = "".join(
            f'<div class="{"save" if len(o) > 2 else ""}"><small>{e(o[1])}</small><b id="out-{o[0]}">–</b></div>' for o in t["outputs"])
        expl = "".join(f"<p>{x}</p>" for x in t["explain"])  # bevat bewust <b>-tags
        others = [x for x in TOOLS if x is not t]
        body = f'''<section class="hero sub-hero">
  <div class="wrap narrow center">
    <a class="crumb" href="index.html">← Alle gratis tools</a>
    <span class="pill"><span class="dot"></span>{t["icon"]} Gratis tool</span>
    <h1>{e(t["title"])}</h1>
    <p class="lead">{e(t["intro"])}</p>
  </div>
</section>
<section class="section tool-sec"><div class="wrap">
  <div class="calc" data-calc="{t["calc"]}">
    <div class="calc-in tool-in">{fields}</div>
    <div class="calc-out">{outs}<p class="fine" id="calcNote"></p></div>
  </div>
</div></section>
<section class="section alt"><div class="wrap narrow prose">
  <h2>Hoe werkt het?</h2>{expl}
  <h2>Veelgestelde vragen</h2>{faq_html(t["faq"])}
</div></section>
<section class="section"><div class="wrap">{head_section("Meer gratis tools", "Reken verder")}{link_cards(others, "")}</div></section>
{cta("Laat Merxa het werk doen")}'''
        page(f"gratis-tools/{t['slug']}.html", f"{t['title']} (gratis) — Merxa", t["intro"], body,
             '\n<script src="../calc.js"></script>')
    cards = "".join(
        f'<a class="uc" href="{x["slug"]}.html"><span class="uc-ic">{x["icon"]}</span><b>{e(x["title"])}</b><small>{e(x["intro"])}</small><i>→</i></a>' for x in TOOLS)
    body = f'''<section class="hero sub-hero"><div class="wrap narrow center">
  <span class="pill"><span class="dot"></span>🧰 Gratis tools</span>
  <h1>Gratis rekentools voor webshops</h1>
  <p class="lead">Snel je marge, ROAS, ROI en klantwaarde uitrekenen. Zonder account, en alles blijft in je eigen browser.</p>
</div></section>
<section class="section"><div class="wrap"><div class="uc-grid uc-grid-3">{cards}</div></div></section>
{cta()}'''
    page("gratis-tools/index.html", "Gratis tools voor webshops — Merxa", "Gratis rekentools voor e-commerce: ROAS break-even, winstmarge, ROI, klantwaarde en verkoopprijs.", body)

# ------------------------------------------------------------------ prijzen
def plan_cards(prefix):
    out = ""
    for pl in PLANS:
        feats = "".join(f"<li>{e(x)}</li>" for x in pl["feats"])
        out += f'''<div class="plan{" featured" if pl.get("featured") else ""}">{'<span class="badge">Populairst</span>' if pl.get("featured") else ""}
  <h3>{e(pl["name"])}</h3>
  <p class="price"><b data-m="{pl["m"]}" data-q="{pl["q"]}" data-y="{pl["y"]}">€{pl["m"]}</b>/mnd</p>
  <p class="pdesc">{e(pl["desc"])}</p>
  <ul>{feats}</ul>
  <a href="#" class="btn {"btn-primary" if pl.get("featured") else "btn-ghost"} btn-block">{e(pl["cta"])}</a>
</div>'''
    return out

def build_pricing():
    cell = lambda v: '<span class="yes">✓</span>' if v is True else ('<span class="no">–</span>' if v is False else e(v))
    rows = ""
    for grp, items in COMPARE:
        rows += f'<tr class="grp"><td colspan="4">{e(grp)}</td></tr>'
        rows += "".join(f'<tr><td>{e(n)}</td><td>{cell(a)}</td><td class="hl">{cell(b)}</td><td>{cell(c)}</td></tr>' for n, a, b, c in items)
    body = f'''<section class="hero sub-hero"><div class="wrap narrow center">
  <span class="pill"><span class="dot"></span>Prijzen</span>
  <h1>Eerlijke prijzen, zonder verrassingen</h1>
  <p class="lead">Kies het plan dat bij je past. AI-gebruik loopt via tegoed met een maximum dat je zelf instelt. Opzeggen kan altijd.</p>
</div></section>
<section class="section tool-sec"><div class="wrap">
  <div class="toggle" role="group" aria-label="Facturatie">
    <button class="on" data-bill="m">Maandelijks</button>
    <button data-bill="q">Per kwartaal <span>-10%</span></button>
    <button data-bill="y">Jaarlijks <span>-20%</span></button>
  </div>
  <div class="plans plans-4">{plan_cards("")}
    <div class="plan ent">
      <h3>Enterprise</h3>
      <p class="price"><b>Op maat</b></p>
      <p class="pdesc">Voor agencies en grote merken met veel shops of volume.</p>
      <ul><li>Onbeperkt shops en teamleden</li><li>Afspraken over volume en tegoed</li><li>Eigen Slack-kanaal</li><li>Hulp bij onboarding</li></ul>
      <a href="contact.html" class="btn btn-ghost btn-block">Neem contact op</a>
    </div>
  </div>
</div></section>
<section class="section alt"><div class="wrap">{head_section("Vergelijk", "Alle plannen naast elkaar")}
  <div class="table-wrap"><table class="cmp cmp-plans"><thead><tr><th></th><th>Starter</th><th class="hl">Growth</th><th>Scale</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>
<section class="section"><div class="wrap narrow">{head_section("FAQ", "Vragen over prijzen")}{faq_html(PRICING_FAQ)}</div></section>
{cta()}'''
    page("prijzen.html", "Prijzen — Merxa", "Bekijk de plannen van Merxa: Starter, Growth, Scale en Enterprise. Maandelijks, per kwartaal of jaarlijks.", body)

# ------------------------------------------------------------------ woordenlijst
def build_glossary():
    letters = sorted({t[0].upper() for t, _ in GLOSSARY})
    nav_l = "".join(f'<a href="#l-{l}">{l}</a>' for l in letters)
    items, cur = "", None
    for term, d in sorted(GLOSSARY, key=lambda x: x[0].lower()):
        l = term[0].upper()
        if l != cur:
            items += f'<h2 id="l-{l}" class="gl-letter">{l}</h2>'; cur = l
        items += f'<div class="gl" id="{e(term.lower().replace(" ", "-"))}"><h3>{e(term)}</h3><p>{e(d)}</p></div>'
    body = f'''<section class="hero sub-hero"><div class="wrap narrow center">
  <span class="pill"><span class="dot"></span>📖 Woordenlijst</span>
  <h1>E-commerce woordenlijst</h1>
  <p class="lead">Alle termen die je tegenkomt bij webshops en adverteren, in gewone taal uitgelegd.</p>
</div></section>
<section class="section tool-sec"><div class="wrap narrow"><div class="az">{nav_l}</div>{items}</div></section>
{cta()}'''
    page("woordenlijst.html", "E-commerce woordenlijst — Merxa", "ROAS, CPA, CLV, UGC en meer: alle e-commerce- en advertentietermen in gewone taal uitgelegd.", body)

# ------------------------------------------------------------------ blog
def build_blog():
    def nl_date(d):
        m = ["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
        y, mo, da = d.split("-"); return f"{int(da)} {m[int(mo)-1]} {y}"
    for post in POSTS:
        body = f'''<article class="section tool-sec post"><div class="wrap narrow prose">
  <a class="crumb" href="index.html">← Alle artikelen</a>
  <p class="post-meta"><span class="tag">{e(post["tag"])}</span> {nl_date(post["date"])} · {e(post["read"])} lezen</p>
  <h1>{e(post["title"])}</h1>
  {post["body"]}
</div></article>
{cta("Minder rekenen, meer verkopen")}'''
        page(f"blog/{post['slug']}.html", f"{post['title']} — Merxa blog", post["excerpt"], body)
    cards = "".join(
        f'<a class="post-card" href="{x["slug"]}.html"><span class="tag">{e(x["tag"])}</span><h3>{e(x["title"])}</h3><p>{e(x["excerpt"])}</p><small>{nl_date(x["date"])} · {e(x["read"])}</small></a>'
        for x in sorted(POSTS, key=lambda x: x["date"], reverse=True))
    body = f'''<section class="hero sub-hero"><div class="wrap narrow center">
  <span class="pill"><span class="dot"></span>✍️ Blog</span>
  <h1>Blog</h1>
  <p class="lead">Praktische tips over adverteren, creatives en webshopgroei.</p>
</div></section>
<section class="section tool-sec"><div class="wrap"><div class="posts">{cards}</div></div></section>
{cta()}'''
    page("blog/index.html", "Blog — Merxa", "Praktische artikelen over adverteren, creatives en het laten groeien van je webshop.", body)

# ------------------------------------------------------------------ bedrijf
def simple(path, title, desc, eyebrow, h1, lead, inner, note=""):
    n = f'<p class="draft">⚠️ {e(note)}</p>' if note else ""
    body = f'''<section class="hero sub-hero"><div class="wrap narrow center">
  <span class="pill"><span class="dot"></span>{e(eyebrow)}</span><h1>{e(h1)}</h1><p class="lead">{e(lead)}</p>
</div></section>
<section class="section tool-sec"><div class="wrap narrow prose">{n}{inner}</div></section>
{cta()}'''
    page(path, title, desc, body)

def build_company():
    simple("over-ons.html", "Over ons — Merxa", "Waarom we Merxa bouwen.", "Over ons",
      "Webshops verdienen een eerlijke kans", "We bouwen Merxa omdat goede marketing niet alleen voor grote merken met grote budgetten zou moeten zijn.",
      """<h2>Onze missie</h2>
<p>Een webshop starten is makkelijker dan ooit. Hem laten groeien niet. Wie wil adverteren, heeft onderzoek, creatives, video's en landingspagina's nodig, en dat kost tijd en geld die de meeste ondernemers niet hebben.</p>
<p>Merxa neemt dat werk over. Niet om ondernemers te vervangen, maar zodat zij zich kunnen richten op de beslissingen die er echt toe doen.</p>
<h2>Waar we in geloven</h2>
<ul><li><b>Jij houdt de controle.</b> Merxa doet voorstellen, jij beslist wat er live gaat.</li>
<li><b>Geen verrassingen.</b> Duidelijke prijzen en een limiet op je tegoed die jij instelt.</li>
<li><b>Jouw data is van jou.</b> Je kunt alles altijd exporteren of verwijderen.</li>
<li><b>Eerlijk over wat AI kan.</b> We beloven geen gouden bergen. We beloven dat je sneller kunt testen.</li></ul>""")
    simple("contact.html", "Contact — Merxa", "Neem contact op met Merxa.", "Contact",
      "Neem contact op", "Vragen, feedback of interesse in een Enterprise-plan? We horen graag van je.",
      """<div class="contact-box">
<div data-mail-block hidden><h2>Mail ons</h2><p>Stuur een e-mail naar <a data-mail></a>. We reageren meestal binnen één werkdag.</p></div>
<div data-mail-empty><h2>Binnenkort bereikbaar per e-mail</h2><p>Ons e-mailadres komt hier binnenkort te staan. Zet je in de tussentijd op de lijst hieronder, dan nemen we contact met je op.</p></div>
</div>""")
    simple("affiliate.html", "Affiliate — Merxa", "Verdien commissie door Merxa aan te raden.", "Affiliate",
      f"Verdien {AFFILIATE_PCT}% terugkerende commissie", "Raad Merxa aan bij andere ondernemers en verdien elke maand mee zolang zij klant blijven.",
      f"""<div class="steps-inline">
<div><b>1</b><h3>Meld je aan</h3><p>Zet je op de lijst onderaan deze pagina. We nemen contact op zodra het programma start.</p></div>
<div><b>2</b><h3>Deel je link</h3><p>Je krijgt een persoonlijke link die je kunt delen in je content, community of met klanten.</p></div>
<div><b>3</b><h3>Verdien mee</h3><p>Je ontvangt {AFFILIATE_PCT}% van het abonnement van iedereen die via jou klant wordt, zolang zij blijven.</p></div>
</div>
<h2>Voor wie?</h2>
<p>Voor creators, coaches, freelancers en agencies in e-commerce. Iedereen die ondernemers helpt hun webshop te laten groeien.</p>""",
      note="Concept: de voorwaarden van het affiliateprogramma zijn nog niet definitief.")
    legal_note = "Concept: deze tekst is een placeholder en geen juridisch advies. Laat de definitieve versie controleren voordat de site live gaat."
    simple("voorwaarden.html", "Algemene voorwaarden — Merxa", "Algemene voorwaarden van Merxa.", "Juridisch",
      "Algemene voorwaarden", "Laatst bijgewerkt: nog niet gepubliceerd.",
      """<h2>1. Over deze voorwaarden</h2><p>[Wie is de aanbieder: bedrijfsnaam, KvK-nummer, adres.]</p>
<h2>2. Het abonnement</h2><p>[Looptijd, verlenging, opzegging per maand/kwartaal/jaar.]</p>
<h2>3. Tegoed en gebruik</h2><p>[Hoe usage credits werken, het maximum dat de klant instelt, wat er met ongebruikt tegoed gebeurt.]</p>
<h2>4. Content en rechten</h2><p>[Wie eigenaar is van gemaakte content, verantwoordelijkheid voor wat de klant publiceert.]</p>
<h2>5. Aansprakelijkheid</h2><p>[Beperking van aansprakelijkheid.]</p>
<h2>6. Toepasselijk recht</h2><p>[Nederlands recht, bevoegde rechter.]</p>""", note=legal_note)
    simple("privacy.html", "Privacyverklaring — Merxa", "Hoe Merxa met je gegevens omgaat.", "Juridisch",
      "Privacyverklaring", "Laatst bijgewerkt: nog niet gepubliceerd.",
      """<h2>Welke gegevens we verzamelen</h2><p>[Bijv. e-mailadres bij aanmelding voor de wachtlijst, accountgegevens, gekoppelde shopdata.]</p>
<h2>Waarom</h2><p>[Doelen en grondslagen volgens de AVG.]</p>
<h2>Met wie we gegevens delen</h2><p>[Verwerkers, zoals hosting en AI-aanbieders.]</p>
<h2>Hoe lang we gegevens bewaren</h2><p>[Bewaartermijnen.]</p>
<h2>Jouw rechten</h2><p>[Inzage, correctie, verwijdering, bezwaar. Contact via het e-mailadres op de contactpagina.]</p>
<h2>Cookies</h2><p>Deze site gebruikt geen tracking-cookies. Je aanmelding voor de wachtlijst wordt alleen in je eigen browser onthouden totdat er een verzendadres is ingesteld.</p>""", note=legal_note)

# ------------------------------------------------------------------ homepage
def replace_block(s, name, content):
    pat = re.compile(rf'<!-- {name}:START.*?<!-- {name}:END -->', re.S)
    block = f'<!-- {name}:START (gegenereerd door tools/build.py) -->\n{content}\n<!-- {name}:END -->'
    if not pat.search(s):
        raise SystemExit(f"Marker {name} ontbreekt in index.html")
    return pat.sub(lambda m: block, s)

def build_home():
    idx = ROOT / "index.html"; s = idx.read_text(encoding="utf-8")
    s = re.sub(r'<div class="topbar"[^>]*>.*?</div>', lambda m: topbar(""), s, count=1, flags=re.S)
    s = re.sub(r'<header class="nav">.*?</header>', lambda m: nav(""), s, count=1, flags=re.S)
    s = re.sub(r'<footer class="foot">.*?</footer>', lambda m: footer(""), s, count=1, flags=re.S)
    s = re.sub(r'<body[^>]*>', '<body data-root="">', s, count=1)
    uc = "".join(f'<a class="uc" href="voor/{u["slug"]}.html"><span class="uc-ic">{u["icon"]}</span><b>{e(u["label"])}</b><small>{e(u["title"])}</small><i>→</i></a>' for u in USECASES)
    s = replace_block(s, "USECASES", f'''<section id="usecases" class="section">
  <div class="wrap">
    {head_section("Use cases", "Voor iedereen die in e-commerce bouwt", "Of je nu producten test, campagnes draait of een merk opbouwt: Merxa past zich aan jouw werk aan.")}
    <div class="uc-grid">{uc}</div>
  </div>
</section>''')
    fc = "".join(f'<a class="card card-link" href="functies/{f["slug"]}.html"><div class="ic">{f["icon"]}</div><h3>{e(f["label"])}</h3><p>{e(f["short"])}</p><span class="more">Meer over {e(f["label"].lower())} →</span></a>' for f in FEATURES)
    s = replace_block(s, "FEATURES", f'''<section id="features" class="section">
  <div class="wrap">
    {head_section("Functies", "Een heel marketingteam, in één dashboard", "Alles begint bij onderzoek naar je klanten. Daarna bouwt Merxa de creatives die op die inzichten inspelen.")}
    <div class="cards">{fc}</div>
  </div>
</section>''')
    tc = "".join(f'<a class="uc" href="gratis-tools/{t["slug"]}.html"><span class="uc-ic">{t["icon"]}</span><b>{e(t["label"])}</b><small>{e(t["short"])}</small><i>→</i></a>' for t in TOOLS)
    s = replace_block(s, "TOOLS", f'''<section id="tools" class="section alt">
  <div class="wrap">
    {head_section("Gratis tools", "Reken het zelf uit", "Gratis calculators voor je marge, ROAS en klantwaarde. Geen account nodig.")}
    <div class="uc-grid">{tc}</div>
  </div>
</section>''')
    s = replace_block(s, "PLANS", f'<div class="plans">{plan_cards("")}</div>')
    idx.write_text(s, encoding="utf-8")
    PAGES.insert(0, "index.html")

def build_sitemap():
    if not SITE_URL:
        return
    base = SITE_URL.rstrip("/")
    urls = "".join(f"<url><loc>{base}/{'' if p=='index.html' else p}</loc></url>" for p in PAGES)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")

if __name__ == "__main__":
    build_features(); build_usecases(); build_tools(); build_pricing(); build_glossary(); build_blog(); build_company(); build_home(); build_sitemap()
    print(f"ok: {len(PAGES)} pagina's")
