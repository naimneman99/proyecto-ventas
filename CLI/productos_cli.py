from CRUD_DB.crud_categorias import obtener_todas_categorias 


def _obtener_datos_creacion(mydb) -> dict | None:

    print("\n--- INGRESO DE NUEVO PRODUCTO ---")
    datos = {}
    
    # NOMBRE
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío. Intente de nuevo.")
        else:
            datos['nombre'] = nombre


    # DESCRIPCIÓN
    datos['descripcion'] = input("Ingrese la descripción del producto: ").strip()


    # PRECIO UNITARIO y STOCK
    salir = False
    while not salir:
        try:
        
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario <= 0:
                print("Error: El precio debe ser un número positivo.")
                continue
                
            stock = int(input("Ingrese la cantidad en stock: "))
            if stock < 0:
                print("Error: La cantidad en stock no puede ser negativa.")
                continue
            
            datos['precio_unitario'] = precio_unitario
            datos['stock'] = stock
            salir = True
            
        except ValueError:
            print("Error: El precio o stock deben ser números válidos.")
            input("Presione ENTER para continuar...")

    
    
    # GESTIÓN DE CATEGORÍA
    
    categoria_id = gestionar_seleccion_categoria(mydb)
    
    if categoria_id is None:
        print("Operación de producto cancelada o categoría no seleccionada.")
        return None
        
    datos['categoria_id'] = categoria_id
    
    return datos

def _obtener_datos_actualizacion(mydb, datos_existentes: dict) -> dict | None:
    
    
    datos_nuevos = {}
    datos_nuevos["producto_id"] = datos_existentes["producto_id"]
    datos_nuevos["categoria_id"] = datos_existentes["categoria_id"]

    print("\n--- ACTUALIZACIÓN DE PRODUCTO ---")
    print("\nIngrese los nuevos datos del producto (dejar en blanco para mantener el valor actual):")
    
    # NOMBRE
    nombre = input(f"Ingrese el nuevo nombre del producto: ").strip()
    if nombre == "":
        nombre = datos_existentes['nombre']
    datos_nuevos['nombre'] = nombre


    # DESCRIPCIÓN
    descripcion = input(f"Ingrese la nueva descripción del producto: ").strip()
    if descripcion == "":
        descripcion = datos_existentes['descripcion']
    datos_nuevos['descripcion'] = descripcion


    # PRECIO UNITARIO y STOCK
    salir = False
    while not salir:
        try:
        
            precio_unitario_input = input(f"Ingrese el nuevo precio del producto: ").strip()
            if precio_unitario_input == "":
                precio_unitario = datos_existentes['precio_unitario']
            else:
                precio_unitario = float(precio_unitario_input)
                if precio_unitario <= 0:
                    print("Error: El precio debe ser un número positivo.")
                    continue
                
            stock_input = input(f"Ingrese la nueva cantidad en stock: ").strip()
            if stock_input == "":
                stock = datos_existentes['stock']
            else:
                stock = int(stock_input)
                if stock < 0:
                    print("Error: La cantidad en stock no puede ser negativa.")
                    continue
            
            datos_nuevos['precio_unitario'] = precio_unitario
            datos_nuevos['stock'] = stock
            salir = True
            
        except ValueError:
            print("Error: El precio o stock deben ser números válidos.")
            input("Presione ENTER para continuar...")

    
    
    # GESTIÓN DE CATEGORÍA
    print(f"\nCategoría actual (ID: {datos_existentes['categoria_id']}). Seleccione una nueva o cancele.")
    
    
    categoria_id_seleccionada = gestionar_seleccion_categoria(mydb)
    
    if categoria_id_seleccionada is not None:
         datos_nuevos['categoria_id'] = categoria_id_seleccionada
    
    return datos_nuevos


def pedir_datos_producto(mydb, datos_existentes: dict | None = None) -> dict | None:
    """
    Distingue si se quiere actualizar o crear un producto  y llama al método correspondiente.
    """
    
    # Si nos pasan datos existentes, estamos en modo actualización
    if datos_existentes is not None:
        # Llamamos al menú de Actualización
        return _obtener_datos_actualizacion(mydb, datos_existentes)
    else:
        # Llamamos al menú de Creación
        return _obtener_datos_creacion(mydb)





def gestionar_seleccion_categoria(mydb) -> int | None:
    """
    Muestra el menú de categorías y gestiona la selección o creación.
    Retorna el ID de la categoría seleccionada (int) o None (si cancela).
    """
    while True:
        categorias = obtener_todas_categorias(mydb)
        
        print("\n--- SELECCIÓN DE CATEGORÍA ---")
        
        # --- CASO 1: NO HAY CATEGORÍAS ---
        if not categorias:
            print("No hay categorías disponibles.")
            print("[0] - Volver al menú de producto")
            
            eleccion = input("Seleccione [0] para volver: ")
            if eleccion == '0':
                return None
            else:
                print("Opción no válida. Intente de nuevo.")
                continue
        
        # --- CASO 2: MOSTRAR Y SELECCIONAR ---
        
        print("Categorías existentes:")
        contador = 1
        for _, nombre_cat in categorias:
            print(f"[{contador}] - {nombre_cat}")
            contador += 1
            
        print("[0] - Cancelar / Volver")

        eleccion = input("Seleccione una opción: ")
            
        try:
            indice_elegido = int(eleccion)
            
            # 1. Manejar Cancelación
            if indice_elegido == 0:
                return None # 0. Salir
            
            # 2. Manejar Selección Válida
            elif 1 <= indice_elegido <= len(categorias):
                id_seleccionado = categorias[indice_elegido - 1][0] 
                nombre_seleccionado = categorias[indice_elegido - 1][1]
                print(f"-> Categoría seleccionada: {nombre_seleccionado}")
                return id_seleccionado
            
            # 3. Manejar Opción Fuera de Rango
            else:
                print(f"Opción no válida. El rango debe ser entre 1 y {len(categorias)}, o 0.")

        except ValueError as e:
            print(f"Error: {e}")
            
        input("Presione ENTER para continuar...")









