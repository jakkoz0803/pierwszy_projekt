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
