# Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
# con el siguiente menú de opciones:
# Bienvenido a su Cajero Virtual
# 1. Ingresar dinero en cuenta
# 2. Retirar dinero de la cuenta
# 3. Salir

saldo = 1000
Continuar = True

while Continuar:
    print("\nBienvenido a lcagero automatico:")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")

    opcion = input("Seleciona una opcion(1, 2 o 3):")

    if opcion == "1":
        ingreso = float(input("Introduce la cantidad a ingresar: "))

        if ingreso > 0:
            saldo = + ingreso
            print(f"Ingreso exitoso. Tu cuenta se actualizo y ahora tienes de {saldo} saldo")
        else:
            print("La cantidad debe de ser positiva")
    elif opcion == 2:
        Retiro = float(input("Introduce la cantidad que quieres retirar: "))

        if Retiro > 0:
            saldo = - Retiro
            print(f"Retirada con exsito. Tu cueta se actualizo a {saldo}")
        else:
            print("La cantidad debe de ser positiva")
    elif opcion == 3:
        print("Gracias por utilizar nuestro cajero.")
        Continuar = False
    else:
        print("Opcion no valida. Introduce un numero de nuevo.")
