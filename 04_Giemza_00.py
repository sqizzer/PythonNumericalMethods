import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3.-1500000.*x**2+750000000002.*x-125000000000999990.

def f_p(x):
    return 3.*x**2.-2.*1500000.*x+750000000002.

def f_pp(x):
    return 6.*x-2.*1500000.

epsilon = 0.5

a = 0.
b = 1E6


x_tested = []
y_tested = []

x_a = a
x_b = b

#Metoda rownego podziału
"""while epsilon < abs(x_a - x_b):
    x_i = 0.5*(x_a + x_b)
    if f(x_i) * f(x_a) < 0:
        x_b = x_i
    else:
        x_a = x_i
    x_tested.append(x_i)
    y_tested.append(0.)
print("wynik dla metody rownego podziału to:", x_i)  



def wykres1():

    fig, ax = plt.subplots()

    ax.plot(np.linspace(a, b, 3000), f(np.linspace(a, b, 3000)), ':', c='k') 
    ax.plot(x_tested, y_tested, '.',  c='r')
    ax.set(xlabel='x', ylabel='y')
    #plt.yscale('symlog', linthreshy=0.01)


    plt.show()
wykres1()"""

#metoda Newtona
x_a1 = a
x_b1 = b
Xn = []
X = []
Y = []
i = 0
kroki = []

while epsilon < abs(x_a1 - x_b1):   
    Y.append([f(x_a1), 0.])
    Xn.append(x_a1-499000)
    x_b1 = x_a1
    x_a1 = x_a1 - f(x_a1)/f_p(x_a1)
    
    X.append([x_b1,x_a1])
    
    i += 1
    kroki.append(i)
    
    #print(i, Xn)
    
print('wynik dla metody newtona to: ', x_a1)
print('wynik został podany dla numeru itracji rownego: ', i)


def wykres2():
    
    fig, ax = plt.subplots()

    #ax.plot(np.linspace(a, i,), f(np.linspace(a, i,)), ':', c='k')

    #for xx, yy in  zip(kroki, Xn):
    ax.plot(kroki, Xn, '-', c='r')


    ax.set(xlabel='i', ylabel='Xn')

    plt.yscale('symlog', linthreshy=0.01)


    plt.show()
wykres2()
"""
#metoda Halleya
x_a2 = a
x_b2 = b

X2 = []
Y2 = []


i = 0
while epsilon < abs(x_a2 - x_b2):
    Y2.append([f(x_a2), 0.])
    x_b2 = x_a2
    x_a2 = x_a2 - f(x_a2)/f_p(x_a2)*(1-f(x_a2)/f_p(x_a2)*f_pp(x_a2)/f_p(x_a2)/2)**-1.
    #print(abs(x_a - x_b), x_a, x_b)
    X2.append([x_b2,x_a2])
print("wynik dla metody Halleya to:")
print(abs(x_a2 - x_b2), x_a2, x_b2)    

def wykres3():
    fig, ax = plt.subplots()

    ax.plot(np.linspace(a, b, 3000), f(np.linspace(a, b, 3000)), ':', c='k')

    for xx, yy in  zip(X2, Y2):
        ax.plot(xx, yy, '-', c='r')

    ax.set(xlabel='x', ylabel='y')
#plt.yscale('symlog', linthreshy=0.01)


    plt.show()
wykres3()    


print("Porównanie wszystkich metod:") 
fig, ax = plt.subplots()

ax.plot(np.linspace(a, b, 3000), f(np.linspace(a, b, 3000)), ':', c='k') #linespace tworzy liste od [a,.....b] 3000takich
ax.plot(x_tested, y_tested, '.',  c='r', label = ("metoda rownego podziału"))
for xx, yy in  zip(X, Y):
        ax.plot(xx, yy, '-', c='b')
   
for xx, yy in  zip(X2, Y2):
        ax.plot(xx, yy, '-', c='g')        

plt.legend()
plt.show()
print("Kolor niebieski = metoda Newtona")
print("Kolor zielony = metoda Halleya")"""

 










