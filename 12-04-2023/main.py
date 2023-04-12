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
#
znaki = b'ogolna'
z1 = np.frombuffer(znaki,dtype='S1') # string dlugosci 1
print(z1)
z2 = np.frombuffer(znaki,dtype='S2') # string dlugosci 2
print(z2)
#
znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki,dtype = 'S1')
print("===================")
print(z3)
print(z4)
print(z5)
print(z6)
print("===================")
#
a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
#mozemy ciac tablice rowniez w sposob znany z ciecia cos tam
print(a[2:7:2])
#lub tak
print(a[1:])
print(a[2:5])
# w podobny sposob postepujemy w przypadki tablic wielocos tam
mat = np.arange(25)
#teraz zmieniamy ksztalt tablicy jednowymiarowej na mcos tam
mat = mat.reshape((5,5))
print(mat)
print(mat[1:])              # od drugiego wiersza
print(mat[:,1])             # druga kolumna jako wektor
print(mat[:,1:2])           # druga kolumna jako wektor ale inaczej, z macierzy 5x5 -> 5x1, ostatni element cos tam
print(mat[:,-1])            # ostatnia kolumna
print(mat[:,4:5])           # ostatnia kolumna to samo co druga kolumna
print(mat[2:6,1:3])         # 2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, range(2,6,2)]) # 3 i 5 kolumna (sam dwukropek - wszystkie wiersze)
print(mat[:, [2,4]])        # to samo ale inaczej

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x)
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print(y)
