---
title: Research
permalink: /research/
description: Public Studio Lab research, with methods, findings, limits, and evidence links.
---

<p class="eyebrow">Research</p>
<h1>Studies and investigations</h1>
<p class="lede">Each page separates the research question, method, observations, interpretation, limitations, and supporting material where it can be shared publicly.</p>

<section class="section">
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
