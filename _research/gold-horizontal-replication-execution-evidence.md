---
layout: research
title: "GOLD horizontal levels: the reaction effect replicated and survived one execution-aware validation"
research_id: "PILOT-TRADING-001 / GOLD horizontal replication and execution"
status: "Replicated / execution-aware — promising for further test"
updated: "2026-09-10"
topic: "Trading / GOLD horizontal levels"
summary: "The same 60-minute rolling-extrema reaction effect was positive in 2024, 2022, and 2020, and a separate 2019 validation remained positive after crossing observed historical BID/ASK quotes. The evidence is stronger, but it still does not establish a durable live trading edge."
---

## Current conclusion

The GOLD horizontal-level line has moved beyond a single development result.

Under the frozen XAU/USD BID M1 protocol, contacts with prior-60-minute rolling extrema were followed by the defined 15-minute directional reaction more often than a recent observed non-extreme price control in **three separated historical samples**. A later execution-aware validation using observed historical BID/ASK quotes also produced a positive real-side mean return under the frozen quote-crossing proxy.

The research classification remains **PROMISING_FOR_FURTHER_TEST**. This is deliberately narrower than saying that the strategy is profitable or ready for live use.

## Reaction evidence across three periods

The mechanism and comparison were kept materially unchanged across the three reaction-rate studies.

<div class="result-summary-grid" aria-label="GOLD horizontal-level replication summary">
  <div class="result-stat">
    <span class="result-stat-label">2024 development</span>
    <strong>+26.55 pp</strong>
    <span>95% CI +21.23 to +31.82</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2022 independent validation</span>
    <strong>+23.79 pp</strong>
    <span>95% CI +18.73 to +29.02</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2020 robustness replication</span>
    <strong>+25.44 pp</strong>
    <span>95% CI +20.74 to +30.23</span>
  </div>
</div>

<div class="metric-chart" role="img" aria-label="Real-minus-control 15-minute directional-reaction effect: 2024 development 26.55 percentage points, 2022 independent validation 23.79 points, 2020 robustness replication 25.44 points.">
  <div class="metric-row">
    <div class="metric-label">2024 development</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div>
    <div class="metric-value">+26.55 pp</div>
  </div>
  <div class="metric-row">
    <div class="metric-label">2022 validation</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:89.6%"></span></div>
    <div class="metric-value">+23.79 pp</div>
  </div>
  <div class="metric-row">
    <div class="metric-label">2020 robustness</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:95.8%"></span></div>
    <div class="metric-value">+25.44 pp</div>
  </div>
</div>

<p class="chart-note">The bars compare the same session-level real-minus-control reaction-rate metric. Exact estimates and 95% bootstrap intervals are printed above. Reaction rate is not trade return.</p>

The 2022 validation passed its design-validity gate with 60/60 contributing sessions. Its real session reaction rate was 0.790698 versus 0.550132 for the control, giving **+23.792 percentage points** with a 95% bootstrap interval of **[+18.734, +29.020] points**.

The 2020 robustness replication also passed with 60/60 contributing sessions. Its primary effect was **+25.439 percentage points**, with a 95% bootstrap interval of **[+20.741, +30.230] points**.

The closeness of the three point estimates does not prove invariance across regimes, but it materially reduces the chance that the original 2024 reaction-rate difference was unique to one sampled period under this exact protocol.

## Added filters did not improve the baseline

After the standalone horizontal mechanism survived independent validation, several simple conditioning ideas were tested separately. The reviewed research record did **not** find incremental information from the tested 60-minute trend context, New York time context, or prior-session volatility state beyond the horizontal-line baseline. A separate recent session-direction continuation line was also rejected or deprioritized.

These negative results are useful: the current evidence supports keeping the mechanism simple rather than stacking indicators merely because the base effect replicated.

## Execution-aware 2019 validation

The next major question was whether the phenomenon survived a more realistic historical quote-crossing proxy.

The 2019 study used the same horizontal signal family but waited until the M1 contact bar was fully observable, then used **observed historical BID/ASK quotes** for entry and exit. Long events entered at ASK and exited at BID; short events entered at BID and exited at ASK. The exit horizon remained 15 minutes. No synthetic spread, commission, extra slippage, latency, market impact, or fill-probability assumption was added.

The original plan called for 60 sessions. A full-year structural scan found only 57 eligible sessions, so the sample rule was prospectively amended to use all 57 **before any 2019 return was computed or inspected**. This weakens the purity of the original preregistration and is part of the result.

<div class="result-summary-grid" aria-label="2019 execution-aware validation summary">
  <div class="result-stat">
    <span class="result-stat-label">Real mean return</span>
    <strong>+1.189 bps</strong>
    <span>95% CI +0.528 to +1.889</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Control mean</span>
    <strong>−2.309 bps</strong>
    <span>recent-price control</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Real − control</span>
    <strong>+3.498 bps</strong>
    <span>95% CI +2.531 to +4.500</span>
  </div>
</div>

All 57 sessions contributed. Both preregistered primary point estimates were positive and both bootstrap lower bounds were above zero, so the frozen support condition was met.

The positive **real mean** matters more than the larger real-minus-control difference because it shows that the result is not solely a consequence of a weak control series. Even so, this remains one execution-aware historical period and a quote-crossing proxy rather than actual broker fills.

## Current frontier: independent execution-aware replication on 2018

The next decision gate is a preregistered **2018 execution-aware replication** using the same mechanism, quote-side mapping, 15-minute horizon, control construction, bootstrap, and classification rules.

The latest durable progress has structurally verified **50 of the required first 60 eligible 2018 sessions**, with 7 candidate dates excluded under the frozen structural rules. The official Dukascopy Historical Data Export interface then became unresponsive at the 2018-03-21 candidate. No 2018 signal event, quote-crossing return, primary estimate, bootstrap interval, or research classification has been computed or inspected.

A versioned successor is ready to resume from that exact boundary rather than restart or change the data source. The 2018 line therefore remains **in progress, outcome untouched**.

## What is not established

The current evidence does not establish:

- actual broker fills or broker-specific spread behavior;
- commissions, swap, or slippage beyond the observed quote crossing;
- latency, rejection, market impact, or fill probability;
- position sizing, drawdown, tail risk, or capacity;
- live performance or validity in the current market regime;
- transfer to another instrument;
- a durable profitable trading rule.

The correct public claim is therefore about a **replicated short-horizon reaction phenomenon under a frozen GOLD protocol**, plus one positive execution-aware historical validation. It is not a buy/sell instruction.

## Evidence boundary

This page publishes reviewed summary statistics and the current research decision only. Raw files, manifests, internal work-order state, detailed acquisition logs, credentials, positions, and current trading decisions remain outside the public site.

*This is a research record, not investment advice. Historical validation does not establish future profitability.*