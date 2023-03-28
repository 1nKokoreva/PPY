import requests
import datetime

url = input("Podaj adres strony internetowej: ")
# pętla dla każdej z trzech dat w przeszłości
for i in range(3):

    # Otrzymujemy datę w żądanym formacie, odejmując od bieżącej daty liczbę dni równą numerowi iteracji
    date_str = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y%m%d')

    # Tworze adres URL, aby uzyskać archiwum strony z określoną datą
    archive_url = f"{url}?date={date_str}"
    # Wysyla żądanie GET do serwera
    response = requests.get(archive_url)


    # Jeśli odpowiedź z serwera się powiedzie
    if response.status_code == 200:
        # Zapisuje wynikowy kod html do pliku o nazwie postaci: 20220317.html
        with open(f"{date_str}.html", 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Pobrano archiwum z dnia {date_str}")
    else:
        print(f"Nie udało się pobrać archiwum z dnia {date_str}")

print("Pobieranie archiwalnych wersji zakończone.")
