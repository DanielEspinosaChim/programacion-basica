cantidad=0
x=1
n=int(input("cuantas piezas cargara?"))
while x<=n:
    largo=float(input("ingrese la medida de la pieza"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print("la cantidad de pieza aptas son")
print(cantidad)