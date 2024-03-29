import random
import math

print("podaj a: ")
a = input()
print("podaj b: ")
b = input()
try:
    wynik = int(a)/int(b)
    print("a/b = " + str(wynik))
except ZeroDivisionError: #nazwa bledu dzdizld 0
    print("nie mozesz\n")

print("============ zad 1 ============")
lista_a = [1-x for x in (1,10)]
print(lista_a)
lista_b = [4**x for x in range(7)]
print(lista_b)
lista_c = [x for x in lista_b if x % 2 == 0]
print(lista_c)

print("============ zad 2 ============")
listy1 = []
for i in range(10):
    listy1.append(random.randint(1,10))
print(listy1)
listy1_parzyste = [x for x in listy1 if x % 2 == 0]
print(listy1_parzyste)

print("============ zad 3 ============")
# Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu a
# wartość - jednostka w jakiej się je kupuje
# (np. sztuki, kg). Wykorzystaj Python Comprehension do
# zdefiniowania nowej listy, gdzie będą produkty,
# których wartości to sztuki.
skroty = {
    "cukier": "kg",
    "woda": "l",
    "jablko": "szt"
}
print(skroty)
# --- zwykla petla:
odwrocone = {}
for key, value in skroty.items():
    odwrocone[value] = key
print(odwrocone)
# --- python comprehension:
odwrocone2 = {value: key for key, value in skroty.items()}
print(odwrocone2)

print("============ zad 4 ============")
# Zdefiniuj funkcję, która sprawdzi, czy trójkąt jest prostokątny
def czy_prostokatny(a,b,c):
    if a**2 + b**2 == c**2:
        print("prostokatny, a^2 + b^2 = c^2")
        return True
    elif a**2 + c**2 == b**2:
        print("prostokatny, a^2 + c^2 = b^2")
        return True
    elif b**2 + c**2 == a**2:
        print("prostokatny, b^2 + c^2 = a^2")
        return True
    else:
        return False
print(czy_prostokatny(3,6,2))
print(czy_prostokatny(4,1,7))
print(czy_prostokatny(3,4,5))

print("============ zad 5 ============")
# Zdefiniuj fuckcję, która obliczy pole trapezu.
# Funkcja ma przyjmować wartości domyślne
def pole_trapezu(a = 0, b = 0, h = 0):
    return ((a+b)*h)/2
# wywołanie funkcji dla wartości domyślnych:
print(pole_trapezu())
# wywołanie funkcji dla podanych wartości:
print(pole_trapezu(3,7,5))                  # kolejnosc ważna
print(pole_trapezu(h = 3, a = 7, b = 5))    # kolejność dowolna

print("============ zad 6 ============")
def ilo_elem_ciagu_1(a = 1, b = 4, ile = 10):
    wynik = 1
    for i in range(ile):
        wynik = wynik * a*(b**i)
    return wynik
print(ilo_elem_ciagu_1())         # wartosci domyslne
print(ilo_elem_ciagu_1(1,2,4))    # podane wartosci

print("============ zad 7 ============")
def ilo_elem_ciagu_2(*, a = 1, b = 4, ile = 10):
    wynik = 1
    for i in range(ile):
        wynik = wynik * a*(b**i)
    return wynik
print(ilo_elem_ciagu_2())                           # wartosci domyslne
print(ilo_elem_ciagu_2(a = 1, b = 2, ile = 4))      # podane wartosci
# praktycznie to samo tylko trzeba podac
# np. a=1, b=2, ile=4 zamiast
# 1,2,4

print("============ zad 8 ============")
# ** - możemy użyć dowolną ilość argumentów z kluczem
# kiedys zrobie

print("============ zad 9 ============")
print("podaj a: ")
a = int(input())
if a < 0:
    print("nie mozna")
else:
    print(math.sqrt(a))
