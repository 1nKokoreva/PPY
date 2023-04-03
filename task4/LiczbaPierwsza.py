"""
Napisz funkcję sprawdzającą czy podane liczby są liczbami pierwszymi
w szybszy sposób niż w przykładzie.
Do funkcji można przekazać dowolną liczbę argumentów (liczby).
Liczby 0 i 1 nie są liczbami pierwszymi
"""
from math import isqrt


def prime(*liczby):
    for liczba in liczby:
        if liczba > 1:
            for i in range(2, isqrt(liczba) + 1):
                if (liczba % i) == 0:
                    print(str(liczba) + '  is not prime')
                    break
            else:
                print(str(liczba) + '  is prime number')
        else:
            print(str(liczba) + '  is not prime')

prime(0, 1, 2, 3, 4, 5)