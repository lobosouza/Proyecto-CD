# Al ingresar la opción 3. del menú principal, se abre el menú de Detalle_Ventas.
# Este menú permite elegir las opciones de crear, ver, modificar o eliminar los datos del detalle de venta.
# Para ello, se importará el CRUD de Detalle_Ventas y se usarán sus funciones, acorde a la elección del usuario.

import CRUD_Detalle_Ventas

def menuDetalle_Venta():

    print("1. Crear nuevo detalle de venta")
    print("2. Ver detalle de venta")
    print("3. Modificar detalle de venta")
    print("4. Eliminar detalle de venta")
    print("5. Salir del menú")
    
    menu = int(input("Ingrese el número de la opción elegida: "))

    if menu < 1 or menu > 5:
        print("La opción elegida no es válida. Ingrese el número de opción nuevamente: ")
        menuDetalle_Venta()
    elif menu == 1:
        CRUD_Detalle_Ventas.crearDetalle_Venta()
    elif menu == 2:
        CRUD_Detalle_Ventas.verDetalle_Venta()
    elif menu == 3:
        CRUD_Detalle_Ventas.modificarDetalle_Venta()
    elif menu == 4:
        CRUD_Detalle_Ventas.eliminarDetalle_Venta()
    elif menu == 5:
        print("Gracias por utilizar nuestros servicios.")

#menuDetalle_Venta()