from CRUD_DB.crud_categorias import obtener_todas_categorias 

def pedir_datos_producto(mydb, datos_existentes: dict | None = None) -> dict | None:
    """
    Distingue si se quiere actualizar o crear un producto  y llama al método correspondiente.
    """

    if datos_existentes is not None:
        # Estamos en modo actualización
    
        datos_nuevos = {}
        datos_nuevos["producto_id"] = datos_existentes["producto_id"]
        datos_nuevos["categoria_id"] = datos_existentes["categoria_id"]

        print("\n--- ACTUALIZAR PRODUCTO ---")
        print("\nIngrese los nuevos datos del producto (dejar en blanco para mantener el valor actual):")
    else:
        # Estamos en modo creación
        print("\n--- INGRESAR NUEVO PRODUCTO ---")
        datos_nuevos = {}

    # PEDIR NOMBRE
    nombre = input("Ingrese el nombre del producto: ").strip()

    if datos_existentes is None:
        # Si estamos creando Validamos
        while nombre == "":
            print("Error: El nombre no puede estar vacío. Intente de nuevo.")
            nombre = input("Ingrese el nombre del producto: ").strip()
    else:
        # Si estamos actualizando mantenemos el existente si no se ingresa nada
        if nombre == "":
            nombre = datos_existentes['nombre']

    datos_nuevos['nombre'] = nombre

    # PEDIR DESCRIPCIÓN
    descripcion = input("Ingrese la descripción del producto: ").strip()
    if datos_existentes is not None and descripcion == "":
        descripcion = datos_existentes['descripcion']
    datos_nuevos['descripcion'] = descripcion
    
    # PEDIR PRECIO UNITARIO y STOCK
    salir = False
    while not salir:
        try:
        
            precio_unitario_input = input("Ingrese el precio unitario del producto: ").strip()
            if datos_existentes is not None and precio_unitario_input == "":
                precio_unitario = datos_existentes['precio_unitario']
            else:
                precio_unitario = float(precio_unitario_input)
                if precio_unitario <= 0:
                    print("Error: El precio debe ser un número positivo.")
                    continue
                
            stock_input = input("Ingrese la cantidad en stock: ").strip()
            if datos_existentes is not None and stock_input == "":
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

    if datos_existentes is not None:
        print(f"\nCategoría actual (ID: {datos_existentes['categoria_id']}). Seleccione una nueva o cancele.")
    
    categoria_id_seleccionada = gestionar_seleccion_categoria(mydb)
    
    if categoria_id_seleccionada is not None:
         datos_nuevos['categoria_id'] = categoria_id_seleccionada
    
    return datos_nuevos


def gestionar_seleccion_categoria(mydb) -> int | None:
    """
    Muestra el menú de categorías y gestiona la selección o creación.
    Retorna el ID de la categoría seleccionada (int) o None (si cancela).
    """
    while True:
        categorias = obtener_todas_categorias(mydb)
        
        print("\n--- SELECCIONAR CATEGORÍA ---")
        
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









