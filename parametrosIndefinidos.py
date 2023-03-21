def sumar(v1,v2,*lista):#se usa el asterisco cuando no conocemos el numero de parametros que se la mandan al metodos
    suma=v1+v2
    for x in range(len(lista)):#el len devuelve el una serie de caracteres de rtipo cadena ya que es el lrgo o la extencion que tenga el array
        suma=suma+lista[x]
    return suma

print("suma de dos valores")
print(sumar(1,2))
print("suma de cuatro valores")
print(sumar(1,2,3,4))
print("suma de diez valores")
print(sumar(1,2,3,4,5,6,7,8,9,10))

print("aqui inicia el ejercicio 2")
def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):#inicia en la posicion 1 y recorre toda la lista
      if lista[x]>may:
        may=lista[x]
    return may

def menor(lista):
    men=lista[0]#menor tiebe el valor de la lista en la posicion 0
    for x in range(1,len(lista)):
     if lista[x]<men:
        men=lista[x]
    return men

listaValore=[10,56,23,34,190,298]
print("lista completa")
print(listaValore)
print("suma de los elementos",sumarizar(listaValore))
print("el numero mayor es; "+str(mayor(listaValore)))
print("el numero menor es; "+str(menor(listaValore)))
