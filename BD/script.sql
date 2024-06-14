SELECT
    detalle_compras.ID_Detalle_Compra,
    detalle_compras.cantidad,
    proveedores.Nombre_Proveedor,
    proveedores.Direccion,
    proveedores.Telefono
FROM
    detalle_compras
INNER JOIN
    compras ON detalle_compras.ID_Compra = compras.ID_Compra
INNER JOIN
    proveedores ON compras.ID_Proveedor = proveedores.ID_Proveedor
WHERE
    detalle_compras.Cantidad > 10;