###  PROYECTO 2 CALCULADORA EVOLUTIVA

def Sumar():
    sum1 = int(input("Sumando uno: "))
    sum2 = int(input("Sumando dos: "))
    print("La Suma es:", sum1 + sum2)

def Restar():
    res1 = int(input("Minuendo: "))
    res2 = int(input("Sustraendo: "))
    print("La Resta es:", res1 - res2)

def Multiplicar():
    mul1 = int(input("Multiplicador uno: "))
    mul2 = int(input("Multiplicador dos: "))
    print("La Multiplicacion es: ", mul1 * mul2)

def Division():
    div1 = int(input("Dividendo: "))
    div2 = int(input("Divisor: "))
    print("La Division es: ", div1 / div2)

def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opcion:"))
        if (opc == 1):
            Sumar()
        elif (opc == 2):
            Restar()
        elif (opc == 3):
            Multiplicar()
        elif (opc == 4):
            Division()
        elif(opc == 5):
            fin = 1

print("""********************
CALCULADORA DE FRAN 
********************

Choose Options:
1º Suma:
2º Resta:
3º Multi:
4º Div:
5 Exit:""")

Calculadora()
