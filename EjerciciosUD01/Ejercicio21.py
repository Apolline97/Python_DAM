# Escriba un programa que calcula el salario neto semanal de un trabajador en función del
# número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
# • Las primeras 35 horas se pagan a tarifa normal.
# • Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
# • Las tasas de impuesto son:
#   o Los primeros 500€ son libres de impuestos.
#   o Los siguientes 400€ tiene un 25% de impuesto.
#   o Los restantes un 45% de impuesto.
# Escribe el nombre del trabajador, salario bruto, tasas y salario neto.

try:
    nombre = input("Nombre del trabajador: ")
    horas_trabajadas = float(input("Horas trabajadas esta semana: "))
    tarifa_horaria = float(input("Tarifa por hora (€): "))

    salario_bruto = 0
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_horaria
    else:
        horas_normales = 35
        horas_extra = horas_trabajadas - 35
        salario_bruto = (horas_normales * tarifa_horaria) + (horas_extra * tarifa_horaria * 1.5)

    impuestos = 0
    if salario_bruto > 500:
        if salario_bruto <= 900:
            impuestos = (salario_bruto - 500) * 0.25
        else:
            impuestos_tramo1 = 400 * 0.25
            impuestos_tramo2 = (salario_bruto - 900) * 0.45
            impuestos = impuestos_tramo1 + impuestos_tramo2
    
    salario_neto = salario_bruto - impuestos

    print(f"\n--- Recibo de {nombre} ---")
    print(f"Salario Bruto: {salario_bruto:.2f} €")
    print(f"Tasas (Impuestos): {impuestos:.2f} €")
    print(f"Salario Neto: {salario_neto:.2f} €")

except ValueError:
    print("Error: Ingrese valores numéricos válidos para horas y tarifa.")