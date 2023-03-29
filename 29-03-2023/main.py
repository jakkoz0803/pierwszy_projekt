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
