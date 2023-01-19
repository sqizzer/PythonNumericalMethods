import numpy as np
import matplotlib.pyplot as plt
from scipy import special

#a

a = -0.1
b = 3
c = 0.1

n_a = 1000000
X_a = np.zeros(n_a)

for i in range(n_a):
	r_a = np.random.rand()
	if r_a >= 0 and r_a <= (c - a)/(b - a):
		X_a[i] = np.sqrt(r_a * (b - a) * (c - a)) + a
	elif r_a <= 1 and r_a <= (c - a)/(b - a):
		X_a[i] = b - np.sqrt((1 - r_a) * (b - a) * (b - c))

y, bins = np.histogram(X_a, 10)
fig, ax = plt.subplots()

ax.plot(bins[0: -1], y, c = "blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Histogram, Rozklad trojkatny')

plt.show()

#_______________________________________________________________
# b

mu = 1
sigma = 2

n_b = 1000000
X_b = np.zeros(n_b)

for i in range(n_b):
	r_b = np.random.rand()
	X_b[i] = sigma * np.sqrt(2) * special.erfinv(2 * r_b - 1) + mu

y, bins = np.histogram(X_b, 100)
fig, ax = plt.subplots()

ax.plot(bins[0: -1], y, c = "red")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Histogram, Rozklad normalny')

plt.show()

#_______________________________________________________________
# c

lbd = 1
n_c = 1000000
X_c = np.zeros(n_c)

for i in range(n_c):
	r_c = np.random.rand()
	X_c[i] = -(np.log(np.abs(1 - r_c)))/lbd

y, bins = np.histogram(X_c, 100)
fig, ax = plt.subplots()

ax.plot(bins[0: -1], y, c = "green")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Histogram, Rozklad wykladniczy')

plt.show()

#w jaki sposob otrzymujemy te rozklady  (dystrybuanta)