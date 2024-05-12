# class OperarValores:
#     def __init__(self,v1,v2):
#         self.__V1 = v1
#         self.__V2 = v2
#     def __Sumar(self):
#         return self.__V1 + self.__V2
#     def __Restar(self):
#         return self.__V1 - self.__V2
#     def Operar(self):
#         print("El resultado de la suma es: ", self.__Sumar())
#         print("El resultado de la resta es: ", self.__Restar())

# operarvalores = OperarValores(10,12)
# operarvalores.Operar()


# class OperarValores:
#     def __init__(self,v1,v2):
#         self.__V1 = v1
#         self.__V2 = v2
#     def __Sumar(self):
#         return self.__V1 + self.__V2
#     def __Restar(self):
#         return self.__V1 - self.__V2
#     def Operar(self):
#         print("El resultado de la suma es: ", self.__Sumar())
#         print("El resultado de la resta es: ", self.__Restar())

# operarvalores = OperarValores(10,12)
# operarvalores.Operar()
# print("El resultado de la suma es: ", operarvalores.__Sumar())


#  Fase 2: Herencia

class Electrodomestico:
    def __init__(self):
        self._Encendido = False
        self._Tension = 0

    def Encender(self):
        self._Encendido = True
    def Apagar(self):
        self._Encendido = False
    def Encendido(self):
        return self._Encendido
    def SetTension(self,tension):
        self.__Tension = tension
    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomestico):
    def __init__(self):
        self.__RPM = 0
        self.__Kilo = 0
    def SetRPM(self, rpm):
        self.__RPM = rpm
    def SetKilos(self, kilos):
        self.__Kilos = kilos
    def MostrarLavadora(self):
        print("########### \n")
        print("Lavadora:")
        print("\tRPM:",self.__RPM)
        print("\tKilos:",self.__Kilos)
        print("\tTension:", self.GetTension())
        if self.Encendido():
            print("\t¡Lavadora encendida! \n")
        else:
            print("\tLavadora no encendida.")
        print("########")

lavadora = Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(7)
lavadora.SetTension(220)
lavadora.Encender()
lavadora.MostrarLavadora()
