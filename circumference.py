#Program Name: Circumference
#Objective: We'll learn how to calculate the area and diameter from a circumference
    #also, we'll import math library
#Author:Brandon I. Pérez Sandoval
#Date: July 1 2019

import math as mat
import os

#-------------------------------------------------------
#Area calculation
#-------------------------------------------------------
def areaCalculation(r):
    area = mat.pi*(mat.pow(r, 2))
    return area


#-------------------------------------------------------
# Diameter calculation
#-------------------------------------------------------    
def diamCalculation(r):
    diam = r * 2
    return diam

#-------------------------------------------------------
#Main method
#-------------------------------------------------------
def main():
    
    while(True):
        print('\n.:Script for Circle area calculation:.')
        radio = float(input('Insert radious value: '))
        #Invoque a method
        print('The area is: ' , areaCalculation(radio))
        print('The diameter is: ' , diamCalculation(radio))
        
        resp = input('\n>>>Wanna go again? (Y/N): ')
        
        if (resp.upper() != 'Y'):
            os.system('cls')
            print('See you!')
            break         

        os.system('cls')        
#-------------------------------------------------------

if __name__ == "__main__":
    main()