# Solicitud de datos al usuario
# Usamos float() para permitir decimales y poder realizar cálculos matemáticos
precio_venta = float(input("Ingrese el Precio de Venta: "))
costo_fabricacion = float(input("Ingrese el Costo de Fabricación: "))

# Cálculo de la ganancia neta
ganancia_neta = precio_venta - costo_fabricacion

# Muestra del resultado
print(f"La ganancia neta del producto es: {ganancia_neta}")