# La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
# postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
# el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
# control switch).
#
# Datos de la imagen:
# Ing. de Sistemas: 350, 650
# Derecho: 300, 550
# Ing. Naviera: 300, 500
# Ing. Pesquera: 310, 460
# Contabilidad: 280, 490
# Administración: 360, 520

nombre = input("Nombre del postulante: ")
facultad = input("Facultad a estudiar: ").strip().lower()

importe_matricula = 0
mensualidad = 0
facultad_valida = True

if facultad == "ing. de sistemas" or facultad == "sistemas":
    importe_matricula = 350
    mensualidad = 650
elif facultad == "derecho":
    importe_matricula = 300
    mensualidad = 550
elif facultad == "ing. naviera" or facultad == "naviera":
    importe_matricula = 300
    mensualidad = 500
elif facultad == "ing. pesquera" or facultad == "pesquera":
    importe_matricula = 310
    mensualidad = 460
elif facultad == "contabilidad":
    importe_matricula = 280
    mensualidad = 490
elif facultad == "administración" or facultad == "administracion":
    importe_matricula = 360
    mensualidad = 520
else:
    facultad_valida = False
    print(f"Error: La facultad '{facultad}' no se encuentra en la lista.")

if facultad_valida:
    base_imponible = importe_matricula + mensualidad
    igv = base_imponible * 0.18
    monto_final = base_imponible + igv

    print(f"\n--- Liquidación de Matrícula ---")
    print(f"Postulante: {nombre.title()}")
    print(f"Facultad: {facultad.capitalize()}")
    print(f"Importe de Matrícula: {importe_matricula:.2f}")
    print(f"Mensualidad: {mensualidad:.2f}")
    print(f"IGV (18%): {igv:.2f}")
    print(f"Monto Final a Pagar (Matrícula + 1ra Mensualidad + IGV): {monto_final:.2f}")