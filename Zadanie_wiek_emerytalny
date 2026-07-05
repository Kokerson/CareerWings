name = input("Podaj imie: ");
year = int(input("Podaj rok urodzenia: "));

age = 2026 - year; #obliczanie wieku

if name[-1]=='a': #sprawdzanie wieku w zależności czy kobieta czy mężczyzna dla imion polskich
    pension_age=60; #wiek emerytalny kobiet
else:
    pension_age=65; #wiek emerytalny mężczyzn

years_to_pension = pension_age - age; #lata do emerytury

if years_to_pension <= 0: #wypisanie spersnonalizowanej wiadomości
    print(f"Witaj {name}, możesz być na emeryturze.");
else:
    print(f"Witaj {name}, do emerytury zostało ci {years_to_pension} lat.");
