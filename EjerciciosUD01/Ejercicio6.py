# Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre el porcentaje de descuento realizado.
precio_articulo = float(input("Introduce en precio del articulo:"))
precio_venta = float(input("Introduce al precio de venta:"))
descuento = ((precio_articulo - precio_venta) / precio_articulo) * 100
print("El porcentaje de descuento realizado es:", descuento, "%")
