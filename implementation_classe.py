import mysql.connector

class Voiture:
    def __init__(self,mat=11,model="",marque="",type_voiture="",nbre_place=0,nbre_porte=0,nbre_cylindre=0,energie="",puissance=0,boite="",prix=0,nbre_kilo=0):
        self.matricule=mat
        self.model=model
        self.marque=marque
        self.type_voiture=type_voiture
        self.nbre_place=nbre_place
        self.nbre_porte=nbre_porte
        self.nbre_cylindre=nbre_cylindre
        self.energie=energie
        self.puissance=puissance
        self.boite=boite
        self.prix=prix
        self.nbre_kilo=nbre_kilo
        self.db = mysql.connector.connect(
        host="localhost",
        user="randa",
        password="randa25990383..",
        database="agencelocation"
        
    )
        self.mycursor=self.db.cursor()
 
class Client:
    def __init__(self,cin=14236,nom="",prenom="",num_tel="",adresse=""):
        self.cin_c=cin
        self.nom=nom
        self.prenom=prenom
        self.num_tel=num_tel
        self.adresse=adresse
        self.db = mysql.connector.connect(
        host="localhost",
        user="randa",
        password="randa25990383..",
        database="agencelocation"
        
    )
        self.mycursor=self.db.cursor()   
     
class Location_v:
    def __init__(self,id_l=1,description="",date_debut="",date_fin="",prix_loc=0):
        self.id_l=id_l
        self.description=description
        self.date_debut=date_debut
        self.date_fin=date_fin
        self.prix_loc=prix_loc
        self.db = mysql.connector.connect(
        host="localhost",
        user="randa",
        password="randa25990383..",
        database="agencelocation"
        
    )
        self.mycursor=self.db.cursor()  
    def AjouterLocation_v(self):
        sql = "INSERT INTO location (id_l,description,date_debut,date_fin,prix_loc) VALUES (%s, %s, %s, %s,%s)"
        val = (self.id_l,self.description,self.date_debut,self.date_fin,self.prix_loc)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")#optionnel
 #fonction d'affichage de tous les étudiants
    def afficherLocation_v(self):
        self.mycursor.execute('SELECT * FROM location ')
        result=self.mycursor.fetchall()
        return result   
    def supprimerLocation(self,id_l):
        sql = "DELETE FROM location WHERE id_l = %s"
        val = (id_l,)
        self.mycursor.execute(sql, val)
        self.db.commit()                 
    def modifierLocation(self,id_l,description,date_debut,date_fin,prix_loc):
        sql="UPDATE location set description=%s,date_debut=%s,date_fin=%s,prix_loc=%s where id_l=%s"
        val= (description,date_debut,date_fin,prix_loc,id_l)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record update.")
    def chercher(self,id_l):
        self.mycursor.execute("SELECT * FROM location where id_l = '%s'" % (id_l))  
        result=self.mycursor.fetchone()
        return result


class Facture:
    def __init__(self,id_f=1,id_l=1,date_fact="",date_pai="",prix_fact=0):
        self.id_f=id_f
        self.id_l=id_l
        self.date_fact=date_fact
        self.date_pai=date_pai
        self.prix_fact=prix_fact
        self.db = mysql.connector.connect(
        host="localhost",
        user="randa",
        password="randa25990383..",
        database="agencelocation"
        
    )
        self.mycursor=self.db.cursor() 
    def AjouterFacture(self):
        sql = "INSERT INTO facture (id_f,id_l,date_fact,date_pai,prix_fact) VALUES (%s, %s, %s, %s,%s)"
        val = (self.id_f,self.id_l,self.date_fact,self.date_pai,self.prix_fact)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")#optionnel
 #fonction d'affichage de tous les étudiants
    def afficherFacture(self):
        self.mycursor.execute('SELECT * FROM facture')
        result=self.mycursor.fetchall()
        return result   
    def supprimerFacture(self,id_f):
        sql = "DELETE FROM facture WHERE id_f = %s"
        val = (id_f,)
        self.mycursor.execute(sql, val)
        self.db.commit()  
    def modifierFacture(self,id_f,id_l,date_fact,date_pai,prix_fact):
        sql="UPDATE facture set id_l=%s,date_fact=%s,date_pai=%s,prix_fact=%s where id_f=%s"
        val= (id_l,date_fact,date_pai,prix_fact,id_f)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record update.")    
    def chercher(self,id_f):
        self.mycursor.execute("SELECT * FROM facture where id_f = '%s'" % (id_f))  
        result=self.mycursor.fetchone()
        return result    

#l=Location_v()
#print(l.chercher(14))