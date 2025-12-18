# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:39:12 2022

@author: simon
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Exercice1
#%% 1.1
def ResolutionDH(N,a,b,c,f):
    X=np.linspace(a,b,N+2) # de a à b en N+2 points
    h=(b-a)/(N+1) #longueur du pas
    # REMARQUE : la dimension du système sera N car les deux points sur le bord sont déjà connus 
    # Remarque : approche vectorielle plus efficace que des boucles for
    A=2*np.eye(N) # la matrice d'approximation de la dérivée seconde (laplacien)
    A=A-np.eye(N,k=1)-np.eye(N,k=-1)  #des -1 sur la sur-diagonale (k=1) et sous-diagonale (k=-1)
    A=A/h**2
    C=c(X[1:-1])
    A=A+np.diag(C)
    F=f(X[1:-1])
    
    uh=np.dot(np.linalg.inv(A),F) # la solution numérique sur les points intérieurs du maillage
    # On peut aussi utiliser linalg.solve(A,F)

    Uh=np.zeros(N+2) # contiendra la solution numérique (pour i=0,....,N+1)
    Uh[1:N+1]=uh # Uh[0] et Uh[-1] sont déjà initialisées à 0  
    return X, Uh



 

#%% 1.2 et 1.3
# u est bien solution, le principe du max est vérifié : u reste positive. On 
# pouvait s'y attendre car c>=0 et f>=0.
def c1 (x) :  
    return 2*x 
def f1 (x):
    return (np.pi**2+2*x)*np.sin(np.pi*x)
def u1 (x) : 
    return np.sin(np.pi*x)


N=100 ; a=0 ; b=1 ;  c=c1 ; f=f1 ; u=u1
X,Uh=ResolutionDH(N,a,b,c,f)
plt.figure()
plt.plot(X[1:-1],Uh[1:-1],lw=3,label='approchee')
plt.plot(X,u(X),lw=2,label='exacte')
plt.title("Comparaison solutions numérique et exacte",size=10)
plt.xlabel('x',size=8)
plt.ylabel('solutions',size=8)
plt.legend()


#%% 1.4
# Exactement comme la question 1 avec en plus :
    ### 1) l'intialisation de Uh[0] et Uh[-1] aux valeurs ua et ub 
    ### 2) l'influence des bords sur le calcul de Uh[1] et Uh[-2]

def ResolutionD(N,a,b,c,f,ua,ub):
    #Ce premier bloc est identique à celui de ResolutionDH
    X=np.linspace(a,b,N+2)
    h=(b-a)/(N+1)
    A=2*np.eye(N) # la matrice d'approximation de la dérivée seconde (laplacien)
    A=A-np.eye(N,k=1)-np.eye(N,k=-1)  #des -1 sur la sur-diagonale (k=1) et sous-diagonale (k=-1)
    A=A/h**2
    C=c(X[1:-1])
    A=A+np.diag(C)

    # Ici il faut ajouter l'effet de ua et ub sur u_1 et u_N (Cf énoncé du TP)    
    F=f(X[1:-1])
    F[0]=F[0]+ua/h**2  
    F[-1]=F[-1]+ub/h**2    
    
    # Bloc identique à ResolutionDH
    uh=np.dot(np.linalg.inv(A),F) # la solution numérique sur les points intérieurs du maillage
    Uh=np.zeros(N+2) # contiendra la solution numérique (pour i=0,....,N+1)
    Uh[1:N+1]=uh  

    # Conditions de Dirichlet non homogènes.
    Uh[0]=ua
    Uh[-1]=ub
    return X, Uh




#%% 1.5
# Un choix possible : 
def u2(x):
    return 16+x*np.cos(5*x*np.pi/2)**2
def c2(x):
    return x**2
# on en déduit f2=-u''+cu
def f2(x):
    a=5*np.pi/2
    return 4*a*np.cos(a*x)*np.sin(a*x)-2*x*(a)**2+4*a**2*x*np.cos(a*x)**2+c2(x)*u2(x)

