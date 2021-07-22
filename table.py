import mysql.connector
def connect_DB():
    mydb=mysql.connector.connect(
        host="localhost",
        user="randa",
        password="randa25990383..",
        database="agencelocation"
    )
    return mydb
db=connect_DB()
mycursor = db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS VOITURE(matricule int PRIMARY KEY,model VARCHAR(255),marque VARCHAR(255),type_voiture VARCHAR(255),nbre_place int,nbre_porte int,nbre_cylindre int ,energie VARCHAR(255) ,puissance FLOAT,boite VARCHAR(255),prix FLOAT,nbre_kilo int )")
mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENT(cin_c int PRIMARY KEY,nom VARCHAR(255),prenom VARCHAR(255),num_tel VARCHAR(255),adresse VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS LOCATION(id_l int PRIMARY KEY,description VARCHAR(255),date_debut VARCHAR(255) ,date_fin VARCHAR(255) , prix_loc FLOAT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS FACTURE(id_f int PRIMARY KEY,id_l int,prix_fact FLOAT , date_fact VARCHAR(255) , date_pai VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)    
