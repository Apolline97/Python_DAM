# Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
# de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
# Visualizar el descuento y el total a pagar por la compra.


monto_compra = float(input("Ingrese el monto de la compra: "))
dia_semana = input("Ingrese el día de la semana: ").lower().strip()
    
descuento = 0.0
    
if dia_semana == "martes" or dia_semana == "jueves":
    descuento = monto_compra * 0.15
    print(f"¡Descuento del 15% aplicado por ser {dia_semana.capitalize()}!")
    
total_pagar = monto_compra - descuento
    
print(f"Descuento: {descuento:.2f}")
print(f"Total a pagar: {total_pagar:.2f}")