---
title: "Repeat trading external holdout: lower risk did not become a profit edge"
research_id: "PILOT-TRADING-001 / 2020–2022 holdout"
status: "Completed — mixed / inconclusive"
updated: "2026-08-29"
topic: "Trading / systematic strategy evaluation"
summary: "A pre-specified external holdout test of two dynamic-exit rules reduced drawdown-related burden but did not improve matched median P/L versus a no-common-stop benchmark."
---

## Research question

A dynamic-exit rule looked promising during development and stress testing. Would that improvement survive when the same rules were taken, without retuning, to a previously unused 2020–2022 evaluation period?

The narrower question was important: **can a rule that appears to reduce the damage from adverse trends also improve profitability out of sample, or are those two benefits separate?**

## Method

The evaluation compared a finite USD/JPY repeat-trading grid against two pre-specified dynamic-exit variants:

- benchmark: finite grid with no common stop;
- `ret20 < -2%`: liquidate when the 20-active-day return falls below -2%;
- `ret20 < 0%`: liquidate when the 20-active-day return falls below 0%.

The benchmark used a fixed ±5 yen grid, 0.50 yen step, 0.20 yen take-profit, one unit per order, and mark-to-market treatment for positions still open at the end of each 180-day window.

The external holdout covered 2020–2022. It was opened after the comparison definitions and thresholds had been fixed. The final dataset passed completeness checks across **81 combined windows**.

Primary evaluation measures included terminal P/L, maximum drawdown, maximum open positions, maximum unrealized loss, ending open positions, and exposure. Risk reduction was not treated as equivalent to profit improvement.

After the holdout was inspected, the 2020–2022 period was frozen against further tuning of these thresholds or exit semantics.

## Results

The two exit rules reduced some forms of risk burden, but neither improved matched median P/L versus the benchmark.

<div class="result-summary-grid" aria-label="External holdout summary">
  <div class="result-stat">
    <span class="result-stat-label">Holdout windows</span>
    <strong>81</strong>
    <span>combined windows</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Evaluation period</span>
    <strong>2020–2022</strong>
    <span>previously unused for this test</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Final classification</span>
    <strong>Mixed / inconclusive</strong>
    <span>risk improved; profit did not</span>
  </div>
</div>

### Matched median P/L delta

Relative to the no-common-stop benchmark. Negative values mean the dynamic-exit rule produced a lower matched median P/L.

<div class="metric-chart" role="img" aria-label="Matched median P/L delta: ret20 below minus 2 percent was minus 4.412; ret20 below 0 percent was minus 12.340.">
  <div class="metric-row">
    <div class="metric-label"><code>ret20 &lt; -2%</code></div>
    <div class="bar-track"><span class="bar-fill bar-negative" style="width:35.8%"></span></div>
    <div class="metric-value">−4.412</div>
  </div>
  <div class="metric-row">
    <div class="metric-label"><code>ret20 &lt; 0%</code></div>
    <div class="bar-track"><span class="bar-fill bar-negative" style="width:100%"></span></div>
    <div class="metric-value">−12.340</div>
  </div>
</div>

### Median drawdown reduction

Positive values mean lower median drawdown than the benchmark.

<div class="metric-chart" role="img" aria-label="Median drawdown reduction: ret20 below minus 2 percent improved by 2.040; ret20 below 0 percent improved by 3.307.">
  <div class="metric-row">
    <div class="metric-label"><code>ret20 &lt; -2%</code></div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:61.7%"></span></div>
    <div class="metric-value">+2.040</div>
  </div>
  <div class="metric-row">
    <div class="metric-label"><code>ret20 &lt; 0%</code></div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div>
    <div class="metric-value">+3.307</div>
  </div>
</div>

### P/L and drawdown improved at the same time

This stricter measure asks how often a matched comparison improved both profit and drawdown rather than only reducing risk.

<div class="metric-chart" role="img" aria-label="Simultaneous P/L and drawdown improvement rate: ret20 below minus 2 percent 3.7 percent; ret20 below 0 percent 13.6 percent.">
  <div class="metric-row">
    <div class="metric-label"><code>ret20 &lt; -2%</code></div>
    <div class="bar-track"><span class="bar-fill bar-neutral" style="width:27.2%"></span></div>
    <div class="metric-value">3.7%</div>
  </div>
  <div class="metric-row">
    <div class="metric-label"><code>ret20 &lt; 0%</code></div>
    <div class="bar-track"><span class="bar-fill bar-neutral" style="width:100%"></span></div>
    <div class="metric-value">13.6%</div>
  </div>
</div>

<p class="chart-note">Bar lengths are scaled within each metric. Compare the printed values across metrics rather than comparing bar length from one chart to another.</p>

## Why the holdout mattered

The same rules had looked much stronger in the 2024 development period. In the 180-day matched-control analysis, median P/L was **-33.638** for no exit, **+7.800** for `ret20 < -2%`, and **+7.768** for `ret20 < 0%`.

That apparent improvement was useful for forming the hypothesis, but it was not independent evidence because the rule was being evaluated in the same broad development context in which it had been selected and stress-tested.

The untouched 2020–2022 result changed the interpretation: the dynamic exits retained some **risk-control value**, but the evidence did **not** support describing either rule as a robust profit-improving edge.

## Interpretation

The main result is a separation between two claims that are easy to blur together:

1. **A rule can reduce exposure to damaging trends.**
2. **That does not mean the rule increases expected profit.**

Both exit variants reduced drawdown-related burden, maximum-position pressure, unrealized-loss burden, or exposure in the external holdout. But matched median P/L was lower than the benchmark for both variants.

The strongest supported conclusion is therefore not that the dynamic exits are “good” or “bad.” It is that **their defensive value did not generalize into a consistent profitability improvement in this holdout**.

This result also weakens the case for increasing real-money position size on the basis of the tested exit logic alone.

## Limitations and uncertainty

- This is one strategy family, one instrument, one set of frozen rules, and one historical holdout period.
- Backtested and reference-market results are not the same as realized broker execution.
- Spread, slippage, swap, capital requirements, and implementation details can materially change real-world outcomes.
- A mixed or inconclusive result is not proof that no profitable repeat-trading variant exists.
- The 2020–2022 holdout can no longer serve as an untouched test set for newly tuned versions of these same rules.
- Trend/regime stratification remains a separate research question and is not inferred from this result.

## Evidence boundary

The public claim is limited to the reviewed summary statistics above. Reproduction code, detailed CSV outputs, execution logs, and broker-side mechanics records remain in the private research archive and are not exposed by this site.

This page does not publish live positions, account information, or current trade decisions.

## Practical status

The result does **not** provide a basis for increasing live trading size. Further work is aimed at determining whether trend/regime information can explain part of the observed risk and P/L variation without retroactively changing the already-opened holdout rules.

*This is a research record, not investment advice. Historical and simulated results do not establish future performance.*
