# Crear un archivo
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura
archivo = open(nombre_archivo, 'w')
archivo.write('Hola como estas')
archivo.write('\nestoy agregando informacion al archivo')
archivo.close()

print(f'Se creo el archivo {nombre_archivo}')