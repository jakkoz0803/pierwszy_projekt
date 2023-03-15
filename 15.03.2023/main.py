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
# VVV to ejst na razie przyklad, nie zadanie 4
def kwadratowe(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("brak pierwiastkow")
        return -1
    elif delta == 0:
        print("jeden")
        x = (-b)/(2*a)
        return x
    else:
        print("dwa")
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1,x2
print(kwadratowe(3,6,2))
print(kwadratowe(4,1,7))
