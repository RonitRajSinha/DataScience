import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",password="12345678",port="3306")
print(mycon.connection_id)
