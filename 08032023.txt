a = 'napis'
print(a)
print(type(a))
b = 5
print(a+str(b))

c = 5
d = 5.3

print(c, d)
e = c+d
print(e)
f = 2+3j
print(f)
print(type(f))

print(c-d)
print(c//d)
print(c%d)
print(c**d)
print(2**(1/2))
print(c)
c+=2
print(c)


listy = ['2', 5, 6, 7, 6.5, [2,3,4]]
print(listy)
listy.append(4)
print(listy)
print('-------------')

# dodanie elementu do listy na danej pozycji
listy.insert(3,'asdf')
print(listy)
print('-------------')

# usuniecie elementu z danej pozycji
del listy[2]
print(listy)
listy.pop(1)
print(listy)
print('-------------')

# usuniecie elementu o danej wartosci
listy.remove(6.5)
print(listy)
print('-------------')

# dodac sekwencje do listy

# odwrocic liste
listy.reverse()
print(listy)
print('-------------')

# posortowac elementy w liscie
listy.pop(1)
listy.pop(2)
listy.pop(2)
listy.reverse()
print(listy)
listy.sort()
print(listy)
print('-------------')

slownik = {1: 'a', 2: 2, 3: 'klucz',1:3}
print(slownik)    # {1: 3, 2: 2, 3: 'klucz'}

print(slownik[3])    # klucz
slownik['nowy'] = 'wartosc'
print(slownik)    # {1: 3, 2: 2, 3: 'klucz', 'nowy': 'wartosc'}
slownik.pop(2)
print(slownik)    # {1: 3, 3: 'klucz', 'nowy': 'wartosc'}
del(slownik[3])
print(slownik)    # {1: 3, 'nowy': 'wartosc'}

print(slownik.keys())    # dict_keys([1, 'nowy'])
print(slownik.values())    # dict_values([3, 'wartosc'])

print('a = %(zm)d' % {'zm': 12}) # a = 12
print('a = {}'.format(12)) # a = 12

napis = input('wprowadz liczbe: ')
print(napis)
# wprowadz liczbe: 13
# 13
print(type(napis))    # <class 'str'>
napis = int(napis)
print(type(napis))    # <class 'int'>

#instrukcja warunkowa
#if warunek:
    #instrukcje
#elif warunek
    #instrukcje
#else:
    #instrukcje

a = input('podaj a: ')
b = input('podaj b: ')
a = int(a)
b = int(b)
c = input('podaj c: ')
d = input('podaj d: ')
c = int(c)
d = int(d)

if (a > b) & (c > d):
    print('a > b oraz c > d')
else:
    print('a <= b lub c <= d')
# podaj a: 5
# podaj b: 3
# podaj c: 7
# podaj d: 5
# a > b oraz c > d

a = input('podaj a: ')
b = input('podaj b: ')
a = int(a)
b = int(b)

if a == b:
    print('a rowne b')
else:
    print('a nie rowne b')


# for element in sekwencja:
#     instrukcje:
# else:
#     instrukcje po petli

for x in range(1, 6, 1):        # element poczatkowy, element koncowy (jest pomijany), o ile sie zwieksza
    print(x)
else:
    print('koniec petli for')
# 1
# 2
# 3
# 4
# 5
# koniec petli for

lista = [3,5,2,3,3,4]
for x in lista:
    print(x)
else:
    print('----')

for x in range(0, lista.__sizeof__(), 1):
    print(lista[x])
else:
    print('---')