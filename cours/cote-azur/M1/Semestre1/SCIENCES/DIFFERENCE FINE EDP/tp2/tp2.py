# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:41:51 2023

@author: Roland
"""

import numpy as np 
import matplotlib.pyplot as plt


#%%
#1.a) Méthode d'Euler explicite
def EulerExplicite(k,r,t0,tf,y0,N):
    t = np.linspace(t0,tf,N)
    y = np.zeros(N)
    y[0] = y0
    dt = (tf - t0)/(N-1)
    for i in range(1,N):
        y[i] = y[i-1] + dt*(-k*y[i-1] + r)
    return y,t

#%%
#1.b) Application numérique
def f(t):
    return np.exp(-150*t)

k = 150; r = 0; y0 = 1; t0 = 0; tf = 1

#%%
# dt = 1/50 => N1 = 51
N1 = 70
y1,t1 = EulerExplicite(k, r, t0, tf, y0, N1)

plt.figure()
plt.plot(t1,y1,label='Solution Numérique')
plt.plot(t1,f(t1),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('Solution numérique vs solution exacte pour N = '+str(N1),size=15)
plt.legend()    

#%%
#N2 = 71
N2 = 71
y2,t2 = EulerExplicite(k, r, t0, tf, y0, N2)

plt.figure()
plt.plot(t2,y2,label='Solution Numérique')
plt.plot(t2,f(t2),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('Solution numérique vs solution exacte pour N = '+str(N2),size=15)
plt.legend()

#%%
#N2 = 91
N3 = 91
y3,t3 = EulerExplicite(k, r, t0, tf, y0, N3)

plt.figure()
plt.plot(t3,y3,label='Solution Numérique')
plt.plot(t3,f(t3),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('Solution numérique vs solution exacte pour N = '+str(N3),size=15)
plt.legend()

#%%
#N2 = 91
N4 = 161
y4,t4 = EulerExplicite(k, r, t0, tf, y0, N4)

plt.figure()
plt.plot(t4,y4,label='Solution Numérique')
plt.plot(t4,f(t4),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('Solution numérique vs solution exacte pour N = '+str(N4),size=15)
plt.legend()

#%%
# 1.c) 

test = np.arange(1001,1501,20)
Normeoo = np.zeros(len(test))
for i in range(len(test)):
    y,t = EulerExplicite(k, r, t0, tf, y0, test[i])
    Normeoo[i] = np.max(np.abs(y-f(t)))

test_h = (tf-t0)/test

plt.figure()
plt.plot(test_h,Normeoo,label='Erreur')
plt.legend()
plt.xlabel('dt',size=15)
plt.ylabel('erreur globale',size=15)

#%%
plt.figure()
plt.plot(np.log(test_h),np.log(Normeoo),label='Erreur en log-log')
plt.legend()
plt.xlabel('ln(dt)',size=15)
plt.ylabel('ln(erreur globale)',size=15) 

ordreoo=np.polyfit(np.log(test_h),np.log(Normeoo),1)[0] 
ordreoo1=(np.log(Normeoo[-1])-np.log(Normeoo[-2]))/(np.log(test_h[-1])-np.log(test_h[-2])) 
print(ordreoo,ordreoo1) 

#%% 
# 2) Méthode d' Euler implicite
# a) 
def EulerImplicite(k,r,t0,tf,y0,N):
    t = np.linspace(t0,tf,N)
    y = np.zeros(N)
    y[0] = y0
    dt = (tf - t0)/(N-1)
    for i in range(0,N-1):
        y[i+1] = (r*dt + y[i])/(1 + k*dt)
    return y,t

#%%
# b)

y11,t11 = EulerImplicite(k, r, t0, tf, y0, N1)

plt.figure()
plt.plot(t11,y11,label='Solution Numérique')
plt.plot(t11,f(t11),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('(EI)Solution numérique vs solution exacte pour N = '+str(N1),size=15)
plt.legend()

#%%

y22,t22 = EulerImplicite(k, r, t0, tf, y0, N2)

plt.figure()
plt.plot(t22,y22,label='Solution Numérique')
plt.plot(t22,f(t22),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('(EI)Solution numérique vs solution exacte pour N = '+str(N2),size=15)
plt.legend()

#%% 

y33,t33 = EulerImplicite(k, r, t0, tf, y0, N3)

plt.figure()
plt.plot(t33,y33,label='Solution Numérique')
plt.plot(t33,f(t33),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('(EI)Solution numérique vs solution exacte pour N = '+str(N3),size=15)
plt.legend()

#%%

y44,t44 = EulerImplicite(k, r, t0, tf, y0, N4)

plt.figure()
plt.plot(t44,y44,label='Solution Numérique')
plt.plot(t44,f(t44),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('(EI)Solution numérique vs solution exacte pour N = '+str(N4),size=15)
plt.legend()

#%% 
# 2c)

# test = np.arange(1001,1501,20)
Normeoo1 = np.zeros(len(test))
for i in range(len(test)):
    y,t = EulerImplicite(k, r, t0, tf, y0, test[i])
    Normeoo1[i] = np.max(np.abs(y-f(t)))

test_h = (tf-t0)/test

plt.figure()
plt.plot(test_h,Normeoo1,label='Erreur')
plt.legend()
plt.xlabel('dt',size=15)
plt.ylabel('erreur globale',size=15)

#%% 

plt.figure()
plt.plot(np.log(test_h),np.log(Normeoo1),label='Erreur en log-log')
plt.legend()
plt.xlabel('ln(dt)',size=15)
plt.ylabel('ln(erreur globale)',size=15) 

ordreoo1=np.polyfit(np.log(test_h),np.log(Normeoo1),1)[0] 
ordreoo11=(np.log(Normeoo1[-1])-np.log(Normeoo1[-2]))/(np.log(test_h[-1])-np.log(test_h[-2])) 
print(ordreoo1,ordreoo11)

#%% 
# 3) Méthode de Crank-Nicolson

def CrankNicolson(k,r,t0,tf,y0,N):
    t = np.linspace(t0,tf,N)
    y = np.zeros(N)
    y[0] = y0
    dt = (tf - t0)/(N-1)
    for i in range(0,N-1):
        y[i+1] = y[i] + ((dt/2)*((-k*y[i] + r) + ((r/(1 + k*dt)) + (y[i]/(dt+k*dt**2)))))
    return y,t

#%%

y111,t111 = CrankNicolson(k, r, t0, tf, y0, N1)

plt.figure()
plt.plot(t111,y111,label='Solution Numérique')
plt.plot(t111,f(t111),label='Solution exacte')
plt.xlabel('Temps',size=15)
plt.ylabel('Solutions',size=15)
plt.title('(CN)Solution numérique vs solution exacte pour N = '+str(N1),size=15)
plt.legend()

