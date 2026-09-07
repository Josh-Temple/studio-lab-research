---
layout: research
title: "GOLD horizontal levels: development reaction rate exceeded a recent-price control"
research_id: "PILOT-TRADING-001 / GOLD horizontal recent-price control"
status: "Development — promising for further test"
updated: "2026-09-08"
topic: "Trading / GOLD horizontal levels"
summary: "In a sealed 60-session 2024 development sample, 60-minute rolling-extrema zones had a higher pre-specified 15-minute directional-reaction rate than a recent observed non-extreme price control. The result is development evidence only and does not establish profitability or out-of-sample replication."
---

## Research question

Do pre-specified GOLD support and resistance zones derived from recent price extrema contain more short-horizon directional-reaction information than a comparison price drawn mechanically from the same recent observed price distribution?

The comparison was designed to test the **standalone horizontal-level mechanism** before adding trend, regime, moving averages, volume profile, positioning, or other explanatory variables.

## Why this comparison was run

An earlier development test used a continuous-uniform pseudo-level control. That control was not sufficiently comparable: only 1 of 60 sessions contributed to both real and pseudo sides. The failure was treated as a control-design problem rather than evidence that horizontal levels had no effect.

A new recent-price control was therefore specified. Because that new control was designed after the earlier failure and after the 2024 real-side outcomes had already been inspected, the new experiment was explicitly treated as **development-stage evidence**, not independent validation.

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

Under the frozen classification rule, the result is **PROMISING_FOR_FURTHER_TEST**.

## Interpretation

This result moves the standalone horizontal-level mechanism from development-stage inconclusive to a credible candidate for independent replication. In this development sample, rolling-extrema zones produced a materially higher 15-minute directional-reaction rate than a fully evaluable control drawn from recent observed non-extreme prices.

That is a narrower claim than “horizontal lines work.” The result shows a development-sample difference under one pre-specified event definition and one comparison design.

## Why this is not yet an edge

This is **not independent evidence**. The recent-price control was designed after an earlier control failed and after the 2024 real-side outcomes had been inspected. The control may also differ from real extrema events in pre-event path characteristics that the current design does not fully match.

The result therefore does not establish:

- profitability or positive expectancy after transaction costs;
- spread or slippage tolerance;
- execution feasibility;
- drawdown characteristics;
- robustness across periods, regimes, or instruments;
- superiority to every credible control;
- incremental value from trend/regime or other indicators;
- a durable live-trading edge.

## Current status: independent validation preregistered

The next decision gate has now been frozen as a **2022 independent protocol validation**.

The preregistered plan uses the same rolling-extrema definition, recent-price control, 15-minute outcome, session estimator, design-validity gate, and classification rule. Starting from 2022-01-03 UTC, it will select the first 60 structurally eligible sessions using data-structure rules that do not depend on horizontal-line outcomes.

At the time of preregistration, **no 2022 horizontal-line or control reaction outcome had been inspected or computed**.

Continuation is supported only if the design gate passes, the primary effect remains positive, and the 95% bootstrap lower bound remains above zero. If the 2022 result fails to replicate, the 2024 result remains development evidence and the mechanism should be downgraded rather than retuned on the same holdout.

## Evidence boundary

This page reports reviewed public summary statistics and the current research decision. Detailed raw files, execution artifacts, control streams, manifests, and internal operational records remain outside the public site.

*This is a research record, not investment advice. Historical development results do not establish future trading performance.*