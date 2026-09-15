---
layout: research
title: "GOLD horizontal touch: an untouched 2026H2 replication did not support the unconditional effect"
research_id: "PILOT-TRADING-001 / 2026H2 unconditional touch replication"
status: "Completed — no unconditional-touch support"
updated: "2026-09-15"
topic: "Trading / GOLD horizontal levels"
summary: "A preregistered unused-data test across 60 sessions found a negative mean 15-minute touch-to-outcome return (-1.379 bps; 95% session-clustered bootstrap interval -1.909 to -0.862), so the unconditional-touch line was closed without rescue tuning."
---

## Current conclusion

A preregistered test on an **unused 2026H2 sample did not support the unconditional horizontal-touch hypothesis**.

The frozen primary mean was **−1.379 bps** and the session-clustered 95% bootstrap interval was **[−1.909, −0.862] bps**, entirely below zero. Under the preregistered interpretation rule, the result is **NO_UNCONDITIONAL_TOUCH_SUPPORT**.

This is an important update to the earlier GOLD horizontal research. Repeated signal-level reaction differences in older samples remain observations about those earlier definitions and comparisons, but they did not establish that entering from an unconditional touch would retain a positive return on untouched data.

## Why this test mattered

Earlier research found a repeatable difference in the defined 15-minute directional-reaction rate between rolling-extrema zones and a recent-price control across 2024, 2022, 2020, and early 2025. A separate 2019 historical quote-crossing validation was also positive under its specification.

Later work on the consumed 2026H1 strategy sample showed a more difficult picture: price movement from touch to the later confirmed entry was positive on average, but post-entry movement was negative. That left a narrower question worth testing independently: **does the touch itself have a positive directional return before the confirmation step selects events?**

The 2026H2 replication tested that question on untouched data rather than changing the consumed sample.

## Frozen evaluation

The result preserved the preregistered research boundary:

- **60 sessions** were fixed for the 2026H2 replication;
- source identity and required M1 / raw-Tick coverage passed the fixed checks;
- no prior 2026H2 unconditional-touch outcome had been computed;
- **4,788** touch events were identified;
- **4,786** had the required outcome and entered the primary calculation;
- **2** were unavailable because the required +15-minute quote was unavailable under the frozen quote rule;
- unavailable events were not imputed and no provider was substituted;
- inference used **10,000 session-level bootstrap replicates**.

No protocol, sample, parameter, time-of-day, side, regime, or trading-rule search was introduced after viewing the result.

## Result

<div class="result-summary-grid" aria-label="2026H2 unconditional horizontal-touch replication summary">
  <div class="result-stat">
    <span class="result-stat-label">Primary mean</span>
    <strong>−1.379 bps</strong>
    <span>15-minute direction-adjusted return</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">95% clustered interval</span>
    <strong>−1.909 to −0.862 bps</strong>
    <span>10,000 session resamples</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">Positive events</span>
    <strong>46.95%</strong>
    <span>4,786 evaluable events</span>
  </div>
</div>

The primary median was **−0.649 bps**. Long and short subsets were also negative descriptively: long mean **−1.750 bps** with a 95% interval of **[−2.491, −0.962]**, and short mean **−0.968 bps** with **[−1.803, −0.122]**.

Those side-specific figures are secondary descriptions. They do not turn the result into evidence for trading in the opposite direction.

An independent recomputation from the persisted event-level output matched the event count, primary mean, and bootstrap interval exactly.

## Interpretation

The result changes the public evidence boundary in two ways.

First, it weakens the idea that the earlier positive horizontal-level observations can be carried directly into an unconditional touch-entry claim. The prior positive 2026H1 touch-to-outcome diagnostic is compatible with **confirmation-conditioned selection**: events that later satisfied the confirmation rule were not necessarily representative of all touches.

Second, this is not evidence that every horizontal-level mechanism is ineffective. The older studies tested different constructs and comparisons, and one historical execution-aware specification was positive. The new result is narrower and more useful: **the preregistered unconditional-touch claim failed on its unused sample**.

## Research decision

The unconditional-touch replication line is now closed as **not supported**.

The consumed H1/H2 samples will not be used to rescue the result by optimizing confirmation delay, changing thresholds, selecting time windows, adding side filters, or designing a new touch-entry rule after the fact. A materially different hypothesis must be preregistered separately and tested on another unused or prospective sample.

This is the main practical value of the result: a repeated-looking market story was allowed to fail when a stricter untouched test disagreed.

## What this does not establish

This study does not establish:

- a profitable opposite-direction strategy;
- causality for the negative return;
- live broker performance or fill quality;
- general invalidity of all support/resistance or horizontal-level methods;
- transfer to other instruments or horizons;
- a new trading instruction.

## Evidence boundary

This page publishes reviewed summary statistics and the research decision. Raw market files, event-level ledgers, internal work-order state, credentials, current positions, and current trading decisions remain outside the public site.

*This is a research record, not investment advice. Historical research does not establish future profitability.*