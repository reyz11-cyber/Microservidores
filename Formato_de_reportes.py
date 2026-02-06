# Definimos las variables
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

# Generación del reporte de venta
print(f"\nVenta de {producto}: {cantidad} unidades a un precio de ${precio} cada una.")

# Calculo del total de la venta
Total = precio * cantidad
print(f"Total de la venta: ${Total:.2f}") # Formateo a 2 decimales