"""Alle teksten van de site. Pas hier aan en draai daarna: python3 tools/build.py"""

# Domein voor sitemap.xml (bijv. "https://www.merxa.nl"). Leeg = geen sitemap.
SITE_URL = ""

# Placeholder: commissie voor het affiliateprogramma (pas aan naar je echte aanbod).
AFFILIATE_PCT = 30

# ---------------------------------------------------------------- FUNCTIES
FEATURES = [
  dict(slug="klantonderzoek", icon="🔎", label="Klantonderzoek",
    short="Pijnpunten, wensen en koopmotieven uit reviews en comments.",
    title="Weet wat je klanten echt denken.",
    lead="Merxa leest reviews, comments, supportvragen en concurrenten, en maakt daar heldere inzichten en testbare angles van. Elke ad en pagina begint hier.",
    points=[("Reviews en comments","Van je eigen shop, van marketplaces en uit de comments onder ads in je niche."),
            ("Angles met bewijs","Elke angle komt met echte citaten van klanten, zodat je weet waar hij vandaan komt."),
            ("Bezwaren in kaart","Waarom twijfelen mensen? Merxa zet de grootste bezwaren op een rij, met een antwoord erbij."),
            ("Altijd up-to-date","Nieuwe reviews komen er automatisch bij. Je onderzoek veroudert niet.")],
    steps=["Koppel je shop of plak een productlink","Merxa verzamelt en clustert alles wat klanten zeggen","Je krijgt een rapport met angles, hooks en bezwaren"]),
  dict(slug="ugc-videos", icon="🎬", label="UGC-video's",
    short="Script, AI-creator, scènes en ondertitels in één flow.",
    title="UGC-video's zonder creators in te huren.",
    lead="Merxa schrijft het script, kiest een vaste AI-creator en bouwt elke scène met jouw product erin. Jij keurt het storyboard goed voordat er iets gerenderd wordt.",
    points=[("Script op basis van onderzoek","Hooks en opbouw komen uit wat je klanten echt zeggen, niet uit een standaardtemplate."),
            ("Vaste creator","Dezelfde AI-creator in elke video, zodat je merk herkenbaar blijft."),
            ("Storyboard eerst","Je ziet elke scène voordat de video gemaakt wordt. Pas aan wat je wil."),
            ("Klaar voor elk platform","9:16 voor TikTok en Reels, 4:5 en 1:1 voor de feed, met ondertitels.")],
    steps=["Kies een product en een angle","Keur het script en storyboard goed","Download de video in alle formaten"]),
  dict(slug="ad-creatives", icon="🖼️", label="Ad creatives",
    short="Statische ads met je echte productfoto's, in elk formaat.",
    title="Statische ads die op je merk lijken.",
    lead="Merxa kiest een angle uit het onderzoek, schrijft de copy en maakt kant-en-klare ads met je echte productfoto's. Jij kiest welke live gaan.",
    points=[("Echte productfoto's","Geen nepproducten: Merxa bouwt de ad rond jouw eigen beelden."),
            ("Varianten per angle","Meerdere hooks, layouts en CTA's per angle om tegen elkaar te testen."),
            ("Alle formaten","1:1, 4:5 en 9:16 in één keer, klaar voor Meta en TikTok."),
            ("Goedkeuren met één klik","Goed? Bewaren. Niet goed? Weggooien, of Merxa laten aanpassen.")],
    steps=["Upload je productfoto's","Kies de angles die je wil testen","Keur goed en download of zet klaar voor je ads"]),
  dict(slug="landingspaginas", icon="⚡", label="Landingspagina's",
    short="Van één chatbericht naar een live pagina op je domein.",
    title="Landingspagina's in minuten, niet in weken.",
    lead="Vraag om een pagina en Merxa doet de rest: tekst, opbouw, beelden en een check op mobiel. Daarna zet je hem met één klik live op je eigen domein.",
    points=[("Copy die verkoopt","Gebaseerd op de angles en bezwaren uit je klantonderzoek."),
            ("Mobiel eerst","Elke pagina wordt gecontroleerd op mobiel, waar de meeste bezoekers zitten."),
            ("Op je eigen domein","Geen vreemde links: de pagina staat gewoon onder jouw merk."),
            ("Snel varianten testen","Maak een tweede versie met een andere hook en vergelijk.")],
    steps=["Beschrijf wat de pagina moet doen","Bekijk en pas de eerste versie aan","Publiceer op je domein"]),
  dict(slug="campagne-inzicht", icon="📈", label="Campagne-inzicht",
    short="Dagelijks advies: wat opschalen, wat stoppen.",
    title="Je campagnes in de gaten, ook als jij slaapt.",
    lead="Merxa kijkt elke dag naar je advertentiecijfers en vertelt in gewone taal wat er gebeurt, wat je moet opschalen en wat je beter kunt stoppen.",
    points=[("Dagelijkse samenvatting","Een kort overzicht via dashboard, Slack of WhatsApp."),
            ("Grenzen die jij bepaalt","Stel je maximale CPA of minimale ROAS in en krijg een melding als het misgaat."),
            ("Uitleg, niet alleen cijfers","Merxa vertelt waarom iets gebeurt, bijvoorbeeld creative fatigue of een duurdere doelgroep."),
            ("Van inzicht naar actie","Een ad zakt in? Merxa stelt meteen nieuwe varianten voor.")],
    steps=["Koppel je advertentieaccounts","Stel je doelen en grenzen in","Ontvang elke dag advies en alerts"]),
  dict(slug="merkgeheugen", icon="🧠", label="Merkgeheugen",
    short="Onthoudt je stijl, doelgroep en wat eerder werkte.",
    title="Een AI die je merk niet vergeet.",
    lead="Merxa onthoudt je tone of voice, kleuren, doelgroep en de resultaten van eerdere tests. Hoe langer je het gebruikt, hoe beter het werk wordt.",
    points=[("Tone of voice","Schrijft zoals jouw merk praat, inclusief woorden die je juist niet wil gebruiken."),
            ("Huisstijl","Kleuren, lettertypes en logo worden automatisch toegepast."),
            ("Learnings","Wat werkte en wat niet, bewaard en meegenomen in nieuwe taken."),
            ("Leert van feedback","Elke keer dat je iets afkeurt of aanpast, onthoudt Merxa waarom.")],
    steps=["Vul je merkprofiel in, of laat Merxa je site lezen","Geef feedback op wat Merxa maakt","Merxa past alles daarna automatisch toe"]),
]

