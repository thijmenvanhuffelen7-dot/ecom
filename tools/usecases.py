"""Genereert de use-case pagina's in /voor/. Draai: python3 tools/usecases.py
Pas teksten hieronder aan en draai opnieuw."""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

USECASES = [
  dict(slug="dropshippers", icon="📦", label="Dropshippers",
    title="Test meer producten. Verbrand minder budget.",
    lead="Als dropshipper win je door snel te testen. Merxa zet een nieuw product binnen een middag om in onderzoek, ads, een UGC-video en een productpagina, zodat jij alleen nog hoeft te beslissen wat blijft.",
    pains=[("Elke test kost dagen","Creatives laten maken, een pagina bouwen, wachten op een freelancer: tegen de tijd dat je live bent is de trend voorbij."),
           ("Creatives zijn duur","€150 voor een UGC-video die misschien niet werkt. Bij tien producten per maand tikt dat hard aan."),
           ("Te veel tabs, te weinig overzicht","Shopify, Ads Manager, spreadsheets en chats. Je weet niet meer welke test waar staat.")],
    helps=[("🔎","Productonderzoek in minuten","Merxa leest reviews en comments van vergelijkbare producten en vertelt welke pijnpunten en hoeken je moet testen."),
           ("🖼️","Testpakket per product","Per product 5–10 statische ads in alle formaten, gebouwd op je productfoto's."),
           ("🎬","UGC zonder creator","Een korte UGC-video met script en ondertitels, klaar voor TikTok en Reels."),
           ("⚡","Productpagina live","Een converterende pagina op je eigen domein, inclusief mobiele check.")],
    chat=[("jij","Nieuw product: magnetische telefoonhouder. Maak een testpakket."),
          ("merxa","Op zoek naar angles… 3 gevonden: 'nooit meer vallen', 'één hand rijden', 'past op elk dashboard'."),
          ("merxa","8 ads, 1 UGC-video en een productpagina staan klaar ter goedkeuring.")],
    plan="Starter of Growth", stat=("Van product naar test","< 1 dag")),
  dict(slug="media-buyers", icon="📈", label="Media buyers",
    title="Nooit meer wachten op creatives.",
    lead="Je campagnes zijn zo goed als de creatives die je krijgt. Merxa levert verse varianten op het moment dat je ze nodig hebt en houdt je accounts in de gaten terwijl jij slaapt.",
    pains=[("Creative fatigue","Een winnende ad zakt na een week in. Nieuwe varianten laten te lang op zich wachten."),
           ("Handmatig monitoren","Elke ochtend door Ads Manager scrollen om te zien wat is ingestort of juist knalt."),
           ("Rapporteren kost uren","Klanten willen weten waarom, niet alleen wat. Dat uitschrijven vreet tijd.")],
    helps=[("♻️","Iteraties op winnaars","Geef een winnende ad en Merxa maakt varianten met nieuwe hooks, visuals en formaten."),
           ("🚨","Alerts op je KPI's","Meldingen via Slack of WhatsApp zodra CPA, ROAS of spend buiten je grenzen gaat."),
           ("📊","Dagelijkse samenvatting","Wat schalen, wat pauzeren en waarom, in gewone taal."),
           ("🧪","Testplanning","Merxa stelt een testmatrix voor op basis van wat eerder werkte in het account.")],
    chat=[("jij","Ad #12 loopt goed. Maak 6 varianten met andere hooks."),
          ("merxa","6 varianten klaar. 2 met een probleem-hook, 2 met social proof, 2 met een prijsanker."),
          ("merxa","Let op: ad #7 zit 40% boven je CPA-limiet. Pauzeren?")],
    plan="Growth", stat=("Nieuwe variant","minuten")),
  dict(slug="freelancers", icon="🧑‍💻", label="Freelancers",
    title="Meer klanten bedienen zonder meer uren.",
    lead="Als freelancer verkoop je je tijd. Merxa neemt het uitvoerende werk over, zodat jij meer klanten aankunt en je tijd steekt in strategie en contact.",
    pains=[("Je uren zijn op","Nog een klant erbij betekent avonden en weekenden doorwerken."),
           ("Elke klant is anders","Andere merkstijl, andere doelgroep, andere tools. Schakelen kost energie."),
           ("Opleveren duurt te lang","Klanten verwachten snelheid, maar goed werk kost tijd.")],
    helps=[("🗂️","Aparte werkruimte per klant","Merxa onthoudt per klant de merkstijl, doelgroep en eerdere resultaten."),
           ("⚡","Snel eerste versies","Ads, pagina's en scripts als startpunt. Jij schaaft bij en levert op."),
           ("🧾","Rapportages","Overzichten die je zo naar je klant kunt sturen."),
           ("💶","Betere marge","Lever meer op tegen dezelfde tarieven, met lagere kosten per opdracht.")],
    chat=[("jij","Klant B: maak 3 landingspagina-varianten voor de zomeractie."),
          ("merxa","Gebruik ik de tone of voice van klant B uit vorige maand? Die converteerde 18% beter."),
          ("merxa","3 varianten klaar, plus een korte toelichting die je naar de klant kunt sturen.")],
    plan="Scale", stat=("Klanten per freelancer","2–3× meer")),
  dict(slug="dtc-merken", icon="🏷️", label="DTC-merken",
    title="Een marketingteam dat je merk echt kent.",
    lead="Je merk is je belangrijkste bezit. Merxa leert je stem, je klanten en wat verkoopt, en maakt daarmee content die voelt alsof je eigen team het maakte.",
    pains=[("Content kost een vermogen","Bureaus en fotoshoots vreten budget, terwijl je elke week nieuwe content nodig hebt."),
           ("Merk raakt verwaterd","Elke freelancer schrijft net anders. Je merk klinkt niet meer als één geheel."),
           ("Data zonder actie","Je hebt reviews, cijfers en klantvragen, maar niemand die er iets mee doet.")],
    helps=[("🧠","Brand memory","Tone of voice, kleuren, do's en don'ts: Merxa houdt zich eraan in alles wat het maakt."),
           ("💬","Voice of customer","Merxa leest je reviews en supportvragen en maakt er hooks en pagina's van."),
           ("🎬","Content op ritme","Een vaste stroom ads en UGC-video's per week, zonder fotoshoot."),
           ("🔗","Gekoppeld aan je stack","Shopify, Meta en Klaviyo, zodat Merxa ziet wat echt verkoopt.")],
    chat=[("jij","Wat zeggen klanten het vaakst over ons hardloopshirt?"),
          ("merxa","Top 3: 'droogt snel', 'geen schuurplekken', 'maat valt klein'. De eerste twee zijn sterke hooks."),
          ("merxa","Ik heb 4 ads gemaakt rond 'geen schuurplekken'. En zal ik een maattabel aan de productpagina toevoegen?")],
    plan="Growth of Scale", stat=("Content per week","10+ assets")),
  dict(slug="creative-strategists", icon="🎯", label="Creative strategists",
    title="Van inzicht naar creative in één flow.",
    lead="Jij bedenkt de hoeken, Merxa bouwt ze uit. Van onderzoek en briefing tot de eerste versie van elke creative, zodat jij meer ideeën kunt testen.",
    pains=[("Onderzoek is handwerk","Reviews lezen, comments doorspitten, concurrenten bijhouden: uren werk voor één briefing."),
           ("Briefings gaan verloren","Wat jij bedoelt komt er bij de maker anders uit."),
           ("Te weinig tests","Je hebt meer ideeën dan het team kan produceren.")],
    helps=[("🔍","Angle research","Merxa clustert reviews en comments tot motieven, bezwaren en hooks."),
           ("📝","Briefings in één klik","Gestructureerde briefs met hook, opbouw, visuele richting en CTA."),
           ("🎨","Direct prototypes","Elke briefing meteen als statische ad of UGC-storyboard."),
           ("📚","Learnings-bibliotheek","Wat werkte en waarom, doorzoekbaar en automatisch bijgewerkt.")],
    chat=[("jij","Geef me 5 angles voor ons slaapsupplement, gericht op jonge ouders."),
          ("merxa","1) 'Slapen als de baby slaapt' 2) 'Geen suf gevoel' 3) 'Natuurlijk'… inclusief bronquotes uit reviews."),
          ("merxa","Briefing en 2 prototypes per angle staan klaar.")],
    plan="Growth", stat=("Angles getest per maand","3× meer")),
]

