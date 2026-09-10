---
layout: research
title: "GOLD horizontal levels: development reaction rate exceeded a recent-price control"
research_id: "PILOT-TRADING-001 / GOLD horizontal recent-price control"
status: "Development — later replicated"
updated: "2026-09-08"
topic: "Trading / GOLD horizontal levels"
summary: "In a sealed 60-session 2024 development sample, 60-minute rolling-extrema zones had a higher pre-specified 15-minute directional-reaction rate than a recent observed non-extreme price control. This was development evidence; later independent and robustness replications are documented separately."
---

## Research question

Do pre-specified GOLD support and resistance zones derived from recent price extrema contain more short-horizon directional-reaction information than a comparison price drawn mechanically from the same recent observed price distribution?

This page records the **2024 development-stage test**. Later replication evidence is summarized on the [current GOLD horizontal evidence page]({{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}).

## Why this comparison was run

An earlier development test used a continuous-uniform pseudo-level control. That control was not sufficiently comparable: only 1 of 60 sessions contributed to both real and pseudo sides. The failure was treated as a control-design problem rather than evidence that horizontal levels had no effect.

A new recent-price control was therefore specified. Because that control was designed after the earlier failure and after the 2024 real-side outcomes had already been inspected, this experiment was explicitly treated as **development-stage evidence**, not independent validation.

## Method

- Instrument: XAU/USD, BID, M1, UTC.
- Sample: the unchanged sealed 60-session 2024 development sample.
- Real levels: support at the minimum Low and resistance at the maximum High over the prior 60 observed M1 bars.
- Outcome: the pre-specified directional reaction at `t+15` minutes.
- Control: one recent observed Close selected from the prior 60 M1 closes after removing values that fell inside the contemporaneous real support or resistance zones.
- Matching unit: session.
- Primary estimate: equal-weight mean across sessions of `reaction rate real − reaction rate control`.
- Inference: 10,000 session bootstrap replicates with a 95% percentile interval.

The design-validity gate passed: **all 60 sessions contributed to both sides**.

## Results

<div class="result-summary-grid" aria-label="GOLD horizontal-level development result summary">
  <div class="result-stat">
    <span class="result-stat-label">Contributing sessions</span>
    <strong>60 / 60</strong>
    <span>design-validity gate passed</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Primary effect</span>
    <strong>+26.55 pp</strong>
    <span>real minus recent-price control</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">95% bootstrap interval</span>
    <strong>+21.23 to +31.82 pp</strong>
    <span>10,000 session resamples</span>
  </div>
</div>

### Equal-weight session reaction rate

<div class="metric-chart" role="img" aria-label="Equal-weight session directional-reaction rate: real rolling-extrema zones 79.78 percent; recent-price control 53.23 percent.">
  <div class="metric-row">
    <div class="metric-label">Real extrema zones</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div>
    <div class="metric-value">79.78%</div>
  </div>
  <div class="metric-row">
    <div class="metric-label">Recent-price control</div>
    <div class="bar-track"><span class="bar-fill bar-neutral" style="width:66.7%"></span></div>
    <div class="metric-value">53.23%</div>
  </div>
</div>

<p class="chart-note">The reaction rate is the frozen 15-minute directional-reaction outcome. It is not a win rate, trade return, or profitability measure.</p>

Across all sessions, the real side had 512 evaluable events and 403 successes; the control had 796 evaluable events and 425 successes. The equal-weight session rates were **0.797817** for real zones and **0.532273** for the recent-price control. The primary effect estimate was **+0.265544**, or **+26.55 percentage points**, with a 95% bootstrap interval of **[+21.23, +31.82] percentage points**.

Under the frozen classification rule, the development result was **PROMISING_FOR_FURTHER_TEST**.

## Interpretation at the development stage

This result was sufficient to move the standalone horizontal-level mechanism from development-stage inconclusive to a credible candidate for independent replication. It was not sufficient to establish that “horizontal lines work” generally, nor did it establish profitability.

At this stage the control had been created after an earlier control failure and after the 2024 real-side outcomes were known, so the result remained vulnerable to development-sample overfitting and structural differences between real extrema events and the control.

## Later evidence — status updated 2026-09-10

This page is no longer the latest evidence boundary.

The same frozen reaction mechanism subsequently produced a positive result in an **unused 2022 independent validation** and again in a **2020 robustness replication**. The real-minus-control effects were +23.79 and +25.44 percentage points respectively, with both 95% bootstrap intervals wholly above zero.

A later **2019 execution-aware historical validation** used observed BID/ASK quote crossing after the M1 signal became observable. Its real mean return was +1.189 bps with a 95% interval of +0.528 to +1.889 bps; the real-minus-control difference was +3.498 bps with a 95% interval of +2.531 to +4.500 bps.

These later results materially strengthen the research case, but they still do not establish a durable live trading edge. See the [current replication and execution evidence summary]({{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}) for the current interpretation and the ongoing 2018 replication.

## Evidence boundary

This page reports reviewed public summary statistics. Raw files, detailed execution artifacts, control streams, manifests, internal operational records, positions, and current trading decisions remain outside the public site.

*This is a research record, not investment advice. Historical results do not establish future trading performance.*