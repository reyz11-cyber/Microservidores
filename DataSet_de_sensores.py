# Datos originales
celsius_data = [30.5, 22.0, 0.0, -4.5, 38.2]

# Conversión a Fahrenheit
fahrenheit_data = [(c * 9/5) + 32 for c in celsius_data]

print(f"Original (C): {celsius_data}")
print(f"Analítico (F): {fahrenheit_data}")