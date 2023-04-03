# Utwórz skrypt, która pobierze od użytkownika odpowiedzi na pytania – ankieta z pytaniami
# jak wprzykładzie (pytania 1-7) oraz pytaniem o imię i nazwisko:
# Wyświetli  pytania wraz z odpowiedziami w formacie pytanie:
# Jak masz na imię oraz nazwisko?odpowiedź: Adam Adamskipytanie:
# W jakich okolicznościach czytasz książki najczęściej?odpowiedź:
# Podczas pracy/nauki (to ich element)

print("       ~Ankieta czytelnicza~")
imie = input("Jak masz na imię oraz nazwisko? \n" )

pytanie1 = input("Jak najczęściej spędzasz swój wolny czas? \n "  +
                      "1 - czytanie książek/czasopism, \n "
                      "2 - słuchanie muzyki, \n "
                      "3 - spotkania z rodziną/przyjaciółmi, \n "
                      "4 - swoją wersję \n" + "odpowiedz: ")
if pytanie1 == '4':
    input("Twoja odpowiedz: ")
pytanie2 = input("Jak często wypożyczasz książki w bibliotece?\n" +
                 "1 - nigdy, \n"
                 "2 - raz w rok \n"
                 "3 - raz na miesiąc \n"
                 "4 - częściej niż raz w miesiącu: \n"
                 "5 - swoją wersję \n "+ "odpowiedz: ")
if pytanie2 == '5':
    input("Twoja odpowiedz: ")

pytanie3 = input("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n" + "odpowiedz: ")

pytanie4 = input("Po książki w jakiej formie sięgasz najczęściej? \n "
                 "1 - papierowej (tradycyjnej) \n"
                 "2 - e-book \n"
                 "3 - książka audio \n" + "odpowiedz: ")
pytanie5 = input("Ile książek czytasz średnio w ciągu roku? \n" + "odpowiedz: ")

pytanie6 = input("Po jakie gatunki książek sięgasz najczęściej?\n "
                 "1 - naukowe \n"
                 "2 - horrory \n"
                 "3 - fantastykę \n"+
                 "4 - psychologiczne \n"
                 "5 - swoją wersję\n"+"odpowiedz: ")
if pytanie6 == '5':
    input("Twoja odpowiedz: ")

pytanie7 = input("W jakim języku książki czytasz?\n"
                 "1 - polskim \n "
                 "2 - angielskim \n "
                 "3 - rosyjskim \n"
                 "4 - hiszpanskim\n"
                 "5 - niemieckim \n"
                 "6 - hinskim \n"
                 "7 - swoją wersję"+ "odpowiedz: ")
if pytanie7 == '7':
    input("Twoja odpowiedz: ")

print("Dziękujemy za odpowiedzi:)")
