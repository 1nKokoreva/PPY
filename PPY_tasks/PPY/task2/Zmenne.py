s1 = "Python 2023"
s2 = "Python 2023"
s3 = "Python 2023"

# Wyświetl wartość logiczną zwróconą przez porównanie napisów
# ze zmiennej pierwszej i drugiej oraz drugiej i trzeciej.
print(s1 == s2)
print(s2 == s3)

# b. Wyświetl typy tych zmiennych oraz ich adres w pamięci
# ( w postaci szesnastkowej – funkcja hex() )
# Pod trzecią zmienną przypisz napis „Java 11”
# Ponownie wykonaj podpunkt a i b

print(type(s1), hex(id(s1)))
print(type(s2), hex(id(s2)))
print(type(s3), hex(id(s3)))

s3 ="Java11"
print(s1 == s2)
print(s2 == s3)

print(type(s1), hex(id(s1)))
print(type(s2), hex(id(s2)))
print(type(s3), hex(id(s3)))