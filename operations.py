#Program Name: Operations
#Objective: We'll learn how aritmetical operations works
    #Also, we'll see while and for loops
#Author:Brandon I. Pérez Sandoval
#Date: Jun 29 2019

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - 2 

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

#Function to compare two int values
def compare(num1, num2):
    if num1 > num2:
        print('The greather is num1: ' , num1)
    elif num2 > num1 :
        print('The greather is num2: ' , num2)
    else:
        print('Both are equals: ' , num1 , ' = ' , num2)

def count(num1, num2):

    if (num2 > num1):
        for i in range(num1, num2+1):
            print('Value of i: ', i)
    elif (num1 > num2):
        for i in range(num1, num2-1, -1):
            print('Value of i: ',i)

def main():
    repeat = True

    while(repeat):
        print('\n\t.:Basic Operations with Intagers:.')
        print('\n')
        n1 = int(input('Insert the first number: '))
        n2 = int(input('Insert the second number: '))
        print('\n')

        #Invoque the methods here
        print("Addition is equals to: " , (add(n1, n2)))
        print("Substraction is equals to: " , (sub(n1, n2)))
        print("Multiplication is equals to: ", (mult(n1, n2)))
        print("Division is equals to: " , (div(n1, n2)))

        #Invoque "compare" method
        compare(n1, n2)

        #Invoque "count" method
        count(n1, n2)

        resp = input("\n>>>Wanna go again? (Y/N): ")
        if (resp == 'Y' or resp == 'y'):
            repeat = True
        else:
            #For anything else
            print('See you later!')
            repeat = False


if __name__ == "__main__":
    main()