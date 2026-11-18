# Merxa — website

Statische site (HTML/CSS/JS). Geen server, geen build-tools, geen kosten.

## Instellingen — `config.js`
- `contactEmail` — contact-e-mail. Leeg = contactlinks gaan naar de wachtlijst.
- `waitlistEndpoint` — URL voor het wachtlijstformulier (bijv. gratis Formspree/Tally). **Leeg = er wordt niets verstuurd.**
- `demoVideoUrl` — YouTube-link of .mp4 voor de knop "Bekijk demo". Leeg = knop verborgen.
- `promo` — actiebalk met afteller. Zet `enabled: true` en kies een einddatum.

## Teksten aanpassen — `tools/content.py`
Functies, use cases, gratis tools, prijzen, vergelijkingstabel, woordenlijst en blogartikelen
staan allemaal in `tools/content.py`. Pas ze daar aan en draai:

    python3 tools/build.py

Dit genereert alle pagina's opnieuw, plus het menu, de footer en de blokken op de homepage.
Pas gegenereerde pagina's dus **niet** met de hand aan. Zet `SITE_URL` in `content.py` zodra je
een domein hebt, dan wordt ook `sitemap.xml` gemaakt.

## Structuur
- `index.html` — homepage (deels handgeschreven)
- `functies/`, `voor/`, `gratis-tools/`, `blog/` — gegenereerde pagina's
- `prijzen.html`, `woordenlijst.html`, `over-ons.html`, `contact.html`, `affiliate.html`, `voorwaarden.html`, `privacy.html`
- `calc.js` — formules van de rekentools

## Gratis hosten
GitHub Pages, Netlify of Cloudflare Pages.
