from tkinter.constants import LEFT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import Frame, Label, StringVar, Toplevel, ttk
from tkinter import font
import tkinter.ttk as ttk
import tkinter.messagebox as mb 
from dbAgence import*
from fournisseur import Fournisseur
from voiture import Voiture
from PIL import ImageTk, Image
from PIL import *
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import winsound
LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage,GestionVoiture,GestionFournisseur,GestionSupprimer,GestionAjouter,GestionModifier,GestionChercher,GestionAjouterVoiture,GestionModifierVoiture,GestionSupprimerVoiture,GestionChercherVoiture,ExproterFournisseur,Visualisation):
			frame = F(container, self)
			# initializing frame of that object from
			
			# for loop
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
            
            

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
        

# first window frame startpage
class StartPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent,bg="lightblue")
            bg = ImageTk.PhotoImage(file = "voiture.png")
  
            bg_label = tk.Label(self, image = bg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.image = bg
            
            style = ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc",font=('Time New Roman', 10, 'bold'))
            
                
            # label of frame Layout 2
            label = ttk.Label(self, text ="Gestion d'agence de location de voiture", font = LARGEFONT,)
            
            # putting the grid in its place by using
            # grid
            label.grid(row = 0, column = 4, padx = 10, pady = 10)
            #label.configure(background="lightblue")
        
            button1 = ttk.Button(self, text ="Gestion Voiture",style="TButton", command = lambda : controller.show_frame(GestionVoiture))
        
            # putting the button in its place by
            # using grid
            button1.grid(row = 1, column = 1,ipady = 4,ipadx = 13,pady = 40)
            ## button to show frame 3 with text layout3
            button3 = ttk.Button(self, text ="Gestion Fournisseur",
            command = lambda : controller.show_frame(GestionFournisseur))
            button3.grid(row = 3, column = 1, ipady = 4,ipadx = 13,pady = 40)
            # putting the button in its place by
            # using grid
            button4 = ttk.Button(self, text ="Visualisation", style="TButton",command = lambda : controller.show_frame(Visualisation))
            button4.grid(row = 4, column = 1, ipady = 4,ipadx = 13,pady = 40)
            def home():
                self.destroy()
                os.system('mailing.py')
            def homemp():
                self.destroy()
                os.system('gestionEmployer.py')    
                 
            #bt=tk.Button(self, text="Play music", command= lambda: winsound.PlaySound("s.wav",winsound.SND_FILENAME))
            #bt.grid(row=5,column=1, padx = 10, pady = 10)
            btexit=ttk.Button(self, text="Gestion Location", style="TButton",command= home)
            btexit.grid(row=5,column=1,ipady = 5,ipadx = 13,pady = 40)
            btex=ttk.Button(self, text="Gestion Employer", style="TButton",command= homemp)
            btex.grid(row=6,column=1,ipady = 5,ipadx = 13,pady = 40)
        def quitter(self):  
            MsgBox = mb.askquestion('Exit Application', 'Voulez-vous  vraiment quitter !', icon='warning')  
            if MsgBox == 'yes':  
                Frame.destroy(self) 
       

# second window frame page1
class GestionVoiture(tk.Frame):
	
	def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            
            bg = ImageTk.PhotoImage(file = "v3.png")
  
            bg_label = tk.Label(self, image = bg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.image = bg
            
            #===============================Menu================================
            labelTitre = ttk.Label(self, text ="Menu Voiture: ", font=('Arial', 18, 'bold'))
            labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
            #labelTitre.configure(background="lightskyblue")
            #=======================Boutton ajouter
            ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Voiture",command= lambda : controller.show_frame(GestionAjouterVoiture))
            ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,pady=40)
            #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
            supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Voiture",command =   lambda : controller.show_frame(GestionSupprimerVoiture))
            supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,pady = 40)
            #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
            update_Fournisseur_btn = ttk.Button(self,text = "Modifier Voiture",command = lambda : controller.show_frame(GestionModifierVoiture))
            update_Fournisseur_btn.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)
            #======================boutton Chercher 
            btn_search = ttk.Button(self, text="Chercher Voiture",command= lambda : controller.show_frame(GestionChercherVoiture)) 
            btn_search.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)

            #======================Boutton exit
            btn_exit = ttk.Button(self, text="Accueil",command = lambda : controller.show_frame(StartPage))
            btn_exit.grid(row = 5,column = 0,ipady = 4,ipadx = 13,pady = 40)
