nota1=int(input("ingrese el primer promedio"))
nota2=int(input("ingrese el segundo promedio"))
nota3=int(input("ingrese el tercer promedio"))
promedio=(nota1+nota2+nota3)/3
#if promedio>=7:
 #   print("eres buenisimo")
#else:
 #   if promedio>=4:
  #      print("regular")
   # else:
    #    print("eres malisimo")
if promedio>=9 or promedio==10:
        print("eres buenisismo")
elif promedio >=7 or promedio>=8:
    print("regular/bien")
elif promedio>=6:
    print("bien")
elif promedio>=5:
     print("suficiente")

else:
    print("insuficiente")