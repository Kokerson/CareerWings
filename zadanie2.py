import json
plik_notatki = "notatki.json"

def wczytaj():
    try:
        with open(plik_notatki, 'r') as plik:
            zawartosc = plik.read()
            if (zawartosc != ""):
                return json.loads(zawartosc)
            else:
                return []
    except FileNotFoundError:
        return []

def zapisz(notatki):
    with open(plik_notatki, 'w') as plik:
        json.dump(notatki, plik)

def dodaj(notatki):
    text = input("Wpisz treść notatki: ")
    if(text==""):
        print("Notatka nie może być pusta")
    else:
        notatki.append(text)
        zapisz(notatki)

def wyswietl(notatki):
    if len(notatki) == 0:
        print("pusty plik")
    else:
        for i in range(len(notatki)):
            print(f"{i + 1} {notatki[i]}")

def usun(notatki):
    if len(notatki) == 0:
        print("Brak notatek do usunięcia")
    else:
        numer = int(input("Którą notatkę chcesz usunąć ?"))
        if (numer > len(notatki) or numer <= 0):
            print("zły numer\n")
        else:
            notatki.pop(numer-1)
            zapisz(notatki)

menu = int(input("0 - koniec, 1 - dodanie notatki, 2 - wyświetlenie, 3 - usunięcie notatki\n"));
notatki = wczytaj()
while(True):
    if(menu==1):
        dodaj(notatki)
    elif(menu==2):
        wyswietl(notatki)
    elif(menu==3):
        usun(notatki)
    elif(menu==0):
        break;
    else:
        print("zły numer\n")
    menu = int(input("0 - koniec, 1 - dodanie notatki, 2 - wyświetlenie, 3 - usunięcie notatki\n"));
