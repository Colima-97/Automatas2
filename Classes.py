#Program Name: Punto
#Objective: We'll learn how to manage classes in python
    #also, we'll look at heritage
#Author:Brandon I. Pérez Sandoval
#Date: July 5th 2019
#-------------------------------------------------------

import math as mat
#-------------------------------------------------------

class Punto(object):
    #Constructor de la clase
    def __init__(self, valorX, valorY):
        self.x = valorX
        self.y = valorY

    #Métodos get    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #Métodos set
    def setX(self, valorX):
        self.x = valorX
    
    def setY(self, valorY):
        self.y = valorY

    
    def toString(self):
        return 'El punto tiene las siguientes coordenadas: (',self.x ,',',self.y,')'

#-------------------------------------------------------
#Herencia en Python
#Clase circunferencia
#-------------------------------------------------------
class Circunferencia(Punto):
    def __init__(self, valorRadio):
        self.radio = valorRadio

    def getRadio(self):
        return self.radio

    def setRadio(self, valorRadio):
        self.radio = valorRadio

    def getArea(self):
        return mat.pi * mat.pow(self.getRadio(), 2)

    def toString(self):
        return "La circunferencia tiene como centro: ", self.getX(),",",self.getY(), self.getRadio()," el área es: ", self.getArea()

#-------------------------------------------------------
#Clase cilindro
#-------------------------------------------------------
class Cilindro(Circunferencia):
    def __init__(self, valorAltura):
        self.altura = valorAltura

    def getAltura(self):
        return self.altura

    def setAltura(self, valorAltura):
        self.altura = valorAltura
        
    def calcularVolumen(self):
        return self.getArea() * self.altura

    def toString(self):
        return "El volumen es: ", self.calcularVolumen()

#-------------------------------------------------------
#Método main
#-------------------------------------------------------
def main():
    #Creamos objeto mi_punto
    print('Punto 1')
    mi_punto = Punto(1,3)
    print(mi_punto.toString())

    #Creamos objeto mi_punto2
    print('Punto 2')
    mi_punto2 = Punto(0,0)
    print(mi_punto2.toString())

    #Invocamo métodos set
    mi_punto2.setX(2)
    mi_punto2.setY(-1)
    print(mi_punto2.toString())

    #Creamos punto3
    print("Punto 3")
    mi_punto3 = Circunferencia(12.34)
    mi_punto3.setX(10)
    mi_punto3.setY(12)
    print(mi_punto3.toString())

    #Creamos punto4
    print("Punto 4")
    mi_punto4 = Cilindro(0)
    mi_punto4.setX(9)
    mi_punto4.setY(11)
    mi_punto4.setRadio(7)
    mi_punto4.setAltura(10)
    print(mi_punto4.toString())

if __name__ == '__main__':
    main()