import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Sort the result
# Use the ORDER BY statement to sort the result in ascending or descencindg order.
# The ORDER BY keyword sorts the result ascending by default.
# To sort the result in descending order, use de DESC keyword.
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# ORDER BY DESC
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
