// js/linkedin-feed.js

class LinkedInIntegration {
  constructor() {
    this.profileURL = 'https://www.linkedin.com/in/gérardkra-data-engineer-devops-nlp-data-science-telecom';
    
  }

  createManualPostCard(postData) {
    const card = document.createElement('div');
    card.className = 'linkedin-post-card';
    card.style.cssText = `
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow);
      border-left: 4px solid #0077b5;
    `;

    card.innerHTML = `
      <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
        <div style="width: 48px; height: 48px; background: #0077b5; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 1.2rem;">
          ${postData.authorInitials || 'GK'}
        </div>
        <div>
          <strong style="color: var(--text-color);">${postData.author || 'Gérard Kra'}</strong>
          <div style="font-size: 0.85rem; color: #888;">${postData.date || ''}</div>
        </div>
      </div>
      <p style="color: var(--text-color); line-height: 1.6; margin: 1rem 0;">
        ${postData.content || ''}
      </p>
      ${postData.image ? `<img src="${postData.image}" alt="Post image" style="width: 100%; border-radius: 8px; margin: 1rem 0;">` : ''}
      ${postData.postURL ? `
        <a href="${postData.postURL}" target="_blank" style="display: inline-block; margin-top: 1rem; color: #0077b5; text-decoration: none; font-weight: 600;">
          Voir le post complet sur LinkedIn →
        </a>
      ` : ''}
    `;

    return card;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.linkedInIntegration = new LinkedInIntegration();
});

// Ajouter un post depuis la console :
// addLinkedInPost({ content: 'Mon post...', date: 'Aujourd\'hui' })
window.addLinkedInPost = function(postData) {
  const container = document.getElementById('linkedin-posts-container');
  if (container && window.linkedInIntegration) {
    container.prepend(window.linkedInIntegration.createManualPostCard(postData));
  }
};