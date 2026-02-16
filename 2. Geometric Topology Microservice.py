def clasificar_triangulo(a, b, c):
    if (a + b + c) != 180:
        return "Los ángulos no suman 180°"
    
    tiene_recto = " (incluye Ángulo Recto)" if (a == 90 or b == 90 or c == 90) else ""
    
    if a == b == c:
        resultado = "Equilátero"
    elif a == b or b == c or a == c:
        resultado = "Isósceles"
    else:
        resultado = "Escaleno"
    return f"Resultado: Triángulo {resultado}{tiene_recto}"

print("--- Clasificador de Triángulos ---")
ang1 = float(input("Ingrese el primer ángulo: "))
ang2 = float(input("Ingrese el segundo ángulo: "))
ang3 = float(input("Ingrese el tercer ángulo: "))

print(clasificar_triangulo(ang1, ang2, ang3))