#=========================================Interface ajouter voiture            
class GestionAjouterVoiture(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="mediumseagreen")
        bg = ImageTk.PhotoImage(file = "v3.png")
  
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        #root.config(bg='SteelBlue')
        self.matricule=tk.StringVar()
        self.modele=tk.StringVar()
        self.typeVoiture=tk.StringVar()
        self.nbrPlace=tk.IntVar()
        self.prix=tk.IntVar()
        self.quantite=tk.IntVar()
        
       
         #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Voiture: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="mediumseagreen")
        
        #=====================Boutton Supprimer
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Voiture",command =   lambda : controller.show_frame(GestionSupprimerVoiture))
        supp_Fournisseur_btn.grid(row = 1,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Voiture",command = lambda : controller.show_frame(GestionModifierVoiture))
        update_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Voiture",command= lambda : controller.show_frame(GestionChercherVoiture)) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)

        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Accueil",command = lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)

        
        #********************label*****************************************************   

        #============== id Fournisseur TEXTFIELD AND LABEL
        lblMat = ttk.Label(self, text="Matricule",font=('Time New Roman', 20, 'bold'))
        lblMat.grid(row = 1,column = 1,padx = 40,pady = 40)
        lblMat_field = ttk.Entry(self,textvariable = self.matricule)
        lblMat_field.grid(row = 1,column = 2,ipady = 7,ipadx = 5,padx = 5)
        #==============nom  TEXTFIELD AND LABEL
        lblModele = ttk.Label(self, text="Modele:",font=('Time New Roman', 20, 'bold'))  
        lblModele.grid(row = 1,column = 3,padx = 40,pady = 40)
        lblModele_field = ttk.Entry(self,textvariable = self.modele)
        lblModele_field.grid(row = 1,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #=======================prenom LABEL AND TEXTFIELD
        lblType = ttk.Label(self, text="Type de Voiture:",font=('Time New Roman', 20, 'bold'))
        lblType.grid(row = 1,column = 5,pady = 40)
        lblType_field = ttk.Entry(self,textvariable = self.typeVoiture)
        lblType_field.grid(row = 1,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=======================adresse LABEL AND TEXTFIELD
        lblNbrePlace = ttk.Label(self, text="Nombre de Place:",font=('Time New Roman', 20, 'bold'))
        lblNbrePlace.grid(row = 2,column = 1,pady = 40)
    
        lblNbrePlace_field = ttk.Entry(self,textvariable = self.nbrPlace)
        lblNbrePlace_field.grid(row = 2,column = 2,ipady = 7,ipadx = 20,padx = 20)
        #======================email LABEL AND TEXTFIELD
        lblPrix = ttk.Label(self, text="Prix:",font=('Time New Roman', 20, 'bold'))  
        lblPrix.grid(row = 2,column = 3,pady = 40)
       
        lblPrix_field = ttk.Entry(self,textvariable = self.prix)
        lblPrix_field.grid(row = 2,column = 4,ipady = 7,ipadx = 20,padx = 20)

        #======================email LABEL AND TEXTFIELD
        lblQuantite = ttk.Label(self, text="Quantite:",font=('Time New Roman', 20, 'bold'))  
        lblQuantite.grid(row = 2,column = 5,pady = 40)
        
        lblQuantite_field = ttk.Entry(self,textvariable = self.quantite)
        lblQuantite_field.grid(row = 2,column = 6,ipady = 7,ipadx = 20,padx = 20)

        #=========================Button=====================================================
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter",command= self.ajouter)
        ajout_Fournisseur_btn.grid(row=3,column=3,ipady=4,ipadx=13,pady=40)
        ajout_Fournisseur_btn=ttk.Button(self,text="Annuler",command= self.reset_values)
        ajout_Fournisseur_btn.grid(row=3,column=4,ipady=4,ipadx=13,pady=40)
        #========================Main Frame================================================
       
        s=ttk.Style().configure("T.Frame",bg="red")
        main_frame = ttk.Frame(self,style=s)
        main_frame.place(width = 800,height = 500,x = 200,y = 400)
    
        #main_frame.wm_attributes('-transparentcolor', '#ab23ff')
        
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "matricule",anchor='c')
        tree.heading("2",text = "modele",anchor='w')
        tree.heading("3",text = "typeVoiture",anchor='w')
        tree.heading("4",text="nbrePlace",anchor='w')
        tree.heading("5",text="prix",anchor='w')
        tree.heading("6",text="quantite",anchor='w')
        v=Voiture()
        rows=v.afficherVoiture()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
    #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
        self.matricule.set("")
        self.modele.set("")
        self.typeVoiture.set("")
        self.nbrPlace.set(0)
        self.prix.set(0)
        self.quantite.set(0)
    

    def ajouter(self):
        if self.matricule.get()=="" or self.modele.get()=="" or self.typeVoiture.get()=="" or self.nbrPlace.get()==0 or self.prix.get()==0 or self.quantite.get()==0:
            mb.showerror("Info","svp remplir les champs")
        else:
            voi=Voiture(self.matricule.get(),self.modele.get(),self.typeVoiture.get(),self.nbrPlace.get(),self.prix.get(),self.quantite.get())
            print("Fournisseur: ",voi.matricule)
            voi.ajouterVoiture()
            mb.showinfo("Info","ajoutation validé")
#=========================================Interface modifier voiture  =========================================================================          
class GestionModifierVoiture(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="mediumseagreen")
        #root.config(bg='SteelBlue')
        bg = ImageTk.PhotoImage(file = "v3.png")
  
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        self.matricule=tk.StringVar()
        self.modele=tk.StringVar()
        self.typeVoiture=tk.StringVar()
        self.nbrPlace=tk.IntVar()
        self.prix=tk.IntVar()
        self.quantite=tk.IntVar()
        
       
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Voiture: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="mediumseagreen")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Voiture",command= lambda : controller.show_frame(GestionAjouterVoiture))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,pady=40)
        #=====================Boutton Supprimer 
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Voiture",command =   lambda : controller.show_frame(GestionSupprimerVoiture))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,pady = 40)
    
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Voiture",command= lambda : controller.show_frame(GestionChercherVoiture)) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)

        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Accueil",command = lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)

        
        #********************label*****************************************************   

        #============== id Fournisseur TEXTFIELD AND LABEL
        lblMat = ttk.Label(self, text="Matricule",font=('Time New Roman', 20, 'bold'))
        lblMat.grid(row = 1,column = 1,padx = 40,pady = 40)

        lblMat_field = ttk.Entry(self,textvariable = self.matricule)
        lblMat_field.grid(row = 1,column = 2,ipady = 7,ipadx = 5,padx = 5)
        #==============nom  TEXTFIELD AND LABEL
        lblModele = ttk.Label(self, text="Modele:",font=('Time New Roman', 20, 'bold'))  
        lblModele.grid(row = 1,column = 3,padx = 40,pady = 40)
       
        lblModele_field = ttk.Entry(self,textvariable = self.modele)
        lblModele_field.grid(row = 1,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #=======================prenom LABEL AND TEXTFIELD
        lblType = ttk.Label(self, text="Type de Voiture:",font=('Time New Roman', 20, 'bold'))
        lblType.grid(row = 1,column = 5,pady = 40)
        
        lblType_field = ttk.Entry(self,textvariable = self.typeVoiture)
        lblType_field.grid(row = 1,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=======================adresse LABEL AND TEXTFIELD
        lblNbrePlace = ttk.Label(self, text="Nombre de Place:",font=('Time New Roman', 20, 'bold'))
        lblNbrePlace.grid(row = 2,column = 1,pady = 40)
        
        lblNbrePlace_field = ttk.Entry(self,textvariable = self.nbrPlace)
        lblNbrePlace_field.grid(row = 2,column = 2,ipady = 7,ipadx = 20,padx = 20)
        #======================email LABEL AND TEXTFIELD
        lblPrix = ttk.Label(self, text="Prix:",font=('Time New Roman', 20, 'bold'))  
        lblPrix.grid(row = 2,column = 3,pady = 40)
        
        lblPrix_field = ttk.Entry(self,textvariable = self.prix)
        lblPrix_field.grid(row = 2,column = 4,ipady = 7,ipadx = 20,padx = 20)

        #======================email LABEL AND TEXTFIELD
        lblQuantite = ttk.Label(self, text="Quantite:",font=('Time New Roman', 20, 'bold'))  
        lblQuantite.grid(row = 2,column = 5,pady = 40)
       
        lblQuantite_field = ttk.Entry(self,textvariable = self.quantite)
        lblQuantite_field.grid(row = 2,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=========================Button=====================================================
        ajout_Fournisseur_btn=ttk.Button(self,text="Modifier",command= self.modifier)
        ajout_Fournisseur_btn.grid(row=3,column=3,ipady=4,ipadx=13,pady=40)
        ajout_Fournisseur_btn=ttk.Button(self,text="Annuler",command= self.reset_values)
        ajout_Fournisseur_btn.grid(row=3,column=4,ipady=4,ipadx=13,pady=40)
        #========================Main Frame================================================
        main_frame = ttk.Frame(self)
        main_frame.place(width = 800,height = 500,x = 200,y = 400)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "matricule",anchor='c')
        tree.heading("2",text = "modele",anchor='w')
        tree.heading("3",text = "typeVoiture",anchor='w')
        tree.heading("4",text="nbrePlace",anchor='w')
        tree.heading("5",text="prix",anchor='w')
        tree.heading("6",text="quantite",anchor='w')
        v=Voiture()
        rows=v.afficherVoiture()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
    #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
        self.matricule.set("")
        self.modele.set("")
        self.typeVoiture.set("")
        self.nbrPlace.set(0)
        self.prix.set(0)
        self.quantite.set(0)
    def modifier(self):
        if self.matricule.get()=="" or self.modele.get()=="" or self.typeVoiture.get()=="" or self.nbrPlace.get()==0 or self.prix.get()==0 or self.quantite.get()==0:
            mb.showerror("Info","svp remplir les champs")
        else:
            voi=Voiture()
            voi.modifierVoiture(self.matricule.get(),self.modele.get(),self.typeVoiture.get(),self.nbrPlace.get(),self.prix.get(),self.quantite.get())
            mb.showinfo("Info","modification validé")
    

    
#=================================================Interface Supprimer=========================================================================
class GestionSupprimerVoiture(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="tomato")
        bg = ImageTk.PhotoImage(file = "v3.png")
  
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        main_frame = ttk.Frame(self)
        main_frame.place(width = 200,height = 200,x = 200,y = 400)
        self.matriculeSupp=StringVar()
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Voiture: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="tomato")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Voiture",command= lambda : controller.show_frame(GestionAjouterVoiture))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,pady=40)
        
        #=====================Boutton modifier 
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Voiture",command = lambda : controller.show_frame(GestionModifierVoiture))
        update_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Voiture",command= lambda : controller.show_frame(GestionChercherVoiture)) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)

        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Accueil",command = lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)

        
        #********************label*****************************************************   

        #============== id Fournisseur TEXTFIELD AND LABEL
        lblMat = ttk.Label(self, text="Matricule",font=('Time New Roman', 20, 'bold'))
        lblMat.grid(row = 1,column = 1,padx = 40,pady = 40)
        #lblMat.configure(background="tomato")
        lblMat_field = ttk.Entry(self,textvariable = self.matriculeSupp)
        lblMat_field.grid(row = 1,column = 2,ipady = 7,ipadx = 5,padx = 5)
        #=======================boutton==========================================
        supp_voiture_btn = ttk.Button(self,text = "Supprimer ",command = self.supprimer)
        supp_voiture_btn.grid(row = 2,column = 4,ipady = 4,ipadx = 13,pady = 40)
        annuler_btn=ttk.Button(self,text = "Annuler",command = self.reset_values)
        annuler_btn.grid(row = 2,column =5 ,ipady = 5,ipadx = 13,pady = 40)

         #========================Main Frame================================================
        main_frame = ttk.Frame(self)
        main_frame.place(width = 800,height = 500,x = 200,y = 400)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "matricule",anchor='c')
        tree.heading("2",text = "modele",anchor='w')
        tree.heading("3",text = "typeVoiture",anchor='w')
        tree.heading("4",text="nbrePlace",anchor='w')
        tree.heading("5",text="prix",anchor='w')
        tree.heading("6",text="quantite",anchor='w')
        v=Voiture()
        rows=v.afficherVoiture()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
    #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
       self.matriculeSupp.set("")
    def supprimer(self):
        if self.matriculeSupp.get()=="" :
            mb.showerror("Info","svp remplir les champs")
        
        else:
            v = Voiture()
            v.supprimerVoiture(self.matriculeSupp.get())
            mb.showinfo("Info","suppression validé")    
     
#=========================================Interface Chercher voiture===============================================================
class GestionChercherVoiture(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="turquoise")
        bg = ImageTk.PhotoImage(file = "v3.png")
  
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        main_frame = ttk.Frame(self)
        main_frame.place(width = 600,height = 500,x = 200,y = 300)
        
        self.matriculeCherche=tk.StringVar()
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Voiture: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="turquoise")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Voiture",command= lambda : controller.show_frame(GestionAjouterVoiture))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,pady=40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Voiture",command =   lambda : controller.show_frame(GestionSupprimerVoiture))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Voiture",command = lambda : controller.show_frame(GestionModifierVoiture))
        update_Fournisseur_btn.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)
        

        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Accueil",command = lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)

        
        #********************label*****************************************************   

        #============== matricule voiture TEXTFIELD AND LABEL
        lblMat = ttk.Label(self, text="Matricule",font=('Time New Roman', 20, 'bold'))
        lblMat.grid(row = 1,column = 3,padx = 40,pady = 40)
        #lblMat.configure(background="turquoise")
        lblMat_field = ttk.Entry(self,textvariable = self.matriculeCherche)
        lblMat_field.grid(row = 1,column = 4,ipady = 7,ipadx = 5,padx = 5)
        #=======================boutton=========================================

        Search_FournisseurId_btn = ttk.Button(self,text = "Chercher ",command = self.chercher)
        Search_FournisseurId_btn.grid(row = 2,column = 4,ipady = 4,ipadx = 13,pady = 40)
        annuler_btn=ttk.Button(self,text = "Annuler",command = self.reset_values)
        annuler_btn.grid(row = 2,column =5 ,ipady = 4,ipadx = 13,pady = 40)
          #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
       self.matriculeCherche.set(0)

   
    
    def chercher(self):
        #self.root.title("Fournisseur Management(Details)")
        #==========================Show Frame================================
        #===========================label 
        main_frame = ttk.Frame(self)
        main_frame.place(width = 600,height = 500,x = 200,y = 300)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "matricule",anchor='c')
        tree.heading("2",text = "modele",anchor='w')
        tree.heading("3",text = "typeVoiture",anchor='w')
        tree.heading("4",text="nbrPlace",anchor='w')
        tree.heading("5",text="prix",anchor='w')
        tree.heading("6",text="Quantite",anchor='w')
    
        v=Voiture()
        rows=v.chercherVoiture(self.matriculeCherche.get())
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
#=========================================Gestion Fournisseur =====================================================================
class GestionFournisseur(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="lightblue")
        bg = ImageTk.PhotoImage(file = "v6.jpg")
  
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        #root.config(bg='SteelBlue')
        self.idFour=tk.StringVar()
        self.nomFour=tk.StringVar()
        self.prenomFour=tk.StringVar()
        self.adresseFour=tk.StringVar()
        self.email=tk.StringVar()
        self.numTel=tk.IntVar()
        self.idSearch=tk.StringVar()
        self.idFourSupp=tk.StringVar()
       
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Fournisseur: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="lightblue")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Fournisseur",command= lambda : controller.show_frame(GestionAjouter))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,padx=10,pady=40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Fournisseur",command =   lambda : controller.show_frame(GestionSupprimer))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Fournisseur",command = lambda : controller.show_frame(GestionModifier))
        update_Fournisseur_btn.grid(row = 3,column = 0,ipady = 4,ipadx = 13,padx=10,pady = 20)
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Fournisseur",command= lambda : controller.show_frame(GestionChercher)) 
        btn_search.grid(row = 4,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================boutton exporter 
        btn_exporter= ttk.Button(self, text="Exporter",command= lambda : controller.show_frame(ExproterFournisseur)) 
        btn_exporter.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 6,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        

#======================================Interface Ajouter======================================================================
class GestionAjouter(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent)
        #root.config(bg='SteelBlue')
        bg = ImageTk.PhotoImage(file = "v6.jpg")
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        self.idFour=tk.StringVar()
        self.nomFour=tk.StringVar()
        self.prenomFour=tk.StringVar()
        self.adresseFour=tk.StringVar()
        self.email=tk.StringVar()
        self.numTel=tk.IntVar()
    
       
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Fournisseur: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="lightblue")
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Fournisseur",command =   lambda : controller.show_frame(GestionSupprimer))
        supp_Fournisseur_btn.grid(row = 1,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Fournisseur",command = lambda : controller.show_frame(GestionModifier))
        update_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,padx=10,pady = 20)
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Fournisseur",command= lambda : controller.show_frame(GestionChercher)) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================boutton exporter 
        btn_exporter= ttk.Button(self, text="Exporter",command= lambda : controller.show_frame(ExproterFournisseur)) 
        btn_exporter.grid(row = 4,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        

        
        #********************label*****************************************************   

        #============== id Fournisseur TEXTFIELD AND LABEL
        lblId = ttk.Label(self, text="Id",font=('Time New Roman', 20, 'bold'))
        lblId.grid(row = 1,column = 1,padx = 40,pady = 40)
        #lblId.configure(background="mediumseagreen")
        lblId_field = ttk.Entry(self,textvariable = self.idFour)
        lblId_field.grid(row = 1,column = 2,ipady = 7,ipadx = 5,padx = 5)
        #==============nom  TEXTFIELD AND LABEL
        lblNom = ttk.Label(self, text="Nom:",font=('Time New Roman', 20, 'bold'))  
        lblNom.grid(row = 1,column = 3,padx = 40,pady = 40)
        #lblNom.configure(background="mediumseagreen")
        lblNom_field = ttk.Entry(self,textvariable = self.nomFour)
        lblNom_field.grid(row = 1,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #=======================prenom LABEL AND TEXTFIELD
        lblPrenom = ttk.Label(self, text="Prenom:",font=('Time New Roman', 20, 'bold'))
        lblPrenom.grid(row = 1,column = 5,pady = 40)
        #lblPrenom.configure(background="mediumseagreen")
        lblPrenom_field = ttk.Entry(self,textvariable = self.prenomFour)
        lblPrenom_field.grid(row = 1,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=======================adresse LABEL AND TEXTFIELD
        lblAdd = ttk.Label(self, text="adresse:",font=('Time New Roman', 20, 'bold'))
        lblAdd.grid(row = 2,column = 1,pady = 40)
        #lblAdd.configure(background="mediumseagreen")
        lblAdd_field = ttk.Entry(self,textvariable = self.adresseFour)
        lblAdd_field.grid(row = 2,column = 2,ipady = 7,ipadx = 20,padx = 20)
        #======================email LABEL AND TEXTFIELD
        lblEmail = ttk.Label(self, text="email:",font=('Time New Roman', 20, 'bold'))  
        lblEmail.grid(row = 2,column = 3,pady = 40)
        #lblEmail.configure(background="mediumseagreen")
        lblEmail_field = ttk.Entry(self,textvariable = self.email)
        lblEmail_field.grid(row = 2,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #======================num Tel LABEL AND TEXTFIELD
        lblNumTel = ttk.Label(self, text="Num Tel:",font=('Time New Roman', 20, 'bold'))    
        lblNumTel.grid(row = 2,column = 5,pady = 40)
        #lblNumTel.configure(background="mediumseagreen")
        lblNumTel_field = ttk.Entry(self,textvariable = self.numTel)
        lblNumTel_field.grid(row = 2,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=========================Button=====================================================
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter",command= self.ajouter)
        ajout_Fournisseur_btn.grid(row=3,column=3,ipady=4,ipadx=13,pady=40)
        ajout_Fournisseur_btn=ttk.Button(self,text="Annuler",command= self.reset_values)
        ajout_Fournisseur_btn.grid(row=3,column=4,ipady=4,ipadx=13,pady=40)
        #========================Main Frame================================================
        main_frame = ttk.Frame(self)
        main_frame.place(width = 800,height = 500,x = 200,y = 400)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
        f=Fournisseur()
        rows=f.afficherFournisseur()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
    #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
        self.idFour.set("")
        self.nomFour.set("")
        self.prenomFour.set("")
        self.adresseFour.set("")
        self.email.set("")
        self.numTel.set(0)
    
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
        if MsgBox == 'yes':  
            Frame.destroy(self)  

    def ajouter(self):
        if self.idFour.get()=="" or self.nomFour.get()=="" or self.prenomFour.get()=="" or self.adresseFour.get()=="" or self.email.get()=="" or self.numTel.get()==0:
            mb.showerror("Info","svp remplir les champs")
        else:
            four=Fournisseur(self.idFour.get(),self.nomFour.get(),self.prenomFour.get(),self.adresseFour.get(),self.email.get(),self.numTel.get())
            print("Fournisseur: ",four.idFour)
            four.ajouterFournisseur()
            mb.showinfo("Info","ajoutation validé")
#=======================================================Interface supprimer===========================================================================
class GestionSupprimer(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="tomato")
        bg = ImageTk.PhotoImage(file = "v6.jpg")
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        main_frame = ttk.Frame(self)
        main_frame.place(width = 200,height = 200,x = 200,y = 400)
        
        self.idFourSupp=tk.StringVar()
        self.idFour=tk.StringVar()
        self.nomFour=tk.StringVar()
        self.prenomFour=tk.StringVar()
        self.adresseFour=tk.StringVar()
        self.email=tk.StringVar()
        self.numTel=tk.IntVar()
        self.idSearch=tk.StringVar()
        self.idFourSupp=tk.StringVar()
       
       #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Fournisseur: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="lightblue")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Fournisseur",command= lambda : controller.show_frame(GestionAjouter))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,padx=10,pady=40)
       
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Fournisseur",command = lambda : controller.show_frame(GestionModifier))
        update_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,padx=10,pady = 20)
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Fournisseur",command= lambda : controller.show_frame(GestionChercher)) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================boutton exporter 
        btn_exporter= ttk.Button(self, text="Exporter",command= lambda : controller.show_frame(ExproterFournisseur)) 
        btn_exporter.grid(row = 4,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        


        #============== id Fournisseur Supprimer TEXTFIELD AND LABEL
        lblIdSupp = ttk.Label(self, text="Id",font=('Time New Roman', 20, 'bold'))
        lblIdSupp.grid(row = 1,column = 3,padx = 40,pady = 40)
        
        lblIdSupp_field = ttk.Entry(self,textvariable = self.idFourSupp)
        lblIdSupp_field.grid(row = 1,column = 4,ipady = 7,ipadx = 5,padx = 5)

        supp_FournisseurId_btn = ttk.Button(self,text = "Supprimer ",command = self.supprimer)
        supp_FournisseurId_btn.grid(row = 2,column = 4,ipady = 4,ipadx = 13,pady = 40)

        annuler_btn=ttk.Button(self,text = "Annuler",command = self.reset_values)
        annuler_btn.grid(row = 2,column =5 ,ipady = 5,ipadx = 13,pady = 40)
         #========================Main Frame================================================
        main_frame = ttk.Frame(self)
        main_frame.place(width = 800,height = 500,x = 200,y = 300)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
        f=Fournisseur()
        rows=f.afficherFournisseur()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
    #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
       self.idFourSupp.set("")
    def supprimer(self):
        if self.idFourSupp.get()=="" :
            mb.showerror("Info","svp remplir les champs")
        else:
            f = Fournisseur()
            f.supprimerFournisseur(self.idFourSupp.get())
            mb.showinfo("Info","suppression validé")    
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
        if MsgBox == 'yes':  
            Frame.destroy(self)  
    
#=======================================Interface modifier===============================================================
class GestionModifier(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="mediumseagreen")
        #root.config(bg='SteelBlue')
        bg = ImageTk.PhotoImage(file = "v6.jpg")
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        self.idFour=tk.StringVar()
        self.nomFour=tk.StringVar()
        self.prenomFour=tk.StringVar()
        self.adresseFour=tk.StringVar()
        self.email=tk.StringVar()
        self.numTel=tk.IntVar()
        self.idSearch=tk.StringVar()
        self.idFourSupp=tk.StringVar()
       
      #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Fournisseur: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="lightblue")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Fournisseur",command= lambda : controller.show_frame(GestionAjouter))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,padx=10,pady=40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Fournisseur",command =   lambda : controller.show_frame(GestionSupprimer))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Fournisseur",command= lambda : controller.show_frame(GestionChercher)) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================boutton exporter 
        btn_exporter= ttk.Button(self, text="Exporter",command= lambda : controller.show_frame(ExproterFournisseur)) 
        btn_exporter.grid(row = 4,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        


        
        #********************label*****************************************************   

        #============== id Fournisseur TEXTFIELD AND LABEL
        lblId = ttk.Label(self, text="Id",font=('Time New Roman', 20, 'bold'))
        lblId.grid(row = 1,column = 1,padx = 40,pady = 40)
        
        lblId_field = ttk.Entry(self,textvariable = self.idFour)
        lblId_field.grid(row = 1,column = 2,ipady = 7,ipadx = 5,padx = 5)
        #==============nom  TEXTFIELD AND LABEL
        lblNom = ttk.Label(self, text="Nom:",font=('Time New Roman', 20, 'bold'))  
        lblNom.grid(row = 1,column = 3,padx = 40,pady = 40)
        
        lblNom_field = ttk.Entry(self,textvariable = self.nomFour)
        lblNom_field.grid(row = 1,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #=======================prenom LABEL AND TEXTFIELD
        lblPrenom = ttk.Label(self, text="Prenom:",font=('Time New Roman', 20, 'bold'))
        lblPrenom.grid(row = 1,column = 5,pady = 40)
        
        lblPrenom_field = ttk.Entry(self,textvariable = self.prenomFour)
        lblPrenom_field.grid(row = 1,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=======================adresse LABEL AND TEXTFIELD
        lblAdd = ttk.Label(self, text="adresse:",font=('Time New Roman', 20, 'bold'))
        lblAdd.grid(row = 2,column = 1,pady = 40)
        
        lblAdd_field = ttk.Entry(self,textvariable = self.adresseFour)
        lblAdd_field.grid(row = 2,column = 2,ipady = 7,ipadx = 20,padx = 20)
        #======================email LABEL AND TEXTFIELD
        lblEmail = ttk.Label(self, text="email:",font=('Time New Roman', 20, 'bold'))  
        lblEmail.grid(row = 2,column = 3,pady = 40)
        
        lblEmail_field = ttk.Entry(self,textvariable = self.email)
        lblEmail_field.grid(row = 2,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #======================num Tel LABEL AND TEXTFIELD
        lblNumTel = ttk.Label(self, text="Num Tel:",font=('Time New Roman', 20, 'bold'))    
        lblNumTel.grid(row = 2,column = 5,pady = 40)
        
        lblNumTel_field = ttk.Entry(self,textvariable = self.numTel)
        lblNumTel_field.grid(row = 2,column = 6,ipady = 7,ipadx = 20,padx = 20)

        #=========================Button=====================================================
        ajout_Fournisseur_btn=ttk.Button(self,text="Modifier",command= self.modifier)
        ajout_Fournisseur_btn.grid(row=3,column=3,ipady=4,ipadx=13,pady=40)
        ajout_Fournisseur_btn=ttk.Button(self,text="Annuler",command= self.reset_values)
        ajout_Fournisseur_btn.grid(row=3,column=4,ipady=4,ipadx=13,pady=40)
        #========================Main Frame================================================
        main_frame = ttk.Frame(self)
        main_frame.place(width = 800,height = 500,x = 200,y = 400)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
        f=Fournisseur()
        rows=f.afficherFournisseur()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Voulez-vous quitter', icon='warning')  
        if MsgBox == 'yes':  
            Frame.destroy(self)  
    #Fonction de modification d"un fournisseur sera appelée dans le boutton "modifier"
    def modifier(self):
        if self.idFour.get()=="" or self.nomFour.get()=="" or self.prenomFour.get()=="" or self.adresseFour.get()=="" or self.email.get()=="" or self.numTel.get()==0:
            mb.showerror("Info","svp remplir les champs")
        else:
            four=Fournisseur()
            four.modifierFournisseur(self.idFour.get(),self.nomFour.get(),self.prenomFour.get(),self.adresseFour.get(),self.email.get(),int(self.numTel.get()))
            mb.showinfo("Info","modification validé")
    def reset_values(self):
        self.idFour.set("")
        self.nomFour.set("")
        self.prenomFour.set("")
        self.adresseFour.set("")
        self.email.set("")
        self.numTel.set(0)
#==========================================Interface chercher==============================================================
class GestionChercher(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent)
        bg = ImageTk.PhotoImage(file = "v6.jpg")
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        main_frame = ttk.Frame(self)
        main_frame.place(width = 600,height = 500,x = 200,y = 300)
        
        self.idSearch=tk.StringVar()
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Fournisseur: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="lightblue")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Fournisseur",command= lambda : controller.show_frame(GestionAjouter))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,padx=10,pady=40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Fournisseur",command =   lambda : controller.show_frame(GestionSupprimer))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Fournisseur",command = lambda : controller.show_frame(GestionModifier))
        update_Fournisseur_btn.grid(row = 3,column = 0,ipady = 4,ipadx = 13,padx=10,pady = 20)
        
        #======================boutton exporter 
        btn_exporter= ttk.Button(self, text="Exporter",command= lambda : controller.show_frame(ExproterFournisseur)) 
        btn_exporter.grid(row = 4,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        

        #============== id Fournisseur Supprimer TEXTFIELD AND LABEL
        lblIdSearch = ttk.Label(self, text="Id",font=('Time New Roman', 20, 'bold'))
        lblIdSearch.grid(row = 1,column = 3,padx = 40,pady = 40)
        
        lblIdSearch_field = ttk.Entry(self,textvariable = self.idSearch)
        lblIdSearch_field.grid(row = 1,column = 4,ipady = 7,ipadx = 5,padx = 5)

        Search_FournisseurId_btn = ttk.Button(self,text = "Chercher ",command = self.chercher)
        Search_FournisseurId_btn.grid(row = 2,column = 4,ipady = 4,ipadx = 13,pady = 40)

        annuler_btn=ttk.Button(self,text = "Annuler",command = self.reset_values)
        annuler_btn.grid(row = 2,column =5 ,ipady = 4,ipadx = 13,pady = 40)
          #fonction reset values permet d'initialiser les champs à 0
    def reset_values(self):
       self.idSearch.set("")

    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Voulez-vous quitter', icon='warning')  
        if MsgBox == 'yes':  
            Frame.destroy(self)  
    
    def chercher(self):
        #self.root.title("Fournisseur Management(Details)")
        #==========================Show Frame================================
        #===========================label 
        main_frame = ttk.Frame(self)
        main_frame.place(width = 600,height = 500,x = 200,y = 300)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
    
        f=Fournisseur()
        rows=f.chercherFournisseur(self.idSearch.get())
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
class ExproterFournisseur(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent,bg="lightblue")
        bg = ImageTk.PhotoImage(file = "v6.jpg")
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
        #root.config(bg='SteelBlue')
        self.idFour=tk.StringVar()
        self.nomFour=tk.StringVar()
        self.prenomFour=tk.StringVar()
        self.adresseFour=tk.StringVar()
        self.email=tk.StringVar()
        self.numTel=tk.IntVar()
        self.idSearch=tk.StringVar()
        self.idFourSupp=tk.StringVar()
       
        #===============================Menu================================
        labelTitre = ttk.Label(self, text ="Menu Fournisseur: ", font=('Arial', 15, 'bold'))
        labelTitre.grid(row = 0, column = 0, padx = 10, pady = 10)
        #labelTitre.configure(background="lightblue")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Ajouter Fournisseur",command= lambda : controller.show_frame(GestionAjouter))
        ajout_Fournisseur_btn.grid(row=1,column=0,ipady=4,ipadx=13,padx=10,pady=40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "Supprimer Fournisseur",command =   lambda : controller.show_frame(GestionSupprimer))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        update_Fournisseur_btn = ttk.Button(self,text = "Modifier Fournisseur",command = lambda : controller.show_frame(GestionModifier))
        update_Fournisseur_btn.grid(row = 3,column = 0,ipady = 4,ipadx = 13,padx=10,pady = 20)
        #======================boutton Cherhcher 
        btn_search = ttk.Button(self, text="Chercher Fournisseur",command= lambda : controller.show_frame(GestionChercher)) 
        btn_search.grid(row = 4,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        
        #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx=10,pady=20)
        

        def save_csv(rows):
            header=["idFournisseur","nom","prenom","adresse","email","num Tel"]
            
            with open('fournisseur.csv','w') as f:
                w=csv.writer(f,dialect="excel")
                w.writerow(header)
                w.writerows(rows)
    
            mb.showinfo("Info","Exporté validé")
            
         #========================Main Frame================================================
        main_frame = ttk.Frame(self)
        main_frame.place(width = 800,height = 500,x = 250,y = 80)
        tree = ttk.Treeview(main_frame,height = 100)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = 'right',fill = 'y')
        tree.pack(side = 'top',fill = 'x')
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
        f=Fournisseur()
        rows=f.afficherFournisseur()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
        #======================boutton exporter 
        btn_exporter= ttk.Button(self, text="Exporter",command= lambda : save_csv(rows)) 
        btn_exporter.grid(row = 0,column = 3,ipady = 4,ipadx = 13,padx=10,pady=20)
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
        if MsgBox == 'yes':  
            Frame.destroy(self)  
    

import plotly.express as px
import pandas as pd
import plotly as py
import plotly.graph_objs as go
class Visualisation(tk.Frame):
    def __init__(self,parent, controller): 
        tk.Frame.__init__(self, parent)
        bg = ImageTk.PhotoImage(file = "vis.png")
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg
       
        
        #labelTitre.configure(background="lightblue")
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=ttk.Button(self,text="Statistique Fournisseur")
        ajout_Fournisseur_btn.grid(row=0,column=2,ipady=4,ipadx=13,padx=30,pady=50)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = ttk.Button(self,text = "statistique  voiture",command =self.graph)
        supp_Fournisseur_btn.grid(row = 0,column = 3,ipady = 4,ipadx = 13,padx=30,pady=50)
         #======================Boutton exit
        btn_exit = ttk.Button(self, text="Retour",command= lambda : controller.show_frame(StartPage))
        btn_exit.grid(row = 0,column = 4,ipady = 4,ipadx = 13,padx=30,pady=50)
    def graph(self):
        v=Voiture()
        rows=v.ModQte()
        str(rows)
        resQte=v.QuantiteVoiture()
        resMod=v.ModeleVoiture()
        #self.resModele=v.ModeleVoiture()
        self.modeles=[]
        self.quantites=[]
        for i in resQte:
            self.quantites.append(i)
        for j in resMod:
            self.modeles.append(j)
        #mod=np.random.normal(self.modeles)
        qte=np.random.normal(self.quantites)
        #mod=np.array(self.modeles)
        plt.bar(qte, 5)
        plt.ylim(0, 5)
        plt.xlabel("Modele Voiture")
        plt.ylabel("Quantite Voiture")
        plt.title("Information Voiture")
        plt.show()

        '''plt.bar(500, 200,250)
        plt.ylim(0, 5)
        plt.xlabel("Modele Voiture")
        plt.ylabel("Quantite Voiture")
        plt.title("Information Voiture")
        plt.show()'''

# Driver Code
app = tkinterApp()
app.mainloop()
