# Escriba un programa que lea dos números y lo visualiza en orden ascendente.
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
if num1 < num2:
    print("El orden de los numero es:", num1, ",", num2)
elif num1 > num2:
    print("El orden de los numeros es:", num2, ",", num1)
