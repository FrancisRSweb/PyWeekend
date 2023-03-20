### OBJETIVO 5 FUNCIONES

# def Saludar():
#     print("Hola github")
# 
# Saludar()

# def EsMayorQueCero(param):
#     if param > 0:
#         print(param, " Es mayor a 0")
#     else:
#         print(param, " No es mayor a 0")
# 
# numero = int(input("Introduce un numero: "))
# EsMayorQueCero(numero)

# def Sumar(param1, param2):
#     return param1 + param2
# 
# sumando1 = int(input("Introduce el primer sum: "))
# sumando2 = int(input("Introduce el segundo sum: "))
# resultado = Sumar(sumando1, sumando2)
# print("El resultado de la suma es: ", resultado)

# def SumarRestar(param1, param2):
#     return param1 + param2, param1 - param2
# 
# numero1 = int(input("Introduce el primer numero: "))
# numero2 = int(input("Introduce el segundo numero: "))
# resultadosuma, resultadoresta = SumarRestar(numero1,numero2)
# print("El resultado de la suma es: ", resultadosuma)
# print("El resultado de la resta es: ", resultadoresta)

# def Sumar(*valores):
#     resultado = 0
#     for item in valores:
#         resultado = resultado + item
#     return resultado
# 
# resultado = Sumar(23,43,1,4,2)
# print("Esta es la suma de todos los valores= ", resultado)


## FASE 2 FUNCIONES ANIDADAS

 # def SumarRestar(param1, param2):
 #     return Sumar(param1,param2), Restar(param1,param2)
 # 
 # def Sumar(sumando1, sumando2):
 #     return sumando1 + sumando2
 # 
 # def Restar(minuendo, sustraendo):
 #     return minuendo - sustraendo
 # 
 # numero1 = int(input("Introduce el primer numero: "))
 # numero2 = int(input("Introduce el segundo numero: "))
 # resultadosuma, resultadoresta = SumarRestar(numero1,numero2)
 # print("El resultado de la suma es: ", resultadosuma)
 # print("El resultado de la resta es: ", resultadoresta)