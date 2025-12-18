# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:48:52 2022

@author: simon
"""


import numpy as np
import matplotlib.pyplot as plt
# Exercice 2
#%% 2.1
#On peut repartir du code de ResolutionD et l'adapter

def ResolutionN(N,a,b,c,f,ua,vb):
    X=np.linspace(a,b,N+2)
    h=(b-a)/(N+1)
    # REMARQUE : la dimension du système sera N car la valeur de u en a est déjà connue
    # et sa valeur en x=b est liée à sa valeur en b-h par la relation de dérivée discrète.

    A=2*np.eye(N) # la matrice d'approximation de la dérivée seconde (laplacien)
    A=A-np.eye(N,k=1)-np.eye(N,k=-1)  #des -1 sur la sur-diagonale (k=1) et sous-diagonale (k=-1)
    A[-1,-1]=1 # Cf relation (3) du TP.
    A=A/h**2
    C=c(X[1:-1])
    A=A+np.diag(C)  
 

    F=f(X[1:-1])
    F[0]=F[0]+ua/h**2
    F[-1]=F[-1]+vb/h   

    
    # identique à ResolutonDH
    uh=np.dot(np.linalg.inv(A),F) # la solution numérique sur les points intérieurs du maillage
    # On peut aussi utiliser np.linalg.solve
    Uh=np.zeros(N+2) # contiendra la solution numérique (pour i=0,....,N+1)
    Uh[1:N+1]=uh  
    Uh[0]=ua


    # expression de u_{N+1} à partir de U_N
    Uh[-1]=Uh[-2]+h*vb
    return X, Uh
 

 





#%% 2.2
# Un choix quelconque : 
def u4(x):
    return 2*x*np.cos(8*x)
def c4(x):
    return x
# on en déduit f2=-u''+cu
def f4(x):
    return 4*8*np.sin(8*x)+2*x*8**2*np.cos(8*x)+c4(x)*u4(x)

def du4(x): # dérivée de u4, pour la condition de Neumann
    return 2*np.cos(8*x)-2*8*x*np.sin(8*x)
##On a alors les conditions de bord ua=u4(a), vb=u4'(b)



# def u4(x):
#     return np.cos(np.pi*x)
# def c4(x):
#     return 2*x
# # on en déduit f4=-u''+cu
# def f4(x):
#     return np.pi**2*np.cos(np.pi*x)+2*x*np.cos(np.pi*x)

# def du4(x):
#     return -np.sin(np.pi*x)*np.pi
    


# on vérifie que ResolutionN fonctionne bien :
N=250 ; a=0 ; b=3 ;  c=c4 ; f=f4 ; u=u4 ; ua=u4(a) ; vb=du4(b)
x,V=ResolutionN(N,a,b,c,f,ua,vb)
plt.figure()
plt.plot(x,V,lw=3,label='approchee')
plt.plot(x,u(x),lw=2,label='exacte')
plt.title("Comparaison solutions numérique et exacte",size=10)
plt.xlabel('x',size=8)
plt.ylabel('solutions',size=8)
plt.legend()

#%% Tracé de l'erreur (code identique  celui de la question 1.7)
test_N=np.arange(50,1001,10) # par exemple, on teste avec N allant de 5 à 300 par pas de 5
Norme2=np.zeros(len(test_N))
Normeoo=np.zeros(len(test_N))
for i in range(len(test_N)):
    h=(b-a)/(test_N[i]+1)
    x,V=ResolutionN(test_N[i],a,b,c,f,ua,vb)
    Norme2[i]=np.sqrt(h*(V-u(x))@(V-u(x))) # ou np.linalg.norm((V-sol_exacte1(x)),2)
    Normeoo[i]=np.max(np.abs(V-u(x)))

test_h=(b-a)/test_N

plt.figure()
plt.plot(np.log(test_h),np.log(Norme2),label='norme 2')
plt.plot(np.log(test_h),np.log(Normeoo),label='norme inf')
plt.legend()
plt.xlabel('ln(h)',size=15)
plt.ylabel('ln(erreur globale)',size=15)
# Une méthode  rudimentaire :
ordre2=(np.log(Norme2[-1])-np.log(Norme2[-2]))/(np.log(test_h[-1])-np.log(test_h[-2]))
ordreoo=(np.log(Normeoo[-1])-np.log(Normeoo[-2]))/(np.log(test_h[-1])-np.log(test_h[-2]))


# Avec la régression linéaire
ordre2=np.polyfit(np.log(test_h),np.log(Norme2),1)[0] # le premier coef renvoyé est le coef du terme de degré 1 
ordreoo=np.polyfit(np.log(test_h),np.log(Normeoo),1)[0] # le premier coef renvoyé est le coef du terme de degré 1 


print(" ordre de convergence en norme 2 = ", ordre2 ,  "\n ordre en norme oo = ", ordreoo)
# On trouve 1 ! 
# C'était prévisible car l'approximation de la dérivée n'est que d'ordre 1 !

#### Remarque : dans certains cas très particuliers on peut obtenir une convergence d'ordre 2
### Explication : 
# De façon générale,
# - au point x=b, on fait un développement de Taylor de u au point b, donc : u(b+h)=u(b)+h*u'(b)+ h²u''(b)/2+ O(h**3).

# - A partir de l'expression précédente on obtient : u'(b)- (u(b+h)-u(b))/h = h*u''(b)/2 + O(h²)

# - Le taux d'accroissement est donc à priori une approximation d'ordre 1 de u'(b) puisqu'on a négligé le terme h*u''(b)/2 + O(h²) , qui est un O(h).

# Dans le cas particulier ou u''(b)=0 (exemple u=sin(pi*x) avec b entier), alors le terme en h*u''(b) ci-dessus est nul et finalement on a seulement négligé un terme en O(h**2) et on a une approximation d'ordre 2 (et pas plus, car le terme en u'''(x) dans le développement de Taylor est en cos(b*pi), donc non nul)

#%% Méthode du point fantôme.

def ResolutionN2(N,a,b,c,f,ua,vb):
    h=(b-a)/(N+1)
    X=np.linspace(a,b+h,N+3) ## Attention : on ne fait pas qu'ajouter un point
    # à la subdivision, on étend aussi l'intervalle à [A,b+h]
    # REMARQUE : la dimension du système est N+1 car on a ajouté le point fantôme
    A=2*np.eye(N+1) # la matrice d'approximation de la dérivée seconde (laplacien)
    
    A=A-np.diag(np.ones(N),k=1)-np.diag(np.ones(N),k=-1) 
    A[-1,-2]=-2 # Cf TP.
    A=A/h**2
    C=c(X[1:-1])
    A=A+np.diag(C)  

    

    F=f(X[1:-1]) # pour la fonction f
    F[0]=F[0]+ua/h**2
    F[-1]=F[-1]+2*vb/h   

    Uh=np.zeros(N+3) # coniendra la solution numérique
    Uh[1:N+2]=np.dot(np.linalg.inv(A),F) 
    Uh[0]=ua
    Uh[-1]=Uh[-2]+h*vb
    return X, Uh




#%% On applique le code de la question 2.2 avec ResolutionN2 au lieu de ResolutionN
# pour tester notre fonction

N=600 ; a=0 ; b=1 ;  c=c4 ; f=f4 ; u=u4 ; ua=u4(a) ; vb=du4(b)
x,V=ResolutionN2(N,a,b,c,f,ua,vb)
plt.figure()
plt.plot(x,V,lw=3,label='approchee')
plt.plot(x,u(x),lw=2,label='exacte')
plt.title("Comparaison solutions numérique et exacte",size=10)
plt.xlabel('x',size=8)
plt.ylabel('solutions',size=8)
plt.legend()
# Ca fonction bien.

#%% On applique le code de la question 2.2 avec ResolutionN2 au lieu de ResolutionN
# pour évaluer l'ordre de convergence

test_N=np.arange(1100,1301,10) # par exemple, on teste avec N allant de 5 à 300 par pas de 5
Norme2=np.zeros(len(test_N))
Normeoo=np.zeros(len(test_N))
for i in range(len(test_N)):
    h=(b-a)/(test_N[i]+1)
    x,V=ResolutionN2(test_N[i],a,b,c,f,ua,vb)
    Norme2[i]=np.sqrt(h*(V-u(x))@(V-u(x))) # ou np.linalg.norm((V-sol_exacte1(x)),2)
    Normeoo[i]=np.max(np.abs(V-u(x)))
    print(i)
test_h=(b-a)/test_N

plt.figure()
plt.plot(np.log(test_h),np.log(Norme2),label='norme 2')
plt.plot(np.log(test_h),np.log(Normeoo),label='norme inf')
plt.legend()
plt.xlabel('ln(h)',size=15)
plt.ylabel('ln(erreur globale)',size=15)
# Une méthode  rudimentaire :
ordre2=(np.log(Norme2[-1])-np.log(Norme2[-10]))/(np.log(test_h[-1])-np.log(test_h[-10]))
ordreoo=(np.log(Normeoo[-1])-np.log(Normeoo[-10]))/(np.log(test_h[-1])-np.log(test_h[-10]))


# Avec la régression linéaire
ordre2=np.polyfit(np.log(test_h),np.log(Norme2),1)[0] # le premier coef renvoyé est le coef du terme de degré 1 
ordreoo=np.polyfit(np.log(test_h),np.log(Normeoo),1)[0] # le premier coef renvoyé est le coef du terme de degré 1 


print(" ordre de convergence en norme 2 = ", ordre2 ,  "\n ordre en norme oo = ", ordreoo)
# Ordre 2, Hourra !