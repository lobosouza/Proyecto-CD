Algoritmo AppKioscodrugtore
	Definir opc Como Cadena
	
	Mientras (opc<>'5') hacer
		Escribir '_____________________________________________'
		Escribir 'Inventario Kiosco Drugstore'
		Escribir 'Bienvenido a la carga de productos y cliente'
		Escribir '_____________________________________________'
		Escribir '1. Productos'
		Escribir '2. Ventas'
		Escribir '3. Proveedor'
		Escribir '4. Clientes'
		Escribir '5. Salir'
		Escribir 'Ingresar una opci�n: '
		Leer opc
		// Intrucciones para acceso a las opciones// 
		Seg�n opc Hacer
			'1':
			Limpiar Pantalla
			Escribir 'Opci�n 1'
			Escribir 'Productos'
			Escribir 'pulsa una tecla para continuar...'
			Esperar Tecla
			'2':
			Limpiar Pantalla
			Escribir 'Opci�n 2'
			Escribir 'Ventas'
			Escribir 'pulsa una tecla para continuar...'
			Esperar Tecla
			'3':
			Limpiar Pantalla
			Escribir 'Opci�n 3'
			Escribir 'Proveedor'
			Escribir 'pulsa una tecla para continuar...'
			Esperar Tecla
			'4':
			Limpiar Pantalla
			Escribir 'Opci�n 4'
			Escribir 'Clientes'
			Escribir 'pulsa una tecla para continuar...'
			Esperar Tecla
			'5':
			Limpiar Pantalla
			Escribir 'Opci�n 5'
			Escribir 'Muchas Gracias'
			Esperar Tecla
		De Otro Modo:
			Limpiar Pantalla
			Escribir opc, ' No es una opci�n correcta. Intente de nuevo...'
			Escribir 'pulsa una tecla para continuar'
			Esperar Tecla
		FinSeg�n
	Fin Mientras

FinAlgoritmo
