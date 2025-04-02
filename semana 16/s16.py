# Escribo el archivo de texto y pongo las notas
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: Comprar cámara para dar los examenes.\n")
    file.write("Nota 2: Estudiar para los examenes.\n")
    file.write("Nota 3: Tomar las fotos para los anexos.\n")
    file.write("Nota 4: Repasar teorema de medios (no entendí).\n")

# Abre el archivo my_notes.txt en modo de lectura ('r').
with open('my_notes.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Cierre de archivos
# Los archivos se cierran automáticamente al salir del bloque 'with'