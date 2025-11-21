tamano = 5

for fila in range(1, tamano + 1):

    for columna in range(fila):

        if columna == 0 or columna == fila - 1 or fila == tamano:
            print("* ", fin="")
        else:
            print("  ", fin="")

    print()
