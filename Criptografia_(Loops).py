def es_numero_perfecto(numero):
    # Paso 1: Iniciamos la variable acumuladora
    suma_divisores = 0
    
    # Paso 2: Utilizamos un bucle for para encontrar divisores
    # Vamos desde 1 hasta el número (sin incluirlo)
    for i in range(1, numero):
        # Paso 3: Verificamos si 'i' es un divisor
        if numero % i == 0:
            # Si el residuo es 0, lo sumamos al acumulador
            suma_divisores += i
            
    # Paso 4: Verificamos si la suma acumulada es igual al número original
    return suma_divisores == numero

# Pruebas de funcionamiento
print(f"¿Es 6 un número perfecto?: {es_numero_perfecto(6)}")    # True 
print(f"¿Es 28 un número perfecto?: {es_numero_perfecto(28)}")  # True
print(f"¿Es 10 un número perfecto?: {es_numero_perfecto(10)}")  # False