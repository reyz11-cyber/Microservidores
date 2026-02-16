def auditor_latencia():
    print("--- Auditor de Latencia (Con Flag) ---")
    
    entrada = input("Ingrese los tiempos de respuesta separados por coma: ")
    tiempos = [float(x.strip()) for x in entrada.split(",")]
    
    umbral_critico = float(input("Ingrese el Umbral Crítico (ms): "))
    
    promedio = sum(tiempos) / len(tiempos)
    flag_pico_sospechoso = False
    
    for t in tiempos:
        if t >= (promedio * 3):
            flag_pico_sospechoso = True
            break
    hay_alerta = promedio > umbral_critico or flag_pico_sospechoso
    
    print("-" * 30)
    print(f"Promedio calculado: {promedio:.2f} ms")
    print(f"¿Se triplicó el promedio en algún punto?: {'Sí' if flag_pico_sospechoso else 'No'}")
    
    if hay_alerta:
        return "RESULTADO: True (Alerta activada)"
    else:
        return "RESULTADO: False (Todo normal)"

print(auditor_latencia())