def swiss_army_calc():
    print("--- Swiss-Army Calculator ---")
    print("Operaciones: suma, resta, multiplicacion, division, fibonacci, bases")
    op = input("¿Qué operación desea realizar?: ").lower()

    if op == "fibonacci":
        n = int(input("¿Cuántos números de la serie desea?: "))
        a, b = 0, 1
        serie = []
        for _ in range(n):
            serie.append(a)
            a, b = b, a + b
        return f"Serie Fibonacci: {serie}"
    
    elif op == "bases":
        n = int(input("Ingrese el número decimal a convertir: "))
        return f"Binario: {bin(n)} | Hexadecimal: {hex(n)}"
    
    else: # Operaciones aritméticas normales
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        if op == "suma": return f"Resultado: {n1 + n2}"
        elif op == "resta": return f"Resultado: {n1 - n2}"
        elif op == "multiplicacion": return f"Resultado: {n1 * n2}"
        elif op == "division": return f"Resultado: {n1 / n2}" if n2 != 0 else "Error: Div por 0"
        else: return "Operación no válida."

print(swiss_army_calc())