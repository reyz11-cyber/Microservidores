def conversor_manual():
    print("--- Conversor Manual (Sin bin/hex) ---")
    decimal = int(input("Ingrese un número entero positivo: "))
    
    n = decimal
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2

    n = decimal
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
        
    print("-" * 20)
    print(f"Decimal: {decimal}")
    print(f"Binario: {binario if binario else '0'}")
    print(f"Hexadecimal: {hexadecimal if hexadecimal else '0'}")

conversor_manual()