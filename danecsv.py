import pandas as pd

df = pd.read_csv("dane_sprzedazowe.csv")

df["Wartosc_zamowienia"] = df["Cena"] * df["Ilosc"]

top_5_produktow = df.groupby("Produkt")["Wartosc_zamowienia"].sum().reset_index()

top_5_produktow = top_5_produktow.sort_values("Wartosc_zamowienia", ascending=False).head(5)

srednia_wartosc = df["Wartosc_zamowienia"].mean()

df["Data"] = pd.to_datetime(df["Data"])
df["Miesiac"] = df["Data"].dt.to_period("M")

miesieczne_sumy = df.groupby("Miesiac")["Wartosc_zamowienia"].sum().reset_index()

top_5_produktow.to_csv("raport_top5.csv", index=False)
miesieczne_sumy.to_csv("raport_miesieczny.csv", index=False)

print(f"Średnia wartość zamówienia to: {srednia_wartosc:.2f} PLN")
print("Raporty zostały zapisane do plików CSV!")
