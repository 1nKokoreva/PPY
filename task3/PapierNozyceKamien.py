import getpass
import random

print("  ~Papier-Nożyczki-Kamień~")

trybGry = int(input("Wybierz tryb gry: \n"
                    "Z komputerem wpisz - 1\n"
                    "Dla 2 graczy wpisz - 2 \n"))
odpowiedzKomputera = ["Papier", "Nozyce", "Kamien"]
# result[0] - komputer, result[1] - gracz/gracz1, result[2] - gracz2
result = [0, 0, 0]
if trybGry == 1:
    name = input("Wpisz swoje imie: ")
    total_rounds = int(input("Ile rund chcesz zagrac: "))
    rundCount = total_rounds
    odpowiedzKomputera = ["Papier", "Nozyce", "Kamien"]
    while rundCount > 0:
        wariantGracza = int(input("Wybierz:\nPapier - 1, Nozyce - 2, Kamien - 3\n"))
        komputer = random.choice(odpowiedzKomputera)
        if (komputer == "Papier" and wariantGracza == 1) or (komputer == "Nozyce" and wariantGracza == 2) or (
                komputer == "Kamien" and wariantGracza == 3):
            print("remis")
            result[0] += 1
            result[1] += 1
            rundCount -= 1
        elif (komputer == "Papier" and wariantGracza == 2) or (komputer == "Nozyce" and wariantGracza == 3) or (
                komputer == "Kamien" and wariantGracza == 1):
            print("wygral " + name)
            result[1] += 1
            rundCount -= 1
        elif (komputer == "Papier") and (wariantGracza == 3) or (komputer == "Nozyce" and wariantGracza == 1) or (
                komputer == "Kamien" and wariantGracza == 2):
            print("wygral komputer")
            result[0] += 1
            rundCount -= 1
        else:
            print("Nieznany wybor. Sprobuj ponownie.")

    print("resultat komputera: " + str(result[0]) + ", resultat " + name + ": " + str(result[1]))
elif trybGry == 2:
    gracz1 = input("imię 1 gracza: ")
    gracz2 = input("imię 2 gracza: ")
    rundCount = int(input("Ile rund chcecie zagrac: "))
    while rundCount > 0:
            player1 = getpass.getpass(gracz1 + ", Wprowadź swój ruch (Kamien -1 / Papier-2 / Nozyce - 3): ")
            player2 = getpass.getpass(gracz2 + ", Wprowadź swój ruch (Kamien -1 / Papier-2 / Nozyce - 3): ")
            if player1 == player2:
                print("remis!")
                result[0] += 1
                result[1] += 1
                rundCount -= 1
            elif (player1 == "1" and player2 == "3") or (player1 == "2" and player2 == "1") or (
                    player1 == "3" and player2 == "2"):
                print("Wygral " + gracz1)
                result[1] += 1
                rundCount -= 1
            else:
                print("Wygral " + gracz2)
                result[2] += 1
                rundCount -= 1
    print(f"resultat {gracz1} = {result[1]}, resultat {gracz2} = {result[2]}")
    if (result[2] > result[1]):
        print("Gratuluje gracza " + gracz2)
    elif (result[1] > result[2]):
        print("Gratuluje gracza " + gracz1)
    else:
        print("remisss!")
else:
    print("~nie ma takiej opcji~")


