# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:20:10 2023

@author: Roland
"""

class suite_g:
    def __init__(self,a_ini=1,raison=2):
        self.a = a_ini
        self.r = raison
        
    def __str__(self):
        return f"Suite géométrique de terme initial {self.a} et de raison {self.r}"
        
    def terme(self,n):
        u_n = self.a*(self.r)**n
        return u_n
    def __mul__(self,s):
        if(type(s) == type(self)):
            return suite_g(self.a*s.a,self.r*s.r)
        else:
            return suite_g(self.a*s,self.r)
        
   
S = suite_g(10,3);print(S)
S1 = suite_g(3j,4);print(S1)
print(S1.terme(10))
T1 = suite_g(2,4);T2=suite_g(3,2);z=1+2j
print(T1*z)

        
    