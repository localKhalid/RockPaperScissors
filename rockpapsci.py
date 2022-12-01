from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title("Rock, Paper Scissors Game")
root.geometry("1000x500")
root.config (bg = "white")
root.iconbitmap('C:/Users/user/Documents/Coding/SnakeGame')

#define images.
rock = PhotoImage(file='rock.png')
paper = PhotoImage(file='paper.png')
scissors = PhotoImage(file='scissors.png')

options = [rock, paper, scissors]

computerinput = randint(0,2)

image_choosen = Label(root, image=options[computerinput])
image_choosen.pack(pady=20, padx= 20)

def new():
    computerinput = randint(0,2)
    image_choosen.config(image=options[computerinput])

spinbutton = Button(root, text = "NEXT", command= new )
spinbutton.pack(pady=20)


#PLAYER INPUT
playerinput = ttk.Combobox(root, value =("Rock", "Paper", "Scissors"))     
#A combobox is a combination of an Entry widget and a Listbox widget. A combobox widget allows you to select one value in a set of values. In addition, it allows you to enter a custom value.
playerinput.current(0)
playerinput.pack(pady=20)

#Deciding who won.
outcome = Label(root, text="" , font = ("Helvetica", 20), bg="white")
outcome.pack(pady=40)


if playerinput.get() == "Rock":
    playinputvalue = 0
elif playerinput.get() == "Paper":
    playinputvalue = 1
elif playerinput.get() == "Scissors":
    playinputvalue = 2

if playinputvalue == 0:
    if computerinput == 0:
        outcome.config(text="Its a tie! Try again!")
    if computerinput == 2: 
        outcome.config(text="You Win!, Play again?")
    if computerinput == 1:
        outcome.config(text="You Lose!, Try again!")

elif playinputvalue == 1:
    if computerinput == 0:
        outcome.config(text="You Win!, Play again?")
    if computerinput == 1: 
        outcome.config(text="Its a tie! Try again!")
    if computerinput == 2:
        outcome.config(text="You Lose!, Try again")


elif playinputvalue == 2:
    if computerinput == 0:
        outcome.config(text="You Lose!, Try again!")
    if computerinput == 2: 
        outcome.config(text="Its a tie! Try again!")
    if computerinput == 1:
        outcome.config(text="You Win!, Play again?")

#FUNCTION FOR NEW IMAGE TO BE SELECTED- AGAIN AT RANDOM


root.mainloop()