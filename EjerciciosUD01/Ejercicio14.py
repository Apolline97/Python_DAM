# Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 < num2:
    print("El segundo número es mayor que el primero.")
else:
    print("Ambos números son iguales.")
