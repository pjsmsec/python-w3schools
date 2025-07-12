import mysql.connector

# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password=""
)

print(mydb)