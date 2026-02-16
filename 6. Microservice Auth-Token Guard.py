def validar_token():
    print("--- Validador de Auth-Token ---")
    token = input("Ingrese el token a validar: ")
    
    largo_ok = len(token) > 12
    
    tiene_numero = False
    for caracter in token:
        if caracter.isdigit():
            tiene_numero = True
            break
            
    no_es_test = not token.startswith("TEST")
    
    es_valido = largo_ok and tiene_numero and no_es_test
    
    print("-" * 30)
    if es_valido:
        return "Cumple con todas las normas de seguridad."
    else:
        return "No cumple con los requisitos mínimos."

print(validar_token())