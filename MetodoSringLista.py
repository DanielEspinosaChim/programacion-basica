archivo = open("archivo.txt", "r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()
lista = ['Línea 1\n', 'Línea 2']
 
archivo.writelines(lista)
archivo.seek(final_de_archivo)
 
print (archivo.readline())
# Línea 1
 
print (archivo.readline())
# Línea 2