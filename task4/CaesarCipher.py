"""
Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy
przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery.
Funkcja przyjmuje:
    wiadomość – tekst do zaszyfrowania,
    klucz – liczbę o ile należy przesunąć litery w alfabecie
oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string.
Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej
zaszyfrowanej wiadomości bez zmian.
Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres tablicy
z alfabetem oraz  problem podania klucza o dowolnej wielkości.
Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego
 """

alphabet_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z')

text = input("Wpisz swój tekst do szyfrowania: \n")


def caesar_cipher(tekst, klucz, alfabet=alphabet_tuple):
    tekst = tekst.lower()  # robi wchodzacy tekst malymi literami
    enc = ""
    klucz = klucz % len(alfabet)
    for char in tekst:
        # jesli znaka nie ma w alfabecie, wtedy go nie zmienia i idzie do nastepnego znaku
        if char not in alfabet:
            enc +=char
        else:
            index = alfabet.index(char)
            encIndex = (index + klucz)
            encChar = alfabet[encIndex]
            enc += encChar
    return  enc

print(caesar_cipher(text, 29))