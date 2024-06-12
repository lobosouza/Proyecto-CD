# Al ingresar la opción 5. del menú principal, se abre el menú de Detalle_Compras.
# Este menú permite elegir las opciones de crear, ver, modificar o eliminar los datos del detalle de compra.
# Para ello, se importará el CRUD de Detalle_Compra y se usarán sus funciones, acorde a la elección del usuario.

import CRUD_Detalle_Compras

def menuDetalle_Compra():

    print("1. Crear nuevo detalle de compra")
    print("2. Ver detalle de compra")
    print("3. Modificar detalle de compra")
    print("4. Eliminar detalle de compra")
    print("5. Salir del menú")
    
    menu = int(input("Ingrese el número de la opción elegida: "))

    if menu < 1 or menu > 5:
        print("La opción elegida no es válida. Ingrese el número de opción nuevamente: ")
        menuDetalle_Compra()
    elif menu == 1:
        CRUD_Detalle_Compras.crearDetalle_Compra()
    elif menu == 2:
        CRUD_Detalle_Compras.verDetalle_Compra()
    elif menu == 3:
        CRUD_Detalle_Compras.modificarDetalle_Compra()
    elif menu == 4:
        CRUD_Detalle_Compras.eliminarDetalle_Compra()
    elif menu == 5:
        print("Gracias por utilizar nuestros servicios.")

#menuDetalle_Compra()