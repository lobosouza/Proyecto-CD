''' Cuando se ingrese a la opción "1" del menu principal
se abre el menu de productos:'''

def menu_productos():
    print("1. Ver productos")
    print("2. Crear producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    menu = int(input("ingrese una opción: "))

    if menu <1 or menu >5:
        print("Opción incorrecta, ingrese nuevamente...")
        menu_productos()
    elif menu == 1:
        print("Ver Productos")
    elif menu == 2:
        print("Crear Producto")
    elif menu == 3:
        print("Actualizar Producto")    
    elif menu == 4:
        print("Eliminar Producto")
    elif menu ==5:
        print("Gracias por utilizar nuestro sistema!")


menu_productos()
   
