from Conexion import *

class Market:
    
    def ingresarClientes(DNI,Apellido_Nombre,Mail,Telefono,Direccion):
        
        
        try:
         cone = conexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="insert into Clientes values(null,%s,%s,%s,%s,%s);"
         #La variable valores tiene que ser una tupla
         valores = (DNI,Apellido_Nombre,Mail,Telefono,Direccion)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Ingresado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error al ingresar los datos {}".format(error))
            