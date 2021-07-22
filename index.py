import pygame
import turtle
import random
import math
import sys
import os
#from location import *
from tkinter import*
app = Tk()
app.geometry("890x480")
app.resizable(width=False, height=False)
app.title("voiture")
app.wm_iconbitmap('C:/Users/lenovo/Pictures/location-voiture/25834.png')
img = PhotoImage(file = 'C:/Users/lenovo/Pictures/location-voiture/25834.png')
canvas = Canvas(app, width=600, height=480)
canvas.create_image(250, 250, image=img)
canvas.grid()
def gestion():
    app.destroy()
    os.system('affichagelocation.py')

def createlocation():
    app.destroy()
    os.system('affichagelocation.py')
def createfacture():
    app.destroy()
    #os.system('affichagefacture.py')
    os.system('affichagefacture.py')   
def analyse():
    app.destroy()
    #root.destroy()
    os.system('analyse2.py')
def Acceuil():
    app.destroy()
    #root.destroy()
    os.system('app.py')

#canvas.create_text(320, 210, font=('batmfa.ttf', 45), text="Bienvenue sur", fill='white')
#canvas.create_text(320, 280, font=('batmfa.ttf', 35), text="Sky-Future", fill='red')
menubar = Menu(app)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer")
menu1.add_command(label="Editer")

menu1.add_separator()
menu1.add_command(label="Quitter", command=app.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos")
menubar.add_cascade(label="Aide", menu=menu3)

app.config(menu=menubar)
bouton_quit = Button(app, text='Acceuil', font='batmfa.ttf', command=Acceuil, padx=20, pady=10, cursor="target",bg="powder blue")
bouton_quit.place(x=610, y=400)

bouton_regle = Button(app, text='Gestion location', font='arial.ttf',command=createlocation, padx=20, pady=10, cursor="target",bg="powder blue")
bouton_regle.place(x=610, y=100)

bouton_regle = Button(app, text='Gestion facture', font='arial.ttf',command=createfacture, padx=20, pady=10, cursor="target",bg="powder blue")
bouton_regle.place(x=610, y=200)

bouton_analyse = Button(app, text='Statistique', font='arial.ttf',command=analyse, padx=20, pady=10, cursor="target",bg="powder blue")
bouton_analyse.place(x=610, y=300)

#bouton_analyse = Button(app, text='home', font='arial.ttf',command=analyse, padx=20, pady=10, cursor="target",bg="powder blue")
#bouton_analyse.place(x=610, y=30)

#bouton_start = Button(app, text='START', command=start, font='arial.ttf', padx=20, pady=10, cursor="target")
#bouton_start.place(x=610, y=100)


#root = Tk()
#l = GestionFacture(root)

app.mainloop()