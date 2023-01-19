"""1.1a Metodą równego podziału znaleźć miejsca zerowe f(x)= x^3 - 1500000*x^2
+750000000002*x - 12500000000099990  w przedziale [0;10^6] z Epsilon=0,01"""

x1 = 0              #początek przedziału
x2 = 1E6            #koniec przedziału
Epsilon = 0.01     #dokładnosc z jaką szukam miejsca zerowego

def f(x):
    return x**3 - (1.5*1E6*x**2) +750000000002*x - 125000000000099990  #okreslam wzor funckji
    

while abs(x1 - x2) >= Epsilon:   #sprawdzam czy zadany przedzial jest wiekszy badz rowny dokladnosci wartosci miejsca zerowego
    y1 = (x1 + x2)/2          #dziele przedział na poł (metoda równego podziału)
    y2 = f(x1) * f(y1)        #dzieląc przedział na pół zyskuje 2 inne przedziały. Miejsce zerowe jest w tym przedziale w którym wartosci
                              #na koncach jedengo z tych 2 przedziałow mają przeciwne znaki (wtedy funkja sie przecina z osia 0X, wiec
                              #na przecieciu znajduje sie miejsce zerowe funkcji. Szukam ktory to przedział"""
    
    if y2 > 0:            
        x1 = y1                # nadpisywanie lewego krańca przedziału
    elif y2 < 0:
        x2 = y1                # nadpisywanie prawego krańca przedziału
print(y1)           #miejsce zerowe z dokładnoscia do Epsilon




   
