def proceso(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")
    

# bloque principal
#podemos utilizar valores negativos para acceder a valores de las estructuras de datos
#para aceder a último valor pondremos el indice -1, para el penúltimo el -2 así hasta el primero
#lista =[1,2,3]  print(lista[-1]) accedemos a valor 3 print([-2]) accedemos al valor 2


proceso("1331")
proceso("3851")