plik = open("tekst.txt","r")

znaki = plik.read(10)

linia = plik.readline()

wiersze = plik.readlines()

plik.close()

print(znaki)
print("---\n")

print(linia)
print("---\n")

print(wiersze)
print("---\n")
#---------------------------------------------------
dane = "inf, 1, io"

plik = open("dane.txt","w+")
plik.write(dane)
plik.close()
#---------------------------------------------------
print("--- klasy i obiekty ---\n")

class PierwszaKlasa:
    """Przykład klasy"""
    atrybut = 54321
    def pierwsza_metoda(self):
        return "Teraz działa pierwsza metoda"
obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
print(obiekt.pierwsza_metoda())
obiekt.tekst = "trololo"
print(obiekt.tekst)
