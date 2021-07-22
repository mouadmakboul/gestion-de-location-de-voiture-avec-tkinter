import mysql.connector
mydb = mysql.connector.connect (
    host="localhost",
    user="randa",
    password="randa25990383.."

)
mycursor =mydb.cursor()
mycursor.execute("CREATE DATABASE agencelocation")
    