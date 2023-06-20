import tkinter as tk
import pandas as pd
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from tkinter import ttk
import joblib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

nazwa_pliku_modelu: str = "model.pkl"
nazwa_pliku_bazy_danych = "result.db"  # Nazwa pliku bazy danych SQLite


def utworz_baze_danych(nazwa_pliku):
    polaczenie = sqlite3.connect(nazwa_pliku)
    polaczenie.close()
    print("Baza danych utworzona.")

utworz_baze_danych(nazwa_pliku_bazy_danych)


def trenuj_model():
    dane = pd.read_csv('dane/tic-tac-toe.data', header=None)


    X = dane.iloc[:, :-1]
    y = dane.iloc[:, -1]
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    X_encoded = pd.get_dummies(X)
    # Dzieli dane na zbiór treningowy i testowy
    X_treningowe, X_testowe, y_treningowe, y_testowe = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()  # Tworzenie i generacja modelu
    model.fit(X_treningowe, y_treningowe)

    y_pred = model.predict(X_testowe)  # Predykcja

    dokladnosc = accuracy_score(y_testowe, y_pred) * 100  # Oblicza dokładność w %
    messagebox.showinfo("Model wytrenowany", f"Dokładność: {dokladnosc} %")

    joblib.dump(model, nazwa_pliku_modelu)
    print("Model zapisany na dysku.")


def wczytaj_model():
    try:
        model = joblib.load(nazwa_pliku_modelu)  # Wczytuje zserializowany obiekt modelu z podanego pliku.
        messagebox.showinfo("Model", "Model wczytany z dysku.")
        return model
    except FileNotFoundError:
        messagebox.showerror("Model", "Model nie znaleziony na dysku.")
        return None


def przegladaj_dane():
    dane = pd.read_csv('dane/tic-tac-toe.data', header=None)
    ramka_drzewa = tk.Frame(okno)
    ramka_drzewa.pack(fill=tk.BOTH, expand=True)
    pasek_przewijania_y = tk.Scrollbar(ramka_drzewa, orient="vertical")
    pasek_przewijania_x = tk.Scrollbar(ramka_drzewa, orient="horizontal")
    pasek_przewijania_y.pack(side=tk.RIGHT, fill=tk.Y)
    pasek_przewijania_x.pack(side=tk.BOTTOM, fill=tk.X)

    drzewo = ttk.Treeview(ramka_drzewa, yscrollcommand=pasek_przewijania_y.set, xscrollcommand=pasek_przewijania_x.set)
    drzewo.pack(fill=tk.BOTH, expand=True)

    pasek_przewijania_y.config(command=drzewo.yview)
    pasek_przewijania_x.config(command=drzewo.xview)

    kolumny = list(dane.columns)
    drzewo["columns"] = kolumny
    for kolumna in kolumny:
        drzewo.column(kolumna, width=100)

    if kolumna == kolumny[-1]:  # Ostatnia kolumna
        drzewo.heading(kolumna, text="etykieta")  # Podpis "etykieta"

    else:
        drzewo.heading(kolumna, text=kolumna)

    for indeks, wiersz in dane.iterrows():
        drzewo.insert("", "end", text=indeks, values=list(wiersz))


def wizualizuj_dane():
    dane = pd.read_csv('dane/tic-tac-toe.data', header=None)
    fig = plt.figure(figsize=(8, 6))
    dane[9].value_counts().plot(kind='bar')
    plt.xlabel("Etykieta")
    plt.ylabel("Liczba wystąpień")
    plt.title("Rozkład etykiet")
    plt.xticks(rotation=0)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=okno)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


