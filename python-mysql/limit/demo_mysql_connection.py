import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Limit the result
mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Start from another position
# If you want to return five records, starting from the third record, you can use
# the "OFFSET" keyword:

# Example: start form position 3, and return 5 records:
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