## autre exp : 
#def u2(x):
#    return (np.exp(1) - np.exp(x))*x**2
#def c2(x):
#    return np.cos(3*np.pi*x)+1
## on en déduit f2=-u''+cu
#def f2(x):
#    return np.exp(x)*x**2+4*x*np.exp(x)+2*np.exp(x)-2*np.exp(1)+c2(x)*u2(x)


# # Un choix possible : 
# def u2(x):
#     return np.cos(x)
# def c2(x):
#     return 2*x
# # on en déduit f2=-u''+cu
# def f2(x):
#     return np.cos(x)+2*x*np.cos(x)


# on peut vérifier :
N=500 ; a=0 ; b=4 ;  c=c2 ; f=f2 ; u=u2 ; ua=u2(a) ; ub=u2(b)
x,V=ResolutionD(N,a,b,c,f,ua,ub)
plt.figure()
plt.plot(x,V,lw=3,label='approchee')
plt.plot(x,u(x),lw=2,label='exacte')
plt.title("Comparaison solutions numérique et exacte",size=10)
plt.xlabel('x',size=8)
plt.ylabel('solutions',size=8)
plt.legend()



#%% 1.6
test_N=np.arange(100,1001,10) # par exemple, on teste avec N allant de 5 à 300 par pas de 5
Norme2=np.zeros(len(test_N))
Normeoo=np.zeros(len(test_N))
for i in range(len(test_N)):
    h=(b-a)/(test_N[i]+1)
    x,V=ResolutionD(test_N[i],a,b,c,f,ua,ub)
    Norme2[i]=np.linalg.norm((V-u(x)),2)*np.sqrt(h) # ou  np.sqrt(h*(V-u(x))@(V-u(x))) 
    Normeoo[i]=np.max(np.abs(V-u(x)))
    print(i)

test_h=(b-a)/test_N

plt.figure()
plt.plot(test_h,Norme2,label='norme 2')
plt.plot(test_h,Normeoo,label='norme inf')
plt.legend()
plt.xlabel('h',size=15)
plt.ylabel('erreur globale',size=15)


#%% 1.7
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
# On trouve 2


#%% 1.8 : on reprend 1.5 et 1.6 en prenant u3 polynomiale de degré 2
# Un choix possible : 
def u3(x):
    return 2*x**2-8*x+6 # sur [0,6]
def c3(x):
    return x**2
# on en déduit f2=-u''+cu
def f3(x):
    return -4+c3(x)*u3(x)

# on peut vérifier :
N=30 ; a=0 ; b=6 ;  c=c3 ; f=f3 ; u=u3 ; ua=6 ; ub=30
x,V=ResolutionD(N,a,b,c,f,ua,ub)
plt.figure()
plt.plot(x,V,lw=3,label='approchee')
plt.plot(x,u(x),lw=2,label='exacte')
plt.title("Comparaison solutions numérique et exacte",size=10)
plt.xlabel('x',size=8)
plt.ylabel('solutions',size=8)
plt.legend()



Norme2=np.zeros(len(test_N))
Normeoo=np.zeros(len(test_N))
for i in range(len(test_N)):
    h=1/(test_N[i]+1)
    x,V=ResolutionD(test_N[i],a,b,c,f,ua,ub)
    Norme2[i]=np.sqrt(h*(V-u(x))@(V-u(x))) # ou np.linalg.norm((V-sol_exacte1(x)),2)
    Normeoo[i]=np.max(np.abs(V-u(x)))
    print(i)

test_h=1/test_N

plt.figure()
plt.plot(test_h,Norme2,label='norme 2')
plt.plot(test_h,Normeoo,label='norme inf')
plt.xlabel('h',size=15)
plt.ylabel('erreur globale',size=15)
plt.legend()

# L'erreur du schéma est nulle (erreurs d'arrondis). C'était prévisible car
# l'approximation centrée de la dérivée seconde est exacte sur les polynomes
# de degré 2 (et même 3) (car obtenue par développement limité à l'ordre 3 (et même
# à l'ordre 4 puisque les termes d'ordre 3 s'annulent).







