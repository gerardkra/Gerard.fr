// js/github-api.js

const GITHUB_USERNAME = 'gerardkra';

class GitHubAPI {
  constructor(username) {
    this.username = username;
    this.baseURL = 'https://api.github.com';
  }

  async getUserProfile() {
    try {
      const response = await fetch(`${this.baseURL}/users/${this.username}`);
      if (!response.ok) throw new Error('Erreur lors de la récupération du profil');
      return await response.json();
    } catch (error) {
      console.error('Erreur GitHub profile:', error);
      return null;
    }
  }

  async getRepositories(sort = 'updated', perPage = 12) {
    try {
      const response = await fetch(
        `${this.baseURL}/users/${this.username}/repos?sort=${sort}&per_page=${perPage}&type=owner`
      );
      if (!response.ok) throw new Error('Erreur lors de la récupération des repos');
      return await response.json();
    } catch (error) {
      console.error('Erreur GitHub repos:', error);
      return [];
    }
  }

  formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', { year: 'numeric', month: 'long', day: 'numeric' });
  }

  createRepoCard(repo) {
    const card = document.createElement('div');
    card.className = 'repo-card slide-in';

    const languageColor = this.getLanguageColor(repo.language);

    card.innerHTML = `
      <div class="repo-header">
        <h3>
          <a href="${repo.html_url}" target="_blank" rel="noopener">
            ${repo.name}
          </a>
        </h3>
        ${repo.private
          ? '<span class="repo-badge private">Privé</span>'
          : '<span class="repo-badge public">Public</span>'}
      </div>

      <p class="repo-description">
        ${repo.description || 'Pas de description disponible'}
      </p>

      <div class="repo-stats">
        ${repo.language ? `
          <span class="repo-language">
            <span class="language-dot" style="background: ${languageColor};"></span>
            ${repo.language}
          </span>
        ` : ''}
      </div>

      <div class="repo-footer">
        <span class="repo-updated">Mis à jour: ${this.formatDate(repo.updated_at)}</span>
        <a href="${repo.html_url}" class="btn btn-outline btn-small" target="_blank">
          Voir sur GitHub →
        </a>
      </div>
    `;

    return card;
  }

  createProfileStats(profile) {
    return `
      <div class="github-stats">
        <div class="stat-item">
          <div class="stat-number">${profile.public_repos}</div>
          <div class="stat-label">Dépôts</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">${profile.followers}</div>
          <div class="stat-label">Abonnés</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">${profile.following}</div>
          <div class="stat-label">Abonnements</div>
        </div>
      </div>
    `;
  }

  getLanguageColor(language) {
    const colors = {
      'JavaScript': '#f1e05a',
      'Python': '#3572A5',
      'Java': '#b07219',
      'TypeScript': '#2b7489',
      'C++': '#f34b7d',
      'C': '#555555',
      'Go': '#00ADD8',
      'Rust': '#dea584',
      'Ruby': '#701516',
      'PHP': '#4F5D95',
      'Swift': '#ffac45',
      'Kotlin': '#F18E33',
      'R': '#198CE7',
      'Julia': '#a270ba',
      'HTML': '#e34c26',
      'CSS': '#563d7c',
      'Shell': '#89e051',
      'Jupyter Notebook': '#DA5B0B',
    };
    return colors[language] || '#8c8c8c';
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  const githubAPI = new GitHubAPI(GITHUB_USERNAME);

  const profileStatsContainer = document.getElementById('github-profile-stats');
  const reposContainer = document.getElementById('github-repos');
  const loadingIndicator = document.getElementById('loading-repos');

  if (!reposContainer) return;

  try {
    if (loadingIndicator) loadingIndicator.style.display = 'block';

    const profile = await githubAPI.getUserProfile();
    if (profile && profileStatsContainer) {
      profileStatsContainer.innerHTML = githubAPI.createProfileStats(profile);
    }

    const repos = await githubAPI.getRepositories('updated', 12);

    if (loadingIndicator) loadingIndicator.style.display = 'none';

    if (repos && repos.length > 0) {
      reposContainer.innerHTML = '';
      repos.forEach(repo => reposContainer.appendChild(githubAPI.createRepoCard(repo)));

      setTimeout(() => {
        document.querySelectorAll('.repo-card').forEach((card, index) => {
          setTimeout(() => card.classList.add('visible'), index * 100);
        });
      }, 100);

    } else {
      reposContainer.innerHTML = '<p style="text-align: center; color: #888;">Aucun repository trouvé.</p>';
    }

  } catch (error) {
    console.error('Erreur lors du chargement des repos GitHub:', error);
    if (reposContainer) {
      reposContainer.innerHTML = `
        <div class="error-message" style="text-align: center; padding: 2rem; color: #888;">
          <p>⚠️ Impossible de charger les repositories pour le moment.</p>
          <p style="margin-top: 0.5rem;">
            <a href="https://github.com/${GITHUB_USERNAME}" target="_blank" class="btn">
              Voir sur GitHub →
            </a>
          </p>
        </div>
      `;
    }
    if (loadingIndicator) loadingIndicator.style.display = 'none';
  }
});