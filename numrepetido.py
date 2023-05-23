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

#sugerencia con correccion: (La condición if ingreso != len(numeros) and ingreso > len(numeros): 
#no es correcta para validar si el número ingresado está fuera del rango de la tupla. Además,
#la condición ingreso != len(numeros) no es necesaria ya que no tiene sentido comparar el número ingresado con la longitud de la tupla.)

cont = 0
numeros = (7, 4, 9, 7, 2, 0, 3, 2, 5, 5, 1, 8, 0, 5, 4, 9, 2, 9, 2, 3, 3)

ingreso = int(input("Ingrese el número que desea consultar: "))

if ingreso not in numeros:
    print("El número ingresado no existe en la tupla.")
else:
    for e in numeros:
        if ingreso == e:
            cont = cont + 1

    print("El número ingresado se repite", cont, "veces.")

