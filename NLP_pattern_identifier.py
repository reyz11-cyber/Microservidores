def es_vocal(caracter):
    # Definimos el conjunto de busqueda
    VOCALES = "aeiouáéíóú" # Incluimos tildes para mayor robustez

    # Validamos que sea un solo carácter y sea letra
    if len(caracter) != 1 or not caracter.isalpha():
        return "Error: Ingrese un único carácter alfabético."

    # Normalizamos a minusculas y verificamos pertenencia
    if caracter.lower() in VOCALES:
        return True  # Retorno booleano para logica de motor
    else:
        return False

#  Prueba de ejecucion 
entrada = input("Ingrese un caracter para el motor NLP: ")
resultado = es_vocal(entrada)

if isinstance(resultado, bool):
    print(f"¿Es vocal?: {'Confirmado' if resultado else 'Consonante/Otro'}")
else:
    print(resultado)