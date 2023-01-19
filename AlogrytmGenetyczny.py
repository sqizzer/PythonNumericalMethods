"""Łukasz Giemza
Fizyka Techniczna 2019/2020
Ustalanie położenia atomów przy pomocy algorytmów genetycznych
oraz wpływ wielkości populacji na zbieżność algorytmu i czas obliczeń"""

import numpy as np
import random
from itertools import combinations
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import warnings
from pprint import pprint
warnings.filterwarnings("ignore")

#Informacje na temat algorytmów genetycznych oraz implementowaniu ich w języku python
#z których korzystano podczas pisania programu:
#https://www.researchgate.net/publication/224250405_Global_Optimization_of_Lennard-Jones_Potential_Using_Newly_Developed_Real_Coded_Genetic_Algorithms
#https://mmazurek.dev/algorytmy-genetyczne-w-pythonie/
#Wykład z podstaw metod numerycznych dla FT
#https://www.math.uni.lodz.pl/~marta/2012_2013_z/zz/gen.pdf

print("PROGRAM USTALAJĄCY POŁOŻENIA ATOMÓW ZAIMPLEMENTOWANY PRZY POMOCY ALGORYTMÓW GENETYCZNYCH")
eps = 1.                   #paramtetr epsilon
sigma = 1.                 #parametr sigma
N = 200                   #populacja
Generacja = 300           #liczba generacji (ile razy ma sie zmieniac populacja)
MutacjaSzansa = 0.05       #szansa na mutacje 
Rx=[]                      #puste tablice  
Ry=[]
Rz=[]   
        
LiczbaAtomów = 2
R1=np.random.rand(3)       #3 Generowanie 3 losowych liczb z przedziału (0;1)
R2=np.random.rand(3)

def Lostablica():
    y = [10,10,10]         #Generowanie tablicy trzech dziesiątek
    z = np.random.rand(3)  #Generowanie 3 losowych liczb z przedziału (0;1)
    tablica = (y*z)         #Generowanie tablicy z 3 liczbami o wartosciach z przedziału (0;10)
    return tablica
    

def Losmacierz():
    #Generowanie macierzy n wymiarowej gdzie n to liczba atomów
    macierz = np.array([Lostablica() for i in range(LiczbaAtomów)])
    return macierz
                                                                   
def Populacja():
    return np.array([Losmacierz() for i in range(N)]) #Generowanie X macierzy n wymiarowych gdzie X to populacja, n to liczba atomów

def Odziaływanie(R1, R2):
    #obliczanie odległości między atomami
    r = np.sum((R1[0]-R2[0])**2 + (R1[1]-R2[1])**2 + (R1[2]-R2[2])**2)**0.5  
    V = (4*eps*((sigma/r)**12-(sigma/r)**6))         #oblicznie potencjału z wzoru Lennarda Jonesa dla pary atomów
    return V
    
    
def OdziaływanieCałkowite(czasteczka):
    combs = combinations(czasteczka, 2) #Badanie wszystkich możliwych kombinacji (pary atomów)
    total = sum(list(map(lambda comb: Odziaływanie(comb[0], comb[1]), combs))) #Zsumowanie wszystkich możliwych kombinacji (pary atomów)
    return total
    

def Krzyzowanie(tata, mama, LiczbaAtomów):
    dziecko = list(tata[0:LiczbaAtomów//2]) + list(mama[0:round(LiczbaAtomów/2)]) #Tworzenie dziecka posiadającego cechy (współrzędne) rodziców
    return dziecko

def mutowanie(czasteczka, MutacjaSzansa):
    if random.random() < MutacjaSzansa/2:     #Mutowanie z prawdopodbienstwem 5%
        return list(map(lambda x: x+np.random.rand(3))) #Zmiana wartości współrzędnych  w przypadku mutacji (dodajemy losowa wartosc z przedziału (0;1) do współrzednych)
    if random.random() > 1 - (MutacjaSzansa/2):
        return list(map(lambda x: x-np.random.rand(3))) #Zmiana wartości współrzędnych  w przypadku mutacji (odejmujemy losowa wartosc z przedziału (0;1) do współrzednych)
        
    
def funkcja():            
    populacja = Populacja()
    for i in range(Generacja):        #Tworzenie pętli po wszystkich generacjach (Liczba ta odpowiada liczbie ewolucji populacji)
        przystosowanie = list(map(OdziaływanieCałkowite, populacja))   #okreslenie przystosowania osbników. Najszliniejsze osobniki będą miały najmniejszy potencjał
        zipped = list(zip(populacja, przystosowanie))                 #osobniki z najlepszym przystosowaniem odpowiadają tym które mają największą szansę na dalsze rozmnażanie
        parents_zipped = sorted(zipped, key = lambda z: (z[1]))[0:int(N/10)] 
        parents = list(zip(*parents_zipped))[0]
        pairs = [np.random.choice(range(int(N/10)), 2) for i in range(int(N-N/10))] #Wybranie najsilniejszych osobników (pierwsze 10% na liscie)
        children = list(map(lambda p: Krzyzowanie(parents[p[0]], parents[p[1]], LiczbaAtomów),pairs))
        populacja = list(parents) + children        #losowa populacja po parach ktore zostały wczesniej wybrane
    return populacja

rozwiazanie = funkcja()
j = ("WPÓŁRZĘDNE ATOMÓW WYNOSZĄ: ",rozwiazanie[0])
pprint(j)
print("POTENCJAŁ WYNOSI: \n",OdziaływanieCałkowite(rozwiazanie[0]))
ListOdl = []
i = 0
j = 0
for i in range(LiczbaAtomów):                #Generowanie tablic współrzędnych w celu narysowania rozmieszczenia atomów w przestrzeni
    Rx.append([rozwiazanie[0][i-1][0]])      #Generowanie współrzędnych dla osi X   
    Ry.append([rozwiazanie[0][i-1][1]])      #Generowanie współrzędnych dla osi Y
    Rz.append([rozwiazanie[0][i-1][2]])      #Generowanie współrzędnych dla osi Z
    i += 1
for j in range(LiczbaAtomów):  
    odl=(((rozwiazanie[0][j-1][0])-(rozwiazanie[0][j][0]))**2 + ((rozwiazanie[0][j-1][1])-(rozwiazanie[0][j][1]))**2 + ((rozwiazanie[0][j-1][2])-(rozwiazanie[0][j][2]))**2)**0.5
    ListOdl.append(odl)
    j+=1
print("NAJMNIEJSZA ODLEGŁOSC MIĘDZY PARĄ ATOMÓW WYNOSI: \n", min(ListOdl),"[Å]") 
sr = sum(ListOdl) 
print("SREDNIA ODLEGŁOSC MIĘDZY ATOMAMI WYNOSI: \n", sr/LiczbaAtomów,"[Å]")

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter3D(Rx, Ry, Rz)
ax.set_xlabel('X')  #Opis osi X
ax.set_ylabel('Y')  #Opis osi Y
ax.set_zlabel('Z')  #Opis osi Z
ax.set(xlim=(0, 12), ylim=(0,12), zlim=(0,12))  #Granice wykresu
plt.show()
