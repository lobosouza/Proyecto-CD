''' Según la opción elegida en el menu Productos se eligirá alguna de las siguientes funciones'''
from conexionpy_mysql import *


def ver_producto():
    print("1. Ver Producto")
    

   
def agregar_producto():
    print("2. Agregar Producto")
    conn = conexion() 
    if conn is None:
        print("No se pudo establecer la conexión con la base de datos.")
        return
    cursor = conn.cursor()

    # Solicitar información del producto
    Nombre_Producto = input("Ingrese nombre: ")
    Precio_Venta = float(input("Ingrese precio de venta: "))
    Precio_Compra = float(input("Ingrese precio de compra: "))
    Cantidad_Stock = int(input("Ingrese la cantidad del producto: "))
    Descripcion = input("Ingrese descripcion del producto: ")

    # Consulta SQL para insertar el producto
    sql = """
    INSERT INTO productos 
    (Nombre_Producto, Precio_Venta, Precio_Compra, Cantidad_Stock, Descripcion) 
    VALUES (%s, %s, %s, %s, %s);
    """

    # Valores a insertar
    valores = (Nombre_Producto, Precio_Venta, Precio_Compra, Cantidad_Stock, Descripcion)

    # Ejecutar la consulta
    cursor.execute(sql, valores)

    # Confirmar los cambios en la base de datos
    conn.commit()
    print(cursor.rowcount, "Producto Agregado")

    # Cerrar la conexión
    conn.close()
   
  
   


def actualizar_producto():
    print("3. Actualizar Producto")
    
def eliminar_producto():
    print("4. Eliminar Producto")


agregar_producto()
