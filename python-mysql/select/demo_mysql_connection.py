import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="teste",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Select from a table
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# Note: use the fetchall() method, which fetches all rows from the last executed 
# statement

# Selecting columns
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Using the fetchone() method
# The fetchone() method will return the forst row of the result
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult) 