# ---------------------------------------------------------------- USE CASES
USECASES = [
  dict(slug="dropshippers", icon="📦", label="Dropshippers",
    short="Test meer producten met minder budget.",
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
    short="Verse creatives en alerts op je KPI's.",
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
    short="Meer klanten bedienen zonder meer uren.",
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
    short="Content op ritme die klinkt als je merk.",
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
    short="Van inzicht naar briefing naar prototype.",
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

# ---------------------------------------------------------------- GRATIS TOOLS
# Velden: (id, label, standaardwaarde, eenheid, stap). Formules staan in calc.js.
TOOLS = [
  dict(slug="roas-break-even-calculator", calc="roas", icon="🎯", label="ROAS break-even",
    short="Bij welke ROAS en CPA maak je geen verlies?",
    title="ROAS break-even calculator",
    intro="Bereken bij welke ROAS je quitte speelt en hoeveel je maximaal per bestelling aan ads kunt uitgeven.",
    fields=[("price","Verkoopprijs (incl. btw)",39.95,"€",0.01),("vat","Btw",21,"%",1),("cogs","Inkoopprijs product",9,"€",0.01),
            ("ship","Verzendkosten per order",5,"€",0.01),("fees","Betaal- en platformkosten",2.9,"%",0.1),("other","Overige kosten per order",1,"€",0.01)],
    outputs=[("margin","Marge per order (vóór ads)"),("beroas","Break-even ROAS",True),("becpa","Maximale CPA")],
    explain=["Je <b>ROAS</b> (Return On Ad Spend) is je omzet gedeeld door je advertentiekosten. Een ROAS van 3 betekent dat je €3 omzet maakt per €1 aan ads.",
             "Je <b>break-even ROAS</b> is het punt waarop je ads precies je marge opeten. Zit je daarboven, dan verdien je geld. Zit je eronder, dan betaal je toe.",
             "We rekenen met omzet inclusief btw, omdat advertentieplatformen ook zo rapporteren. De btw zelf is geen winst en halen we daarom van je marge af."],
    faq=[("Wat is een goede ROAS?","Dat hangt volledig af van je marge. Met een hoge marge kan een ROAS van 1,5 al winstgevend zijn, met een lage marge heb je soms 4 of meer nodig. Daarom is je eigen break-even belangrijker dan een gemiddelde."),
         ("Wat is het verschil tussen ROAS en CPA?","ROAS kijkt naar omzet per uitgegeven euro. CPA is wat je betaalt voor één bestelling. Ze zeggen hetzelfde vanuit een andere hoek.")]),
  dict(slug="winstmarge-calculator", calc="margin", icon="💶", label="Winstmarge",
    short="Wat houd je echt over per verkocht product?",
    title="Winstmarge calculator",
    intro="Zie in één oogopslag wat je per bestelling echt overhoudt na inkoop, verzending, kosten, btw en ads.",
    fields=[("price","Verkoopprijs (incl. btw)",49.95,"€",0.01),("vat","Btw",21,"%",1),("cogs","Inkoopprijs product",12,"€",0.01),
            ("ship","Verzendkosten per order",5.5,"€",0.01),("fees","Betaal- en platformkosten",2.9,"%",0.1),("ads","Advertentiekosten per order",10,"€",0.01)],
    outputs=[("ex","Omzet excl. btw"),("net","Nettowinst per order",True),("pct","Nettomarge"),("markup","Opslag op inkoop")],
    explain=["<b>Brutomarge</b> is je verkoopprijs min je inkoop. <b>Nettomarge</b> is wat er overblijft als alle kosten eraf zijn: verzending, betaalkosten en ads.",
             "<b>Opslag</b> (markup) is iets anders dan marge: het zegt hoeveel procent je bovenop je inkoopprijs vraagt. Een opslag van 100% is een marge van 50%.",
             "Veel webshops sturen op brutomarge en schrikken aan het eind van de maand. Reken daarom altijd met je advertentiekosten per order erbij."],
    faq=[("Wat is een gezonde nettomarge voor een webshop?","Veel webshops mikken op 15–30% nettomarge, maar dat verschilt sterk per niche en per model. Dropshipping zit vaak lager, eigen merken hoger."),
         ("Moet ik btw meerekenen?","Ja. Btw ontvang je wel, maar draag je af. Het is dus geen omzet voor jou, en je marge moet je berekenen over de prijs zonder btw.")]),
  dict(slug="roi-calculator", calc="roi", icon="📊", label="ROI",
    short="Levert je investering genoeg op?",
    title="ROI calculator",
    intro="Bereken je rendement op een campagne, een productlancering of elke andere investering.",
    fields=[("inv","Investering",2000,"€",1),("ret","Opbrengst (winst vóór investering)",3200,"€",1),("months","Looptijd",3,"maanden",1)],
    outputs=[("profit","Nettoresultaat"),("roi","ROI",True),("monthly","Resultaat per maand")],
    explain=["<b>ROI</b> (Return On Investment) laat zien hoeveel je terugverdient ten opzichte van wat je erin stopt: (opbrengst − investering) ÷ investering.",
             "Gebruik als opbrengst de winst die de investering oplevert, niet de omzet. Anders lijkt een campagne beter dan hij is.",
             "Een ROI van 0% betekent dat je je geld precies terugverdient. Alles daarboven is winst."],
    faq=[("Wat is het verschil tussen ROI en ROAS?","ROAS kijkt alleen naar omzet ten opzichte van advertentiekosten. ROI kijkt naar echte winst ten opzichte van de totale investering, dus ook productkosten en andere uitgaven.")]),
  dict(slug="klantwaarde-calculator", calc="clv", icon="🔁", label="Klantwaarde (CLV)",
    short="Hoeveel is één klant je waard over de tijd?",
    title="Customer lifetime value calculator",
    intro="Bereken wat een klant je gemiddeld oplevert over de hele relatie, en hoeveel je mag uitgeven om er een binnen te halen.",
    fields=[("aov","Gemiddelde orderwaarde (excl. btw)",45,"€",0.01),("freq","Bestellingen per jaar",2.5,"×",0.1),
            ("years","Jaren klant",2,"jaar",0.5),("gm","Brutomarge",55,"%",1)],
    outputs=[("rev","Omzet per klant"),("clv","Winst per klant (CLV)",True),("cac","Max. acquisitiekosten (CAC)")],
    explain=["<b>Customer lifetime value</b> (CLV) is de totale winst die een klant oplevert zolang hij bij je koopt.",
             "Ken je je CLV, dan weet je hoeveel een nieuwe klant mag kosten. Een veelgebruikte vuistregel is dat je CAC maximaal een derde van je CLV is. Die vuistregel gebruiken we hier.",
             "Webshops met veel herhaalaankopen kunnen daardoor op de eerste bestelling verlies accepteren, omdat ze het later terugverdienen."],
    faq=[("Hoe verhoog ik mijn CLV?","Door mensen vaker te laten bestellen (e-mailflows, abonnementen), meer per bestelling te laten kopen (bundels, upsells) of langer klant te houden (goede service).")]),
  dict(slug="verkoopprijs-calculator", calc="price", icon="🏷️", label="Verkoopprijs",
    short="Welke prijs heb je nodig voor je doelmarge?",
    title="Verkoopprijs calculator",
    intro="Vul je kosten en je gewenste marge in en zie welke verkoopprijs je nodig hebt.",
    fields=[("cogs","Inkoopprijs product",10,"€",0.01),("ship","Verzendkosten per order",5,"€",0.01),("ads","Verwachte advertentiekosten per order",12,"€",0.01),
            ("fees","Betaal- en platformkosten",2.9,"%",0.1),("target","Gewenste nettomarge",20,"%",1),("vat","Btw",21,"%",1)],
    outputs=[("ex","Prijs excl. btw"),("incl","Verkoopprijs incl. btw",True),("profit","Winst per order")],
    explain=["Veel webshops prijzen hun producten door de inkoopprijs keer drie te doen. Dat werkt niet meer zodra je adverteert: dan moet je ook je advertentiekosten per order terugverdienen.",
             "Deze calculator rekent terug vanaf de marge die je wil overhouden. Zo zie je direct of een product haalbaar is.",
             "Komt er een prijs uit die veel hoger is dan je concurrenten? Dan moet je je kosten omlaag krijgen of een sterker aanbod maken, bijvoorbeeld een bundel."],
    faq=[("Waarom eindigen prijzen vaak op ,95 of ,99?","Mensen lezen prijzen van links naar rechts, dus €29,95 voelt merkbaar goedkoper dan €30. Rond daarom af naar een prijs die bij je merk past.")]),
]

# ---------------------------------------------------------------- PRIJZEN
PLANS = [
  dict(name="Starter", m=49, q=44, y=39, desc="Voor shops die net beginnen met adverteren.",
       feats=["Klantonderzoek","Statische ads","1 gekoppelde shop","Chat via WhatsApp"], cta="Kies Starter"),
  dict(name="Growth", m=99, q=89, y=79, desc="Alles wat je nodig hebt om op te schalen.", featured=True,
       feats=["Alles uit Starter","UGC-video's","Landingspagina's","Campagne-inzicht","€40 starttegoed"], cta="Kies Growth"),
  dict(name="Scale", m=249, q=224, y=199, desc="Voor merken met meerdere shops of markten.",
       feats=["Alles uit Growth","Tot 5 shops","3 teamleden","Persoonlijke support"], cta="Kies Scale"),
]
# Vergelijkingstabel: (groep, [(functie, starter, growth, scale)])  True=✓ False=–
COMPARE = [
  ("Onderzoek", [("Klantonderzoek",True,True,True),("Concurrentieanalyse",False,True,True),("Automatisch bijwerken",False,True,True)]),
  ("Creatie", [("Statische ads","20 / mnd","Onbeperkt","Onbeperkt"),("UGC-video's",False,"10 / mnd","40 / mnd"),
               ("Landingspagina's",False,"5 / mnd","Onbeperkt"),("Merkgeheugen",True,True,True)]),
  ("Groei", [("Campagne-inzicht",False,True,True),("KPI-alerts",False,True,True),("Testplanning",False,False,True)]),
  ("Account", [("Gekoppelde shops","1","1","5"),("Teamleden","1","1","3"),("Chat via WhatsApp/Slack",True,True,True),
               ("Support","Community","E-mail","Persoonlijk")]),
]
PRICING_FAQ = [
  ("Wat zijn usage credits?","Sommige taken, zoals video's renderen, kosten rekenkracht. Dat betaal je met tegoed. Je stelt zelf een maximum in, zodat je nooit voor verrassingen komt te staan."),
  ("Kan ik later van plan wisselen?","Ja, je kunt altijd op- of afschalen. Het verschil wordt naar rato verrekend."),
  ("Is er een proefperiode?","Je start met €40 gratis tegoed op het Growth-plan, zodat je Merxa eerst kunt uitproberen."),
  ("Kan ik maandelijks opzeggen?","Ja. Maandabonnementen zijn per maand opzegbaar. Kwartaal- en jaarplannen lopen tot het einde van de periode door."),
]

# ---------------------------------------------------------------- WOORDENLIJST
GLOSSARY = [
  ("AOV","Average order value: de gemiddelde waarde van een bestelling. Omzet gedeeld door het aantal bestellingen."),
  ("Angle","De invalshoek van een advertentie: welk probleem, verlangen of argument je centraal zet."),
  ("Break-even ROAS","De ROAS waarbij je precies quitte speelt: je ads kosten evenveel als je marge."),
  ("CAC","Customer acquisition cost: wat het je gemiddeld kost om één nieuwe klant binnen te halen."),
  ("CLV","Customer lifetime value: de totale winst die een klant oplevert zolang hij bij je koopt."),
  ("CPA","Cost per acquisition: wat je betaalt voor één conversie, zoals een bestelling."),
  ("CPM","Cost per mille: wat je betaalt voor duizend vertoningen van je advertentie."),
  ("CTR","Click-through rate: het percentage mensen dat op je advertentie klikt nadat ze hem zien."),
  ("Conversieratio","Het percentage bezoekers dat een bestelling plaatst."),
  ("Creative fatigue","Wanneer een advertentie slechter gaat presteren omdat je doelgroep hem te vaak heeft gezien."),
  ("DTC","Direct-to-consumer: een merk dat rechtstreeks aan consumenten verkoopt, zonder winkels ertussen."),
  ("Dropshipping","Een model waarbij je producten verkoopt die een leverancier direct naar je klant verstuurt, zonder eigen voorraad."),
  ("Hook","De eerste seconden of zin van een advertentie, bedoeld om de aandacht te pakken."),
  ("Landingspagina","Een pagina speciaal gemaakt om bezoekers uit een advertentie te laten converteren."),
  ("Media buyer","Iemand die advertentiebudget inkoopt en campagnes beheert, bijvoorbeeld op Meta of TikTok."),
  ("ROAS","Return on ad spend: omzet gedeeld door advertentiekosten."),
  ("ROI","Return on investment: (opbrengst − investering) gedeeld door de investering."),
  ("UGC","User generated content: content die eruitziet alsof een gewone klant hem gemaakt heeft, zoals een review-video."),
]

# ---------------------------------------------------------------- BLOG
POSTS = [
  dict(slug="wat-is-een-goede-roas", date="2026-11-10", read="4 min", tag="Advertenties",
    title="Wat is een goede ROAS? Zo bereken je je eigen grens",
    excerpt="Een ROAS van 3 klinkt goed, maar kan alsnog verlies zijn. Zo bepaal je welke ROAS jij nodig hebt.",
    body="""
<p>"Wat is een goede ROAS?" is waarschijnlijk de meest gestelde vraag onder webshop-eigenaren die adverteren. Het eerlijke antwoord: dat hangt af van je marge. Een ROAS die voor de ene shop winst oplevert, is voor de andere een verliespost.</p>
<h2>ROAS in het kort</h2>
<p>ROAS staat voor <i>return on ad spend</i>: je omzet gedeeld door wat je aan advertenties uitgeeft. Geef je €1.000 uit en verkoop je voor €3.000, dan is je ROAS 3.</p>
<p>Het probleem: die €3.000 is omzet, geen winst. Daar gaan nog btw, inkoop, verzending en betaalkosten vanaf.</p>
<h2>Begin bij je marge</h2>
<p>Stel, je verkoopt een product voor €40 inclusief btw. Na btw blijft er €33,06 over. Je inkoop is €10, verzending €5 en betaalkosten ongeveer €1,20. Dan houd je per bestelling zo'n €16,86 over vóór advertentiekosten.</p>
<p>Dat bedrag is je <b>maximale CPA</b>: meer mag één bestelling je aan ads niet kosten, anders lever je in.</p>
<h2>Van marge naar break-even ROAS</h2>
<p>Je break-even ROAS bereken je zo: verkoopprijs ÷ marge per order. In het voorbeeld is dat €40 ÷ €16,86 ≈ 2,37. Haal je een ROAS van 2,37, dan speel je quitte. Alles daarboven is winst.</p>
<p>Verkoop je hetzelfde product met €25 inkoop, dan zakt je marge naar €1,86 en heb je ineens een ROAS van ruim 21 nodig. Hetzelfde product, een totaal ander verhaal.</p>
<h2>Wat je hiermee doet</h2>
<ul>
<li><b>Ken je getal.</b> Bereken voor elk product je break-even ROAS en zet die naast je campagnes.</li>
<li><b>Verhoog je marge</b> voordat je meer budget uitgeeft. Bundels en upsells verhogen je orderwaarde zonder dat je advertentiekosten meestijgen.</li>
<li><b>Kijk verder dan de eerste bestelling.</b> Komen klanten terug? Dan kun je een lagere ROAS accepteren bij de eerste aankoop.</li>
</ul>
<p>Wil je het snel uitrekenen? Gebruik onze gratis <a href="../gratis-tools/roas-break-even-calculator.html">ROAS break-even calculator</a>.</p>
"""),
  dict(slug="hookstructuren-voor-ugc-ads", date="2026-11-03", read="5 min", tag="Creatives",
    title="6 hookstructuren om te testen in je volgende UGC-ad",
    excerpt="De eerste drie seconden bepalen of iemand blijft kijken. Zes structuren die je direct kunt testen.",
    body="""
<p>Bij een UGC-video beslist je kijker in de eerste seconden of hij doorscrolt. Daarom loont het om niet één hook te maken, maar meerdere structuren tegen elkaar te testen. Hieronder zes vormen waarmee je kunt beginnen.</p>
<h2>1. Het herkenbare probleem</h2>
<p>Open met een situatie die je doelgroep direct herkent. Hoe specifieker, hoe beter. "Ik heb last van mijn rug" is vaag. "Elke ochtend sta ik krom op na een nacht op dit matras" is beeldend.</p>
<h2>2. Het onverwachte resultaat</h2>
<p>Begin met het eindresultaat en laat de kijker zich afvragen hoe dat kan. Laat daarna pas het product zien.</p>
<h2>3. De tegenspraak</h2>
<p>Ga in tegen wat mensen denken: "Je hoeft niet elke dag te sporten om fitter te worden." Zo prikkel je nieuwsgierigheid, maar zorg dat je de claim ook echt kunt onderbouwen.</p>
<h2>4. De vergelijking</h2>
<p>Laat een voor- en na-situatie zien, of jouw product naast het alternatief. Visueel en snel te begrijpen, ook zonder geluid.</p>
<h2>5. De vraag</h2>
<p>Stel een vraag waar je doelgroep "ja" op antwoordt. "Ben jij ook zo klaar met kabels die altijd in de knoop zitten?" Het werkt omdat de kijker zich direct aangesproken voelt.</p>
<h2>6. De ervaring van een klant</h2>
<p>Gebruik letterlijk de woorden uit een echte review. Die klinken bijna altijd natuurlijker dan wat een copywriter bedenkt. Kies reviews die een duidelijk probleem en resultaat noemen.</p>
<h2>Zo test je het</h2>
<p>Houd de rest van de video gelijk en verander alleen de hook. Zo weet je zeker dat een verschil in resultaat door de opening komt. Kijk vooral naar hoeveel mensen na drie seconden nog kijken, niet alleen naar klikken.</p>
<p>Zoek je inspiratie? Onze gratis tools helpen je verder met de cijfers, zoals de <a href="../gratis-tools/winstmarge-calculator.html">winstmarge calculator</a>.</p>
"""),
]
