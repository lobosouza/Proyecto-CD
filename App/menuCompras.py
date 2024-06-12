# Al ingresar la opción 4. del menú principal, se abre el menú de Clientes.
# Este menú permite elegir las opciones de crear, ver, modificar o eliminar los datos del cliente.
# Para ello, se importará el CRUD de clientes y se usarán sus funciones, acorde a la elección del usuario.

import CRUD_Compras

def menuCompras():

    print("1. Crear nueva compra")
    print("2. Ver compra")
    print("3. Modificar compra")
    print("4. Eliminar compra")
    print("5. Salir del menú")
    
    menu = int(input("Ingrese el número de la opción elegida: "))

    if menu < 1 or menu > 5:
        print("La opción elegida no es válida. Ingrese el número de opción nuevamente: ")
        menuCompras()
    elif menu == 1:
        CRUD_Compras.crearCompra()
    elif menu == 2:
        CRUD_Compras.verCompra()
    elif menu == 3:
        CRUD_Compras.modificarCompra()
    elif menu == 4:
        CRUD_Compras.eliminarCompra()
    elif menu == 5:
        print("Gracias por utilizar nuestros servicios.")

#menuCompras()