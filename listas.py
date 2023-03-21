lista = []
for k in range(10):#se usa la palabra resevada rang para indicar la extencion de la lista
     lista.append(input("introduce valor en lista"))#apped sirve para llenar ell aray

print("los elementos de la lista son"+str(lista))
valor=int(input("introduce el valor a modificar de la lista por el indice: "))#indice donde se insertara un nuevo valror
nuevo= input("intrpoduce el nuevo valior")#valor nuevo por incertar
lista [valor]=nuevo #es hacemos la modificacion
print("los elementos de la lista actualizada son: "+str(lista))
valor=int(input("introduce el indice en el que se insertara el nuevo valor: "))#indice donde se insertara un nuevo valror
nuevo= input("intrpoduce el nuevo volior")#valor nuevo por incertar
lista.insert(valor, nuevo)#el inserte es otra forma de modificar el arreglo, primero pon el ijndice y despues el valor
print("los elementos de la lista actualizada son: "+str(lista))
nuevo=input("introduce el valor a eliminar")
lista.remove(nuevo)#esto remueve ese valor de la l¿ista
print("los elementos de la lista actualizada son: "+str(lista))
nuevo=input("introduce el valor que deseas buscar")
resultado=(nuevo in lista)#con in vas a buscar la variable nuevo dentro de la lista y ver si existe
if(resultado):
    print("el resultado existe y su indice es"+str(lista.index(nuevo)))#el operador index te dice el indice donde se encuentra el elemento que has escrito en teclado y antes lista por que es el lugar donde lo ira a buscar
else:
    print("no existe se elemento")
