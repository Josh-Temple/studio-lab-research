---
title: Research
permalink: /research/
description: Public Studio Lab research, with methods, findings, limits, and evidence links.
---

<p class="eyebrow">Research</p>
<h1>Studies and investigations</h1>
<p class="lede">Each page separates the research question, method, observations, interpretation, limitations, and supporting material where it can be shared publicly.</p>

<section class="section compact-section" aria-labelledby="research-lines-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Research lines</p>
      <h2 id="research-lines-title">Start with the question, then follow the evidence</h2>
    </div>
  </div>
  <div class="research-line-list">
    <a class="research-line" href="{{ '/trading/' | relative_url }}">
      <span class="research-line-index">01</span>
      <div>
        <span class="research-line-kicker">Trading</span>
        <strong>Systematic trading research</strong>
        <p>Development tests, untouched validations, replication across periods, execution-aware checks, and negative results.</p>
      </div>
    </a>
    <a class="research-line" href="{{ '/research/openalex-bridge-adoption-lag/' | relative_url }}">
      <span class="research-line-index">02</span>
      <div>
        <span class="research-line-kicker">Research methodology</span>
        <strong>Validity gates and methodological non-results</strong>
        <p>Research designs that stop before the primary comparison when the evidence needed for interpretation does not meet a pre-set threshold.</p>
      </div>
    </a>
    <a class="research-line" href="{{ '/research/heckerman-replicability-bounded-replication/' | relative_url }}">
      <span class="research-line-index">03</span>
      <div>
        <span class="research-line-kicker">Reproducibility</span>
        <strong>Bounded replication checks</strong>
        <p>Small, pre-specified recomputations that verify one reported numeric relation without expanding the claim to a paper's broader conclusions.</p>
      </div>
    </a>
  </div>
</section>

<section class="section compact-section">
  <div class="section-heading">
    <div><p class="eyebrow">Current direction · reviewed 2026-09-25</p><h2>One bounded public-data test reached a result; retrieval still gates the rest</h2></div>
    <a href="{{ '/research/noaa-mauna-loa-co2-2025-seasonal-amplitude/' | relative_url }}">Read the new study</a>
  </div>
  <p class="lede">The latest completed non-trading test used NOAA GML's official Mauna Loa monthly CO₂ file. After fixing the source representation and monthly-average field before opening the 2025 values, the 12-month max-minus-min amplitude was 6.14 ppm, above the pre-specified 5 ppm threshold. Several other public-data candidates remained on hold because their exact machine-readable retrieval path or representation could not be verified without substitution. Trading research has not produced a newer confirmatory performance result; its latest work remains focused on coverage, source fidelity, and unopened tests.</p>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">All research</p>
      <h2>Published studies</h2>
    </div>
  </div>
  <p class="registry-note">The research lines above are curated entry points. This list remains the full public record, including negative and stopped studies.</p>
  {% assign items = site.research | sort: 'updated' | reverse %}
  {% if items.size > 0 %}
  <div class="research-list">
    {% for item in items %}
    <article class="research-item">
      <div>
        <p class="research-entry-meta">
          {% if item.topic %}<span>{{ item.topic }}</span>{% endif %}
          {% if item.updated %}<time datetime="{{ item.updated }}">{{ item.updated }}</time>{% endif %}
        </p>
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
