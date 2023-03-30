def meses_faltantes(inicio):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[:inicio]#los dos puntos indican los valores antes 


# bloque principal
# se recupera todos los meses anteriores a mes indicado
print("Imprimir los nombres de meses y todos los anteriores:")
inicio=int(input("Ingrese el numero de mes:"))

mesesfalta=meses_faltantes(inicio)
print(mesesfalta)