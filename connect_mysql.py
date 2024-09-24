import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Cambia esto a la dirección de tu servidor MySQL
            database='mydb',  # Cambia esto al nombre de tu base de datos
            user='root',         # Cambia esto a tu usuario de MySQL
            password='Osni2810'   # Cambia esto a tu contraseña de MySQL
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Conectado a MySQL Server versión", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a la base de datos:", record)

    except Error as e:
        print("Error al conectar a MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == '__main__':
    connect()