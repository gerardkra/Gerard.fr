# EXERCICE 1: equation de second degré
equation_2gre2 <- function(a,b,c)
{
  # Calcul du determinant
  disc <- b^2 - 4 * a * c
  
  if (disc == 0) # Une racine double
  {
    x0<-(-b / (2 * a))
    return(x0)
  }   
  else
  {
    if (disc > 0) # Deux racines simples
    {
      x1 <- (-b - sqrt(disc)) / (2 * a)
      x2 <- (-b + sqrt(disc)) / (2 * a)
      return(c(x1,x2))
      
    }
    else # Aucun rÃ©sultat dans R
    {
      return("pas de solution dans R")
    }   
  }   
}
#EXERCICE:1 fiche de TD

# 1) Créer le vecteur u composé de 5000 uns.
u=rep(1,5000)
#3. Créer le vecteur A = (???10, ???9, . . . , 9, 10) que vous nommerez vecA
#avec la commande seq(). Donner sa longueur directement à partir
#d'une commande sans calcul.

vecA=c(seq(-10,10,1))
length(vecA)
# 4. Créer le vecteur B = (???1.5, ???1.4, . . . , 0.5) que vous nommerez vecB.
vecB=c(seq(-1.5,0.5,0.5))
# 5. Créer le vecteur C = (c1, . . . , cn) à partir de vecA tel que ci = 1 si
#ai < 0 et ci = ai si ai ??? 0.
vecC=ifelse(vecA<0,1,vecA)
# Exercice: 2 On collecte la couleur des yeux de 12 personnes
# 1) 1. Créer un facteur couleurs regroupant les 12 valeurs obtenues qui sont
#les suivantes : bleu, marron, vert, marron, marron, bleu, marron, marron, vert, vert, marron, vert
couleur=c(rep("bleu",2),rep("marron",6),rep("vert",4))

# 2) Donner les commandes renvoyant le nombre de modalités de la variable étudiée et l'eectif total.
couleure=as.factor(couleur)

# 3) 3. Donner le tableau des eectifs correspondant aux données.
tb=table(couleure)
effto=length(couleur)
tab=c(tb)
data.frame(effectif=tab,frequence=round(tab/effto,2))
library(datasets)
data(Puromycin)
data=Puromycin
hist(data$rate,
col="lightblue",
breaks=c(0.75,100,130,160,210),
min="Histogramme des vitesses de réactions",
xlab="vitesses de réaction soigné",
ylab="pourcentage"
)