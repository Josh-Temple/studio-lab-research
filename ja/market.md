---
title: 市場
lang: ja
permalink: /ja/market/
description: 毎時のデータスナップショットを表示する軽量な公開市場観測ページ。記述的な観測のみで、売買シグナルやポジション情報は含みません。
---

<p class="eyebrow">Market observer</p>
<h1>8市場を、1枚の軽い画面で見る。</h1>
<p class="lede">Studio Labの毎時・読み取り専用の市場観測ページです。少数の市場proxyと標準的な記述指標だけを表示します。売買シグナル、ポジション画面、取引推奨ではありません。</p>

<section class="section market-panel" aria-labelledby="market-status-title-ja">
  <div class="market-meta">
    <div><span>更新時刻</span><strong id="market-updated">読み込み中…</strong></div>
    <div><span>データ元</span><strong id="market-provider">—</strong></div>
    <div><span>状態</span><strong id="market-health">—</strong></div>
  </div>

  <div class="market-table-wrap">
    <table class="market-table">
      <thead>
        <tr><th>銘柄</th><th>市場</th><th>方向</th><th>終値</th><th>1時間</th><th>24時間</th><th>RSI14</th><th>ATR%</th></tr>
      </thead>
      <tbody id="market-body"><tr><td colspan="8">市場データを読み込んでいます…</td></tr></tbody>
    </table>
  </div>
  <p class="small-note">データはGitHub Pagesのビルド時に毎時生成します。元データより遅れる場合や、一時的に取得できない場合があります。</p>
</section>

<section class="section public-boundary">
  <p class="eyebrow">公開範囲</p>
  <h2>観測であり、売買判断ではありません。</h2>
  <p>ポジション、口座情報、注文、数量判断、AIによる売買推奨は表示しません。GLD、USO、SPY、QQQ、UUP、TLTなどのETFはproxyであり、現物・先物の約定価格として扱うものではありません。</p>
</section>

<script>
(() => {
  const url = "{{ '/assets/data/market/latest.json' | relative_url }}";
  const fmt = (v, d=2) => (v === null || v === undefined || Number.isNaN(Number(v))) ? "—" : Number(v).toFixed(d);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));
  const labels = {up:"上向き",down:"下向き",mixed:"混在",insufficient:"データ不足"};
  fetch(url, {cache:"no-store"})
    .then(r => { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
    .then(data => {
      document.getElementById("market-updated").textContent = data.generated_at_utc || "不明";
      document.getElementById("market-provider").textContent = data.provider || "—";
      const health = data.health?.market?.status || "unknown";
      document.getElementById("market-health").textContent = health;
      const rows = data.market || [];
      document.getElementById("market-body").innerHTML = rows.length ? rows.map(x => x.status === "ok" ? `
        <tr>
          <td><strong>${esc(x.symbol)}</strong></td><td>${esc(x.label)}</td><td>${esc(labels[x.trend] || x.trend)}</td>
          <td>${fmt(x.close,4)}</td><td>${fmt(x.return_1h_pct)}%</td><td>${fmt(x.return_24h_pct)}%</td>
          <td>${fmt(x.rsi14,1)}</td><td>${fmt(x.atr14_pct)}%</td>
        </tr>` : `<tr><td><strong>${esc(x.symbol)}</strong></td><td>${esc(x.label)}</td><td colspan="6">取得不可: ${esc(x.error || "error")}</td></tr>`).join("")
        : '<tr><td colspan="8">ライブ市場データはまだ利用できません。</td></tr>';
    })
    .catch(() => {
      document.getElementById("market-health").textContent = "unavailable";
      document.getElementById("market-body").innerHTML = '<tr><td colspan="8">市場スナップショットを読み込めませんでした。</td></tr>';
    });
})();
</script>
