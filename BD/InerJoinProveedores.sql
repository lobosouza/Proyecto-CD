SELECT
    proveedores.ID_Proveedor,
    proveedores.Nombre_Proveedor,
    proveedores.Direccion,
    proveedores.Mail,
    proveedores.Telefono,
    compras.ID_Compra,
    Compra.fecha
FROM
    proveedores
INNER JOIN
    compras ON proveedores.ID_Proveedor = compras.ID_Proveedor;