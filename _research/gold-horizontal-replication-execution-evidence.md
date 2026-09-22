---
layout: research
title: "GOLD horizontal levels: replicated reaction evidence, later unconditional-touch test negative"
research_id: "PILOT-TRADING-001 / GOLD horizontal replication and execution"
status: "Mixed evidence — replicated signal, unconditional touch not supported"
updated: "2026-09-15"
topic: "Trading / GOLD horizontal levels"
summary: "The horizontal-level reaction-rate difference was positive across four historical samples and a 2019 quote-crossing validation was positive under its specification. A later preregistered unused 2026H2 test did not support an unconditional touch effect, narrowing the claim substantially."
---

## Current conclusion

The GOLD horizontal-level research now contains **both replicated positive signal-level evidence and a material unused-data negative result**.

Under the earlier frozen reaction-rate protocol, contacts with prior-60-minute rolling extrema showed a higher defined 15-minute directional-reaction rate than a recent-price control in four separated historical samples: 2024 development, independent 2022 validation, 2020 robustness, and preregistered early-2025 robustness. A separate 2019 historical BID/ASK quote-crossing validation was also positive under its specification.

That evidence remains part of the research record. It is no longer sufficient, however, to summarize the current state as simply “promising.” A later preregistered test on **unused 2026H2 data** asked a stricter question: whether an unconditional horizontal touch itself carried positive 15-minute directional return. It did not. The primary mean was **−1.379 bps**, with a session-clustered 95% interval of **[−1.909, −0.862] bps**.

The current public claim is therefore narrower: **a short-horizon reaction-rate difference replicated under the earlier signal definition, but it did not establish an unconditional touch edge on untouched data.**

<p class="card-links"><a href="{{ '/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">Read the 2026H2 unused-data replication</a></p>

## Historical reaction evidence across four periods

The earlier reaction-rate studies kept the mechanism and comparison materially unchanged.

<div class="result-summary-grid" aria-label="Historical GOLD horizontal-level reaction replication summary">
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
    <span class="result-stat-label">2020 robustness</span>
    <strong>+25.44 pp</strong>
    <span>95% CI +20.74 to +30.23</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Early-2025 robustness</span>
    <strong>+23.66 pp</strong>
    <span>95% CI +19.43 to +28.02</span>
  </div>
</div>

<div class="metric-chart" role="img" aria-label="Historical real-minus-control 15-minute directional-reaction effect: 2024 development 26.55 percentage points, 2022 independent validation 23.79 points, 2020 robustness 25.44 points, early-2025 robustness 23.66 points.">
  <div class="metric-row"><div class="metric-label">2024 development</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div><div class="metric-value">+26.55 pp</div></div>
  <div class="metric-row"><div class="metric-label">2022 validation</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:89.6%"></span></div><div class="metric-value">+23.79 pp</div></div>
  <div class="metric-row"><div class="metric-label">2020 robustness</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:95.8%"></span></div><div class="metric-value">+25.44 pp</div></div>
  <div class="metric-row"><div class="metric-label">Early-2025 robustness</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:89.1%"></span></div><div class="metric-value">+23.66 pp</div></div>
</div>

<p class="chart-note">These bars compare the same historical session-level real-minus-control reaction-rate metric. Reaction rate is not trade return.</p>

The 2022 validation passed with 60/60 contributing sessions and a real-minus-control effect of **+23.792 pp**. The 2020 robustness replication also used 60/60 contributing sessions and produced **+25.439 pp**. Early-2025 froze the first 60 structurally eligible sessions before outcome computation and produced **+23.663 pp**; its selected sample covered 2025-01-02 through 2025-04-11, not the full year.

The similarity of those estimates made a one-period explanation less plausible for that specific reaction-rate construct. It did not prove that the same information survived every entry rule or selection process.

## 2019 execution-aware historical validation

