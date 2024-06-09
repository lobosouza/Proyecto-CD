# Al ingresar la opción 3. del menú principal, se abre el menú de Proveedores.
# Este menú permite elegir las opciones de crear, ver, modificar o eliminar los datos del proveedor.
# Para ello, se importará el CRUD de proveedores y se usarán sus funciones, acorde a la elección del usuario.

import CRUD_Proveedores

def menuProveedores():

    print("1. Crear nuevo proveedor")
    print("2. Ver proveedor")
    print("3. Modificar proveedor")
    print("4. Eliminar proveedor")
    print("5. Salir del menú")
    
    menu = int(input("Ingrese el número de la opción elegida: "))

    if menu < 1 or menu > 5:
        print("La opción elegida no es válida. Ingrese el número de opción nuevamente: ")
        menuProveedores()
    elif menu == 1:
        CRUD_Proveedores.crearProveedor()
    elif menu == 2:
        CRUD_Proveedores.verProveedor()
    elif menu == 3:
        CRUD_Proveedores.modificarProveedor()
    elif menu == 4:
        CRUD_Proveedores.eliminarProveedor()
    elif menu == 5:
        print("Gracias por utilizar nuestros servicios.")

menuProveedores()