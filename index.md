---
title: Home
description: Studio Lab presents selected public-sector operational reform cases, research, tools, and the evidence behind them.
---

<section class="hero dashboard-hero">
  <p class="eyebrow">Studio Lab</p>
  <h1>Operational reform, research, and tools—with the evidence behind the work.</h1>
  <p class="lede">A public record of selected case studies and research. The portfolio shows how problems are framed and redesigned under real constraints; the research pages show methods, results, and limits—including findings that did not survive stricter tests.</p>
  <div class="hero-actions">
    <a class="button primary" href="{{ '/portfolio/' | relative_url }}">View portfolio</a>
    <a class="button secondary" href="{{ '/research/' | relative_url }}">Explore research</a>
  </div>
</section>

<section class="section compact-section" aria-labelledby="featured-case-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Featured case</p>
      <h2 id="featured-case-title">Scaling digital improvement across a constrained organization</h2>
    </div>
    <a href="{{ '/portfolio/' | relative_url }}">Full case →</a>
  </div>
  <div class="editorial-feature">
    <div class="editorial-feature-main">
      <p class="feature-deck">A public-sector operational reform case built around a practical question: how can useful DX examples move from isolated successes to repeatable organizational capability?</p>
      <p>The work connects case sharing, inquiry redesign, consultation, small experiments, evaluation, and wider adoption. AI is treated as one enabling tool rather than the objective.</p>
    </div>
    <dl class="evidence-note" aria-label="Case study structure">
      <div><dt>01</dt><dd><strong>Problem framing</strong><span>Define the operational constraint before choosing technology.</span></dd></div>
      <div><dt>02</dt><dd><strong>Operating design</strong><span>Show the process, handoffs, controls, and implementation path.</span></dd></div>
      <div><dt>03</dt><dd><strong>Evidence and limits</strong><span>Separate observed results, estimates, assumptions, and unresolved questions.</span></dd></div>
    </dl>
  </div>
</section>

<section class="section" aria-labelledby="featured-finding-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Featured finding</p>
      <h2 id="featured-finding-title">A repeated-looking market story failed a stricter unused-data test</h2>
    </div>
    <a href="{{ '/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">Read study →</a>
  </div>
  <div class="finding-feature">
    <div class="finding-number">
      <span class="finding-kicker">GOLD · 2026H2</span>
      <strong>−1.379 bps</strong>
      <span>mean 15-minute direction-adjusted return</span>
    </div>
    <div class="finding-copy">
      <p class="finding-conclusion">The preregistered unconditional horizontal-touch hypothesis was not supported.</p>
      <p>Across 60 unused sessions, the session-clustered 95% interval was −1.909 to −0.862 bps. Earlier positive reaction evidence remains in the record, but the later result narrows what it can support. The line was closed without tuning the consumed sample to rescue the result.</p>
      <div class="inline-links">
        <a href="{{ '/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">Result and limits</a>
        <a href="{{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">Evidence lineage</a>
        <a href="{{ '/methods/' | relative_url }}">Methods</a>
      </div>
    </div>
  </div>
</section>

<section class="section compact-section evidence-lineage-section" aria-labelledby="evidence-lineage-title">
  <div class="section-heading lineage-heading">
    <div>
      <p class="eyebrow">Evidence lineage</p>
      <h2 id="evidence-lineage-title">One research line, progressively narrower claims</h2>
    </div>
    <a href="{{ '/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">Full evidence record →</a>
  </div>
  <p class="lineage-intro">The studies below do not estimate exactly the same quantity. Read together, they show how a repeated signal-level pattern was tested against increasingly execution-relevant and untouched-data questions instead of being compressed into one headline score.</p>
  <ol class="lineage-track">
    <li class="lineage-step">
      <span class="lineage-index">01</span>
      <div><strong>Reaction-rate signal replicated</strong><span>2024 · 2022 · 2020 · early 2025</span><p>Real horizontal zones showed a higher defined 15-minute reaction rate than the recent-price control across four historical samples.</p></div>
    </li>
    <li class="lineage-step">
      <span class="lineage-index">02</span>
      <div><strong>Historical execution-aware check</strong><span>2019 · positive under its specification</span><p>Observed BID/ASK quote crossing remained positive in a separate historical validation, while still falling short of live broker execution.</p></div>
    </li>
    <li class="lineage-step">
      <span class="lineage-index">03</span>
      <div><strong>Entry geometry became the question</strong><span>2026H1 · exploratory diagnosis</span><p>Touch-to-confirmed-entry movement was favorable on average while post-entry movement was adverse, suggesting that selection around confirmation mattered.</p></div>
    </li>
    <li class="lineage-step lineage-step-terminal">
      <span class="lineage-index">04</span>
      <div><strong>Unused-data test did not support the unconditional claim</strong><span>2026H2 · preregistered · 60 sessions</span><p>The unconditional touch mean was −1.379 bps, so that research line was closed without tuning the consumed sample to rescue it.</p></div>
    </li>
  </ol>
</section>

<section class="section">
  <div class="section-heading">
    <div><p class="eyebrow">Latest research</p><h2>Recent published studies</h2></div>
    <a href="{{ '/research/' | relative_url }}">View all →</a>
  </div>
  {% assign items = site.research | sort: 'updated' | reverse %}
  {% if items.size > 0 %}
  <div class="research-list">
    {% for item in items limit: 3 %}
    <article class="research-item">
      <div><h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>{% if item.summary %}<p>{{ item.summary }}</p>{% endif %}</div>
      {% if item.status %}<span class="status">{{ item.status }}</span>{% endif %}
    </article>
    {% endfor %}
  </div>
  {% else %}<p class="empty-state">No public research pages yet.</p>{% endif %}
</section>

<section class="section compact-section" aria-labelledby="explore-title">
  <div class="section-heading">
    <div><p class="eyebrow">Explore</p><h2 id="explore-title">Other ways into the work</h2></div>
  </div>
  <div class="link-grid">
    <a class="link-panel" href="{{ '/projects/' | relative_url }}"><span>Projects</span><strong>Working tools and learning systems</strong><small>Things that can be tried directly.</small></a>
    <a class="link-panel" href="{{ '/writing/' | relative_url }}"><span>Writing</span><strong>Readable notes and articles</strong><small>Findings and design decisions in plain language.</small></a>
    <a class="link-panel" href="{{ '/methods/' | relative_url }}"><span>Methods</span><strong>How claims are bounded and checked</strong><small>Methods, stop conditions, and publication discipline.</small></a>
    <a class="link-panel" href="{{ '/market/' | relative_url }}"><span>Market</span><strong>Public market observation</strong><small>Descriptive data only, separated from trading decisions.</small></a>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">Boundary</p>
  <h2>Public outputs, not internal telemetry.</h2>
  <p>The site publishes reviewed outputs and their evidence boundaries. Work queues, private data, operational logs, unpublished claims, live positions, and current trading decisions remain outside the public layer.</p>
  <a href="{{ '/about/' | relative_url }}">Read the publishing principles</a>
</section>
