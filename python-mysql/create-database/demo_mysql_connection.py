import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password="",
    database="mydatabase"
    # This attemps an immediate connection
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
# This avoids raising errors caused by trying to create the same database several 
# times

# Check if the database exists

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
