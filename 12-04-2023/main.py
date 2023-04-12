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
######
a = np.array([[0,1],[2,3]])
print(a)
#zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b)
print(b.dtype)
#wypisanie rozmiaru tablicy
print(b.shape)
# mozna tez sprawdzic ilosc wymiarow tablicy
print(a.ndim)
#stworzenie tablicy wielowymiarowej moze wygladac cos tam
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
#ponownie typem jest ndarray
print(type(m))

zera = np.zeros([3,3])
jedynki = np.ones([4,4])
print(zera)
print(jedynki)
#warto sprawdzic jaki jset domyslny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)
#mozna rowniez stworzyc "pusta" macierz o podanych wymiarach
#wartosci umieszczane sa losowe, najpierw podawana jest cos tam
pusta = np.empty([2,2])
print(pusta)
# #do elementow tablic mozemy odwolac sie tak jak do cos tam