def e(s): return html.escape(s, quote=True)

def nav(prefix, current=None):
    items = "".join(
        f'<a href="{prefix}voor/{u["slug"]}.html"{" class=\"cur\"" if u["slug"]==current else ""}><span>{u["icon"]}</span>{e(u["label"])}</a>'
        for u in USECASES)
    return f'''<header class="nav">
  <div class="wrap nav-inner">
    <a href="{prefix}index.html" class="logo"><span class="logo-mark">M</span>Merxa</a>
    <nav class="nav-links">
      <div class="dd"><button class="dd-btn" type="button">Use cases ▾</button><div class="dd-menu">{items}</div></div>
      <a href="{prefix}index.html#features">Functies</a>
      <a href="{prefix}index.html#how">Zo werkt het</a>
      <a href="{prefix}index.html#compare">Vergelijk</a>
      <a href="{prefix}index.html#pricing">Prijzen</a>
      <a href="{prefix}index.html#roadmap">Roadmap</a>
      <a href="{prefix}index.html#faq">FAQ</a>
    </nav>
    <div class="nav-cta">
      <a href="#" class="btn btn-ghost">Inloggen</a>
      <a href="{prefix}index.html#pricing" class="btn btn-primary">Start gratis</a>
    </div>
    <button class="burger" aria-label="Menu" onclick="document.body.classList.toggle('menu-open')">☰</button>
  </div>
</header>'''

