from scipy.optimize import differential_evolution
import numpy as np

def f(x):
    x0 = x[0]   #x0 = y
    x1 = x[1]    #x1 = x
    
    
    return x[0] * np.sin(x[1]) * np.sin(x[1])  + 2 * x[1] * np.cos(x[0])
    

bounds = [(-10,10), (-10,10)]
result = differential_evolution(f, bounds, polish = True)
print('wartosci kolejno dla y oraz x wynosza: ', result.x)
print('minimum funkcji wynosi: ', result.fun)
