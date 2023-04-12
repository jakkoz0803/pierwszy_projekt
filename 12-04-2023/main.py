import numpy as np
#inicjalizacja tablicy
a = np.array([0, 1])
print(a)
#drugi sposob
a = np.arange(2)
print(a)
#wypisanie typu zmiennej tablicy (nie jej elementow)
print(type(a))
#sprawdzenie typu danych tablicy
print(a.dtype)
#inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype = 'int64')
print(a.dtype)