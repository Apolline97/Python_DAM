# Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de
# 10.
try:
    num = input("Ingrese un numero: ")

    if num % 10 == 0:
        print(f"El numero {num} es multiplo de 10.")
    else:
        print(f"El numero {num} no es multiplo de 10.")

except ValueError:
    print("Error: debes ingresar un numero entero.")