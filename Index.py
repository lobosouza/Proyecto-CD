

def menuPrincipal():
    print("---------------------------------------------------------------")
    print("** Menu Principal **")
    print("---------------------------------------------------------------")
    print("1. Productos")
    print("2. Ventas")
    print("3. Proveedor") 
    print("4. Clientes" )
    print("5. Salir")
    print("---------------------------------------------------------------")
    opc = int(input("Seleccione una opción: "))
    
    if opc <1 or opc>5:
        print("Opción incorrecta, ingrese nuevamente...")
        menuPrincipal()
    elif opc == 1:
        print("Productos")
        menu_productos()
    elif opc == 2:
        print("Ventas")
    elif opc == 3:
        print("Proveedor")    
    elif opc == 4:
        print("Clientes")
    elif opc==5:
        print("Gracias por utilizar nuestro sistema!")
    

    

menuPrincipal()