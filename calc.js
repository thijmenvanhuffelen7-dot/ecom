// Formules voor de gratis rekentools. Alles draait in de browser.
(function () {
  var box = document.querySelector('[data-calc]');
  if (!box) return;
  var eur = function (n) {
    return (n < 0 ? '−€' : '€') + Math.abs(n).toLocaleString('nl-NL', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  };
  var pct = function (n) { return n.toLocaleString('nl-NL', { maximumFractionDigits: 1 }) + '%'; };
  var x = function (n) { return n.toLocaleString('nl-NL', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + '×'; };
  var v = function (id) { var el = document.getElementById(id); var n = parseFloat(el && el.value); return isFinite(n) ? n : 0; };
  var out = function (id, txt) { var el = document.getElementById('out-' + id); if (el) el.textContent = txt; };
  var note = function (txt) { var el = document.getElementById('calcNote'); if (el) el.textContent = txt || ''; };

  var calcs = {
    roas: function () {
      var price = v('price'), ex = price / (1 + v('vat') / 100);
      var margin = ex - v('cogs') - v('ship') - price * v('fees') / 100 - v('other');
      out('margin', eur(margin));
      if (margin <= 0) { out('beroas', 'n.v.t.'); out('becpa', eur(0)); note('Je maakt al verlies vóór advertentiekosten. Verhoog je prijs of verlaag je kosten.'); return; }
      out('beroas', x(price / margin)); out('becpa', eur(margin));
      note('Boven deze ROAS maak je winst, eronder verlies.');
    },
    margin: function () {
      var price = v('price'), ex = price / (1 + v('vat') / 100);
      var net = ex - v('cogs') - v('ship') - price * v('fees') / 100 - v('ads');
      out('ex', eur(ex)); out('net', eur(net));
      out('pct', ex > 0 ? pct(net / ex * 100) : '–');
      out('markup', v('cogs') > 0 ? pct((ex - v('cogs')) / v('cogs') * 100) : '–');
      note(net < 0 ? 'Je maakt verlies op elke bestelling.' : '');
    },
    roi: function () {
      var inv = v('inv'), ret = v('ret'), m = Math.max(1, v('months'));
      out('profit', eur(ret - inv));
      out('roi', inv > 0 ? pct((ret - inv) / inv * 100) : '–');
      out('monthly', eur((ret - inv) / m));
      note('');
    },
    clv: function () {
      var rev = v('aov') * v('freq') * v('years'), clv = rev * v('gm') / 100;
      out('rev', eur(rev)); out('clv', eur(clv)); out('cac', eur(clv / 3));
      note('Vuistregel: geef maximaal een derde van je CLV uit om een klant te werven.');
    },
    price: function () {
      var costs = v('cogs') + v('ship') + v('ads');
      var vat = v('vat') / 100, f = v('fees') / 100 * (1 + vat), t = v('target') / 100;
      var denom = 1 - f - t;
      if (denom <= 0) { out('ex', '–'); out('incl', '–'); out('profit', '–'); note('Deze marge is niet haalbaar met deze kosten. Verlaag je doelmarge.'); return; }
      var ex = costs / denom;
      out('ex', eur(ex)); out('incl', eur(ex * (1 + vat))); out('profit', eur(ex * t));
      note('Tip: rond af naar een prijs die bij je merk past, bijvoorbeeld op ,95.');
    }
  };

  var fn = calcs[box.dataset.calc];
  if (!fn) return;
  box.addEventListener('input', fn);
  fn();
})();
