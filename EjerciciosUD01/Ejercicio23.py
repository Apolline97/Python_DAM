# Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
# el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
# se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
# según sea el caso y el total a pagar de la compra.

valor_compra = float(input("Cuanto vale la comprar: "))
metodo_pago = input("En efectivo o con targeta: ").lower().strip()

pagar = 0

if metodo_pago == "targeta":
    incremento = valor_compra * 0.03
    pagar = valor_compra + incremento
    print(f"El incremento es {incremento}€")
    print(f"La cantidad a apagar con el incremento es del {pagar}€")
elif metodo_pago == "efectivo":
    descuento = valor_compra * 0.05
    pagar = valor_compra + descuento
    print(f"El descuento es {descuento}€")
    print(f"La cantidad a apagar con el incremento es del {pagar}€")
else:
    print("El metodo de pago es erroneo. Tiene que ser (targeta/efectivo).")
    