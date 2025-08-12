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

<script>
// Custom sorting to put first-author papers first, with special handling for specific papers
document.addEventListener('DOMContentLoaded', function() {
  const yearSections = document.querySelectorAll('.year-section');
  
  yearSections.forEach(function(yearSection) {
    const publicationsGrid = yearSection.querySelector('.publications-grid');
    const cards = Array.from(publicationsGrid.querySelectorAll('.publication-card'));
    
    // Sort cards: first-author papers first, then others
    cards.sort(function(a, b) {
      const aAuthors = a.querySelector('.publication-authors');
      const bAuthors = b.querySelector('.publication-authors');
      
      // Check if "Cao, M." appears first in the author list
      const aIsFirstAuthor = aAuthors && aAuthors.textContent.trim().startsWith('Cao, M.');
      const bIsFirstAuthor = bAuthors && bAuthors.textContent.trim().startsWith('Cao, M.');
      
      // Special case: if both are first-author papers, check for the specific system identification paper
      if (aIsFirstAuthor && bIsFirstAuthor) {
        const aTitle = a.querySelector('.publication-title').textContent.trim();
        const bTitle = b.querySelector('.publication-title').textContent.trim();
        
        // Move the system identification paper to the end of first-author papers
        if (aTitle.includes('System identification and control of the ground operation mode')) {
          return 1; // Move a to the end
        }
        if (bTitle.includes('System identification and control of the ground operation mode')) {
          return -1; // Move b to the end
        }
      }
      
      if (aIsFirstAuthor && !bIsFirstAuthor) return -1;
      if (!aIsFirstAuthor && bIsFirstAuthor) return 1;
      return 0;
    });
    
    // Reorder the cards in the DOM and add first-author class
    cards.forEach(function(card) {
      const authors = card.querySelector('.publication-authors');
      const isFirstAuthor = authors && authors.textContent.trim().startsWith('Cao, M.');
      
      if (isFirstAuthor) {
        card.classList.add('first-author');
      }
      
      publicationsGrid.appendChild(card);
    });
  });
});
</script>
