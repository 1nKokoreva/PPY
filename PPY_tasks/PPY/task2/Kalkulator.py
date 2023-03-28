# 2. Napisz skrypt kalkulator, który pobierze od użytkownika 2 liczby
# a następnie po podaniu odpowiedniego operatora wykona adekwatną operację i wyświetli wynik.
liczba1 = int(input("liczba 1: "))
liczba2 = int(input("liczba 2: "))
operator = input("operator: ")

if (operator == '+'):
    print(liczba1 + liczba2)
elif (operator == '-'):
    print(liczba1 - liczba2)
elif (operator == '*'):
    print(liczba1 * liczba2)
elif (operator == '/'):
    print(liczba1 / liczba2)
elif (operator == '//'):
    print(liczba1 // liczba2)
elif (operator == '%'):
    print(liczba1 % liczba2)
elif (operator == '**'):
    print(liczba1 ** liczba2)
else: print("Nie ma takiego operatoru")

