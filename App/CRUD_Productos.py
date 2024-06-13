''' Según la opción elegida en el menu Productos se eligirá alguna de las siguientes funciones'''
from conexionpy_mysql import *


def ver_producto():
    print("1. Ver Producto")
    

   
def agregar_producto():
   print("2. Agregar Producto")
   conn = conexion() 
   cursor = conn.cursor()


   Nombre_Producto = input("Ingrese nombre: ")
   Precio_Venta = float(input("Ingrese precio de venta: "))
   Precio_Compra = float(input("Ingrese precio de compra: "))
   Cantidad_Stock = int(input("Ingrese la cantidad del producto: "))
   Descripcion = input("Ingrese descripcion del producto: ")

  # sql = "INSERT INTO Productos (ID_Producto, Nombre_Producto, Precio_Venta, Precio_Compra, Cantidad_Stock, Descripcion) VALUES ('null,%s,%s,%s,%s,%s');"
   valores = (Nombre_Producto, Precio_Venta, Precio_Compra, Cantidad_Stock, Descripcion)
   # cursor.execute(sql,valores)
   cursor.execute(f"INSERT INTO Productos (Nombre_Producto, Precio_Venta, Precio_Compra, Cantidad_Stock, Descripcion) VALUES ({valores})")
   conn.commit()
   print(cursor.rowcount, "Producto Agregado")
   conn.close()
   
  
   


def actualizar_producto():
    print("3. Actualizar Producto")
    
def eliminar_producto():
    print("4. Eliminar Producto")


agregar_producto()