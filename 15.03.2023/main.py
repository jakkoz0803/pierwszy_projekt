import random

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
