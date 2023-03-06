def CargarPaisPoblacion():
    paises=[]
    for x in range(5):
        nom=input("ingresa el nombre del pais")
        cant=int(input("ingrese la cantidad de haitantes de la poblacion"))
        paises.append((nom, cant))# con el apend estoy metiendo los valores de la tupla a ala lista
    return(paises)

def imprimir(paises):
    print("paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])
    
def paisConMasPoblacion(paises):
    pos=0
    for x in range(1 , len(paises)):
        if paises[x][1] > paises[pos][1]:
            pos=x
    print("pais con mayor numero de habitantes", paises[pos][0])
    
paises=CargarPaisPoblacion()
imprimir(paises)
paisConMasPoblacion(paises)

        
    