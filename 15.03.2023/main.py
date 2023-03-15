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
