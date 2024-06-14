# Proyecto-CD
# Proyecto Integrador del módulo Progamador de la tecnicatura en Ciencia de Datos e Inteligencia Artificial 

   Integrantes:
   
1. Bruno Lobo Souza, 95690709, lobosouza.it@gmail.com, https://github.com/lobosouza
2. Marián Chazarreta, 37509774, marianchazarreta@hotmail.com, https://github.com/marianuvita
3. Carlos Direni, 28117281, direnicarlos1@gmail.com, https://github.com/Cdireni1

  Propuesta de Proyecto:
  
Se propone una aplicación para un Market que registra la provición, venta y compra dentro del negocio, así como datos de los clientes. Está diseñado usando pseudocódigo PSEint, lenguaje Python, y base de datos con MySQL.
La aplicación está ubicada en la carpeta "App", y posee un Menú Principal "index.py" para acceder a Crear, Leer, Actualizar y Eliminar los siguientes datos: 
1. Productos (nombre, precio de compra, nombre de venta, stock, ID)
2. Ventas (fecha, precio total, ID)
3. Proveedor (nombre, mail, teléfono, dirección, ID)
4. Clientes (nombre, mail, teléfono, dirección, DNI)

 Requisitos:

- mySQL Workbench 8.0
- Visual Studio Code
- Instalar extensiones en Visual Studio: Python Path, MySQL management tool, Database manager for MySQL
- Descargar las carpertas 'App' y 'BD'
- Tener la base de datos cargada localmente a través de MySQL
- Ingresar usuario y contraseña de base de datos local en el archivo "conexionpy_mysql.py"
 

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
- menuVentas: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Ventas.

3. ModuloDetalle_Ventas
Se compone de los siguientes módulos:
- CRUD_Detalle_Ventas: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del detalle de ventas.
- menuDetalle_Ventas: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Detalle_Ventas.

4. ModuloProveedor
Se compone de los siguientes módulos:
- CRUD_Proveedor: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del proveedor.
- menuProveedor: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Proveedor.

5. ModuloCompras
Se compone de los siguientes módulos:
- CRUD_Compras: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos de compras.
- menuCompras: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Compras.

6. ModuloDetalle_Compras
Se compone de los siguientes módulos:
- CRUD_Detalle_Compras: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del detalle de compras.
- menuDetalle_Compras: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Detalle_Compras.

4. ModuloClientes
Se compone de los siguientes módulos:
- CRUD_Clientes: se definen las funciones para Crear, Ver, Actualizar y Eliminar los datos del cliente.
- menuClientes: presenta las opciones disponibles al usuario y le permite elegir la acción deseada, importando para ello las funciones de CRUD_Clientes.

