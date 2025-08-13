// Custom sorting to put first-author papers first, with special handling for specific papers
function sortPublications() {
  try {
    console.log('Starting publication sorting...');
    
    const yearSections = document.querySelectorAll('.year-section');
    console.log('Found year sections:', yearSections.length);
    
    yearSections.forEach(function(yearSection, yearIndex) {
      const publicationsGrid = yearSection.querySelector('.publications-grid');
      if (!publicationsGrid) {
        console.log('No publications grid found in year section', yearIndex);
        return;
      }
      
      const cards = Array.from(publicationsGrid.querySelectorAll('.publication-card'));
      console.log('Found cards in year', yearIndex, ':', cards.length);
      
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
      cards.forEach(function(card, cardIndex) {
        const authors = card.querySelector('.publication-authors');
        if (authors) {
          const isFirstAuthor = authors.textContent.trim().startsWith('Cao, M.');
          
          if (isFirstAuthor) {
            card.classList.add('first-author');
            console.log('Added first-author class to card', cardIndex, 'in year', yearIndex);
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
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOMContentLoaded fired, running sortPublications');
  sortPublications();
});

// Fallback for when DOMContentLoaded has already fired
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', sortPublications);
} else {
  // DOM is already loaded, run immediately
  console.log('DOM already loaded, running sortPublications immediately');
  sortPublications();
}

// Additional fallback with a small delay
setTimeout(function() {
  console.log('Timeout fallback, running sortPublications');
  sortPublications();
}, 100);

// Additional fallback with a longer delay for slow-loading pages
setTimeout(function() {
  console.log('Long timeout fallback, running sortPublications');
  sortPublications();
}, 1000); 