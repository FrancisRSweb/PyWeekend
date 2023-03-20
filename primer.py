# Primer archivo de python weekend

#lista = ["Roca", "Ruiz", 3, ["Juan", "Gala"]]
#
#print(lista[2])
#print(lista[0])
#print(lista[1])
#print(lista[3][1])
#

# TUPLAS 

# tupla = ("Fran", "Gala", "Dobby")
# 
# print(tupla)
# print(len(tupla))
# print(tupla[1])
# print(tupla[0])
# print(tupla[2])



# Diccionarios    ((  Introducir los nombres en español y obtener por pantalla ingles ))

# mesestraducidos = {"Enero" : "January", "Febrero" : "February", "Marzo" : "March", "Abril" : "April"}
# 
# 
# print(mesestraducidos["Enero"])
# print(mesestraducidos["Marzo"])

# End pashe 3

# Fase 4 Booleanos y operadores logicos.

# variablebooleana = True
# print(variablebooleana)

#### AND / OR

# booleano = True
# booleano1 = False
# print(booleano and booleano1)   == False

# booleano = True
# booleano1 = False
# print(booleano or booleano1) == True

#### NOT

# booleano = False
# print(not booleano) Devuelve el contrario

####  Operadores relacionales

# numero1 = 6
# numero2 = 9
# print(numero1 > numero2) # false
# print(numero1 >= numero2) # false
# print(numero1 < numero2) # true
# print(numero1 <= numero2) # true
# print(numero1 == numero2) # false
# print(numero1 != numero2) # true

#####  FASE 5 Cadenas de texto (Avanzado)

## Capitalize

# cadena = "en un lugar de mi casa..."
# print(cadena.capitalize())

## Upper

# cadena = "en un lugar de mi casa..."
# print(cadena.upper())

## Lower

# cadena = "En un lugar de mi casa.."
# print(cadena.lower())

## Len

# cadena = "en un lugar de mi casa..."
# print(len(cadena))

## isalnum

# cadena = "en un lugar de mi casa.."
# print(cadena.isalnum())
# cadena2 = "12893189"
# print(cadena2.isalnum())
# cadena3 = "adasd12893189"
# print(cadena3.isalnum())
# cadena4 = "adasd 12893189"
# print(cadena4.isalnum())

## isalpha

# cadena = "Enunlugardemicasa"
# print(cadena.isalpha())
# cadena2 = "En un lugar de mi casa"
# print(cadena2.isalpha())
# cadena3 = "28931891"
# print(cadena3.isalpha())

## isdigit

# cadena = "En un lugar de mi casa"
# print(cadena.isdigit())
# cadena3 = "28931891"
# print(cadena3.isdigit())

## islower / isupper

# cadena = "En un lugar de mi casa"
# print(cadena.islower())

## lstrip   rstrip   strip

# cadena = " En un lugar de mi casa"
# print(cadena.lstrip())
# cadena2 = "En un lugar de mi casa "
# print(cadena2.rstrip())
# cadena3 = " En un lugar de mi casa "
# print(cadena3.strip())

## max  /  min

# cadena = "abaskdlzfj"
# print(max(cadena))
# print(min(cadena))

## replace

# cadena = "AEIOU"
# print(cadena.replace('A', 'E'))

## swapcase

# cadena = "En un lugar de mi casa"
# print(cadena.swapcase())

## split  -> Convertir cadena de texto en lista elementos.

#cadena = "En un lugar de mi casa"
#print(cadena.split())

cadena = "15/12/1992"
print(cadena.split("/"))


