import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Delete a table
sql = "DROP TABLE customers"

# mycursor.execute(sql)
# This would raise an error if executed multiple times

# Drop only if exists
# If the table you want to delete is already deleted, or for any other reason does
# not exist, you can use the IF EXISTS keywords to avoid raising errors.
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
