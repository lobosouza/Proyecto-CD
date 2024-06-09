# Proyecto-CD
# Proyecto Integrador del módulo Progamador de la tecnicatura en Ciencia de Datos e Inteligencia Artificial 

   Integrantes:
   
1. Bruno Lobo Souza, 95690709, lobosouza.it@gmail.com, https://github.com/lobosouza
2. Marián Chazarreta, 37509774, marianchazarreta@hotmail.com, https://github.com/marianuvita
3. Carlos Direni, 28117281, direnicarlos1@gmail.com, https://github.com/Cdireni1
4. Federico Cruceño, 39623298, fedecrucenio@gmail.com, https://github.com/federicocruceno


  Propuesta de Proyecto:
  
Se propone una aplicación para un Kiosco que registra la provición, venta y compra dentro del negocio, así como datos de los clientes. Está diseñado usando pseudocódigo PSEint, lenguaje Python, y base de datos con MySQL.
La aplicación está ubicada en la carpeta "App", y posee un Menú Principal "index.py" para acceder a Crear, Leer, Actualizar y Eliminar los siguientes datos: 
1. Productos (nombre, precio de compra, nombre de venta, stock, ID)
2. Ventas (fecha, precio total, ID)
3. Proveedor (nombre, mail, teléfono, dirección, ID)
4. Clientes (nombre, mail, teléfono, dirección, DNI)

  Detalle de la aplicación modularizada:
  
- Index
Ofrece el menú de opciones al usuario, donde puede elegir si quiere acceder a 1. Productos, 2. Ventas, 3. Proveedor, 4. Clientes, ó si desea abandonar el menú 5. Salir.
Este Menú Principal importa las funciones de los siguientes módulos:

  
1. ModuloProductos
Se compone de los siguientes módulos:
- CRUD_Productos: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del producto.
- menuProductos: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Productos.

2. ModuloVentas
Se compone de los siguientes módulos:
- CRUD_Ventas: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos de venta.
- menuVentas: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUDventas.

3. ModuloProveedor
Se compone de los siguientes módulos:
- CRUD_Proveedor: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del proveedor.
- menuProveedor: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUDproveedor.

4. ModuloClientes
Se compone de los siguientes módulos:
- CRUD_Clientes: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del cliente.
- menuClientes: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUDclientes.

