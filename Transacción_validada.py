# Interfaz de Validación de Transacciones
def validar_transaccion():
    print("Verificación de Integridad de Pagos")
    print("Métodos: [1] Pago Móvil | [2] Tarjeta")
    
    # Selección del método
    metodo = input("Seleccione el método de pago: ")
    
    # Validación del método
    if metodo not in ["1", "2"]:
        print("ERROR: Método de pago no reconocido. Reinicie el proceso.")
        return

    # Variable de longitud requerida
    longitud_requerida = 8 if metodo == "1" else 16
    nombre_metodo = "Pago Móvil" if metodo == "1" else "Tarjeta"

    # Bucle para la clave
    while True:
        print(f"\n-> Se nescesita clave de validacion de {nombre_metodo} (requiere {longitud_requerida} dígitos)")
        clave = input("Ingrese su clave de validación: ")

        # 1. Validación de Caracteres
        if not clave.isdigit():
            print("ERROR: La clave contiene caracteres no permitidos. Use solo números.")
            continue # Vuelve a pedir la clave

        # 2. Validación de Longitud
        if len(clave) == longitud_requerida:
            # Éxito
            id_final = clave if metodo == "1" else clave[-4:].rjust(16, '*')
            print(f"{nombre_metodo} VALIDADO CON EXITO (ID: {id_final})")
            break # Sale del bucle de la clave
        else:
            print(f"ERROR: Longitud incorrecta. Requeridos: {longitud_requerida}")

# Ejecución
validar_transaccion()