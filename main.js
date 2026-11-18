(function () {
  var C = window.MERXA_CONFIG || {};
  var $ = function (s) { return document.querySelector(s); };
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  $('#yr').textContent = new Date().getFullYear();

  // ---------- E-mail (pas aan in config.js) ----------
  $$('[data-mail]').forEach(function (el) {
    if (C.contactEmail) {
      el.href = 'mailto:' + C.contactEmail;
      el.textContent = C.contactEmail;
      el.hidden = false;
    }
  });
  $$('[data-mail-link]').forEach(function (el) {
    el.href = C.contactEmail ? 'mailto:' + C.contactEmail : '#waitForm';
  });

  // ---------- Wachtlijst ----------
  var form = $('#waitForm'), msg = $('#waitMsg');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.email.value.trim();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        msg.textContent = 'Vul een geldig e-mailadres in.';
        return;
      }
      var done = function () {
        msg.textContent = 'Top, je staat op de lijst! 🎉';
        form.reset();
      };
      if (C.waitlistEndpoint) {
        fetch(C.waitlistEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ email: email })
        }).then(function (r) {
          if (r.ok) done(); else msg.textContent = 'Er ging iets mis, probeer het later opnieuw.';
        }).catch(function () { msg.textContent = 'Er ging iets mis, probeer het later opnieuw.'; });
      } else {
        try { localStorage.setItem('merxa_waitlist', email); } catch (_) {}
        done();
      }
    });
  }

  // ---------- Prijzen maand/jaar ----------
  $$('.toggle button').forEach(function (b) {
    b.addEventListener('click', function () {
      $$('.toggle button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      var k = b.dataset.bill;
      $$('.price b').forEach(function (p) { p.textContent = '€' + p.dataset[k]; });
    });
  });

  // ---------- ROI-rekenhulp ----------
  var eur = function (n) { return '€' + Math.round(n).toLocaleString('nl-NL'); };
  function calc() {
    var ads = +$('#ads').value, ugc = +$('#ugc').value, lp = +$('#lp').value;
    $('#adsOut').textContent = ads; $('#ugcOut').textContent = ugc; $('#lpOut').textContent = lp;
    var now = ads * 40 + ugc * 150 + lp * 400;
    var merxa = 99 + ads * 0.5 + ugc * 6 + lp * 3; // abonnement + geschat tegoed
    $('#costNow').textContent = eur(now);
    $('#costMerxa').textContent = eur(merxa);
    $('#costSave').textContent = eur(Math.max(0, now - merxa));
  }
  ['#ads', '#ugc', '#lp'].forEach(function (id) { var el = $(id); if (el) el.addEventListener('input', calc); });
  if ($('#ads')) calc();

  // ---------- Live taak-feed in de hero ----------
  var tasks = [
    ['🔎', '142 reviews geanalyseerd', '3 nieuwe angles gevonden'],
    ['🖼️', '6 ad creatives klaar', 'Wacht op goedkeuring'],
    ['🎬', 'UGC-storyboard gemaakt', '"Ochtendroutine" · 28 sec'],
    ['⚡', 'Landingspagina live', '/zomer-sale · mobiel gecheckt'],
    ['📈', 'Ad #12 opschalen?', 'ROAS 5,1× in 3 dagen'],
    ['🛑', 'Ad #7 gepauzeerd', 'CPA boven je limiet'],
    ['🧠', 'Brand voice bijgewerkt', 'Uit je laatste feedback']
  ];
  var feed = $('#feed'), i = 0, count = 47;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function push() {
    var t = tasks[i++ % tasks.length];
    var li = document.createElement('li');
    li.innerHTML = '<span class="fi">' + t[0] + '</span><div><b>' + t[1] + '</b><small>' + t[2] + '</small></div><span class="ok">✓</span>';
    feed.insertBefore(li, feed.firstChild);
    while (feed.children.length > 4) feed.removeChild(feed.lastChild);
    $('#doneCount').textContent = ++count;
  }
  if (feed) {
    for (var n = 0; n < 4; n++) push();
    count = 47; $('#doneCount').textContent = count;
    if (!reduce) setInterval(push, 2600);
  }

  // ---------- Mobiel menu sluit na klik ----------
  $$('.nav-links a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
  });
})();
