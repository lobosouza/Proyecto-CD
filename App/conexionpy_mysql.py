import mysql.connector

def conexion():
    mysql.connector.connect(user='root', password = 'root', 
                                   host='localhost', 
                                   database='mydb', 
                                   port='3306')
print(conexion)

conexion()