# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:06:06 2022

@author: simon
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


#from mpl_toolkits.mplot3D import Axes3D # Peut être nécessaire sur les machines du petit Valrose
 
#%% Q1 : l'expression s'obtient par développement limité comme dans le cas 1D

#%% Q2 : on a, pour tout 1<= i,j <=N
# (1/h^2) * (u_(i+1,j)+u_(i-1,j)+u_(i,j+1)+u_(i,j-1)-4u_(i,j)) + c_(i,j)u_(i,j)=f_(i,j)

#%% Q3 : la matrice $A^~$ a des 4 sur sa diagonale et des -1 sur sa sous-diagonale et 
# sa sous-diagonale.
# La matrice diag(C) est la matrice diagonale des c_{i,j}=c(x_i,y_j) organisés dans l'ordre suivant
# c_{1,1}, c_{2,1},...,c_{N,1}, c_{1,2}, ..., c_{N,2}....

#%% Q4 : après calcul du laplacien de u, on trouve 
# f(x,y)=-Delta u(x,y) + c(x,y)u(x,y) = pi**2*(3**2+4**2)*sin(4 pi x)*sin(3 pi x)+c(x,y)*sin(4 pi x)*sin(3 pi x)

#%% Q5

def DirichletH2D(N,c,f):
    X=np.linspace(0,1,N+2)
    Y=np.linspace(0,1,N+2)
    Xint=X[1:-1] # les points intérieurs du maillage
    Yint=Y[1:-1]
    h=1/(N+1)
    Atilde=4*np.eye(N)-np.diag(np.ones(N-1),1)-np.diag(np.ones(N-1),-1)
    A=np.zeros((N*N,N*N))
    for i in range(N):
        A[i*N:(i+1)*N,i*N:(i+1)*N]=Atilde
    A=A-np.diag(np.ones(N*(N-1)),N)-np.diag(np.ones(N*(N-1)),-N)
    A=A/(h**2)
    F=np.zeros(N*N)
    C=np.zeros(N*N)
    for i in range(N):
        for j in range(N):
            F[i+j*N]=f(Xint[i],Yint[j])
            C[i+j*N]=c(Xint[i],Yint[j])
    C=np.diag(C)
    u=np.zeros((N*N,1))
    u=np.linalg.solve(A+C,F)
    u=u.reshape(N,N)
    U=np.zeros((N+2,N+2))
    U[1:-1,1:-1]=u
    return X,Y,U

def c(x,y):
    return 1
def u(x,y):
    return np.sin(4*x*np.pi)*np.sin(3*y*np.pi)
def f(x,y):
    return 25*np.pi**2*u(x,y)+c(x,y)*u(x,y)
    
X,Y,U=DirichletH2D(80,c,f)


XX,YY=np.meshgrid(X,Y)

fig = plt.figure()
ax = plt.axes(projection ='3d')
surf =ax.plot_surface(XX, YY, U, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, ax = ax)
ax.set_title('Solution numérique')
#surf = ax.plot_surface(XX, YY, U-u(XX,YY), cmap=cm.coolwarm,linewidth=0, antialiased=False)


plt.title("Solution de -u''+cu=f",size=10)
ax.set_xlabel('$x$', fontsize=15, rotation=150)
ax.set_ylabel('$y$', fontsize=15)
ax.set_zlabel('u(x,y)', fontsize=15, rotation=60)
plt.legend()

#%%

test_N=np.arange(10,100,5) # par exemple, on teste avec N allant de 5 à 300 par pas de 5
Norme2=np.zeros(len(test_N))
Normeoo=np.zeros(len(test_N))
for i in range(len(test_N)):
    h=1/(test_N[i]+1)
    X,Y,U =DirichletH2D(test_N[i],c,f)
    XX,YY=np.meshgrid(X,Y)
    Norme2[i]=h*np.sqrt(np.sum((U-u(XX,YY))**2)) # ou np.linalg.norm((V-sol_exacte1(x)),2)
    Normeoo[i]=np.max(np.abs(U-u(XX,YY)))
    print(test_N[i])
test_h=1/(test_N+1)

plt.figure()
plt.plot(test_h,Norme2,label='norme 2')
plt.plot(test_h,Normeoo,label='norme inf')

plt.figure()
plt.plot(np.log(test_h),np.log(Norme2),label='norme 2')
plt.plot(np.log(test_h),np.log(Normeoo),label='norme inf')
plt.legend()
plt.xlabel('ln(h)',size=15)
plt.ylabel('ln(erreur globale)',size=15)
# Une méthode  rudimentaire :
ordre2=(np.log(Norme2[-1])-np.log(Norme2[0]))/(np.log(test_h[-1])-np.log(test_h[0]))
ordreoo=(np.log(Normeoo[-1])-np.log(Normeoo[0]))/(np.log(test_h[-1])-np.log(test_h[0]))


# Avec la régression linéaire
ordre2=np.polyfit(np.log(test_h),np.log(Norme2),1)[0] # le premier coef renvoyé est le coef du terme de degré 1 
ordreoo=np.polyfit(np.log(test_h),np.log(Normeoo),1)[0] # le premier coef renvoyé est le coef du terme de degré 1 
print("norme L2 :", ordre2, " norme oo :", ordreoo)


#%%

XX,YY=np.meshgrid(X,Y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(XX, YY, U-u(XX,YY), cmap=cm.coolwarm,linewidth=0, antialiased=False)
