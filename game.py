#Imports
import tkinter as tk
import random
from tkinter import font
from tkinter.constants import ANCHOR, NE, NSEW, NW
from tkinter.font import Font
from PIL import ImageTk, Image
from ttkbootstrap import Style

#Functions
#Global Variables
playerScore= 0
computerScore= 0

#Randomize Computer Choice
def computerChoice():
 x=random.choice(["Rock","Paper","Scissors"])
 return x

def winner(player):
 computer= computerChoice()
 global computerScore
 global playerScore
 if computer == player:
  print("Draw")
 elif computer== "Rock" and player=="Scissors":
  computerScore+=1
 elif computer== "Rock" and player=="Paper":
  playerScore+=1
 elif computer== "Paper" and player=="Rock":
  computerScore+=1
 elif computer== "Paper" and player=="Scissors":
  playerScore+=1
 elif computer== "Scissors" and player=="Rock":
  playerScore+=1
 elif computer== "Scissors" and player=="Paper":
  computerScore+=1
 score.configure(text="Your Score: {}\nComputer Score: {}".format(playerScore,computerScore))
 computerPhoto(computer)

def playerPhoto(choice):
 playerShot.create_image(0,0, anchor= NW, image= choice)

def computerPhoto(choice):
 if choice=="Rock":
  im=rockImage
 elif choice=="Paper":
  im=paperImage
 elif choice=="Scissors":
  im=scissorsImage
 computerShot.create_image(0,0, anchor= NW, image= im)

def Rock():
 winner("Rock")
 playerPhoto(rockImage)
def Paper():
 winner("Paper")
 playerPhoto(paperImage)
def Scisssors():
 winner("Scissors")
 playerPhoto(scissorsImage)

#Bootstrap Style
style= Style(theme="minty")
#Creates Window
window = style.master
window.title("R-P-S")

rock= tk.Button(master= window, command= Rock, text="Rock", font= 8)
paper= tk.Button(master= window, command= Paper, text= "Paper", font= 8)
scissors= tk.Button(master= window, command= Scisssors, text= "Scissors", font= 8)
rock.grid(row=0, column=0,columnspan=3,pady=2)
paper.grid(row=1, column=0,columnspan=3,pady=2)
scissors.grid(row=2, column=0, columnspan=3,pady=2)

#Photo Label Frame
playerLabelFrame= tk.LabelFrame(master=window, text="You",font= "12")
playerLabelFrame.grid(row=3,column=0, padx=5)
computerLabelFrame= tk.LabelFrame(master=window, text="Computer", font="12")
computerLabelFrame.grid(row=3,column=2,padx=5)

#Versus
versus= tk.Label(master= window,text="Vs",font=8)
versus.grid(row=3,column=1, padx=1)

#Photos
preRockImage=Image.open("rock.png")
newRock=preRockImage.resize((100,100), Image.ANTIALIAS)
rockImage=ImageTk.PhotoImage(newRock)

prePaperImage=Image.open("paper.png")
newPaper=prePaperImage.resize((100,100), Image.ANTIALIAS)
paperImage=ImageTk.PhotoImage(newPaper)

preScissorsImage=Image.open("scissors.png")
newScissors=preScissorsImage.resize((100,100), Image.ANTIALIAS)
scissorsImage=ImageTk.PhotoImage(newScissors)

playerShot= tk.Canvas(master=playerLabelFrame, height= 100, width=100)
playerShot.grid(row=3,column=0)

computerShot= tk.Canvas(master=computerLabelFrame,height=100,width=100)
computerShot.grid(row=3,column=1)

score = tk.Label(text="Your Score: {}\nComputer Score: {}".format(playerScore,computerScore), fon="5")
score.grid(row=4,column=0,columnspan=3)

window.mainloop()