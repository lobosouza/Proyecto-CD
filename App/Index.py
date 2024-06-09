
import menuProductos
import menuVentas
import menuProveedores
import menuClientes


def menuPrincipal():
    print("---------------------------------------------------------------")
    print("** Menu Principal **")
    print("---------------------------------------------------------------")
    print("1. Productos")
    print("2. Ventas")
    print("3. Proveedores") 
    print("4. Clientes" )
    print("5. Salir")
    print("---------------------------------------------------------------")
    opc = int(input("Seleccione una opción: "))
    
    if opc <1 or opc>5:
        print("Opción incorrecta, ingrese el número de su elección nuevamente...")
        menuPrincipal()
    elif opc == 1:
        menuProductos.menu_productos()
    elif opc == 2:
        menuVentas.menuVentas()
    elif opc == 3:
        menuProveedores.menuProveedores()    
    elif opc == 4:
        menuClientes.menuClientes()
    elif opc==5:
        print("Gracias por utilizar nuestro sistema!")
    


menuPrincipal()