#parametros son variables locales que van dentro de los parentesis
#argumentos son los valores que reciben esas vriables
#los argumentos tienen que ir en orden que declaraste los parametros como dijo polanco
#se puedejn asignar valores por defecto a klos parametros
#parametros arbitrarios van a ser recibidos por los argumentos en forma de tupla y van con asterisco
def mostrar_mensaje(mensaje):
    print("*****************")
    print(mensaje)
    print("*****************")

def cargar_suma():
    valor1=int(input("ingresar el primer valor"))
    valor2=int(input("ingresar el segundo valor"))
    suma=valor1 + valor2
    print("la suma es:", suma)

mostrar_mensaje("calculo de la suma de valores")
cargar_suma()