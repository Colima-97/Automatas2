#Program Name: Ventanas gráficas
#Objective: We'll learn how to use graphics 
#Author:Brandon I. Pérez Sandoval
#Date: July 5th 2019
#-------------------------------------------------------
#Here we import the libraries that we need
#-------------------------------------------------------
import tkinter as tk
from tkinter import *

#-------------------------------------------------------
#Create the window
#-------------------------------------------------------
root = tk.Tk()
#This is the title of the main window
root.title('Calculadora sencilla')
#Here we create a frame, it is used to organizate the distributions of widgets
frame = Frame(root)
#Making the frame apears
frame.pack()
#Changing the background
frame.config(bg='lightblue')
#Establishing the size of the label
frame.config(width = 480, height = 320)
#Size of the border in pixels
frame.config(bd=25)

#-------------------------------------------------------
#Creating variables
#-------------------------------------------------------

n1 = StringVar()
n2 = StringVar()
r = StringVar()

#-------------------------------------------------------
#Functions
#-------------------------------------------------------
def sumar():
    r.set( float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    r.set( float(n1.get()) - float(n2.get()))
    borrar()

def mult():
    r.set( float(n1.get()) * float(n2.get()))
    borrar()

def div():
    try:
        r.set( float(n1.get()) / float(n2.get()))
        borrar()
    except ZeroDivisionError:
        r.set("Zero Division Error!")

def borrar():
    n1.set('')
    n2.set('')   

#-------------------------------------------------------
#Here we create a widget, a Label
#-------------------------------------------------------
label1 = Label(frame, text = 'Inserte primer número')
#Add the widget to the window
label1.grid(row = 0, column = 0)
label1.config(bg = 'lightblue', bd = 4, pady = 4)

#Creating an entry
entry1 = Entry(frame)
entry1.grid(row = 0, column = 1)
entry1.config(textvariable = n1)

#Creating another label
label2 = Label(frame, text = 'Inserte segundo número')
label2.grid(row = 1, column = 0)
label2.config(bg = 'lightblue', bd = 4, pady = 4)

#Creating the second entry
entry2 = Entry(frame)
entry2.grid(row = 1, column = 1)
entry2.config(textvariable = n2)

#Labels and Entry disabled for answer
label3 = Label(frame, text = 'Respuesta')
label3.grid(row = 2, column = 0)
label3.config(bg = 'lightblue', bd = 4, pady = 4)

entryAnswer = Entry(frame)
entryAnswer.grid(row = 2, column = 1)
entryAnswer.config(state = DISABLED, justify = CENTER, textvariable = r)

#-------------------------------------------------------
#Buttons
#-------------------------------------------------------
btnSumar = Button(frame, text = 'Suma',command = sumar)
btnSumar.grid(row = 4, column = 0)
btnRestar = Button(frame, text = 'Resta', command = restar)
btnRestar.grid(row = 4, column = 1)
btnMult = Button(frame, text = 'Multip',command = mult)
btnMult.grid(row = 5, column = 0)
btnDiv = Button(frame, text = 'División', command = div)
btnDiv.grid(row = 5, column = 1)

#The window apears 
root.mainloop()