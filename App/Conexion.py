#pip install mysql-connector-python
import mysql.connector

class conexion:
    
 def ConexionBaseDeDatos():
     try:
        #ingresar en user y password de su base de datos local
        conexion = mysql.connector.connect(user='root',
                                               password='root',
                                               host='localhost',
                                               database='mydb',
                                               port='3306')
        print("Conexion exitosa")
            
        return conexion
            
     except mysql.connector.Error as Error:
            print("Error al conectar a la Base de Datos {}".format(Error))
            
     return conexion
        
 ConexionBaseDeDatos()        