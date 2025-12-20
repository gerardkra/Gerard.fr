// js/translation.js - Système de traduction FR/EN avec sauvegarde globale
// Auteur: Gérard KRA
// Date: 2024-06-15

const translations = {
  fr: {
    // Navigation
    'nav.home': 'Accueil',
    'nav.about': 'À propos',
    'nav.parcours': 'Parcours',
    'nav.resources': 'Ressources',
    'nav.pro': 'Professionnel',
    'nav.contact': 'Contact',
    'nav.cv': 'Télécharger CV',

    // Hero
    'hero.title': 'Bienvenue sur mon espace académique',
    'hero.subtitle': 'Je partage mon parcours universitaire et mes ressources d\'apprentissage pour aider les étudiants en mathématiques, data science et informatique.',

    // Stats
    'stats.universities': 'Universités',
    'stats.years': 'Années d\'études',
    'stats.documents': 'Documents partagés',
    'stats.resources': 'Ressources gratuites',

    // Parcours
    'parcours.title': '📚 Mon parcours académique',
    'parcours.intro': 'De l\'Université des Lagunes à Epitech, découvrez mon parcours universitaire complet',
    'univ.see_more': 'Voir les cours →',

    // Université des Lagunes
    'univ.lagunes.name': 'Université des Lagunes',
    'univ.lagunes.period': '2021 - 2023 | Abidjan, Côte d\'Ivoire',
    'univ.lagunes.degree': 'Licence Mathématiques & Applications',
    'univ.lagunes.desc': 'Formation fondamentale en mathématiques pures et appliquées. Algèbre, analyse, probabilités et statistiques.',

    // Université Côte d'Azur
    'univ.uca.name': 'Université Côte d\'Azur',
    'univ.uca.period': '2023 - 2025 | Nice, France',
    'univ.uca.degree': 'Master 2 Ingénierie Mathématique',
    'univ.uca.desc': 'Spécialisation en modélisation mathématique, optimisation, machine learning et data science.',

    // Epitech
    'univ.epitech.name': 'Epitech',
    'univ.epitech.period': '2025 - 2028 | Nice puis Bordeaux',
    'univ.epitech.degree': 'MSc Architecture Systèmes, IA & Big Data',
    'univ.epitech.desc': 'Formation spécialisée en Big Data, Intelligence Artificielle, DevOps et architecture de systèmes distribués.',

    // Ressources
    'resources.title': '🌐 Ressources d\'apprentissage',
    'resources.subtitle': 'Sites, chaînes YouTube et plateformes que j\'utilise pour progresser en autonomie',
    'resources.explore': 'Explorer →',
    'resources.english.title': 'Anglais',
    'resources.english.desc': 'Sites pour améliorer votre anglais académique et professionnel',
    'resources.math.title': 'Mathématiques',
    'resources.math.desc': 'Exo7, BibMaths, exercices corrigés et vidéos explicatives',
    'resources.programming.title': 'Programmation',
    'resources.programming.desc': 'GeeksforGeeks, TutorialsPoint, documentation et tutoriels',
    'resources.youtube.title': 'Vidéos YouTube',
    'resources.youtube.desc': 'Chaînes éducatives recommandées pour tous niveaux',

    // CTA
    'cta.title': '🚀 Prêt à explorer ?',
    'cta.subtitle': 'Tous les documents sont gratuits et régulièrement mis à jour. N\'hésitez pas à me contacter pour toute question !',
    'cta.parcours': 'Voir mon parcours complet',
    'cta.resources': 'Découvrir les ressources',
    'cta.contact': 'Me contacter',

    // Professionnel
    'pro.title': '💼 Suivez mon parcours professionnel',
    'pro.linkedin': 'Suivez mes posts et actualités professionnelles',
    'pro.github': 'Explorez mes projets et contributions open-source',

    // Footer
    'footer.mission': 'Partage de connaissances pour étudiants',

    // About
    'about.title': 'À propos de moi',
    'about.intro': 'Passionné par les mathématiques, la data science et l\'intelligence artificielle',

    // Contact
    'contact.title': 'Contact',
    'contact.subtitle': 'N\'hésitez pas à me contacter pour toute question ou collaboration',
    'contact.form.name': 'Votre nom',
    'contact.form.email': 'Votre email',
    'contact.form.message': 'Votre message',
    'contact.form.send': 'Envoyer',

    // Common
    'download': 'Télécharger',
    'view': 'Voir',
    'learn_more': 'En savoir plus',
    'back': 'Retour',
    'next': 'Suivant'
  },

  en: {
    // Navigation
    'nav.home': 'Home',
    'nav.about': 'About',
    'nav.parcours': 'Academic Path',
    'nav.resources': 'Resources',
    'nav.pro': 'Professional',
    'nav.contact': 'Contact',
    'nav.cv': 'Download CV',

    // Hero
    'hero.title': 'Welcome to my academic space',
    'hero.subtitle': 'I share my academic journey and learning resources to help students in mathematics, data science and computer science.',

    // Stats
    'stats.universities': 'Universities',
    'stats.years': 'Years of study',
    'stats.documents': 'Shared documents',
    'stats.resources': 'Free resources',

    // Parcours
    'parcours.title': '📚 My academic journey',
    'parcours.intro': 'From Université des Lagunes to Epitech, discover my complete academic path',
    'univ.see_more': 'View courses →',

    // Université des Lagunes
    'univ.lagunes.name': 'Université des Lagunes',
    'univ.lagunes.period': '2021 - 2023 | Abidjan, Ivory Coast',
    'univ.lagunes.degree': 'Bachelor\'s in Mathematics & Applications',
    'univ.lagunes.desc': 'Fundamental training in pure and applied mathematics. Algebra, analysis, probability and statistics.',

    // Université Côte d'Azur
    'univ.uca.name': 'Université Côte d\'Azur',
    'univ.uca.period': '2023 - 2025 | Nice, France',
    'univ.uca.degree': 'Master 2 in Mathematical Engineering',
    'univ.uca.desc': 'Specialization in mathematical modeling, optimization, machine learning and data science.',

    // Epitech
    'univ.epitech.name': 'Epitech',
    'univ.epitech.period': '2025 - 2028 | Nice then Bordeaux',
    'univ.epitech.degree': 'MSc Systems Architecture, AI & Big Data',
    'univ.epitech.desc': 'Specialized training in Big Data, Artificial Intelligence, DevOps and distributed systems architecture.',

    // Ressources
    'resources.title': '🌐 Learning resources',
    'resources.subtitle': 'Websites, YouTube channels and platforms I use for autonomous learning',
    'resources.explore': 'Explore →',
    'resources.english.title': 'English',
    'resources.english.desc': 'Websites to improve your academic and professional English',
    'resources.math.title': 'Mathematics',
    'resources.math.desc': 'Exo7, BibMaths, corrected exercises and explanatory videos',
    'resources.programming.title': 'Programming',
    'resources.programming.desc': 'GeeksforGeeks, TutorialsPoint, documentation and tutorials',
    'resources.youtube.title': 'YouTube Videos',
    'resources.youtube.desc': 'Recommended educational channels for all levels',

    // CTA
    'cta.title': '🚀 Ready to explore?',
    'cta.subtitle': 'All documents are free and regularly updated. Feel free to contact me for any questions!',
    'cta.parcours': 'View my complete journey',
    'cta.resources': 'Discover resources',
    'cta.contact': 'Contact me',

    // Professionnel
    'pro.title': '💼 Follow my professional journey',
    'pro.linkedin': 'Follow my posts and professional updates',
    'pro.github': 'Explore my projects and open-source contributions',

    // Footer
    'footer.mission': 'Knowledge sharing for students',

    // About
    'about.title': 'About me',
    'about.intro': 'Passionate about mathematics, data science and artificial intelligence',

    // Contact
    'contact.title': 'Contact',
    'contact.subtitle': 'Feel free to contact me for any question or collaboration',
    'contact.form.name': 'Your name',
    'contact.form.email': 'Your email',
    'contact.form.message': 'Your message',
    'contact.form.send': 'Send',

    // Common
    'download': 'Download',
    'view': 'View',
    'learn_more': 'Learn more',
    'back': 'Back',
    'next': 'Next'
  }
};

