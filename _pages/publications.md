---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

<div class="publications-intro">
  <p>You can also find my full list of articles on <a href="https://scholar.google.com/citations?hl=en&user=ddBNGlwAAAAJ">my Google Scholar profile</a>.</p>
</div>

<div class="publications-container">
  {% assign publications_by_year = site.publications | group_by_exp: "post", "post.date | date: '%Y'" | sort: "name" | reverse %}
  
  {% for year_group in publications_by_year %}
    <div class="year-section">
      <h2 class="year-header">{{ year_group.name }}</h2>
      <div class="publications-grid">
        {% for post in year_group.items %}
          {% include publication-card.html %}
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