def zapisz_dane_do_bazy_danych():
    dane = pd.read_csv('dane/tic-tac-toe.data', header=None)
    polaczenie = sqlite3.connect(nazwa_pliku_bazy_danych)  # Podłączenie do bazy danych SQLite
    kursor = polaczenie.cursor()

    kursor.execute(
         "CREATE TABLE IF NOT EXISTS data (row_index INT, col1 TEXT, col2 TEXT, col3 TEXT, col4 TEXT, col5 TEXT, col6 TEXT, col7 TEXT, col8 TEXT, col9 TEXT, label TEXT)")

    for indeks, wiersz in dane.iterrows():  # Wprowadzenie danych do tabeli
        wartosci = [indeks] + list(wiersz)
        kursor.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", wartosci)

    polaczenie.commit()
    polaczenie.close()

    print("Dane zapisane w bazie danych.")


def odczytaj_dane_z_bazy_danych():
    zapisz_dane_do_bazy_danych()  # Zapis danych do bazy danych przed odczytem
    polaczenie = sqlite3.connect(nazwa_pliku_bazy_danych)  # Podłączenie do bazy danych SQLite
    kursor = polaczenie.cursor()

    kursor.execute("SELECT * FROM data")
    dane = kursor.fetchall()

    ramka_drzewa = tk.Frame(okno)
    ramka_drzewa.pack(fill=tk.BOTH, expand=True)

    pasek_przewijania_y = tk.Scrollbar(ramka_drzewa, orient="vertical")
    pasek_przewijania_x = tk.Scrollbar(ramka_drzewa, orient="horizontal")
    pasek_przewijania_y.pack(side=tk.RIGHT, fill=tk.Y)
    pasek_przewijania_x.pack(side=tk.BOTTOM, fill=tk.X)

    drzewo = ttk.Treeview(ramka_drzewa, yscrollcommand=pasek_przewijania_y.set, xscrollcommand=pasek_przewijania_x.set)
    drzewo.pack(fill=tk.BOTH, expand=True)

    pasek_przewijania_y.config(command=drzewo.yview)
    pasek_przewijania_x.config(command=drzewo.xview)

    kolumny = ['row_index', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'label']
    drzewo["columns"] = kolumny
    for kolumna in kolumny:
     drzewo.column(kolumna, width=100)

    if kolumna == "label":
        drzewo.heading(kolumna, text="etykieta")

    else:
        drzewo.heading(kolumna, text=kolumna)

    for wiersz in dane:
     drzewo.insert("", "end", values=wiersz)

    polaczenie.close()


def przewiduj_dane():
    sciezka_pliku = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if sciezka_pliku:
     dane = pd.read_csv(sciezka_pliku, header=None)
    X_encoded = pd.get_dummies(dane)
    model = wczytaj_model()
    if model:
     przewidywania = model.predict(X_encoded)
    messagebox.showinfo("Predykcje dla nowych danych", str(przewidywania))

# GUI
okno = tk.Tk()
okno.title("Klasyfikator Tic-Tac-Toe")
okno.geometry("600x350")

ramka_menu = tk.Frame(okno)
ramka_menu.pack(side=tk.LEFT, padx=10)

przycisk_treningu = tk.Button(ramka_menu, text="Trenuj model", command=trenuj_model)
przycisk_treningu.pack(pady=10)

przycisk_przegladu = tk.Button(ramka_menu, text="Przegląd danych", command=przegladaj_dane)
przycisk_przegladu.pack(pady=10)

przycisk_wczytania = tk.Button(ramka_menu, text="Wczytaj model", command=wczytaj_model)
przycisk_wczytania.pack(pady=10)

przycisk_wizualizacji = tk.Button(ramka_menu, text="Wizualizacja danych", command=wizualizuj_dane)
przycisk_wizualizacji.pack(pady=10)

przycisk_zapisu = tk.Button(ramka_menu, text="Zapisz dane do bazy", command=zapisz_dane_do_bazy_danych)
przycisk_zapisu.pack(pady=10)

przycisk_odczytu = tk.Button(ramka_menu, text="Odczytaj dane z bazy", command=odczytaj_dane_z_bazy_danych)
przycisk_odczytu.pack(pady=10)

przycisk_predykcji = tk.Button(ramka_menu, text="Przewiduj nowe dane z pliku", command=przewiduj_dane)
przycisk_predykcji.pack(pady=10)

okno.mainloop()
