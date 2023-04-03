#Napisz program, który wyświetli plan wycieczki
#– wybierając losowo z listy 10 największych miast w Polsce miasta do odwiedzenia.
# Miast ma być 10, nie mogą się powtarzać.

import random

listaMiast = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
miasta = random.sample(listaMiast, 10)
print("Plan wycieczki:")
for i, miasto in enumerate(miasta):
    print(f"{i+1}. {miasto}")