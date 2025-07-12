import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Select with a filter
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Wildcards
# You can select the records that start, includes, or ends with a given letter or 
# phase

# Use the % to represent wildcards:
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Prevent SQL injection
# When query values are provided by the user, you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to 
# destroy or missuse your database.

# The mysql.connector module has methods to escape query values:

# Example: escape query values by using the placeholder %s method:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
# This is to create a single valued tupple

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
