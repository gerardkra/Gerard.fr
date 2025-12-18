# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:24:01 2022

@author: simon
"""

import numpy as np

#%% Exercice 2

def Suite(n,m):
    A=np.zeros([n,m]) # initialiser un tableau
    for i in range(n): # parcourir les lignes
        A[i,:]=np.linspace(1,1+i*(m-1),m) # les m premiers termes de la suite arithmétique de raison i
    return A

print(Suite(4,6))
    
#%% Exercice 3

def Norme(x,p):
    return (np.sum(np.abs(x)**p))**(1/p)

#test
x=np.array([3*np.cos(12),3*np.sin(12)])
print(Norme(x,2))

#%% Exercice 4


# a.(i) Si on note $\Delta_t=(t_f-t_0)/(N-1)$ la longeur d'un pas de temps alors 
# 
#  $\forall n\geq 0,\ y_{n+1}=y_n+\Delta_t(-ky_n + r)$
# 
# On reconnait une suite arithmético-géométrique, et on en déduit que
# 
# $y_n=(1-k\Delta_t)^n\left(y_0-\frac{r}{k}\right)+\frac{r}{k}$


def Solution(k,r,t0,tf,y0,N):
    t=np.linspace(t0,tf,N) # la subdivision de l'intervalle de temps
    y=np.zeros(N) #initialisation du vecteur solution
    y[0]=y0 #condition initiale
    dt=(tf-t0)/(N-1) #longueur du pas de temps
    for i in range(1,N):
        y[i]=y[i-1]+dt*(-k*y[i-1]+r) #schéma d'Euler explicite
    return t,y

def Sol_exacte(k,r,t0,tf,y0,N): #solution exacte de l'équation
    t=np.linspace(t0,tf,N)
    return (y0-r/k)*np.exp(-k*t)+r/k 

import matplotlib.pyplot as plt
# Pour N =1000
k=10
r=0
t0=0
tf=5
y0=1
N=1000
t1000,y1000=Solution(k,r,t0,tf,y0,N) #t000 contient les temps (abscisses) et y les valeurs approchées de la solution de l'EDO (ordonnées)

plt.figure # ouvre une nouvelle figure
plt.plot(t1000,y1000,label='sol num') #le label se retrouvera dans la légende
plt.plot(t1000,Sol_exacte(k,r,t0,tf,y0,N),label="sol exacte")
plt.xlabel('Temps',size=15)
plt.ylabel('solutions',size=15)
plt.title('Solution numérique VS solution exacte pour N='+str(N),size=15) #titre = la chaine de caractère "solution blabla" concaténée avec N (convertie en chaine de caractère via str())
plt.legend()

# Pour N =100 (idem en changeant la valeur de N)
N=100
t100,y100=Solution(k,r,t0,tf,y0,N)

plt.figure()  
plt.plot(t100,y100,label="sol num")
plt.plot(t100,Sol_exacte(k,r,t0,tf,y0,N),label="sol exacte")
plt.xlabel('Temps',size=15)
plt.ylabel('solutions',size=15)
plt.title('Solution numérique VS solution exacte pour N='+str(N),size=15)
plt.legend()

# Pour N =10  ## On observe le caractère instable de ce schéma
N=10
t10,y10=Solution(k,r,t0,tf,y0,N)

plt.figure()  
plt.plot(t10,y10,label="sol num")
plt.plot(t10,Sol_exacte(k,r,t0,tf,y0,N),label="sol exacte")
plt.xlabel('Temps',size=15)
plt.ylabel('solutions',size=15)
plt.title('Solution numérique VS solution exacte pour N='+str(N),size=15)
plt.legend()


#%% Tracé de l'erreur (ici pour N=1000 par exemple)
plt.plot(t1000,np.abs(y1000-Sol_exacte(k,r,t0,tf,y0,N=1000)))
plt.xlabel('Temps',size=15)
plt.ylabel('erreur',size=15)
plt.title('|y(t_i)-y_i|',size=15)
plt.legend()


