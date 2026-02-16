def health_check(latencia, uso_cpu, estado_db):
    return latencia < 200 and uso_cpu < 80 and estado_db == True

print("--- Validador de Salud ---")

lat = float(input("Ingrese la latencia (ms): "))
cpu = float(input("Ingrese el uso de CPU (%): "))

db_input = input("¿La base de datos está conectada? (s/n): ").lower()
db_conectada = db_input == 's'

# Ejecución y resultado
resultado = health_check(lat, cpu, db_conectada)

print("-" * 30)
if resultado:
    print("SISTEMA SALUDABLE: El servicio puede recibir tráfico.")
else:
    print("ALERTA: El sistema no es apto para recibir tráfico.")