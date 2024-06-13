
import menuProductos
import menuVentas
import menuDetalle_Ventas
import menuCompras
import menuDetalle_Compras
import menuProveedores
import menuClientes



def menuPrincipal():
    print("---------------------------------------------------------------")
    print("** Menu Principal **")
    print("---------------------------------------------------------------")
    print("1. Productos")
    print("2. Ventas")
    print("3. Detalle de Ventas")
    print("4. Compras")
    print("5. Detalle de Compras")
    print("6. Proveedores") 
    print("7. Clientes" )
    print("8. Salir")
    print("---------------------------------------------------------------")
    opc = int(input("Seleccione una opción: "))
    
    if opc <1 or opc>8:
        print("Opción incorrecta, ingrese el número de su elección nuevamente...")
        menuPrincipal()
    elif opc == 1:
        menuProductos.menu_productos()
    elif opc == 2:
        menuVentas.menuVentas()
    elif opc == 3:
        menuDetalle_Ventas.menuDetalle_Venta() 
    elif opc == 4:
        menuCompras.menuCompras()
    elif opc == 5:
        menuDetalle_Compras.menuDetalle_Compra()
    elif opc == 6:
        menuProveedores.menuProveedores()    
    elif opc == 7:
        menuClientes.menuClientes()
    elif opc==8:
        print("Gracias por utilizar nuestro sistema!")
    


menuPrincipal()