def meses_faltantes(numero):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numero:]


# bloque principal
#Se recupera desde el mes indicado hasta el final de la lista
print("Imprimir los nombres de meses que faltan hasta fin de año")
numero=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)