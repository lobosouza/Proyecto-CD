# Al ingresar la opción 4. del menú principal, se abre el menú de Clientes.
# Este menú permite elegir las opciones de crear, ver, modificar o eliminar los datos del cliente.
# Para ello, se importará el CRUD de clientes y se usarán sus funciones, acorde a la elección del usuario.

import CRUD_Clientes

def menuClientes():

    print("1. Crear nuevo cliente")
    print("2. Ver cliente")
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Salir del menú")
    
    menu = int(input("Ingrese el número de la opción elegida: "))

    if menu < 1 or menu > 5:
        print("La opción elegida no es válida. Ingrese el número de opción nuevamente: ")
        menuClientes()
    elif menu == 1:
        CRUD_Clientes.crearCliente()
    elif menu == 2:
        CRUD_Clientes.verCliente()
    elif menu == 3:
        CRUD_Clientes.modificarCliente()
    elif menu == 4:
        CRUD_Clientes.eliminarCliente()
    elif menu == 5:
        print("Gracias por utilizar nuestros servicios.")

#menuClientes()


