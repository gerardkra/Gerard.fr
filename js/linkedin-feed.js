// js/linkedin-feed.js - Intégration LinkedIn
// Auteur: Gérard KRA
// Date: 2024-06-15

/*
 * NOTE IMPORTANTE :
 * LinkedIn ne fournit pas d'API publique gratuite pour récupérer les posts.
 * Les options sont :
 * 1. Utiliser le widget LinkedIn Profile Badge (déjà intégré dans linkedin.html)
 * 2. Utiliser l'API LinkedIn officielle (nécessite OAuth et clés API payantes)
 * 3. Embed manuel des posts individuels
 * 
 * Pour ce projet, nous utilisons l'approche #1 (widget) + #3 (embeds manuels)
 */

const LINKEDIN_PROFILE_URL = 'https://www.linkedin.com/in/gérardkra-data-engineer-devops-nlp-data-science-telecom';

class LinkedInIntegration {
  constructor() {
    this.profileURL = LINKEDIN_PROFILE_URL;
    this.init();
  }

  init() {
    // Charger le script LinkedIn si nécessaire
    if (!document.querySelector('script[src*="platform.linkedin.com"]')) {
      this.loadLinkedInScript();
    }

    // Initialiser les embeds de posts si présents
    this.initPostEmbeds();
  }

  // Charger le script LinkedIn Platform
  loadLinkedInScript() {
    const script = document.createElement('script');
    script.src = 'https://platform.linkedin.com/badges/js/profile.js';
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
  }

  // Initialiser les embeds de posts LinkedIn
  initPostEmbeds() {
    const embedContainers = document.querySelectorAll('.linkedin-post-embed');
    
    embedContainers.forEach(container => {
      const postURL = container.getAttribute('data-post-url');
      if (postURL) {
        this.createPostEmbed(container, postURL);
      }
    });
  }

  // Créer un embed de post LinkedIn
  createPostEmbed(container, postURL) {
    // LinkedIn permet d'embed des posts via iframe
    // Format: https://www.linkedin.com/embed/feed/update/urn:li:share:XXXX
    
    const iframe = document.createElement('iframe');
    iframe.src = postURL;
    iframe.style.width = '100%';
    iframe.style.height = '600px';
    iframe.style.border = 'none';
    iframe.style.borderRadius = '12px';
    iframe.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
    
    container.appendChild(iframe);
  }

  // Créer le badge profil LinkedIn
  createProfileBadge(container) {
    const badge = document.createElement('div');
    badge.className = 'badge-base LI-profile-badge';
    badge.setAttribute('data-locale', 'fr_FR');
    badge.setAttribute('data-size', 'large');
    badge.setAttribute('data-theme', 'light');
    badge.setAttribute('data-type', 'VERTICAL');
    badge.setAttribute('data-vanity', 'gérardkra-data-engineer-devops-nlp-data-science-telecom');
    badge.setAttribute('data-version', 'v1');
    
    const link = document.createElement('a');
    link.className = 'badge-base__link LI-simple-link';
    link.href = this.profileURL;
    link.textContent = 'Gérard KRA';
    
    badge.appendChild(link);
    container.appendChild(badge);
  }

  // Fonction helper pour ouvrir le profil LinkedIn
  openProfile() {
    window.open(this.profileURL, '_blank');
  }

