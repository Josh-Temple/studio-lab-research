---
title: Trading
permalink: /trading/
description: Reviewed Studio Lab trading research, including development tests, holdouts, independent validations, execution-aware checks, risk controls, and negative results.
---

<p class="eyebrow">Trading research</p>
<h1>Test the edge before trusting the story.</h1>
<p class="lede">Selected systematic-trading research from Studio Lab. This section publishes reviewed development results, holdouts, independent validations, execution-aware checks, and negative or mixed findings while keeping unresolved hypotheses separate. It is not a live trading dashboard, signal service, or record of current positions.</p>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Current evidence</p>
      <h2>GOLD horizontal levels have moved beyond one development sample</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD horizontal levels · replicated / execution-aware</p>
      <h3><a href="{{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">The reaction effect replicated across three periods and remained positive in one quote-crossing validation</a></h3>
      <p>The frozen real-minus-control 15-minute reaction effect was +26.55 pp in 2024 development, +23.79 pp in the independent 2022 validation, and +25.44 pp in the 2020 robustness replication. A prospectively amended 2019 validation using observed BID/ASK quote crossing produced a +1.189 bps real mean and +3.498 bps real-minus-control difference.</p>
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
      <p class="eyebrow">Current research</p>
      <h2>2018 execution-aware replication is the next decision gate</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD horizontal levels · 2018 replication in progress</p>
      <h3>Repeat the 2019 quote-crossing specification on another unused period</h3>
      <p>The first 50 of the required 60 structurally eligible 2018 sessions have been verified, with 7 candidate dates excluded under the frozen rules. The official data interface then became temporarily unresponsive at the 2018-03-21 candidate.</p>
      <p class="card-links">No 2018 signal event, return, primary estimate, bootstrap interval, or classification has been computed or inspected. A versioned successor is ready to resume from the same boundary.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">2019 execution-aware validation · important limit</p>
      <h3>Positive historical quote crossing is not the same as a live edge</h3>
      <p>The 2019 test used observed historical BID/ASK quotes, but it did not model commissions, extra slippage, latency, rejection, market impact, position sizing, drawdown, or broker-specific fills. Those remain separate questions.</p>
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
  <p>Results shown here are experimental and based on historical data. They do not establish future profitability and should not be read as a recommendation to trade, increase position size, or adopt a specific strategy.</p>
</section>
