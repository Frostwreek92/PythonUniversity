# Crear un archivo
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola como estas')
    archivo.write('\nestoy agregando informacion al archivo')

print(f'Se creo el archivo {nombre_archivo}')