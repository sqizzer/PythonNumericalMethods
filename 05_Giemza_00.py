# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:25:50 2019

@author: Lukasz
"""


import numpy as np
import matplotlib.pyplot as plt

eps = 0.01 #dopuszczalny blad
a=0 #początek przedzialu
b=1000000 #koniec przedziału

x_a = a
x_b = b
i = 0


def f(x): 
    return x**3 - (1500000)*x**2 + (750000000002)*x - 125000000000999990
if f(a) * f(b) < 0: #jesli przeciwne znaki na koncach przedzialu to istnieje m zerowe
    for i in range(10000):
        x_c = x_b - (x_b - x_a)/(f(b) - f(a)) * f(b) #wzor na xc (nowa granica przedzialu)
        if abs(f(x_c)) < eps: break   #sprawdzam czy wartosc funkcji w punkcie x_c nie jest mniejsza od dokladnosci eps
        elif f(x_a) * f(x_c) < 0:      #zamiana koncow przedzialow  
            x_b = x_c
        else:
            x_a = x_c
print(x_c, i)
