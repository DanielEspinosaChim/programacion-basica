def cargar():
    productos={} # diccionario
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto:"))
        descripcion=input("Ingrese la descripcion:")
        precio=float(input("Ingrese el precio:"))
        stock=int(input("Ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock) #un diccionario que almacena una tupla con los datos obtenidos anteriorment
        continua=input("Desea cargar otro producto[s/n]?")
    return productos


def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])#esto significa que el for in inicia con una vriable cualquiera y eso hace de contador para que el diccionario valla aumentando y los corchetes con numeros son el codigo del diccionario


def consulta(productos):
    codigo=int(input("Ingrese el codigo de articulo a consultar:"))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])
        

def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])



# bloque principal

productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)