import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword",
    database="mydatabase"
)

mycursor = mydb.connect()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
