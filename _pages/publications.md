---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

<style>
/* Ensure first-author highlighting works on GitHub Pages */
.publication-card.first-author {
  border: 2px solid #6c757d !important;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
  position: relative !important;
}

.publication-card.first-author::after {
  content: '👑 First Author' !important;
  position: absolute !important;
  top: 1rem !important;
  right: 1rem !important;
  background: linear-gradient(135deg, #6c757d 0%, #495057 100%) !important;
  color: white !important;
  padding: 0.3rem 0.8rem !important;
  border-radius: 20px !important;
  font-size: 0.75rem !important;
  font-weight: 700 !important;
  box-shadow: 0 2px 8px rgba(108, 117, 125, 0.3) !important;
  z-index: 10 !important;
}

.publication-card.first-author::before {
  background: linear-gradient(90deg, #6c757d 0%, #495057 100%) !important;
}

.author-highlight {
  background: linear-gradient(135deg, #e9ecef 0%, #dee2e6 100%) !important;
  padding: 0.2rem 0.5rem !important;
  border-radius: 4px !important;
  box-shadow: 0 2px 4px rgba(108, 117, 125, 0.2) !important;
  color: #495057 !important;
  font-weight: 700 !important;
  text-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
  position: relative !important;
  display: inline-block !important;
}

.author-highlight::before {
  content: '👑' !important;
  margin-right: 0.3rem !important;
  font-size: 0.9em !important;
}
</style>

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
function sortPublications() {
  try {
    const yearSections = document.querySelectorAll('.year-section');
    
    yearSections.forEach(function(yearSection) {
      const publicationsGrid = yearSection.querySelector('.publications-grid');
      if (!publicationsGrid) return;
      
      const cards = Array.from(publicationsGrid.querySelectorAll('.publication-card'));
      if (cards.length === 0) return;
      
      // Sort cards: first-author papers first, then others
      cards.sort(function(a, b) {
        const aAuthors = a.querySelector('.publication-authors');
        const bAuthors = b.querySelector('.publication-authors');
        
        if (!aAuthors || !bAuthors) return 0;
        
        // Check if "Cao, M." appears first in the author list
        const aIsFirstAuthor = aAuthors.textContent.trim().startsWith('Cao, M.');
        const bIsFirstAuthor = bAuthors.textContent.trim().startsWith('Cao, M.');
        
        // Special case: if both are first-author papers, check for the specific system identification paper
        if (aIsFirstAuthor && bIsFirstAuthor) {
          const aTitle = a.querySelector('.publication-title');
          const bTitle = b.querySelector('.publication-title');
          
          if (!aTitle || !bTitle) return 0;
          
          // Move the system identification paper to the end of first-author papers
          if (aTitle.textContent.includes('System identification and control of the ground operation mode')) {
            return 1; // Move a to the end
          }
          if (bTitle.textContent.includes('System identification and control of the ground operation mode')) {
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
        if (authors) {
          const isFirstAuthor = authors.textContent.trim().startsWith('Cao, M.');
          
          if (isFirstAuthor) {
            card.classList.add('first-author');
          }
        }
        
        publicationsGrid.appendChild(card);
      });
    });
    
    console.log('Publications sorted successfully');
  } catch (error) {
    console.error('Error sorting publications:', error);
  }
}

// Multiple ways to ensure the script runs
document.addEventListener('DOMContentLoaded', sortPublications);

// Fallback for when DOMContentLoaded has already fired
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', sortPublications);
} else {
  // DOM is already loaded, run immediately
  sortPublications();
}

// Additional fallback with a small delay
setTimeout(sortPublications, 100);
</script>
