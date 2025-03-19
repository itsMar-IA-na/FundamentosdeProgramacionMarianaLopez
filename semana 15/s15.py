# Crear un diccionario con información ficticia
inf_personal = {
    "NOMBRE": "Crhistian Tapia",
    "EDAD": 28,
    "CIUDAD": "Bogotá",
    "PROFESION": "Chef"
}

# Acceder y modificar la clave "ciudad"
inf_personal["CIUDAD"] = "Quito"  # Cambiar de Bogotá a Quito

# Agregar una nueva clave-valor "telefono" si no existe
if ("TELEFONO") not in inf_personal:
    inf_personal["TELEFONO"] = "+593 911 101 102"  # Número ficticio

# Eliminar la clave "edad" ya que no es necesaria
del inf_personal["EDAD"]

# Imprimir el diccionario final
for clave, valor in inf_personal.items():
    print(f"{clave}: {valor}")
