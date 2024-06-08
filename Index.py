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
    elif opc == 1:
        print("1. Productos")
    elif opc == 2:
        print("2. Ventas")
    elif opc == 3:
        print("3. Proveedor")    
    elif opc == 4:
        print("4. Clientes")
    elif opc==5:
        print("Gracias por utilizar nuestro sistema!")
    else:
        ejecutaropc(opc)
        
def ejecutaropc(opc):
    print("opcion")
        

menuPrincipal()