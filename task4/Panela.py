"""
Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym pomieszczeniu,
zakładając prostokątną podłogę i prostokątne panele.
Dane wejściowe to długość i szerokość podłogi, (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela
oraz ilość paneli w opakowaniu.
"""
import math

szerPodl = float(input("wpraowadz szerokosc podlogi: "))
dlugPodl = float(input("wpraowadz dlugosc podlogi: "))
szerPaneli = float(input("wpraowadz szerokosc paneli: "))
dlugPaneli = float(input("wpraowadz szerokosc paneli: "))
iloscOpakowaniu = int(input("ilosc paneli w opakowaniu: "))


def pre(szerokosc_podlogi, dlugosc_podlogi, szerokosc_Paneli, dlugosc_Paneli, ilosc_w_opakowaniu):
    powierzchnia_Pomiszcz = dlugosc_podlogi * szerokosc_podlogi * 1.1
    powierzchnia_Paneli = dlugosc_Paneli * szerokosc_Paneli
    ilosc_ktora_potrzebna = powierzchnia_Pomiszcz // powierzchnia_Paneli
    iloscOpakowan = ilosc_ktora_potrzebna / ilosc_w_opakowaniu
    return math.ceil(iloscOpakowan)


resul = pre(szerokosc_podlogi=szerPodl, dlugosc_podlogi=dlugPodl, szerokosc_Paneli=szerPaneli,
            dlugosc_Paneli=dlugPaneli, ilosc_w_opakowaniu=iloscOpakowaniu)
print(f'Ilosc potrzebnych opakowan = {resul} ')
