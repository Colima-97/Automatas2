#Program Name: Triangle
#Objective: We'll detect whether a triangle is Equilateral, 
    #Isosceles or Scalene
#Author:Brandon I. Pérez Sandoval
#Date: July 1 2019
#-------------------------------------------------------
import os
#-------------------------------------------------------
#Method to identificate the triangle type
#-------------------------------------------------------
def identificator(s1, s2, s3):
    perim = s1+s2+s3
    if (s1 == s2 == s3):
        #Equilateral
        return "Equilateral" , perim
    elif (s1 != s2 != s3 and s1 != s3):
        #Scalene
        return "Scalene" , perim
    else:
        #Isosceles
        return "Isosceles" , perim



#-------------------------------------------------------
#Main method
#-------------------------------------------------------
def main():
    while(True):
        print('.:Script for Triangles:.')
        side1 = float(input('Insert the first side: '))
        side2 = float(input('Insert the second side: '))
        side3 = float(input('Insert the third side: '))

        triangle,perimeter = identificator(side1, side2, side3)

        print('\nThe triangle is ',triangle, ' and the perimeter is ' ,perimeter)
        
        resp = input('\n>>>Wanna go again? (Y/N): ')        
        if (resp.upper() != 'Y'):
            os.system('cls')
            print('See you!')
            break         

        os.system('cls')        

if __name__ == "__main__":
    main()