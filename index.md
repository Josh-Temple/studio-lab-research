---
title: Home
description: Studio Lab is a public index of selected research, projects, writing, and methods.
---

<section class="hero dashboard-hero">
  <p class="eyebrow">Studio Lab</p>
  <h1>Research, experiments, and tools—with evidence attached.</h1>
  <p class="lede">A public index of selected work. Research pages show methods and limits; projects link to working tools; writing turns the work into readable explanations. Internal operational state stays separate.</p>
  <div class="hero-actions">
    <a class="button primary" href="{{ '/research/' | relative_url }}">Explore research</a>
    <a class="button secondary" href="{{ '/projects/' | relative_url }}">See projects</a>
  </div>
</section>

<section class="section compact-section" aria-labelledby="areas-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Public dashboard</p>
      <h2 id="areas-title">Four ways into the work</h2>
    </div>
  </div>
  <div class="area-grid">
    <a class="area-card" href="{{ '/research/' | relative_url }}">
      <span class="area-kicker">01</span>
      <h3>Research</h3>
      <p>Questions, methods, observations, limits, and public evidence.</p>
    </a>
    <a class="area-card" href="{{ '/projects/' | relative_url }}">
      <span class="area-kicker">02</span>
      <h3>Projects</h3>
      <p>Selected tools and learning systems that can be tried directly.</p>
    </a>
    <a class="area-card" href="{{ '/writing/' | relative_url }}">
      <span class="area-kicker">03</span>
      <h3>Writing</h3>
      <p>Readable articles that explain findings, design choices, and lessons.</p>
    </a>
    <a class="area-card" href="{{ '/methods/' | relative_url }}">
      <span class="area-kicker">04</span>
      <h3>Methods</h3>
      <p>How claims are bounded, checked, stopped, and prepared for publication.</p>
    </a>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Latest research</p>
      <h2>Published studies</h2>
    </div>
    <a href="{{ '/research/' | relative_url }}">View all</a>
  </div>

  {% assign items = site.research | sort: 'updated' | reverse %}
  {% if items.size > 0 %}
  <div class="research-list">
    {% for item in items limit: 3 %}
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
  <p class="empty-state">No public research pages yet.</p>
  {% endif %}
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Featured projects</p>
      <h2>Tools in use</h2>
    </div>
    <a href="{{ '/projects/' | relative_url }}">Project index</a>
  </div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">Daily use</p>
      <h3><a href="https://circuit-gold.vercel.app/">CIRCUIT</a></h3>
      <p>Two-digit multiplication practice with problem-level review of speed and accuracy.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Learning system</p>
      <h3><a href="https://world-history-lab.vercel.app/">World History Lab</a></h3>
      <p>World history through chronology, causality, comparison, sources, and argument.</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Knowledge infrastructure</p>
      <h3><a href="https://commonplace-sable.vercel.app/">Lumen / Commonplace</a></h3>
      <p>A connected, source-aware knowledge base for reading, research, and publishing.</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Recent writing</p>
      <h2>From the notebook</h2>
    </div>
    <a href="{{ '/writing/' | relative_url }}">View writing</a>
  </div>
  <div class="writing-list">
    <a class="writing-item" href="https://note.com/joshuajosh/n/nc84e060cf7eb">
      <span>2026-08-29</span>
      <strong>公開AI一覧は「件数」だけで比べない</strong>
    </a>
    <a class="writing-item" href="https://note.com/joshuajosh/n/nc074fbf930f1">
      <span>2026-08-27</span>
      <strong>AIに「最新版」を一つにそろえさせる――検索・編集・レビュー・提出の版ずれを防ぐ実務設計</strong>
    </a>
    <a class="writing-item" href="https://note.com/joshuajosh/n/ned9be54efabf">
      <span>2026-08-27</span>
      <strong>AIと研究して見えた「確認しすぎる」という問題</strong>
    </a>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">Boundary</p>
  <h2>Public outputs, not internal telemetry.</h2>
  <p>The public site shows reviewed outputs and their evidence boundaries. Work queues, private data, operational logs, unpublished claims, and live control state belong in the internal dashboard instead.</p>
  <a href="{{ '/about/' | relative_url }}">Read the publishing principles</a>
</section>
