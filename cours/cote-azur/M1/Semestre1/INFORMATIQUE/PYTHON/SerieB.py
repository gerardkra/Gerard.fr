# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:19:47 2023

@author: Roland
"""

import numpy as np
import matplotlib.pyplot as plt


def f_n(u,n):
    summ = 0
    for i in range(n+1):
        summ = summ + (((-1)**i * u**(2*i+1))/(np.math.factorial(2*i+1)))
    return summ

def DSEsin(n,U):
    R = np.zeros(len(U))
    for i in range(len(U)):
        R[i] = f_n(U[i], n)
    return R

U = np.linspace(-9,9,351)

# n =0 -> rouge, n=2 -> vert, n=4 -> jaune, n=8 -> magenta, n=10 -> cyan
plt.figure()
plt.ylim([-5,5])
# plt.xlim([-8,8])
plt.plot(U,np.sin(U),color='b',ls='-')
plt.plot(f_n(U, n = 0),color='r', ls='--')
plt.plot(f_n(U, n = 2),color='g', ls='--')
plt.plot(f_n(U, n = 4),color='y', ls='--')
plt.plot(f_n(U, n = 8),color='m', ls='--')
plt.plot(f_n(U, n = 10),color='c', ls='--')
plt.legend(['sin(x)','k = 0', 'k = 2', 'k = 4', 'k = 8', 'k = 10'], fontsize = 10)
# plt.xlim([-8,8])
plt.xlabel('u')
plt.ylabel('f_n(u)')
plt.title('Convergence de f_n vers sinus')

# plt.subplot(1,1,1)
# plt.plot(np.linalg.norm(f_n(U, n=0) - np.sin(U)),color='b')
# plt.plot(np.linalg.norm(f_n(U, n=2) - np.sin(U)),color='b')
# plt.plot(np.linalg.norm(f_n(U, n=4) - np.sin(U)),color='b')
# plt.plot(np.linalg.norm(f_n(U, n=8) - np.sin(U)),color='b')
# plt.plot(np.linalg.norm(f_n(U, n=10) - np.sin(U)),color='b')
# plt.show()