The 2019 study used observed historical BID/ASK quotes after the M1 contact bar became observable. Long events entered at ASK and exited at BID; short events entered at BID and exited at ASK, with a 15-minute horizon. No synthetic spread, commission, extra slippage, latency, market impact, or fill-probability assumption was added.

The original target was 60 sessions, but the structural scan found only 57 eligible sessions. The rule was prospectively amended to use all 57 before any 2019 return was computed. That deviation from the original preregistration remains a limitation.

<div class="result-summary-grid" aria-label="2019 execution-aware validation summary">
  <div class="result-stat"><span class="result-stat-label">Real mean return</span><strong>+1.189 bps</strong><span>95% CI +0.528 to +1.889</span></div>
  <div class="result-stat"><span class="result-stat-label">Control mean</span><strong>−2.309 bps</strong><span>recent-price control</span></div>
  <div class="result-stat"><span class="result-stat-label">Real − control</span><strong>+3.498 bps</strong><span>95% CI +2.531 to +4.500</span></div>
</div>

All 57 sessions contributed and the frozen support condition was met. This was stronger than a bar-only reaction comparison, but it remained a historical quote-crossing proxy rather than actual broker execution.

## Later evidence changed the boundary

The research program then tested where the apparent effect was being lost.

On the consumed 2026H1 strategy sample, the average path from touch to the later confirmed entry was favorable, while the average post-entry path was adverse. That diagnosis suggested that event selection around the confirmation step could matter. It was exploratory because the H1 sample had already been consumed.

The decisive follow-up was therefore not another H1 parameter search. The unconditional-touch question was preregistered and moved to unused 2026H2 data. Across 60 frozen sessions, **4,786 evaluable touch events** produced a mean 15-minute direction-adjusted return of **−1.379 bps**, with the clustered interval entirely below zero. The classification was **NO_UNCONDITIONAL_TOUCH_SUPPORT**.

This makes the evidence internally coherent without forcing all tests to say the same thing: an earlier reaction-vs-control statistic can replicate while a later unconditional-return claim fails. They are related, but they are not identical estimands.

## What did not justify rescue tuning

Several simple additions had already failed to add clear information to the historical baseline, including the tested 60-minute trend context, New York time context, and prior-session volatility state. The new H2 result also does not trigger a search for a better confirmation delay, time window, side filter, or threshold on the consumed samples.

The unconditional-touch line is closed as not supported. A materially different mechanism must be framed as a new hypothesis, frozen before outcomes, and tested on another unused or prospective sample.

## 2018 execution-aware replication remains parked

A separate 2018 execution-aware replication was frozen before outcome inspection. The first 60 eligible sessions were selected and the quote-acquisition manifest requires 2,066 event-hour-side units; 23 exact units were preserved before the manual acquisition route was deprioritized.

No 2018 return has been opened. The route was parked because completing roughly two thousand further one-hour/one-side manual acquisitions would make data collection dominate the research value. This is an operational decision, not evidence for or against the 2018 hypothesis.

## Decision implication

Do not treat the replicated historical reaction-rate pattern as a ready trading rule, and do not rescue the failed unconditional-touch claim by tuning the consumed H1/H2 samples. The next research budget should go to materially distinct, pre-outcome hypotheses or to better execution/data-path questions that can be tested independently. The parked 2018 acquisition route remains optional rather than a requirement to keep this line alive.

## What is not established

The combined research record does not establish:

- a durable profitable horizontal-level trading rule;
- a profitable opposite-direction rule from the negative H2 result;
- actual broker fills or broker-specific spread behavior;
- commissions, swap, latency, rejection, market impact, or fill probability beyond the tested proxies;
- a causal explanation for the positive or negative effects;
- transfer to another instrument or horizon;
- live performance in the current market regime.

## Evidence boundary

This page publishes reviewed summary statistics and research decisions only. Raw files, manifests, event-level ledgers, internal work-order state, credentials, positions, and current trading decisions remain outside the public site.

*This is a research record, not investment advice. Historical validation does not establish future profitability.*