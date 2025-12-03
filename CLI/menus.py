from CLI.productos_cli import pedir_datos_producto
from CLI.clientes_cli import pedir_datos_cliente, pedir_datos_contacto
from CRUD_DB.crud_productos import agregar_producto, obtener_todos_productos, eliminar_producto, actualizar_producto, obtener_producto_por_id
from CRUD_DB.crud_clientes import actualizar_cliente, actualizar_contacto, agregar_cliente, obtener_cliente_por_id, obtener_todos_clientes
from CRUD_DB.crud_ordenes import obtener_clientes_con_mas_ordenes, obtener_orden_por_cliente, obtener_productos_mas_vendidos

def console_clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear') 


# Menu de productos
def menu_productos(mydb):

    while True:
        console_clear()
        print("------- Gestión de Productos -------")
        print("1. Agregar Producto")
        print("2. Ver Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("0. Volver al Menú Principal")
        
        eleccion = input("Seleccione una opción: ")
        
        if eleccion == '1':
            console_clear()
            print("Agregar un Nuevo Producto")
            print("-------------------------")
            
            datos_producto = pedir_datos_producto(mydb)
            if datos_producto is None:
                input("Presione ENTER para volver al menú de productos...")
                continue # Vuelve al inicio del bucle while True
            
            try:
                resultado = agregar_producto(mydb, datos_producto) 
                if resultado:
                    print("Producto agregado exitosamente.")
                else:
                    print("ERROR : No se pudo agregar el producto.") 
            except Exception as e:
                print(f"Error inesperado al agregar el producto: {e}")
                
            input("Presione ENTER para continuar...")
            
        elif eleccion == '2':
            productos = obtener_todos_productos(mydb)

            if productos == []:
                print("No hay productos registrados en la base de datos.")
                input("Presione ENTER para volver al menú de productos...")
                continue # Vuelve al inicio del bucle while True
            
            print("\n--- LISTA DE PRODUCTOS ---")

            print(f"{'ID':<5} {'Nombre':<25} {'Descripción':<45} {'Precio':<15} {'Stock':<15} {'Categoría':<20}")
            print("-" * 120)
            for producto in productos:
                producto_id, nombre, descripcion, precio_unitario, stock, categoria = producto
                print(f"{producto_id:<5} {nombre:<25} {descripcion:<45} {precio_unitario:<15.2f} {stock:<15} {categoria:<20}")
            
            input("Presione ENTER para continuar...")
            
        elif eleccion == '3':
            console_clear()
            print("------- ACTUALIZAR PRODUCTO -------")
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: ")) 
                
                producto_a_actualizar = obtener_producto_por_id(mydb, id_producto)
                if producto_a_actualizar is None:
                    return
                
                print("Datos actuales del producto:")
                print(f"ID: {producto_a_actualizar[0]}")
                print(f"Nombre: {producto_a_actualizar[1]}")
                print(f"Descripción: {producto_a_actualizar[2]}")
                print(f"Precio Unitario: {producto_a_actualizar[3]}")
                print(f"Stock: {producto_a_actualizar[4]}")
                print(f"Categoria_ID: {producto_a_actualizar[5]}")
                print(f"Categoría: {producto_a_actualizar[6]}")                


                datos_producto = pedir_datos_producto(mydb, 
                    datos_existentes = {
                        "producto_id": producto_a_actualizar[0],
                        "nombre": producto_a_actualizar[1],
                        "descripcion": producto_a_actualizar[2],
                        "precio_unitario": float(producto_a_actualizar[3]),
                        "stock": producto_a_actualizar[4],
                        "categoria_id": int(producto_a_actualizar[5]),
                        "categoria": producto_a_actualizar[6]
                    }
                )
                
                if datos_producto is None:
                    print("No se pudieron obtener los nuevos datos del producto.")
                    input("Presione ENTER para continuar...")
                    return
                
                resultado = actualizar_producto(mydb, datos_producto)
                
                if resultado:
                    print("Producto actualizado exitosamente.")
                else:
                    print("ERROR: No se pudo actualizar el producto.")
                    
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")

            input("Presione ENTER para continuar...")

        elif eleccion == '4':
            console_clear()
            print("------- ELIMINAR PRODUCTO -------")
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: ")) 
                
                producto_a_eliminar = obtener_producto_por_id(mydb, id_producto)

                if producto_a_eliminar is None:
                    return
                
                print("Se eliminará el producto:")
                print(f"ID: {producto_a_eliminar[0]}")
                print(f"Nombre: {producto_a_eliminar[1]}")
                
                confirmacion = input("¿Está seguro que desea eliminar este producto? Escriba 'y' para confirmar: ").lower()
                
                if confirmacion == 'y':
                    resultado = eliminar_producto(mydb, id_producto)
                    
                    if resultado:
                        print("Producto eliminado exitosamente.")
                    else:
                        print("ERROR: No se pudo eliminar el producto. Podría tener dependencias (órdenes).")
                else:
                    print("Operación de eliminación cancelada por el usuario.")
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")

            input("Presione ENTER para continuar...")

        elif eleccion == '0':
            return # Rompemos el bucle WHILE para volver a menu_inicio()
            
        else:
            print("Opción no válida, por favor intente de nuevo.")
            input("Presione ENTER para continuar...")

# Menu de clientes
def menu_clientes(mydb):
    # 2. Gestión de Clientes: Registrar, actualizar y ver detalles de clientes, gestionar contactos.
    while True:
        console_clear()
        print("------- Gestión de Clientes -------")
        print("1. Registrar Cliente")
        print("2. Actualizar Cliente")
        print("3. Ver Clientes")
        print("4. Ver Detalles del Cliente")
        print("5. Gestionar Contactos del Cliente")
        print("0. Volver al Menú Principal")
        
        eleccion = input("Seleccione una opción: ")


        if eleccion == '1':
            console_clear()
            print("Agregar un Nuevo Cliente")
            print("-------------------------")
            
            datos_cliente = pedir_datos_cliente(mydb)
            if datos_cliente is None:
                input("Presione ENTER para volver al menú de clientes...")
                continue # Vuelve al inicio del bucle while True
            
            try:
                resultado = agregar_cliente(mydb, datos_cliente) 
                if resultado:
                    print("Cliente agregado exitosamente.")
                else:
                    print("ERROR : No se pudo agregar el cliente.") 
            except Exception as e:
                print(f"Error inesperado al agregar el cliente: {e}")
                
            input("Presione ENTER para continuar...") # Pausa

        elif eleccion == '2':
            console_clear()
            print("------- ACTUALIZAR CLIENTE -------")
            try:
                id_cliente = int(input("Ingrese el ID del cliente a actualizar: ")) 
                
                cliente_a_actualizar = obtener_cliente_por_id(mydb, id_cliente)
                if cliente_a_actualizar is None:
                    return
                
                print("Datos actuales del cliente:")
                print(f"ID: {cliente_a_actualizar[0]}")
                print(f"Nombre: {cliente_a_actualizar[1]}")
                print(f"Apellido: {cliente_a_actualizar[2]}")
                print(f"Domicilio: {cliente_a_actualizar[3]}")
                print(f"Teléfono: {cliente_a_actualizar[4]}")
                print(f"Correo Electrónico: {cliente_a_actualizar[5]}")

                datos_cliente = pedir_datos_cliente(mydb, 
                    datos_existentes = {
                        "cliente_id": cliente_a_actualizar[0],
                        "nombre": cliente_a_actualizar[1],
                        "apellido": cliente_a_actualizar[2],
                        "domicilio": cliente_a_actualizar[3],
                        "telefono": cliente_a_actualizar[4],
                        "correo_electronico": cliente_a_actualizar[5]
                    }
                )
                
                if datos_cliente is None:
                    print("No se pudieron obtener los nuevos datos del cliente.")
                    input("Presione ENTER para continuar...")
                    return
                
                resultado = actualizar_cliente(mydb, datos_cliente)
                
                if resultado:
                    print("Cliente actualizado exitosamente.")
                else:
                    print("ERROR: No se pudo actualizar el cliente.")
                    
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")

            input("Presione ENTER para continuar...")

        elif eleccion == '3':
            clientes = obtener_todos_clientes(mydb)

            if clientes == []:
                print("No hay clientes registrados en la base de datos.")
                input("Presione ENTER para volver al menú de clientes...")
                continue # Vuelve al inicio del bucle while True
            
            print("\n--- LISTA DE CLIENTES ---")

            print(f"{'ID':<5} {'Nombre':<25} {'Apellido':<45} {'Domicilio':<15} {'Teléfono':<15} {'Correo Electrónico':<20}")
            print("-" * 120)
            for cliente in clientes:
                cliente_id, nombre, apellido, domicilio, telefono, correo_electronico = cliente
                print(f"{cliente_id:<5} {nombre:<25} {apellido:<45} {domicilio:<15} {telefono:<15} {correo_electronico:<20}")
            
            input("Presione ENTER para continuar...")

        elif eleccion == '4':
            console_clear()

            print("------- DETALLES DEL CLIENTE -------")
            

            cliente_id_seleccionado = input("Ingrese el ID del cliente para ver detalles: ")
            try:
                cliente = obtener_cliente_por_id(mydb, int(cliente_id_seleccionado))
                if cliente is None:
                    print(f"No se encontró un cliente con ID {cliente_id_seleccionado}.")
                    input("Presione ENTER para continuar...")
                    continue
                
                print("\n--- DETALLES DEL CLIENTE ---")
                print(f"ID: {cliente[0]}")
                print(f"Nombre: {cliente[1]}")
                print(f"Apellido: {cliente[2]}")
                print(f"Domicilio: {cliente[3]}")
                print(f"Teléfono: {cliente[4]}")
                print(f"Correo Electrónico: {cliente[5]}")
                
                input("Presione ENTER para continuar...")
                
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")
                input("Presione ENTER para continuar...")

        elif eleccion == '5':
            console_clear()
            try:
                id_cliente = int(input("Ingrese el ID del cliente a actualizar: ")) 
                
                cliente_a_actualizar = obtener_cliente_por_id(mydb, id_cliente)
                if cliente_a_actualizar is None:
                    return
                
                print(f"Datos de contacto actuales del cliente: {cliente_a_actualizar[1]} {cliente_a_actualizar[2]}  ")
                print(f"Teléfono: {cliente_a_actualizar[4]}")
                print(f"Correo Electrónico: {cliente_a_actualizar[5]}")

                datos_contacto = pedir_datos_contacto(mydb,
                    datos_contacto_existentes = {
                        "telefono": cliente_a_actualizar[4],
                        "correo_electronico": cliente_a_actualizar[5]
                    }
                )

                if datos_contacto is None:
                    print("No se pudieron obtener los nuevos datos de contacto del cliente.")
                    input("Presione ENTER para continuar...")
                    return
                
                # Agrego el ID del cliente al diccionario de datos_contacto
                datos_contacto["cliente_id"] = cliente_a_actualizar[0]

                resultado = actualizar_contacto(mydb, datos_contacto)
                
                if resultado:
                    print("Cliente actualizado exitosamente.")
                else:
                    print("ERROR: No se pudo actualizar el cliente.")
                    
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")

            input("Presione ENTER para continuar...")
            
        elif eleccion == '0':
            return
            
        else:
            print("Funcionalidad no implementada aún.")
            input("Presione ENTER para continuar...")


# Menu de búsquedas avanzadas
def menu_busquedas_avanzadas(mydb):
    while True:
        console_clear()
        print("------- Gestión de Clientes -------")
        print("1. Obtener los productos más vendidos")
        print("2. Obtener los clientes con más órdenes")
        print("0. Volver al Menú Principal")
        
        eleccion = input("Seleccione una opción: ")


        if eleccion == '1':
            console_clear()
            print("------- PRODUCTOS MÁS VENDIDOS -------")
            
            try:
                productos_mas_vendidos = obtener_productos_mas_vendidos(mydb)
                
                if productos_mas_vendidos == []:
                    print("No hay productos registrados en la base de datos.")
                    input("Presione ENTER para continuar...")
                    continue

                for producto in productos_mas_vendidos:
                    print(f"""
                            Producto ID: {producto['producto_id']}, 
                            Nombre: {producto['nombre_producto']}, 
                            Cantidad Total Vendida: {producto['total_vendido']}
                        """)

            except Exception as e:
                print(f"Error inesperado al obtener los productos más vendidos: {e}")
                
            input("Presione ENTER para continuar...")

        elif eleccion == '2':
            console_clear()
            print("------- CLIENTES CON MÁS ÓRDENES -------")
        
            try:
                clientes = obtener_clientes_con_mas_ordenes(mydb)

                if clientes == []:
                    print("No hay clientes registrados en la base de datos.")
                    input("Presione ENTER para continuar...")
                    continue

                for cliente in clientes:
                    print(f"""
                            Nombre Completo: {cliente['nombre_completo']}, 
                            Cliente ID: {cliente['cliente_id']}, 
                            Cantidad de Órdenes: {cliente['total_ordenes']}
                        """)
                         
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")

            input("Presione ENTER para continuar...")


        elif eleccion == '0':
            return
            
        else:
            print("Funcionalidad no implementada aún.")
            input("Presione ENTER para continuar...")
        


# --- MENÚ PRINCIPAL ---
def menu_inicio(mydb) -> bool:
    console_clear()
    salir = False
    
    while not salir:

        """
        3. Procesamiento de Órdenes: Mostrar las órdenes pedidas por un cliente dado.
        4. Búsquedas Avanzadas: Recuperar productos o clientes con filtros (e.g., productos más vendidos).
        5. Reporte de productos más vendidos: Generar un reporte del producto más vendido indicando la cantidad total pedida de ese producto.
        6. Modificiación de valor de un producto: Modificar las órdenes de un producto dado para ajustarse una cierta cantidad máxima.
        """
        print("------- Gestión del Sistema de Ventas en Línea -------")
        print("1. Gestionar Productos")
        print("2. Gestionar Clientes")
        print("3. Procesamiento de Órdenes")
        print("4. Búsquedas Avanzadas")
        print("5. Reporte de Productos Más Vendidos")
        print("6. Modificación de Valor de un Producto")
        print("0. Salir")
        
        eleccion = input("Seleccione una opción: ")
        
        if eleccion == '1':
            menu_productos(mydb)

        elif eleccion == '2':
            menu_clientes(mydb)

        elif eleccion == '3':
            console_clear()
            print("--- Procesamiento de Órdenes ---")

            try:
                id_cliente = int(input("Ingrese el ID del cliente para ver sus órdenes: "))

                cliente_seleccionado = obtener_cliente_por_id(mydb, id_cliente)
                if cliente_seleccionado is None:
                    print(f"No se encontró un cliente con ID {id_cliente}.")
                    input("Presione ENTER para continuar...")
                    continue

                orden = obtener_orden_por_cliente(mydb, id_cliente)
    
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")
                salir = True

            if orden == []:
                print("No hay órdenes registradas para este cliente.")
                input("Presione ENTER para continuar...")
                continue

            print(f" --- Ordenes para el cliente: {orden[0]['nombre_completo_cliente']} --- ")
            for orden_detalle in orden:
                print(f"""
                    Orden ID: {orden_detalle['orden_id']}, 
                    Fecha: {orden_detalle['fecha']}, 
                    Tipo de Pago: {orden_detalle['tipo_pago']}, 
                    Estado: {orden_detalle['estado']}, 
                    Monto Total: {orden_detalle['monto_total']}
                    Producto: {orden_detalle['nombre_producto']}, 
                    Descripción: {orden_detalle['descripcion_producto']}, 
                    Cantidad: {orden_detalle['cantidad']},
                    Precio al Momento de la Orden: {orden_detalle['precio_al_momento']}
                    """)

            input("Presione ENTER para continuar...")
        
        elif eleccion == '4':
            menu_busquedas_avanzadas(mydb)

        elif eleccion == '0':
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida, por favor intente de nuevo.")
            input("Presione ENTER para continuar...")
            console_clear()
            
    return salir











            