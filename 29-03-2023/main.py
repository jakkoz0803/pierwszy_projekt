import math
# ---------------- zestaw A ---------------- #
# zad 1
a = input('podaj a: ')
b = input('podaj b: ')

try:
    a = int(a)
    b = int(b)
    wynik1 = int(a*a + a*b + b*b)
    print(wynik1)
    plik = open("zadanie1.txt","w")
    plik.writelines(str(wynik1))
    plik.close()
except ValueError:
    print("niepoprawne wartosci")

# zad 2
lista1 = [3,4,5]
lista2 = [2,5,1]
def sumaList(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    return lista3
print(sumaList(lista1,lista2))

# zad 3
plik = open("tekst.txt","r", encoding="utf8")
plik.read(99)
lines = plik.read(35)
print(lines)
caps = [x for x in lines if x.isupper()]
print(caps)
print(len(caps))

plik.close()

# zad 4
lista1 = [1,3,5,7,9,0,2,4,6,8]
a = 4
lista2 = [lista1[i] for i in range(len(lista1)) if lista1[i] > a]
print(lista2)

# zad 5
wynik = math.pow(pow(math.e,3) + pow(math.cos(39),2),1/5) + math.pow(2/7,3) + math.pi
print(round(wynik,2))
