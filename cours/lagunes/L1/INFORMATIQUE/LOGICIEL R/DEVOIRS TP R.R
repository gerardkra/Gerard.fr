# DEVOIR DE MAISON
# exercice
#Q1 la population c'est: un ensemble de 60 femmes
#Q2 la variable statistique est l'age de la mère: c'est une variable quantitative continue.
age=c(23,24,18,19,35,26,28,24,22,19,19,17,22,26,31,28,29,21,20,22,23,18,20,27,29,24,24,
      21,23,23,32,29,27,21,22,23,24,28,32,30,25,26,23,20,29,35,38,19,20,22,24,23,31,26,
      27,20,21,22,23,28)
#Q3
sum(age)# la somme totale est:
mean(age) # l'age moyen à la naissance du 1er bébé est:
summary(age)# le resumé des données du caractère 

#Q4 le tableau statisque

eff=c(table(age))
freq=prop.table(eff)
fcc=cumsum(freq)
fcd=rev(cumsum(rev(freq)))
cut(age,breaks = c(17,20,23,26,29,32,35,38))

#Q5  l'histogramme des fréquences

histograme=c(hist(age, freq = F))

#Q6 la boite à moustache

boxplot(age)# la distribution n'est pas symétrique, elle s'étale àdroite. cela montre qu'il y a un grand nombre de femme qui ont un age compris entre 23 et 38 ans à la naissance de leur 1er bébé par rapport à celles qui ont un age compris entre 17 et 23 ans à la naissance de leur 1er bébé!

#Q7 courbe des frÃ©quences cumulÃ©e croissante et dÃ©croissante

plot(fcc)# courbe cumulative croissante
plot(fcd)# courbe cumulative décroissante

