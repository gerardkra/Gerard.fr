# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:10:18 2023

@author: Roland
"""


import numpy as np
import scipy.stats as sta
import scipy.integrate as spi
import matplotlib.pyplot as plt

def densGamma(x,N,mu):
    return (x**(N-1)*((np.exp(-x*mu)*mu**N)))/(np.math.factorial(N-1))

# sta.expon.rvs(, kwds)

def RealisationGamma(v,N=10):
    T = np.zeros((len(v),N))
    summ = 0 
    for i in range(len(v)):
        T[i:,] = sta.expon.rvs(size=N, loc = 0, scale = 1/v[i])
    
    for i in range(N):
        summ = summ + min(T[:,i])
        
    return summ
    # print(T)
    
  
# v = np.arange(0.5, 3.3, 0.4)
# print(v)

# print(RealisationGamma(10, np.array([0.75,0.5,0.9,5.5,2.5])))

#2) valeurs par défauts pour RealisationGamma 
# 3) 
G = np.zeros(300)
for i in range(300):
    G[i] = RealisationGamma(v = np.arange(0.5, 3.3, 0.4),N=50)
    
plt.figure()
plt.hist(G,40, density=True)
subreg = np.linspace(min(G),max(G),100)
plt.plot(subreg,densGamma(subreg, 50, 11.9),color='y')

# plt.show(block=False)
#5) 
# calcul de la probabilité

dsc = np.linspace(5,7,30)
P =  spi.simps(densGamma(dsc, N=50, mu=11.9),dsc)
print(f"La probabilité recherchée est {P:.4f}")



        
        
    
    