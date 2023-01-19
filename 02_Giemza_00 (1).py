"""
Równanie dN/N = -λt posiada rozwiązanie analityczne N = N0exp(-λt).
 Sprawdzić różnicę pomiędzy metodą iteracyjną (patrz zestaw 1 ćwiczenie 2.2) a rozwiązaniem analitycznym.
 Narysować wykresy dla różnic pomiędzy metodami obliczeń i porównać dla różnych kroków iteracji Δt.

Dane:
N0 = 1
λ = 1
Δt = 0.0001, 0.01 ,0.1, 1, 10
0 ≤ t ≤ 20

W kodzie skomentować otrzymane wyniki (nie więcej niż 280 znaków)."""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
lbd = 1. #yr**-1 stała zaniku C-14
delta_t = float(0.0001) #yr krok iteracji
def krok1():
    N_0 = 1. # początkowa liczba radionuklidów
    time = np.arange(0., 20., delta_t)
    N_iter = np.zeros(time.size)
    N_a = N_0*np.exp(-lbd*time) #rozwiązanie analityczne
    N = N_0 # ustawiamy początkową liczbę radionuklidów dla metody iteracyjnej
    for i, t in enumerate(time):
       N_iter[i] = N
       N = N - (N * lbd * delta_t)
       
       
     
    fig, ax = plt.subplots()
    ax.plot(time, N_iter, '.', label='Rozwiązanie iteracyjne')
    ax.plot(time, N_a, '.', label='Rozwiązanie analityczne')
    ax.plot(time, N_a-N_iter, '.', label='N_a-N_iter')
    ax.set(xlabel='time (yr)', ylabel='N')
    plt.legend()
    plt.show()
krok1()
delta_t = float(0.01)
krok1()
delta_t = float(0.1)
krok1()
delta_t = float(1)
krok1()
delta_t = float(10)
krok1()

"""W zadaniu mamy 5 różnych kroków iteracji delta_t, dlatego stworzono po 1 wykresie
dla kazdego przypadku. Rozwiązanie analityczne dla każdego przypadku jest oczywiscie
takie samo, ponieważ krok iteracji nie ma w tym wypadku zadnego wpływu. Jak widać
na wykresach, im mniejszy mamy krok iteracji, tym rozwiązanie iteracyjne 
bardziej pokrywa się z rozwiązaniem analitycznym (dla delta_t = 0.0001, rozwiązania
są praktycznie identyczne)"""



    
