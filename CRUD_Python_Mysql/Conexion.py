#pip install mysql-connector-python
import mysql.connector

class conexion:
    
 def ConexionBaseDeDatos():
     try:
        conexion = mysql.connector.connect(user='root',
                                               password='Osni2810',
                                               host='127.0.0.1',
                                               database='mydb',
                                               port='3306')
        print("Conexion exitosa")
            
        return conexion
            
     except mysql.connector.Error as Error:
            print("Error al conectar a la Base de Datos {}".format(Error))
            
     return conexion
        
 ConexionBaseDeDatos()        