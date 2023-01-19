# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:44:09 2020

@author: Lukasz
"""

import matplotlib.pyplot as plt
import random
y = 100000  #liczba obiektow
n = 10       #liczba krokow
x = 0
i = 0
f = 0
lista = []
lista2 = []
for i in range(y):
    x = 0
    for f in range(n):
            
        a = random.randrange(-1,2,2)
        x = x + a
        lista.append(x)
            
    #print(x)  
    lista2.append(x)
h1 = plt.hist(lista2)
plt.show()    
