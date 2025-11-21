# Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.
try:
    entrada_usuario = input("Introduce un número entre 0 y 99999: ")
    numero = int(entrada_usuario)
    
    if 0 <= numero <= 99999:
        
        cifras_str = str(numero)
        cantidad_cifras = len(cifras_str)
        
        if cantidad_cifras == 1:
            print(f"El número {numero} tiene {cantidad_cifras} cifra.")
        else:
            print(f"El número {numero} tiene {cantidad_cifras} cifras.")
            
    else:
        print(f"Error: El número {numero} está fuera del rango permitido (0-99999).")

except ValueError:
    print("Error: La entrada no es un número entero válido.")