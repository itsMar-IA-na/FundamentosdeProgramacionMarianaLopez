# Definir la función
def calcular_descuento(valor_total, valor_desc):
# Calcular el valor del descuento
    descuento = valor_total * (valor_desc / 100)
# Devolver el valor del descuento ya calculado
    return descuento

# Llamar a la función con el valor de la compra y el porcentaje de descuento
valor_total_1 = 145.67  # Asignar valor a la compra
valor_desc_1 = 17  # Asignar valor al descuento
descuento_1 = calcular_descuento(valor_total_1, valor_desc_1)  # Llamar a la función calculo_desc con valor_total_1 y valor_desc_1, y almacena el descuento calculado en descuento_1.
valor_final_1 = valor_total_1 - descuento_1  # Calcular el monto final a pagar restando el descuento del valor total.

# Se repiten los pasos
# Llamar a la función con el valor de la compra y el porcentaje de descuento
valor_total_2 = 564.78  # Asignar valor a la compra
valor_desc_2 = 13  # Asignar valor al descuento
descuento_2 = calcular_descuento(valor_total_2, valor_desc_2)  # Llamar a la Función calculo_desc con valor_total_2 y valor_desc_2, y almacena el descuento calculado en descuento_2.
valor_final_2 = valor_total_2 - descuento_2  # Calcular el Valor Final a Pagar

# Mostrar los resultados con 3 decimales y el porcentaje de descuento
print(f"De la compra 1 el valor total sin descuento es: {valor_total_1:.3f}, el porcentaje de descuento es {valor_desc_1}%, el valor del descuento es = {descuento_1:.3f}, el valor final a pagar es = {valor_final_1:.3f}")
print(f"De la compra 2 el valor total sin descuento es: {valor_total_2:.3f}, el porcentaje de descuento es {valor_desc_2}%, el valor del descuento es = {descuento_2:.3f}, el valor final a pagar es = {valor_final_2:.3f}")
