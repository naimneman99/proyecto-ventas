from CLI.productos_cli import pedir_datos_producto
from CRUD_DB.crud_productos import agregar_producto, obtener_todos_productos, eliminar_producto, actualizar_producto, obtener_producto_por_id


def console_clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear') 


# --- MENÚ PRINCIPAL ---
def menu_inicio(mydb) -> bool:
    console_clear()
    salir = False
    
    while not salir:
        print("------- Gestión del Sistema de Ventas en Línea -------")
        print("1. Gestionar Productos")
        print("0. Salir")
        
        eleccion = input("Seleccione una opción: ")
        
        if eleccion == '1':
            # La función menu_productos debe devolver True si quiere volver, y False si quiere salir completamente
            menu_productos(mydb)


        elif eleccion == '0':
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida, por favor intente de nuevo.")
            input("Presione ENTER para continuar...")
            console_clear()
            
    return salir

# Menu de productos
def menu_productos(mydb):

    while True: # Bucle para mantenerse en el menú de productos
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
                
            input("Presione ENTER para continuar...") # Pausa
            
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



















            