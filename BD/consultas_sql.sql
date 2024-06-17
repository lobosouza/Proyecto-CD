select * from productos;
INSERT INTO productos 
VALUES (null,'Chispas', 400.00, 280.00, 100, 'Galletas con chispas de chocolate');
INSERT INTO proveedores 
VALUES (null,'Distribuidora ABC	', 'Av. Siempre Viva 123', 'contacto@abcdistribu.com', 1234567890);
select * from proveedores;
DELETE FROM productos WHERE ID_Producto=2;
DELETE FROM proveedores WHERE ID_Proveedor=2;