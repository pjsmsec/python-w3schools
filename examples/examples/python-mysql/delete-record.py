import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myusernsame",
    password="mypassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address='Mountain 21'"

mycursor.exectute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
