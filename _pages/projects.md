---
layout: page
title: "Projects"
permalink: /projects/
author_profile: true
---

<div class="projects-container">
  {% assign projects_by_year = site.projects | group_by_exp: "post", "post.date | date: '%Y'" | sort: "name" | reverse %}
  
  {% for year_group in projects_by_year %}
    <div class="year-section">
      <h2 class="year-header">{{ year_group.name }}</h2>
      <div class="projects-grid">
        {% for post in year_group.items %}
          {% include project-card.html %}
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
