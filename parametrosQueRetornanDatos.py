def retorno_superficie(lado):
    sup=lado*lado
    return sup #el return como en java sirve para retornar valores
va=int(input("introduce el valor del cuadrado"))#para hacer un valor entero y pasarlo al parametro despues, si no le vas a poasar un caracter
superficie=retorno_superficie(va)
print("añ algoritmo del cuadrado es; "+str(superficie))

