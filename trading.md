---
title: Trading
permalink: /trading/
description: Reviewed Studio Lab trading research, including development tests, holdouts, independent validations, risk controls, and negative results.
---

<p class="eyebrow">Trading research</p>
<h1>Test the edge before trusting the story.</h1>
<p class="lede">Selected systematic-trading research from Studio Lab. This section publishes reviewed development results, holdouts, independent validations, and negative or mixed findings while keeping unresolved hypotheses separate. It is not a live trading dashboard, signal service, or record of current positions.</p>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Published results</p>
      <h2>What has survived review</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD horizontal levels · development</p>
      <h3><a href="{{ '/research/gold-horizontal-recent-price-control-development/' | relative_url }}">Rolling-extrema zones outperformed a recent-price control in development</a></h3>
      <p>Across all 60 sealed 2024 sessions, the equal-weight 15-minute directional-reaction rate was 79.78% for real zones versus 53.23% for the control. The primary difference was +26.55 percentage points with a 95% bootstrap interval of +21.23 to +31.82 points.</p>
      <p class="card-links"><a href="{{ '/research/gold-horizontal-recent-price-control-development/' | relative_url }}">Read the development study</a></p>
    </article>
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
      <h2>Independent replication is now the decision gate</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD horizontal levels · 2022 validation preregistered</p>
      <h3>Repeat the same mechanism before adding more variables</h3>
      <p>The next test uses the first 60 structurally eligible 2022 UTC sessions from 2022-01-03 onward, with the same rolling-extrema definition, recent-price control, 15-minute reaction outcome, session estimator, design gate, and classification rule.</p>
      <p class="card-links">No 2022 horizontal-line or control reaction outcome had been inspected or computed when the validation protocol was frozen.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Range persistence · deprioritized</p>
      <h3>Do not rescue a weak independent result after seeing it</h3>
      <p>The 2021 validation period is consumed for the previous-session range mechanism. The current plan does not retune the same mechanism on 2021 or automatically add another holdout to rescue it.</p>
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
      <h3>Simple baselines matter</h3>
      <p>More complex filters and forecasting models are not promoted merely because they sound sophisticated. They need incremental value against a simpler comparison.</p>
    </article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">Scope</p>
  <h2>Research record, not investment advice.</h2>
  <p>Results shown here are experimental and may be based on historical or simulated data. They do not establish future profitability and should not be read as a recommendation to trade, increase position size, or adopt a specific strategy.</p>
</section>
