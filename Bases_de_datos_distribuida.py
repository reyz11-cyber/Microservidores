# Interfaz para determinar el servidor
def evaluar_servidor():
    try:
        # 1. Entrada del número de ID
        n = int(input("Ingrese el número de ID: "))

        # 2. Evaluación de paridad
        # Si el residuo de n/2 es 0, el número es par.
        if n % 2 == 0:
            print("Servidor A")
        else:
            print("Servidor B")
            
    except ValueError:
        print("Error: Por favor, ingrese un número entero.")

# Ejemplo de uso
if __name__ == "__main__":
    evaluar_servidor()