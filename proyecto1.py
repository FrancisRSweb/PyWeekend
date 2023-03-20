##  Proyecto 1 Calculadora

eso = False
print("""********************
CALCULADORA DE FRAN 
********************

Choose Options:
1º Suma:
2º Resta:
3º Multi:
4º Div:
5 Exit:""")
while not(eso):
    opc = int(input("Opcion:"))
    if (opc==1):
        sum1 = int(input("Sumando uno:"))
        sum2 = int(input("Sumando dos:"))
        print ("La Suma es:", sum1+sum2)
    elif(opc==2):
        minuendo = int(input("Minuendo:"))
        sustraendo = int(input("Sustraendo:"))
        print ("La Resta es:", minuendo-sustraendo)
    elif(opc==3):
        multiplicando = int(input("Multiplicando:"))
        multiplicador = int(input("Multiplicador:"))
        print ("La Multiplicacion es:", multiplicando*multiplicador)
    elif(opc==4):
        dividendo = int(input("Dividendo:"))
        divisor = int(input("Divisor:"))
        print ("La Division es:", dividendo/divisor)
    elif(opc==5):
        eso = True