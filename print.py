print("Datos de la persona")
#para cargar por teclado una cadena de caracteres utilizamos input
#
nombre1=input("cual es el nombre del producto")
precio=int(input("cual es su precio"))
nombre2=input("cual es el nombre del producto")
precio2=int(input("cual es su precio"))

#constante
BONIFICACION=20 #las constantes se escriben con letras mayusculas por convencion 

precio_Compra_Total=precio+ precio2
comprar=precio>=precio2 #comparacion, se compara si el precio es igual que el segundo precio
logico=(precio<precio2 and precio==precio2)#operador logico

cabecera= "resultados del producto {0}. y del producto {1}.:"#en esos dos sitio ubicaremos el texto que queremos concatenar 
print(cabecera.format(nombre1, nombre2))#para imprimir el formato de arriba
print("el precio del primer valor es mayor o igual al precio del segundo valor")
print(comprar)
print("la suma de los dos articulos es: "+str(precio_Compra_Total))#otra forma de concatenar 
print("precio<precio2 and precio==precio2")
print(logico)
precio_Compra_Total+=BONIFICACION#estas sumandole bonificcion al precio de la compra total
print("al precio total le sumamos el valor de la constantre "+str(precio_Compra_Total))