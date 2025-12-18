#!/bin/bash

# Script pour ajouter Google Translate à toutes les pages HTML

echo "🚀 Ajout de Google Translate à toutes les pages..."

# Liste des fichiers à modifier
FILES=(
  "about.html"
  "contact.html"
  "parcours/index.html"
  "parcours/universite-lagunes.html"
  "parcours/universite-cote-azur.html"
  "parcours/epitech.html"
  "ressources/index.html"
  "ressources/mathematiques.html"
  "ressources/programmation.html"
  "ressources/anglais.html"
  "ressources/videos-youtube.html"
  "professionnel/index.html"
  "professionnel/github.html"
  "professionnel/linkedin.html"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "✅ Modification de $file"
    
    # Créer un fichier temporaire
    temp_file="${file}.tmp"
    
    # Traiter le fichier ligne par ligne
    while IFS= read -r line; do
      echo "$line"
      
      # Ajouter le script Google Translate avant </head>
      if [[ $line == *"</head>"* ]]; then
        cat << 'EOF'
  <script type="text/javascript">
    function googleTranslateElementInit() {
      new google.translate.TranslateElement({
        pageLanguage: 'fr',
        includedLanguages: 'en,fr,es,de,it,pt,ar,zh-CN,ja,ko',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
        autoDisplay: false
      }, 'google_translate_element');
    }
  </script>
  <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
EOF
      fi
      
      # Ajouter le widget après </header>
      if [[ $line == *"</header>"* ]]; then
        cat << 'EOF'

  <!-- Google Translate Widget -->
  <div id="google_translate_element"></div>
EOF
      fi
      
    done < "$file" > "$temp_file"
    
    # Remplacer le fichier original
    mv "$temp_file" "$file"
  else
    echo "⚠️  Fichier non trouvé: $file"
  fi
done

echo "✅ Terminé ! Google Translate ajouté à tous les fichiers."