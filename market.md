---
title: Market
permalink: /market/
description: A lightweight public market-observation page generated from hourly data snapshots. Descriptive observations only; no trading signals or positions.
---

<p class="eyebrow">Market observer</p>
<h1>Eight markets. One lightweight snapshot.</h1>
<p class="lede">An hourly, read-only observation layer for Studio Lab. It shows a small set of market proxies and standard descriptive indicators. It is not a signal service, a position dashboard, or a recommendation to trade.</p>

<section class="section market-panel" aria-labelledby="market-status-title">
  <div class="market-meta">
    <div><span>Snapshot</span><strong id="market-updated">Loading…</strong></div>
    <div><span>Provider</span><strong id="market-provider">—</strong></div>
    <div><span>Health</span><strong id="market-health">—</strong></div>
  </div>

  <div class="market-table-wrap">
    <table class="market-table">
      <thead>
        <tr><th>Symbol</th><th>Market</th><th>Trend</th><th>Close</th><th>1h</th><th>24h</th><th>RSI14</th><th>ATR%</th></tr>
      </thead>
      <tbody id="market-body"><tr><td colspan="8">Loading market snapshot…</td></tr></tbody>
    </table>
  </div>
  <p class="small-note" id="market-note">Hourly data is generated during the GitHub Pages build. Values can lag the source and may be temporarily unavailable.</p>
</section>

<section class="section public-boundary">
  <p class="eyebrow">Boundary</p>
  <h2>Observation, not a trading decision.</h2>
  <p>The page intentionally excludes positions, account data, order placement, position sizing, and AI-generated trade recommendations. ETF observations such as GLD, USO, SPY, QQQ, UUP, and TLT are proxies and should not be treated as execution prices for spot or futures markets.</p>
</section>

<script>
(() => {
  const url = "{{ '/assets/data/market/latest.json' | relative_url }}";
  const fmt = (v, d=2) => (v === null || v === undefined || Number.isNaN(Number(v))) ? "—" : Number(v).toFixed(d);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));
  fetch(url, {cache:"no-store"})
    .then(r => { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
    .then(data => {
      document.getElementById("market-updated").textContent = data.generated_at_utc || "unknown";
      document.getElementById("market-provider").textContent = data.provider || "—";
      const health = data.health?.market?.status || "unknown";
      document.getElementById("market-health").textContent = health;
      const rows = data.market || [];
      document.getElementById("market-body").innerHTML = rows.length ? rows.map(x => x.status === "ok" ? `
        <tr>
          <td><strong>${esc(x.symbol)}</strong></td><td>${esc(x.label)}</td><td>${esc(x.trend)}</td>
          <td>${fmt(x.close,4)}</td><td>${fmt(x.return_1h_pct)}%</td><td>${fmt(x.return_24h_pct)}%</td>
          <td>${fmt(x.rsi14,1)}</td><td>${fmt(x.atr14_pct)}%</td>
        </tr>` : `<tr><td><strong>${esc(x.symbol)}</strong></td><td>${esc(x.label)}</td><td colspan="6">Unavailable: ${esc(x.error || "error")}</td></tr>`).join("")
        : '<tr><td colspan="8">Live market data is not available yet.</td></tr>';
    })
    .catch(() => {
      document.getElementById("market-health").textContent = "unavailable";
      document.getElementById("market-body").innerHTML = '<tr><td colspan="8">Market snapshot could not be loaded.</td></tr>';
    });
})();
</script>
