---
title: Trading
permalink: /trading/
updated: "2026-09-14"
description: Reviewed Studio Lab trading research, including development tests, holdouts, independent validations, execution-aware checks, prospective screens, risk controls, and negative results.
---

<p class="eyebrow">Trading research</p>
<h1>Test the edge before trusting the story.</h1>
<p class="lede">Selected systematic-trading research from Studio Lab. This section publishes reviewed development results, holdouts, independent validations, execution-aware checks, prospective protocols, and negative or mixed findings while keeping unresolved hypotheses separate. It is not a live trading dashboard, signal service, or record of current positions.</p>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Current evidence</p>
      <h2>GOLD horizontal reactions have repeated across four periods</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD horizontal levels · replicated / execution-aware</p>
      <h3><a href="{{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">The reaction effect replicated across four periods and remained positive in one quote-crossing validation</a></h3>
      <p>The frozen real-minus-control 15-minute reaction effect was +26.55 pp in 2024 development, +23.79 pp in independent 2022 validation, +25.44 pp in 2020 robustness, and +23.66 pp in a preregistered early-2025 robustness sample. A separate 2019 validation using observed BID/ASK quote crossing produced a +1.189 bps real mean and +3.498 bps real-minus-control difference.</p>
      <p class="card-links"><a href="{{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">Read the current evidence summary</a></p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">What did not add value</p>
      <h3>More indicators have not automatically improved the baseline</h3>
      <p>Reviewed incremental tests of 60-minute trend context, New York time context, and prior-session volatility did not demonstrate additional information beyond the standalone horizontal-line baseline. Recent session-direction continuation was also rejected or deprioritized.</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Other published results</p>
      <h2>Negative and mixed evidence stays visible</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">Repeat trading · external holdout</p>
      <h3><a href="{{ '/research/repeat-trading-external-holdout/' | relative_url }}">Lower risk did not become a profit edge</a></h3>
      <p>Two dynamic-exit rules reduced drawdown-related burden in an untouched 2020–2022 holdout, but neither improved matched median P/L versus the benchmark.</p>
      <p class="card-links"><a href="{{ '/research/repeat-trading-external-holdout/' | relative_url }}">Read the study and charts</a></p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">GOLD range persistence · independent validation</p>
      <h3><a href="{{ '/research/gold-session-range-independent-validation/' | relative_url }}">Strong development range persistence was not independently confirmed</a></h3>
      <p>The 2024 development association was strong (ρ=0.5621), but the frozen 2021 validation estimate was ρ=0.0626 with a 95% block-bootstrap interval crossing zero.</p>
      <p class="card-links"><a href="{{ '/research/gold-session-range-independent-validation/' | relative_url }}">Read the validation</a></p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Current research · reviewed 2026-09-14</p>
      <h2>Prospective screening, discovery gates, and execution closure are running in parallel</h2>
    </div>
  </div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">VIX prospective screen · E01 fail-closed</p>
      <h3>The first event started, but the required start observations were unavailable</h3>
      <p>E01 began on 2026-09-14, but a valid 09:00 JST VIX snapshot and the specified XAU/USD start observation could not be established within the frozen information boundary. Later values were not substituted. The event therefore recorded an equal-probability forecast, <strong>ABSTAIN / HOLD</strong>, and no performance conclusion.</p>
      <p class="card-links">The E02 preparation now makes the source identities and capture rules explicit. Data-access and one-minute-feed verification still need to pass before the next event can produce a valid observation. Thresholds, horizon, outcome categories, and Brier scoring remain unchanged.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Distinct-mechanism discovery · gate first</p>
      <h3>Test cheap evidence before building data pipelines or backtests</h3>
      <p>The current discovery line screens scientifically distinct GOLD mechanisms with primary evidence first, then asks whether the measure can be observed before outcomes and whether an economic effect is large enough to justify strict validation. Candidates that fail or overlap are pruned rather than turned into parameter variants.</p>
      <p class="card-links">For example, a prospective Commercial Paper check found direct historical research linking CP rates and gold, but only at an associational/contemporaneous level. That is enough to continue evidence-path work, not enough to claim predictive edge.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">2018 execution-aware replication · parked</p>
      <h3>The hypothesis remains untouched; the manual acquisition route was deprioritized</h3>
      <p>The 60-session sample and research rules remain frozen, with 23 of 2,066 required quote units preserved and no 2018 return inspected. After repeated attempts, the one-hour/one-side browser acquisition route was judged too mechanically expensive relative to its information value.</p>
      <p class="card-links">This is an operational decision, not evidence against the horizontal mechanism. The experiment can resume if a compliant first-party route materially reduces acquisition burden without changing the frozen design.</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Research principles</p>
      <h2>What this section tries to preserve</h2>
    </div>
  </div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">01</p>
      <h3>Holdouts stay holdouts</h3>
      <p>Rules and thresholds should be fixed before untouched evaluation periods are opened. Once opened, those periods are not reused to retune the same claim.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">02</p>
      <h3>Reaction is not return</h3>
      <p>A higher directional-reaction rate can justify further mechanism testing without implying positive expectancy, acceptable drawdown, or executable profit.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">03</p>
      <h3>Execution evidence still has boundaries</h3>
      <p>Historical BID/ASK quote crossing is stronger than bar-only reaction evidence, but it is still not actual broker execution and must not be presented as such.</p>
    </article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">Scope</p>
  <h2>Research record, not investment advice.</h2>
  <p>Results shown here are experimental and based on historical or prospective research protocols. They do not establish future profitability and should not be read as a recommendation to trade, increase position size, or adopt a specific strategy.</p>
</section>