  // Fonction pour créer des cartes de posts manuellement
  // (À utiliser si vous voulez afficher des posts spécifiques)
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
          <div style="font-size: 0.85rem; color: #888;">${postData.date || 'Il y a quelques jours'}</div>
        </div>
      </div>
      <p style="color: var(--text-color); line-height: 1.6; margin: 1rem 0;">
        ${postData.content || ''}
      </p>
      ${postData.image ? `<img src="${postData.image}" alt="Post image" style="width: 100%; border-radius: 8px; margin: 1rem 0;">` : ''}
      <div style="display: flex; gap: 1rem; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
        <button style="background: none; border: none; color: #0077b5; cursor: pointer; font-size: 0.9rem;">👍 J'aime</button>
        <button style="background: none; border: none; color: #0077b5; cursor: pointer; font-size: 0.9rem;">💬 Commenter</button>
        <button style="background: none; border: none; color: #0077b5; cursor: pointer; font-size: 0.9rem;">🔄 Partager</button>
      </div>
      ${postData.postURL ? `
        <a href="${postData.postURL}" target="_blank" style="display: inline-block; margin-top: 1rem; color: #0077b5; text-decoration: none; font-weight: 600;">
          Voir le post complet sur LinkedIn →
        </a>
      ` : ''}
    `;

    return card;
  }
}

// Initialiser quand le DOM est prêt
document.addEventListener('DOMContentLoaded', () => {
  window.linkedInIntegration = new LinkedInIntegration();

  // Exemple d'utilisation pour afficher des posts manuels
  const postsContainer = document.getElementById('linkedin-posts-container');
  
  if (postsContainer) {
    // Exemple de posts (à remplacer par vos vrais posts)
    const examplePosts = [
      {
        author: 'Gérard Kra',
        authorInitials: 'GK',
        date: 'Il y a 2 jours',
        content: '🚀 Ravi de partager que je commence mon alternance en Data Engineering ! Hâte de mettre en pratique mes compétences en Big Data et Machine Learning. #DataScience #BigData #Alternance',
        postURL: 'https://www.linkedin.com/in/gérardkra-data-engineer-devops-nlp-data-science-telecom'
      },
      {
        author: 'Gérard Kra',
        authorInitials: 'GK',
        date: 'Il y a 1 semaine',
        content: '📚 Nouveau site web en ligne ! Je partage maintenant tous mes cours, TD, TP et ressources d\'apprentissage gratuitement. L\'objectif : aider les étudiants qui suivent un parcours similaire au mien. Lien dans les commentaires ! #Education #Partage #DataScience',
        postURL: 'https://www.linkedin.com/in/gérardkra-data-engineer-devops-nlp-data-science-telecom'
      }
    ];

    // Afficher les posts
    examplePosts.forEach(postData => {
      const postCard = window.linkedInIntegration.createManualPostCard(postData);
      postsContainer.appendChild(postCard);
    });
  }

  // Gestion du bouton "Voir mon profil LinkedIn"
  const linkedInButtons = document.querySelectorAll('[data-action="open-linkedin"]');
  linkedInButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      e.preventDefault();
      window.linkedInIntegration.openProfile();
    });
  });
});

// Fonction utilitaire pour ajouter un post manuellement depuis la console
// Usage: addLinkedInPost({ content: 'Mon nouveau post...', date: 'Aujourd\'hui' })
window.addLinkedInPost = function(postData) {
  const container = document.getElementById('linkedin-posts-container');
  if (container && window.linkedInIntegration) {
    const postCard = window.linkedInIntegration.createManualPostCard(postData);
    container.prepend(postCard);
  } else {
    console.error('Container "linkedin-posts-container" not found');
  }
};

// Export pour utilisation dans d'autres scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = LinkedInIntegration;
}

/*
 * INSTRUCTIONS D'UTILISATION :
 * 
 * 1. Pour afficher le widget profil LinkedIn :
 *    - Le code est déjà dans professionnel/linkedin.html
 *    - Le widget se charge automatiquement
 * 
 * 2. Pour afficher des posts spécifiques :
 *    - Allez sur votre post LinkedIn
 *    - Cliquez sur "..." → "Intégrer ce post"
 *    - Copiez l'URL d'embed
 *    - Utilisez createPostEmbed() avec cette URL
 * 
 * 3. Pour créer des cartes de posts manuellement :
 *    - Ajoutez un div avec id="linkedin-posts-container" dans votre HTML
 *    - Ce script créera automatiquement des cartes stylisées
 *    - Modifiez le tableau examplePosts avec vos vrais posts
 * 
 * 4. Alternative simple :
 *    - Utilisez juste le widget badge (déjà intégré)
 *    - Ajoutez un bouton "Voir mes posts" qui ouvre votre profil LinkedIn
 */