def footer(prefix):
    uc = "".join(f'<a href="{prefix}voor/{u["slug"]}.html">{e(u["label"])}</a>' for u in USECASES)
    return f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div><a href="{prefix}index.html" class="logo"><span class="logo-mark">M</span>Merxa</a><p>De AI-operator voor e-commerce.</p><a class="contact-mail" data-mail hidden></a></div>
    <div><h4>Product</h4><a href="{prefix}index.html#features">Functies</a><a href="{prefix}index.html#how">Zo werkt het</a><a href="{prefix}index.html#pricing">Prijzen</a></div>
    <div><h4>Use cases</h4>{uc}</div>
    <div><h4>Bedrijf</h4><a href="#">Over ons</a><a href="#" data-mail-link>Contact</a><a href="#">Voorwaarden</a><a href="#">Privacy</a></div>
  </div>
  <p class="wrap copy">© <span id="yr"></span> Merxa. Alle rechten voorbehouden.</p>
</footer>'''

def page(u):
    p = "../"
    pains = "".join(f'<div class="pain"><span>✕</span><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a,b in u["pains"])
    helps = "".join(f'<article class="card"><div class="ic">{i}</div><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i,a,b in u["helps"])
    chat = "".join(f'<div class="msg {w}"><small>{"Jij" if w=="jij" else "Merxa"}</small>{e(t)}</div>' for w,t in u["chat"])
    others = "".join(f'<a class="uc" href="{o["slug"]}.html"><span class="uc-ic">{o["icon"]}</span><b>{e(o["label"])}</b><i>→</i></a>' for o in USECASES if o is not u)
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Merxa voor {e(u["label"].lower())} — {e(u["title"])}</title>
<meta name="description" content="{e(u["lead"])}">
<meta property="og:title" content="Merxa voor {e(u["label"].lower())}">
<meta property="og:description" content="{e(u["lead"])}">
<meta name="theme-color" content="#0b0d12">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}styles.css">
</head>
<body>
<!-- GEGENEREERD door tools/usecases.py — pas daar aan, niet hier -->
{nav(p, u["slug"])}
<main>
<section class="hero uc-hero">
  <div class="wrap hero-grid">
    <div>
      <a class="crumb" href="{p}index.html#usecases">← Alle use cases</a>
      <span class="pill"><span class="dot"></span>{u["icon"]} Voor {e(u["label"].lower())}</span>
      <h1>{e(u["title"])}</h1>
      <p class="lead">{e(u["lead"])}</p>
      <div class="hero-cta">
        <a href="{p}index.html#pricing" class="btn btn-primary btn-lg">Start gratis</a>
        <a href="#hoe" class="btn btn-ghost btn-lg">Zo helpt Merxa</a>
      </div>
      <div class="uc-stat"><small>{e(u["stat"][0])}</small><b class="grad">{e(u["stat"][1])}</b></div>
    </div>
    <div class="chat" aria-label="Voorbeeldgesprek met Merxa">
      <div class="dash-top"><span class="lights"><i></i><i></i><i></i></span><span class="dash-title">merxa / chat</span><span class="live">● online</span></div>
      <div class="chat-body">{chat}</div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Herkenbaar?</span><h2>Waar {e(u["label"].lower())} tegenaan lopen</h2></div>
    <div class="pains">{pains}</div>
  </div>
</section>

<section class="section" id="hoe">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Zo helpt Merxa</span><h2>Gebouwd voor jouw manier van werken</h2></div>
    <div class="cards cards-2">{helps}</div>
    <p class="plan-tip">Aanbevolen abonnement: <b>{e(u["plan"])}</b> · <a href="{p}index.html#pricing">Bekijk prijzen →</a></p>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Andere use cases</span><h2>Merxa werkt ook voor</h2></div>
    <div class="uc-grid uc-grid-4">{others}</div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>Klaar om te beginnen?</h2>
    <p>Zet je op de early-access lijst. Je hoort het als eerste zodra we live gaan.</p>
    <form class="wait" id="waitForm" novalidate>
      <input type="email" name="email" placeholder="jij@jouwshop.nl" required aria-label="E-mailadres">
      <button class="btn btn-light btn-lg" type="submit">Zet me op de lijst</button>
    </form>
    <p class="wait-msg" id="waitMsg" role="status"></p>
  </div>
</section>
</main>
{footer(p)}
<a href="{p}index.html#pricing" class="mobile-cta btn btn-primary">Start gratis</a>
<script src="{p}config.js"></script>
<script src="{p}main.js"></script>
</body>
</html>
'''

