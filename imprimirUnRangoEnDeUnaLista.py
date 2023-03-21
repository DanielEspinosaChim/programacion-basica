def meses_faltantes(inicio, final):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[inicio: final]


# bloque principal
#Se recupera desde el mes indicado hasta el otro mes indicado 
print("Imprimir los nombres de meses compredidos entre un mes y otro:")
inicio=int(input("Ingrese el numero de mes:"))
final=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(inicio, final)
print(mesesfalta)