class TranslationManager {
  constructor() {
    // Récupérer la langue sauvegardée (valable pour TOUTES les pages)
    this.currentLang = localStorage.getItem('language') || 'fr';
    this.init();
  }

  init() {
    // Appliquer la langue sauvegardée immédiatement au chargement
    this.applyLanguage(this.currentLang);

    // Mettre à jour l'attribut lang du HTML
    document.documentElement.setAttribute('lang', this.currentLang);

    // Setup des boutons de langue
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        this.changeLanguage(lang);
      });

      // Marquer le bouton actif selon la langue actuelle
      if (btn.getAttribute('data-lang') === this.currentLang) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    console.log(`🌍 Langue actuelle: ${this.currentLang}`);
  }

  changeLanguage(lang) {
    // Sauvegarder dans localStorage (persistant sur TOUTES les pages)
    this.currentLang = lang;
    localStorage.setItem('language', lang);
    
    console.log(`🔄 Changement de langue vers: ${lang}`);

    // Mettre à jour les boutons
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // Appliquer les traductions
    this.applyLanguage(lang);

    // Mettre à jour l'attribut lang du HTML
    document.documentElement.setAttribute('lang', lang);

    // Message de confirmation
    console.log(`✅ Langue changée en ${lang.toUpperCase()}. Ce choix s'appliquera à toutes les pages !`);
  }

  applyLanguage(lang) {
    const trans = translations[lang];
    
    if (!trans) {
      console.error(`❌ Traductions non trouvées pour la langue: ${lang}`);
      return;
    }

    // Traduire tous les éléments avec data-i18n
    let translatedCount = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {
      const key = element.getAttribute('data-i18n');
      if (trans[key]) {
        element.textContent = trans[key];
        translatedCount++;
      } else {
        console.warn(`⚠️ Traduction manquante pour la clé: ${key}`);
      }
    });

    console.log(`📝 ${translatedCount} éléments traduits en ${lang.toUpperCase()}`);
  }

  // Méthode helper pour récupérer une traduction
  t(key) {
    return translations[this.currentLang][key] || key;
  }

  // Méthode pour obtenir la langue actuelle
  getCurrentLanguage() {
    return this.currentLang;
  }
}

// Initialiser le gestionnaire de traduction dès que le DOM est prêt
document.addEventListener('DOMContentLoaded', () => {
  window.translationManager = new TranslationManager();
  
  // Message dans la console pour confirmer le chargement
  console.log('✅ Système de traduction chargé avec succès !');
  console.log('💡 La langue sélectionnée est sauvegardée et s\'applique automatiquement sur toutes les pages.');
});

// Export pour utilisation dans d'autres scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = TranslationManager;
}