def home_section():
    cards = "".join(f'<a class="uc" href="voor/{u["slug"]}.html"><span class="uc-ic">{u["icon"]}</span><b>{e(u["label"])}</b><small>{e(u["title"])}</small><i>→</i></a>' for u in USECASES)
    return f'''<!-- USECASES:START (gegenereerd door tools/usecases.py) -->
<section id="usecases" class="section">
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Use cases</span>
      <h2>Voor iedereen die in e-commerce bouwt</h2>
      <p>Of je nu producten test, campagnes draait of een merk opbouwt: Merxa past zich aan jouw werk aan.</p>
    </div>
    <div class="uc-grid">{cards}</div>
  </div>
</section>
<!-- USECASES:END -->'''

if __name__ == "__main__":
    for u in USECASES:
        (ROOT/"voor"/f'{u["slug"]}.html').write_text(page(u), encoding="utf-8")
    idx = ROOT/"index.html"; s = idx.read_text(encoding="utf-8")
    import re
    s = re.sub(r'<!-- USECASES:START.*?<!-- USECASES:END -->', lambda m: home_section(), s, flags=re.S)
    s = re.sub(r'<header class="nav">.*?</header>', lambda m: nav(""), s, count=1, flags=re.S)
    s = re.sub(r'<footer class="foot">.*?</footer>', lambda m: footer(""), s, count=1, flags=re.S)
    # anchors on home: strip "index.html" so links stay on-page
    s = s.replace('href="index.html#', 'href="#')
    idx.write_text(s, encoding="utf-8")
    print("ok:", len(USECASES), "pagina's")
