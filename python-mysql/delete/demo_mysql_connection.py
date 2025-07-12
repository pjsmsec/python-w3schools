import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Delete record
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
# Note: the mydb.commit() statement is required to apply the changes.
# Note: The WHERE clause specifies which record(s) should be deleted.
# If you ommit the WHERE clause, all records will be deleted.

# Prevent SQL injection
# It is considered a good practice to escape the values of any query, also in delete
# statements.
# This is to prevent SQL injectionsm which is a common web hacking technique to 
# destroy or miuse your database.
# The mysql.connector module uses the placeholder %s to escape values in the delete 
# statement.
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
