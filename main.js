(function () {
  var C = window.MERXA_CONFIG || {};
  var ROOT = document.body.getAttribute('data-root') || '';
  var $ = function (s) { return document.querySelector(s); };
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  var yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();

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
  $$('[data-mail-block]').forEach(function (el) { el.hidden = !C.contactEmail; });
  $$('[data-mail-empty]').forEach(function (el) { el.hidden = !!C.contactEmail; });

  // ---------- Actiebalk met afteller ----------
  var P = C.promo || {};
  var bar = $('#topbar');
  if (bar && P.enabled && P.endsAt) {
    var end = new Date(P.endsAt).getTime();
    if (end > Date.now()) {
      $('#topbarText').textContent = P.text || '';
      var link = $('#topbarLink');
      link.textContent = P.linkText || 'Bekijk →';
      link.href = ROOT + (P.link || 'prijzen.html');
      var cd = document.createElement('span');
      cd.className = 'countdown';
      bar.insertBefore(cd, link);
      bar.classList.add('promo');
      var pad = function (n) { return (n < 10 ? '0' : '') + n; };
      var tick = function () {
        var s = Math.max(0, Math.floor((end - Date.now()) / 1000));
        if (!s) { bar.classList.remove('promo'); cd.remove(); return; }
        var d = Math.floor(s / 86400), h = Math.floor(s % 86400 / 3600), m = Math.floor(s % 3600 / 60);
        cd.textContent = 'Nog ' + (d ? d + 'd ' : '') + pad(h) + ':' + pad(m) + ':' + pad(s % 60);
      };
      tick(); setInterval(tick, 1000);
    }
  }

  // ---------- Demovideo ----------
  var demoBtn = $('#demoBtn'), dlg = $('#demoDlg');
  if (demoBtn && dlg && C.demoVideoUrl) {
    demoBtn.hidden = false;
    var media = $('#demoMedia');
    var yt = C.demoVideoUrl.match(/(?:youtu\.be\/|v=|embed\/|shorts\/)([\w-]{11})/);
    demoBtn.addEventListener('click', function () {
      media.innerHTML = yt
        ? '<iframe src="https://www.youtube-nocookie.com/embed/' + yt[1] + '?autoplay=1" allow="autoplay; encrypted-media; fullscreen" allowfullscreen title="Demo"></iframe>'
        : '<video src="' + encodeURI(C.demoVideoUrl) + '" controls autoplay playsinline></video>';
      dlg.showModal();
    });
    var close = function () { dlg.close(); };
    dlg.querySelector('.demo-x').addEventListener('click', close);
    dlg.addEventListener('click', function (e) { if (e.target === dlg) close(); });
    dlg.addEventListener('close', function () { media.innerHTML = ''; });
  }

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
      var done = function () { msg.textContent = 'Top, je staat op de lijst! 🎉'; form.reset(); };
      var fail = function () { msg.textContent = 'Er ging iets mis, probeer het later opnieuw.'; };
      if (C.waitlistEndpoint) {
        fetch(C.waitlistEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ email: email, page: location.pathname })
        }).then(function (r) { r.ok ? done() : fail(); }).catch(fail);
      } else {
        try { localStorage.setItem('merxa_waitlist', email); } catch (_) {}
        done();
      }
    });
  }

  // ---------- Prijzen maand/kwartaal/jaar ----------
  $$('.toggle button').forEach(function (b) {
    b.addEventListener('click', function () {
      $$('.toggle button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      var k = b.dataset.bill;
      $$('.price b[data-m]').forEach(function (p) { p.textContent = '€' + (p.dataset[k] || p.dataset.m); });
    });
  });

  // ---------- Besparings-rekenhulp (homepage) ----------
  if ($('#ads') && $('#costSave')) {
    var eur = function (n) { return '€' + Math.round(n).toLocaleString('nl-NL'); };
    var calc = function () {
      var ads = +$('#ads').value, ugc = +$('#ugc').value, lp = +$('#lp').value;
      $('#adsOut').textContent = ads; $('#ugcOut').textContent = ugc; $('#lpOut').textContent = lp;
      var now = ads * 40 + ugc * 150 + lp * 400;
      var merxa = 99 + ads * 0.5 + ugc * 6 + lp * 3; // abonnement + geschat tegoed
      $('#costNow').textContent = eur(now);
      $('#costMerxa').textContent = eur(merxa);
      $('#costSave').textContent = eur(Math.max(0, now - merxa));
    };
    ['#ads', '#ugc', '#lp'].forEach(function (id) { $(id).addEventListener('input', calc); });
    calc();
  }

  // ---------- Live taak-feed in de hero ----------
  var feed = $('#feed');
  if (feed) {
    var tasks = [
      ['🔎', '142 reviews geanalyseerd', '3 nieuwe angles gevonden'],
      ['🖼️', '6 ad creatives klaar', 'Wacht op goedkeuring'],
      ['🎬', 'UGC-storyboard gemaakt', '"Ochtendroutine" · 28 sec'],
      ['⚡', 'Landingspagina live', '/zomer-sale · mobiel gecheckt'],
      ['📈', 'Ad #12 opschalen?', 'ROAS 5,1× in 3 dagen'],
      ['🛑', 'Ad #7 gepauzeerd', 'CPA boven je limiet'],
      ['🧠', 'Brand voice bijgewerkt', 'Uit je laatste feedback']
    ];
    var i = 0, count = 47, dc = $('#doneCount');
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var push = function (inc) {
      var t = tasks[i++ % tasks.length];
      var li = document.createElement('li');
      li.innerHTML = '<span class="fi">' + t[0] + '</span><div><b>' + t[1] + '</b><small>' + t[2] + '</small></div><span class="ok">✓</span>';
      feed.insertBefore(li, feed.firstChild);
      while (feed.children.length > 4) feed.removeChild(feed.lastChild);
      if (inc && dc) dc.textContent = ++count;
    };
    for (var n = 0; n < 4; n++) push(false);
    if (!reduce) setInterval(function () { push(true); }, 2600);
  }

  // ---------- Menu ----------
  $$('.nav-links a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
  });
  // Dropdowns ook met klik/tap openen (touch-schermen hebben geen hover)
  $$('.dd-btn').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.stopPropagation();
      var dd = b.parentNode, open = dd.classList.contains('open');
      $$('.dd.open').forEach(function (x) { x.classList.remove('open'); });
      if (!open) dd.classList.add('open');
    });
  });
  document.addEventListener('click', function () { $$('.dd.open').forEach(function (x) { x.classList.remove('open'); }); });
})();
