from tkinter import *
from implementation_classe import *
import tkinter.ttk as ttk
from tkcalendar import Calendar, DateEntry  
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import sys
import csv
import os
class GestionLocation():
    def __init__(self,root):
        self.root = root

        self.root.geometry("1000x500")
        self.root.title("GestionLocation")
        self.id_l=IntVar()
        self.description=StringVar()
        self.date_debut=StringVar()
        self.date_fin=StringVar()
        self.prix_loc=DoubleVar()
        self.search=IntVar()
        self.v=StringVar()

        def home():
            root.destroy()
            os.system('index.py')
        # Add Some Style
        # Add some style
        style = ttk.Style()
#Pick a theme
        style.theme_use("default")
# Configure our treeview colors

        style.configure("Treeview", 
        	background="#D3D3D3",
        	foreground="black",
        	rowheight=25,
        	fieldbackground="#D3D3D3"
    	)
# Change selected color
        style.map('Treeview', 
        	background=[('selected', 'blue')])

# Create Treeview Frame
        tree_frame = Frame(root)
        tree_frame.pack(pady=20)

# Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the screen
        my_tree.pack()

#Configure the scrollbar
        tree_scroll.config(command=my_tree.yview)

# Define Our Columns
        my_tree['columns'] = ("Id", "Description", "Date Debut","Date Fin","Prix")

# Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Id", anchor=W, width=140)
        my_tree.column("Description", anchor=CENTER, width=100)
        my_tree.column("Date Debut", anchor=W, width=140)
        my_tree.column("Date Fin", anchor=W, width=140)
        my_tree.column("Prix", anchor=W, width=140)

# Create Headings 
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Id", text="Id", anchor=W)
        my_tree.heading("Description", text="Description", anchor=CENTER)
        my_tree.heading("Date Debut", text="Date Debut", anchor=W)
        my_tree.heading("Date Fin", text="Date Fin", anchor=W)
        my_tree.heading("Prix", text="Prix", anchor=W)



# Create striped row tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        global count
        count=0
        L = Location_v()
        data=L.afficherLocation_v()

        for record in data:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))
                count += 1

        add_frame = LabelFrame(root, text="Formulaire",bg="powder blue")
        add_frame.pack(fill="x", expand="yes", padx=20)

#Labels
        Id = Label(add_frame, text="Id")
        Id.grid(row=0, column=0)
 
        Description = Label(add_frame, text="Description")
        Description.grid(row=0, column=2)

        Date_debut = Label(add_frame, text="Date debut")
        Date_debut.grid(row=0, column=4)

        date_fin = Label(add_frame, text="Date Fin")
        date_fin .grid(row=0, column=6)

        prix = Label(add_frame, text="Prix")
        prix.grid(row=0, column=8)

      

#Entry boxes
        Id_box = Entry(add_frame,textvariable = self.id_l)
        Id_box.grid(row=0, column=1)

        Description_box = Entry(add_frame,textvariable = self.description)
        Description_box.grid(row=0, column=3)

        Date_debut_box = DateEntry(add_frame,textvariable =self.date_debut)
        Date_debut_box.grid(row=0, column=5)

        Date_fin_box = DateEntry(add_frame,textvariable =self.date_fin)
        Date_fin_box.grid(row=0, column=7)

        prix_box = Entry(add_frame,textvariable = self.prix_loc)
        prix_box.grid(row=0, column=9)
        prix_box = Entry(add_frame,textvariable = self.prix_loc)
        prix_box.grid(row=0, column=9)

# Add Record
        def add_record():
            my_tree.tag_configure('oddrow', background="white")
            my_tree.tag_configure('evenrow', background="lightblue")
            global count
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(Id_box.get(), Description_box.get(), Date_debut.get(),Date_fin_box.get(),prix_box.get()), tags=('evenrow',))

            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(Id_box.get(), Description_box.get(), Date_debut.get(),Date_fin_box.get(),prix_box.get()), tags=('oddrow',))
                count += 1

	# Clear the boxes
            Id_box.delete(0, END)
            Description_box.delete(0, END)
            Date_debut_box.delete(0, END)
            Date_fin_box.delete(0, END)
            prix_box.delete(0, END)
	        
	        
	        
            
            

# Remove all records
        def remove_all():
            for record in my_tree.get_children():
                my_tree.delete(record)
	
		#Fonction d'ajout d'un étudiant (sera appelée dérière le boutton "Ajouter"
        

        

# Remove one selected
        def remove_one():
            x = my_tree.selection()[0]
            my_tree.delete(x)
	
	        

# Remove many selected
        def remove_many():
            x = my_tree.selection()
            for record in x:
                my_tree.delete(record)
	
	
		

