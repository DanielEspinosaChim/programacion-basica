def SumaDeValores(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

def ValorMayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def ValorMenor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men


datos=[5454, 43430, 3222, 1222, 666, 65656, 545, 2333,21212, 23, 6565]
print("total de datos: ")
print(datos) 
print("el total de sumar los valores del array: ", SumaDeValores(datos))
print("el valor mayor del array es: ",ValorMayor(datos))
print("el valor menor del array es: ",ValorMenor(datos))
   