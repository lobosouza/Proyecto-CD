from CRUD_Productos import *

while True:

    print ("1. Productos")
    print ("2. Ventas")
    print ("3. Proveedor")
    print ("4. Clientes")

    menu = int(input("Ingrese una opción: "))

    if menu == 1:
        menu_productos()
