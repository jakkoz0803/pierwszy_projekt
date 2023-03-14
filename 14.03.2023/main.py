import math

print("-------------- zad 1 --------------")
print(math.pow(math.e,10))
print(math.pow(math.log((5+math.pow(math.sin(8),2)),math.e),(1/6)))
print(math.floor(3.55))
print(math.ceil(4.80))

print("-------------- zad 2 --------------")
imie = "JAKUB"
nazwisko = "KOZICKI"
print(imie.capitalize(), nazwisko.capitalize())

print("-------------- zad 3 --------------")
tekst_piosenki = "The ting goes skrraa POP POP KA KA KA"
print(tekst_piosenki)
print(tekst_piosenki.count("KA"))

print("-------------- zad 4 --------------")
dowolna_zmienna_lancuchowa = "losowe slowa ktore przychodza mi do glowy"
print(dowolna_zmienna_lancuchowa)
print(dowolna_zmienna_lancuchowa[1], dowolna_zmienna_lancuchowa[len(dowolna_zmienna_lancuchowa) - 1])

print("-------------- zad 5 --------------")
print(dowolna_zmienna_lancuchowa.split())

print("-------------- zad 6 --------------")
liczba_1 = str(435)
liczba_2 = float(254)
liczba_3 = hex(353)
print(liczba_1)
print(liczba_2)
print(liczba_3)

print("-------------- zad 7 --------------")
lista_sportow = ["pilka nozna","skoki narciarskie","siatkowka"]
print(lista_sportow)
lista_sportow.reverse()
lista_sportow.append("koszykowka")
lista_sportow.append("curling")
print(lista_sportow)

print("-------------- zad 8 --------------")
skroty = {
    "np": "na przyklad",
    "nwm": "nie wiem",
    "wgl": "w ogole"
}
print(skroty.keys())
print(skroty.values())

print("-------------- zad 9 --------------")
gry = {
    "cs": "Counter Strike: Global Offensive",
    "mc": "Minecraft",
    "phasmo": "Phasmophobia"
}
print(gry.keys())
print(gry.values())

print("-------------- zad 10 --------------")
print("prosze serdecznie o napisanie losowego zdania:\n")
zdanie = input()
print("napisales zdanie: " + zdanie)
print("liczba liter 'a' w twoim zdaniu: ", zdanie.count("a"))

print("-------------- zad 11 --------------")
print("podaj 3 liczby: \n")
a = input()
b = input()
c = input()
max = a
if(b > max):
    max = b
if(c > max):
    max = c
print("najwieksza liczba: ",max)
