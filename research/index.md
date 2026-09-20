---
title: Research
permalink: /research/
description: Public Studio Lab research, with methods, findings, limits, and evidence links.
---

<p class="eyebrow">Research</p>
<h1>Studies and investigations</h1>
<p class="lede">Each page separates the research question, method, observations, interpretation, limitations, and supporting material where it can be shared publicly.</p>

<section class="section compact-section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Research areas</p>
      <h2>Browse by line of work</h2>
    </div>
  </div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">Trading</p>
      <h3><a href="{{ '/trading/' | relative_url }}">Systematic trading research</a></h3>
      <p>Development tests, untouched validations, replication across periods, execution-aware checks, negative results, and the difference between a repeatable market reaction and a tradable edge.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Research methodology</p>
      <h3><a href="{{ '/research/openalex-bridge-adoption-lag/' | relative_url }}">Validity gates and methodological non-results</a></h3>
      <p>Research designs that stop before the primary comparison when the evidence needed for interpretation does not meet a pre-set threshold.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Reproducibility checks</p>
      <h3><a href="{{ '/research/heckerman-replicability-bounded-replication/' | relative_url }}">Bounded replication checks</a></h3>
      <p>Small, pre-specified recomputations that verify one reported numeric relation without expanding the claim to the source paper's full conclusions.</p>
    </article>
  </div>
</section>

<section class="section compact-section">
  <div class="section-heading">
    <div><p class="eyebrow">Current direction · reviewed 2026-09-20</p><h2>Finish pre-outcome decisions, then open the test</h2></div>
    <a href="{{ '/trading/' | relative_url }}">Full trading status</a>
  </div>
  <p class="lede">No newer confirmatory trading-performance result has replaced the unused-data GOLD result above. Current work is moving independent cross-market and medium-horizon candidates toward executable tests while keeping outcomes closed. When a scientific condition has no unique pre-outcome default, the line now stops at a human boundary rather than letting automation choose from performance.</p>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">All research</p>
      <h2>Published studies</h2>
    </div>
  </div>
  {% assign items = site.research | sort: 'updated' | reverse %}
  {% if items.size > 0 %}
  <div class="research-list">
    {% for item in items %}
    <article class="research-item">
      <div>
        <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
        {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
      </div>
      {% if item.status %}<span class="status">{{ item.status }}</span>{% endif %}
    </article>
    {% endfor %}
  </div>
  {% else %}
  <p class="empty-state">No public research pages yet.</p>
  {% endif %}
</section>
