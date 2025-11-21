altura = 6

for fila in range(1, altura + 1):
    for columna in range(fila):

        if columna == 0 or columna == fila - 1:
            print("* ", fin="")
        else:
            print("  ", fin="")

    print()


for fila in range(1, altura):
    limite = altura - fila

    for columna in range(limite):

        if columna == 0 or columna == limite - 1:
            print("* ", fin="")
        else:
            print("  ", fin="")

    print()
