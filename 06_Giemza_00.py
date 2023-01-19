# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:19:10 2019

@author: Lukasz
"""



import numpy as np



c = 14.4*10**-10          #suma poszczegolnych stalych w wzorze
eps = 0.001           #dokładnosc

r0 = 0.33*10**-10
V0 = 1.09*10**3
V = lambda x:(-c/r + (V0 * np.exp(-r/r0)))   #wzor funkcji V(r)


a = 10**-10    #poczatek przedzialu
b = 10*10**-10  #koniec przedzialu



fi = (1 + np.sqrt(5)) / 2   #złota wartosc       
fi2 = 2 - fi                     

def funkcja(V, a, b, eps):
    if abs(a - b) < eps:       
        return (a + b) / 2
    c = b - (b - a) / fi
    d = c + fi2 * (b - c)        
    if V(d) < V(c):
        return funkcja(V, d, b, eps)
    else:
        return funkcja(V, d, a, eps)


print(funkcja(V, a, b, eps))