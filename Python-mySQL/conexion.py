import mysql.connector

conexion= mysql.connector.connect(user='user1', password = '123456', 
                                   host='localhost', 
                                   database='mydb', 
                                   port='3306')
print(conexion)

                        