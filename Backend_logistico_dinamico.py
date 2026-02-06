# Interfaz de transporte
def calcular_transporte():
    print("Sistema de Cotización de Transporte")
    print("Vehículos disponibles: [1] Pickup, [2] Gandola, [3] Mudanza")
    
    opcion = input("Seleccione el tipo de vehículo (1-3): ")
    
    # Validación de entrada para distancia
    try:
        distancia = float(input("Ingrese la distancia a recorrer (km): "))
    except ValueError:
        return "Error: Por favor, ingrese un número válido para la distancia."

    # Constantes
    RECARGO_POR_KM = 1.50
    precio_base = 0.0
    tipo_nombre = ""

    # Selección del vehículo y asignación de precio base
    match opcion:
        case "1":
            precio_base = 6.00
            tipo_nombre = "Pickup"
        case "2":
            precio_base = 7.00
            tipo_nombre = "Gandola"
        case "3":
            precio_base = 10.00
            tipo_nombre = "Mudanza"
        case _:
            return "Opción de vehículo no válida."

    # Cálculo de costos
    costo_distancia = distancia * RECARGO_POR_KM
    total_facturado = precio_base + costo_distancia

    # Generación del reporte
    return generar_reporte(tipo_nombre, precio_base, costo_distancia, total_facturado, distancia)

def generar_reporte(tipo, base, costo_dist, total, km):
    reporte = f"""
    ======================================
     REPORTE FINAL DE FACTURACIÓN
    ======================================
    Vehículo seleccionado:  {tipo}
    Distancia recorrida:    {km:.2f} km
    --------------------------------------
    Precio Base:            ${base:.2f}
    Costo por Distancia:    ${costo_dist:.2f}
    --------------------------------------
    TOTAL A PAGAR:          ${total:.2f}
    ======================================
    """
    return reporte

# Ejecución
print(calcular_transporte())