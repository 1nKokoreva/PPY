# Napisz generator, który użyje generatora read_titles oraz funkcji get_article do zwracania zawartości artykułów z
# wikipedii ( plik small.txt – 1000 tematów). Użyj tego generatora w funkcji, aby policzyć średnią liczbę
# występowania wszystkich odrębnych liter w artykułach. Wywołaj funkcję i wyświetl średnią liczbę liter na artykuł.
import wikipediaapi

def pobierz_artykul(nazwa):
    w_api = wikipediaapi.Wikipedia('pl')
    strona = w_api.page(nazwa)
    if not strona.exists():
        return ""
    else:
        return strona.text

def czytaj_tytuly(sciezka_do_pliku):
    with open(sciezka_do_pliku, 'r') as plik:
        for linia in plik:
            yield linia.strip()

def oblicz_srednia_liczba_liter(sciezka_do_pliku):
    generator_artykulow = generator(sciezka_do_pliku)
    suma_liter = 0
    liczba_artykulow = 0

    for artykul in generator_artykulow:
        if artykul:
            liczba_liter = len(artykul.replace(" ", "").replace("\n", ""))
            suma_liter += liczba_liter
            liczba_artykulow += 1

    if liczba_artykulow > 0:
        srednia_liczba_liter = suma_liter / liczba_artykulow
        return srednia_liczba_liter
    else:
        return 0

srednia_liczba_liter = oblicz_srednia_liczba_liter('small.txt')
print("AVG:", srednia_liczba_liter) #Średnia liczba liter na artykuł
def generator(sciezka_do_pliku):
    generator_tytulow = czytaj_tytuly(sciezka_do_pliku)
    for tytul in generator_tytulow:
        zawartosc_artykulu = pobierz_artykul(tytul)
        yield zawartosc_artykulu


