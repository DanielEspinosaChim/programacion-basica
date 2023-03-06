def cargar():
    diccionario={}
    continuar="s"
    while continuar=="s":
        esp=input("capture la palabra en español")
        ing=input("capture la palabra en ingles")
        diccionario[esp]=ing#diccionario es como una base de datos en la que esp sirve como el codigo y ingles el valor que tendra 
        continuar=input("desea continuar [s/n]")
    return diccionario

def imprimir(diccionario):
    print("listado de valores de la lista")
    for x in diccionario:#x es un iterador cualquiera tecnicamente no importa que sea si x, español, ingles...
        print(x, diccionario[x])#le estas diiendo que lo que esta en el valor uno de diccionario te lo imprima, en este caso x seria esp y diccionario[x] seria ing por que esta igualado a eso arriba
        # en este caso x habla de el valor de español(el valor unico, a lo que metiste en español)
        #diccionario[x] esta igualado a ingles entonces vale lo que ingles(a los valores juntos diccionario[x]esto cuando esta junto vale ingles)
        #cuando solo es x se refere a la variable x y cuando sea diccionario[x] es a lo que este igualado por que ya es una funcion no una variable, es a lo que este igualado el vector de lo que tomara el valor
    
def ConsultaPalabra(diccionario):
    pal=input("captura la palabra en español que deseas buscar")
    if pal in diccionario:
        print("la traduccion al ingles de la palabra es: ", diccionario[pal])
        
diccionario=cargar()
imprimir(diccionario)
ConsultaPalabra(diccionario)