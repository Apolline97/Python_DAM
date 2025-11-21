# Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la
# calificación alfabética, escribiendo el siguiente resultado (switch).
# • De 0 a < 3 Muy Deficiente.
# • De 3 a < 5 Insuficiente.
# • De 5 a < 6 Suficiente.
# • De 6 a < 7 Bien.
# • De 7 a < 9 Notable.
# • De 9 a 10 Sobresaliente.

try:
    calificacion = int(input("Introduce la calificacion que has sacado: "))
    
    if 0 <= calificacion < 3:
        resultado = "Muy Deficiente"
    elif 3 <= calificacion < 5:
        resultado = "Insuficiente"
    elif 5 <= calificacion < 6:
        resultado = "suficiente"
    elif 6 <= calificacion < 7:
        resultado = "Bien"
    elif 7 <= calificacion < 9:
        resultado = "Notable"
    elif 9 <= calificacion < 10:
        resultado = "Sobresaliente"
    else:
        print("Calificacion no valida")
    
    print(f"La calificacion es: {resultado}")
    
except ValueError:
    print("Error debes de ingresar un valor numerocio")