# Select Record
        def select_record():
            Id_box.delete(0, END)
            Description_box.delete(0, END)
            Date_debut_box.delete(0, END)
            Date_fin_box.delete(0, END)
            prix_box.delete(0, END)
            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')
            Id_box.insert(0, values[0])
            Description_box.insert(0, values[1])
            Date_debut_box.insert(0, values[2])
            Date_fin_box.insert(0, values[3])
            prix_box.insert(0, values[4])
	        
	        
            
            
	        
	        
            
            


	# Grab record number
	        
	# Grab record values
	        

	#temp_label.config(text=values[0])

	# output to entry boxes
	         


# Save updated record
        def update_record():
            selected = my_tree.focus()
            my_tree.item(selected, text="", values=(Id_box.get(), Description_box.get(), Date_debut.get(),Date_fin_box.get(),prix_box.get()))
            Id_box.delete(0, END)
            Description_box.delete(0, END)
            Date_debut_box.delete(0, END)
            Date_fin_box.delete(0, END)
            prix_box.delete(0, END)
	# Grab record number
	
	# Save new data
	        

	# Clear entry boxes
	        
	        
	        
            
            

# Create Binding Click function
        def clicker(e):
            select_record()
	

# Move Row up
        def up():
            rows = my_tree.selection()
            for row in rows:
                my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
	
	        
                
		

# Move Row Down
        def down():
            rows = my_tree.selection()
            for row in reversed(rows):
                my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)


            

                    
            
        #print("Location_v: ",E.nom)
        def save_csv(data):
                header=["id","date debut","date fin","prix"]
                with open("location33.csv","w")as f:
                        
                        w=csv.writer(f,dialect="excel") 
                        w.writerow(header)
                        w.writerows(data)
             
                 
        
        
                               
        def createmail():
                root.destroy()
                os.system('mail.py')
    
              
		



#Buttons
        button_frame = LabelFrame(root, text="Commands",bg="powder blue")
        button_frame.pack(fill="x", expand="yes", padx=20)

        update_button = Button(button_frame, text="modifier",command=self.update,bg="powder blue")
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = Button(button_frame, text="ajouter",command=self.add,bg="powder blue")
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_all_button = Button(button_frame, text="supprimer",command=self.remove,bg="powder blue")
        remove_all_button.grid(row=0, column=2, padx=10, pady=10)

        remove_one_button = Button(button_frame, text="reset",command=self.Reset,bg="powder blue")
        remove_one_button.grid(row=0, column=3, padx=10, pady=10)

        

        move_up_button = Button(button_frame, text="Déplacer vers le haut",command=up,bg="powder blue")
        move_up_button.grid(row=0, column=4, padx=10, pady=10)

        move_down_button = Button(button_frame, text="Descendre",command=down,bg="powder blue")
        move_down_button.grid(row=0, column=5, padx=10, pady=10)
        move_down_button = Button(button_frame, text="extract",command=save_csv(data),bg="powder blue")
        move_down_button.grid(row=0, column=6, padx=10, pady=10)
        move_down_button = Button(button_frame, text="envoyer mail",command=createmail,bg="powder blue")
        move_down_button.grid(row=0, column=7, padx=10, pady=10)
        remove_many_button = Button(button_frame, text="exit",command=home,bg="powder blue")
        remove_many_button.grid(row=0, column=8, padx=10, pady=10)
        
    

       # select_record_button = Button(button_frame, text="Select Record",command=select_record)
        #select_record_button.grid(row=0, column=7, padx=10, pady=10)
      
# Bindings
#my_tree.bind("<Double-1>", clicker)
        my_tree.bind("<ButtonRelease-1>", clicker)

    def add(self):

        L = Location_v(self.id_l.get(),self.description.get(),self.date_debut.get(),self.date_fin.get(),self.prix_loc.get())
        #print("Location_v: ",E.nom)
        L.AjouterLocation_v()
    def remove(self):
        reponse = messagebox.askyesno("Question", "Voulez-vous Supprimer ?")
        if reponse ==True:
            L = Location_v()
            L.supprimerLocation(self.id_l.get()) 
       
               
         
    def update (self):
        reponse = messagebox.askyesnocancel("Question", "Voulez-vous continuer ?")
        if reponse == True:
            L = Location_v()
            L.modifierLocation(self.id_l.get(),self.description.get(),self.date_debut.get(),self.date_fin.get(),self.prix_loc.get())                 
    def qExit(self):
        root.destroy() 
    def Reset(self):
        self.id_l.set("") 
        self.description.set("")  
        self.date_debut.set("")  
        self.date_fin.set("")  
        self.prix_loc.set("")  
                                            
root = Tk()
l = GestionLocation(root)
root.mainloop()