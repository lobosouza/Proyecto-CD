# Al ingresar la opción 2. del menú principal, se abre el menú de Ventas.
# Este menú permite elegir las opciones de crear, ver, modificar o eliminar los datos del cliente.
# Para ello, se importará el CRUD de clientes y se usarán sus funciones, acorde a la elección del usuario.

import CRUD_Ventas

def menuVentas():

    print("1. Crear nueva venta")
    print("2. Ver venta")
    print("3. Modificar venta")
    print("4. Eliminar venta")
    print("5. Salir del menú")
    
    menu = int(input("Ingrese el número de la opción elegida: "))

    if menu < 1 or menu > 5:
        print("La opción elegida no es válida. Ingrese el número de opción nuevamente: ")
        menuVentas()
    elif menu == 1:
        CRUD_Ventas.crearVenta()
    elif menu == 2:
        CRUD_Ventas.verVenta()
    elif menu == 3:
        CRUD_Ventas.modificarVenta()
    elif menu == 4:
        CRUD_Ventas.eliminarVenta()
    elif menu == 5:
        print("Gracias por utilizar nuestros servicios.")

menuVentas()