import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="diego",
    passwd="root",
    database="testdatabase"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

#mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("joe", 22))
#db.commit()
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)