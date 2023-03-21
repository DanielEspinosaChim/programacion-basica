##una funcion es coo un metodo parecido, no es igual paara cuando lo lea tu yo del futuro que sepa mas y ande de mamon
#la estructura de las funciones es: palabra reservada def "el nombre que ler quiras poner" ():
def presentacion():
    print("programa para hacer operaciones aritmeticas de suma y resta de dos valores")
    print("**************************+")
    
def introduccioDeDatos():
    global valor1
    global valor2#la variable global es lo que en java lavariable estatica
    valor1=int(input("ingrese el primer valor"))
    valor2=int(input("ingrese el segundo valor"))

def suma():
    suma = valor1 + valor2
    print("la suma de los dos valores es: ",suma)


def resta():
    resta = valor1 - valor2
    print("la suma de los dos valores es: ",resta)

def finalizacion():
    print("******************")
    print("gracias por usar este programa")
    
    #programa principal

presentacion()
introduccioDeDatos()
suma()
resta()
finalizacion()