#Napisz program, który pobierze od użytkownika liczby rozdzielone przecinkiem
#a następnie policzy znajdzie ich max oraz min, bez używania wbudowanych funkcji.

ciag = input("Napisz ciąg liczb, ktore rozdzielone przecinkiem: ")
listaLiczb = ciag.split(",")
listaLiczb = [int(x) for x in listaLiczb]
print("max = " + str(max(listaLiczb)))
print("min = " + str(min(listaLiczb)))

