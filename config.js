// ============================================================
//  Merxa site-instellingen — pas hier alles aan op één plek.
// ============================================================
window.MERXA_CONFIG = {
  // E-mailadres voor contact. Leeg = contactlinks sturen naar de wachtlijst
  // en de contactpagina zegt "binnenkort". Later invullen, bijv. "hallo@merxa.nl".
  contactEmail: "",

  // Endpoint voor het wachtlijstformulier (bijv. een gratis Formspree- of
  // Tally-URL). Leeg = er wordt NIETS verstuurd; het adres blijft alleen in
  // de browser van de bezoeker.
  waitlistEndpoint: "",

  // Demovideo in de hero van de homepage. Een YouTube-link of een .mp4-URL.
  // Leeg = de knop "Bekijk demo" blijft verborgen.
  demoVideoUrl: "",

  // Actiebalk bovenaan met afteller (bijv. Black Friday).
  // Zet enabled op true om de actie te tonen; anders zie je de normale "Nieuw"-balk.
  promo: {
    enabled: false,
    text: "Black Friday: 20% extra korting op jaarplannen",
    linkText: "Bekijk prijzen →",
    link: "prijzen.html",                     // relatief aan de hoofdmap
    endsAt: "2026-12-01T00:00:00+01:00"       // na dit moment verdwijnt de actie vanzelf
  }
};
