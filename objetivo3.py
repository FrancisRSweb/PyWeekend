## IF

# numero = int(input("Escribe un numero del 1 al 10: "))
# if numero >= 10:
#     print("!El numero es mayor a 10")
#     print("Has escrito " + str(numero))
# else:
#     print("Tu numero esta entre el 1 y 10")
#     print("Has escrito " + str(numero))

# cadena = "en un lugar de mi casa"
# 
# if "lugar" in cadena:
#     print("Encontrado!")
# else:
#     print("No encontrado")


# cadena = "En un lugar de mi casa"
# 
# if cadena.startswith('E'):
#     print("Empieza por 'E'")
# else:
#     print("No empieza por 'E'")
# if cadena.endswith('p'):
#     print("Termina por 'p'")
# else:
#     print("NO termina por 'p'")


numero1 = int(input("Escribe un numero: " ))
numero2 = int(input("Escribe un numero: " ))

if numero1 < numero2:
    print("El numero es menor que el segundo")
elif numero1 == numero2:
    print("Son iguales")
else:
    print("El primero es mayor")