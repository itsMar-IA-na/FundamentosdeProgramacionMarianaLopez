import random

num_ciudades = 10
num_semanas = 12
num_dias = 7

ciudades = ["Quito", "Guayaquil", "Cuenca", "Baños", "Salinas",
            "Montañita", "Puellaro", "Cayambe", "Manta", "Isla de Plata"]

temperaturas = [[[random.randint(5, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

print("\n--- Temperaturas Registradas ---\n")
for i in range(num_ciudades):
    print(f"Ciudad: {ciudades[i]}")
    for j in range(num_semanas):
        print(f"  Semana {j + 1}: {temperaturas[i][j]}")
    print()

print("\n--- Promedio de Temperaturas Semanales ---\n")
for i in range(num_ciudades):
    print(f"Ciudad: {ciudades[i]}")
    for j in range(num_semanas):
        promedio = sum(temperaturas[i][j]) / num_dias
        print(f"  Semana {j + 1}: {promedio:.2f}°C")
    print()
