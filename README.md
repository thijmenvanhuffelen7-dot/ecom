# Merxa — landingspagina

Statische site (HTML/CSS/JS, geen build, geen kosten).

## Later invullen
Alles staat in `config.js`:
- `contactEmail` — contact-e-mail (leeg = verborgen)
- `waitlistEndpoint` — URL voor het wachtlijstformulier (bijv. gratis Formspree/Tally). Leeg = er wordt niets verstuurd.
- `communityUrl` — Discord/community-link

## Lokaal bekijken
Open `index.html` in je browser.

## Gratis hosten
GitHub Pages, Netlify of Cloudflare Pages: upload de map, klaar.

## Use-case pagina's
De pagina's in `voor/` (dropshippers, media buyers, freelancers, DTC-merken, creative strategists),
het "Use cases"-menu, de footer en de "Voor wie"-sectie op de homepage worden gegenereerd door
`tools/usecases.py`. Pas teksten daar aan en draai:

    python3 tools/usecases.py
