### Objetivo 6 PROGRAMACION ORIENTADA A OBJETOS BASICA
# 
# class Punto:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
#     
#     def MostarPunto(self):
#         print("El punto es (", self.X,",",self.Y,")")
# 
# p1 = Punto(4,6)
# p2 = Punto(-5,9)
# p3 = Punto(3,-7)
# p4 = Punto(0,4)
# p1.MostarPunto()
# p2.MostarPunto()
# p3.MostarPunto()
# p4.MostarPunto()
# 


## Modificacion valor objeto

# class Punto:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
#     def MostrarPunto(self):
#         print("El punto es (",self.X,",",self.Y,")")
# 
# p1 = Punto(4,6)
# p1.MostrarPunto()
# p1.X = 7
# p1.MostrarPunto()

## objeto en objeto

# class Punto:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
#     def MostrarPunto(self):
#         print("El punto es (",self.X,",",self.Y,")")
# 
# p1 = Punto(4,6)
# p1.MostrarPunto()
# p2 = Punto(3,8)
# p2.MostrarPunto()
# p1.MostrarPunto()
# p1 = p2
# p1.MostrarPunto()

## COMPOSICION

# class Punto:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
#     def MostrarPunto(self):
#         print("El punto es (",self.X,",",self.Y,")")
# 
# 
# class Triangulo:
#     def __init__(self,v1,v2,v3):
#         self.V1 = v1
#         self.V2 = v2
#         self.V3 = v3
#     def MostrarVertices(self):
#         self.V1.MostrarPunto()
#         self.V2.MostrarPunto()
#         self.V3.MostrarPunto()
# 
# v1 = Punto(3,4)
# v2 = Punto(6,8)
# v3 = Punto(9,2)
# triangulo = Triangulo(v1,v2,v3)
# triangulo.MostrarVertices()

