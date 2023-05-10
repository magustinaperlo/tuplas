#Crea una tupla con numeros, pide al usuario un numero por teclado e indica
#cuantas veces se repite segun lo halle en la tupla creada

#VALIDAR LOS INGRESOS DEL USUARIO
cont = 0
numeros = (7,4,9,7,2,0,3,2,5,5,1,8,0,5,4,9,2,9,2,3,3)

ingreso = int(input("ingrese numero que desea consultar: "))

if ingreso != len(numeros) and ingreso > len(numeros):
    print ("numero ingresado inexistente.")
else:
   for e in numeros:
      if ingreso == e:
        cont = cont + 1

print ("El numero ingresado se repite", cont, "veces")
