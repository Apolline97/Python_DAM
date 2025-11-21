# Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división (Ten en cuenta la división por cero).
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("Error: División por cero no está definida.")
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
