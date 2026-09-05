---
title: "GOLD session-range persistence: strong development association was not independently confirmed"
research_id: "PILOT-TRADING-001 / GOLD 2021 independent validation"
status: "Completed — inconclusive independent validation"
updated: "2026-09-06"
topic: "Trading / GOLD / volatility persistence"
summary: "A strong positive session-range association seen in 2024 development data was tested on an independent 2021 period. The validation estimate remained positive but was small, and the frozen 95% block-bootstrap interval crossed zero."
---

## Research question

Does the positive association between the previous and next UTC-session intraday range, seen strongly in 2024 development data, persist in an independently evaluated 2021 GOLD sample?

This is a volatility-persistence question. It does **not** directly test direction, entries, exits, profitability, or a complete trading strategy.

## Development result that motivated the test

The 2024 development study used **60 sealed adjacent-session pairs**. The observed Spearman association between previous-session and next-session range was:

<div class="result-summary-grid" aria-label="Development and validation summary">
  <div class="result-stat">
    <span class="result-stat-label">2024 development</span>
    <strong>ρ = 0.5621</strong>
    <span>60 sealed pairs</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2021 independent validation</span>
    <strong>ρ = 0.0626</strong>
    <span>198 valid adjacent pairs</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2021 bootstrap 95% CI</span>
    <strong>−0.1283 to 0.1439</strong>
    <span>10,000 valid block-bootstrap replicates</span>
  </div>
</div>

The 2024 result was classified as promising for further testing, not as independent evidence or a trading edge.

## Independent validation method

The independent evaluation used official Dukascopy Public Historical Data Export data for **XAU/USD, BID, M1, UTC** across calendar year 2021.

The execution rules were frozen before the result was inspected. The pipeline required structurally complete sessions and did not repair, fill, interpolate, resample, or synthesize missing rows.

The final validation set contained:

- **261** weekday source files acquired from the official export route;
- **227** structurally eligible sessions;
- **198** valid adjacent-session pairs;
- **10,000 / 10,000** valid circular moving-block bootstrap replicates with block length 5.

The primary classification used the frozen 95% bootstrap interval rather than the ordinary Spearman p-value.

## Result

The 2021 Spearman estimate was **ρ = 0.0625556**. Its frozen 95% circular moving-block-bootstrap interval was **[−0.1283186, 0.1439162]**.

Because the interval crossed zero, the predefined classification was **INCONCLUSIVE**.

This means the 2021 result did **not** provide statistically supported independent confirmation of the much stronger 2024 development association. It also does not prove that volatility persistence is absent.

## Why the interpretation changed

The development result alone left open the possibility that previous-session high-low range carried a useful standalone persistence signal.

Two later observations weakened that interpretation:

1. the independent 2021 validation did not confirm the strong 2024 association; and
2. a separate 2024 incremental comparison found that adding previous-session range to a previous-session realized-variance baseline slightly worsened pooled chronological out-of-fold MSE rather than improving it.

Taken together, the current research decision is to **deprioritize previous-session high-low range as a distinct forecasting mechanism** rather than spend additional independent-validation capacity trying to rescue it after seeing the 2021 outcome.

The broader idea that volatility can persist remains plausible. What is not supported here is treating raw previous-session range itself as a demonstrated standalone trading edge.

## Research governance after the result

The 2021 period is now consumed for this mechanism. It must not be used to retune thresholds, session rules, block length, or metrics and then later be described as an untouched holdout for the retuned version.

No automatic new range-persistence holdout is currently recommended.

## Current research direction

The next higher-priority GOLD line is a **horizontal-level reaction development falsification**: testing whether price reactions around pre-specified rolling-window support/resistance zones differ from matched pseudo/non-level controls.

That work is still in preregistration and design closure. The current design includes a 60-minute rolling-extrema level family, a 15-minute reaction horizon, and 2024 as development-only data.

**No horizontal-level outcome has been opened or reported on this site yet.** The hypothesis remains unexecuted until the remaining deterministic design gates are closed.

## Limitations and uncertainty

- The 2021 result is inconclusive, not evidence that the true association is exactly zero.
- Sessions are reused across adjacent pairs, so observations are not treated as independent; the block-bootstrap design was used to preserve local dependence.
- This result concerns session-range association only. It does not establish directional predictability, execution feasibility, P/L, drawdown, Sharpe, hit rate, or position sizing.
- Historical reference-market data are not equivalent to realized broker execution.
- The priority decision combines this independent validation with a separate incremental-baseline comparison; neither result alone proves that every volatility-based strategy is unworkable.

## Evidence boundary

Public source data were obtained through the [Dukascopy Public Historical Data Export](https://widgets.dukascopy.com/en/historical-data-export) interface.

The internal research archive retains the frozen handoff, canonical raw-date identities, evidence CSV, bootstrap configuration, verification records, and research-integration note. Those operational artifacts are not automatically exposed here.

*This is a research record, not investment advice. Historical and simulated results do not establish future performance.*
