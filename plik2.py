dane = ["aba",  101, (5,6), 2.22]
test = [(5,6), 3.33]
for klucz in test:
    if klucz in dane:
        print(klucz, "znaleziono")
else:
    print(klucz, "nie znaleziono")
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def mnozenie(x, y):
    return x *  y
wynik = mnozenie(2, 4)
print(wynik)
