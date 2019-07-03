#Program Name: Lists
#Objective: We'll see how list works in python
#Author:Brandon I. Pérez Sandoval
#Date: July 2nd 2019
#-------------------------------------------------------
import os

#-------------------------------------------------------
#Declaring a global list
#-------------------------------------------------------
myList = []

#-------------------------------------------------------
#Function to add items to the list
#-------------------------------------------------------
def addItem(data):    
    myList.append(data)   

#-------------------------------------------------------
#Print list
#-------------------------------------------------------
def printList():
    j = 0
    for i in myList:
        print('Item [', j ,'] is ', i)
        j += 1
#-------------------------------------------------------
#Remove item
#-------------------------------------------------------
def removeItem(removing):
    if removing in myList:
        myList.remove(removing)
        print('Item (',removing ,') deleted successfully!')
    else:
        print("The item doesn't exist in the list")

#-------------------------------------------------------
#Search item
#-------------------------------------------------------
def searchItem(searching):
    if searching in myList:
        print('The item (',searching,') was found in the index [',myList.index(searching),']')
    else:
        print('Item not found')    

#-------------------------------------------------------
#Modify Item
#-------------------------------------------------------
def modifyItem(mod, newItem):
    if mod in myList:
        index = myList.index(mod)
        myList[index] = mod
        print('The item (',mod,')[',index,'] was replaced successfully by (',newItem,')')
    else:
        myList.append(newItem)
        print('(',mod,') not found')        
#-------------------------------------------------------
#Main mathod
#-------------------------------------------------------
def main():  
    resp = 'Y'
    while(True):      
        print('.:Working with lists:.')
        print('1 - Add item to list')
        print('2 - Search an item')
        print('3 - Modify an item')
        print('4 - Delete an item')
        print('5 - Print the list')
        print('0 - Exit')

        opc = int(input('Please choose an option bwtn 0 and 5 \n: '))

        if(opc == 0):
            #Exit
            print('See you!')
        elif(opc == 1):
            #Add
            adding = input('Add an item: ')
            addItem(adding)
        elif(opc == 2):
            #Search
            searching = input('Insert an item that you are looking for: ')
            searchItem(searching)
        elif(opc == 3):
            #Modify
            modify = input('Insert the item that you want to modify: ')
            newItem = input('Insert the new item: ')
            modifyItem(modify, newItem)
        elif(opc == 4):
            #Delete
            deleting = input('Insert an item that you want to delete: ')
            removeItem(deleting)
        #Need to end this shit later
        elif(opc == 5):
            #Print
            printList()
        else:
            #None
            print('Option ',opc,' not found!')
        #Almost the end
        if(opc == 0):
            resp = 'N'            
            break
        else:    
            resp = input('\n>>>Wanna go again? (Y/N): ')
            if (resp.upper() != 'Y'):
                os.system('cls')
                print('See you!')
                break         

        os.system('cls')        

if __name__ == "__main__":
    main()