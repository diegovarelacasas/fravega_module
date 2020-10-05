import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="diego",
    passwd="root"
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")