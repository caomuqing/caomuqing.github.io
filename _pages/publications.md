---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

  <!-- You can also find my full list of articles on <a href="https://scholar.google.com/citations?hl=en&user=ddBNGlwAAAAJ">my Google Scholar profile</a>.  -->



{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
