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
      <p>Holdout tests, tail-risk controls, simple baselines, and the difference between reducing risk and improving profit.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Research methodology</p>
      <h3><a href="{{ '/research/openalex-bridge-adoption-lag/' | relative_url }}">Validity gates and methodological non-results</a></h3>
      <p>Research designs that stop before the primary comparison when the evidence needed for interpretation does not meet a pre-set threshold.</p>
    </article>
  </div>
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
