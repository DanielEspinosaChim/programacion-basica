def cargar_lista():
    li=[]#crear una lista
    for x in range(5):
        valor=int(input("captura el valor"+str(x)+"en la lista"))
        li.append(valor)#apend añade un nuevo valor al final de la lista
    return li

def imprimir_mayor(li):
    print("valores de la lista mayores a 10: ")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])
        
lista=cargar_lista()
imprimir_mayor(lista)

    
