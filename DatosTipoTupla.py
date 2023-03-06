def cargarFechas():
    dd=int(input("que dia es hoy"))
    mes=int(input("que mes es hoy"))
    año=int(input("en que año estamos"))
    tupla=dd,mes,año
    return(tupla)

def ImprimirFecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")
    
fecha=cargarFechas()
ImprimirFecha(fecha)
    