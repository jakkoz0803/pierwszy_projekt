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
macierz = np.empty([2,2])
print(macierz)
# #do elementow tablic mozemy odwolac sie tak jak do cos tam
poz_1 = macierz[1,1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)
# #tworzenie macierzy 2x2 wraz z uzupelnieniem
liczby = np.arange(1,2,0.1)
print(liczby)
# podobnie dziala funkcja linspace
liczby_lin = np.linspace(1,2,5,endpoint=False)
print(liczby_lin)
liczby_lin = np.linspace(1,2,5,endpoint=True)
print(liczby_lin)
#a teraz mozemy utworzyc dwie macierze, najpierw wartosci cos tam
z = np.indices((5,3))
print("=========")
print(z)
print("=========")
print(z[0])
print(z[0][1])
print(z[0][1][2])
# #podobnie jak w MATLAB mozemy tworzyc macierz diagonal
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
#w powyzszym przykladzie stworzony wektor wartosci cos tam
#mozemy podac drugi parametr funkcji diag, ktory okresla cos tam
#ktora zostanie wypelniona wartosciami podanego wektora
mat_diag_k = np.diag([a for a in range(5)], 1)
print(mat_diag_k)
#Numpy jest w stanie stworzyc tablice jednowymiarowa z cos tam
z = np.fromiter(range(5), dtype='int32')
print(z)
