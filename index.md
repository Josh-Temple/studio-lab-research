---
title: Home
description: Studio Lab Research publishes research questions, methods, findings, limits, and supporting evidence.
---

<section class="hero">
  <p class="eyebrow">Studio Lab Research</p>
  <h1>Research that shows its work.</h1>
  <p class="lede">A public record of research questions, methods, findings, limits, and supporting evidence. The site is designed to distinguish what was observed from what remains uncertain.</p>
  <div class="hero-actions">
    <a class="button primary" href="{{ '/research/' | relative_url }}">Browse research</a>
    <a class="button secondary" href="{{ '/about/' | relative_url }}">How this site works</a>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Research</p>
      <h2>Public studies</h2>
    </div>
    <a href="{{ '/research/' | relative_url }}">View all</a>
  </div>

  {% assign items = site.research | sort: 'updated' | reverse %}
  {% if items.size > 0 %}
  <div class="research-list">
    {% for item in items limit: 5 %}
    <article class="research-item">
      <div>
        <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
      </div>
      {% if item.status %}<span class="status">{{ item.status }}</span>{% endif %}
    </article>
    {% endfor %}
  </div>
  {% else %}
  <p class="empty-state">No research pages have been published yet. Research is added only after its public scope and claims are reviewed.</p>
  {% endif %}
</section>
