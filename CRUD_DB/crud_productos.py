
import mysql.connector


def agregar_producto(mydb, datos_producto: dict)-> bool:
    """
    Agrega un nuevo producto a la base de datos.

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_producto -- Diccionario con los datos del producto a agregar.

    Retorna:
    True si el producto fue agregado exitosamente, False en caso contrario.
    """
    
    if datos_producto is None:
        raise ValueError("No se proporcionaron datos para agregar el producto.")

    # Varificar conexión
    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    try:
        with mydb.cursor() as cursor:

            sql = """
            INSERT INTO productos (nombre, descripcion, precio_unitario, stock, categoria_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            valores_producto = (
                datos_producto["nombre"],
                datos_producto["descripcion"],
                datos_producto["precio_unitario"],
                datos_producto["stock"],
                datos_producto["categoria_id"]
            )
            
            cursor.execute(sql, valores_producto)
            mydb.commit()
            return True 
    except mysql.connector.Error as err:
        print(f"Error de base de datos (INSERT): {err}")
        # Deshacer la transacción si falla
        mydb.rollback() 
        return False    
    except Exception as e:
        print(f"Error inesperado al agregar producto: {e}")
        return False

def obtener_todos_productos(mydb) -> list:
    """
    Consulta la base de datos para obtener la lista de todos los productos.

    Parámetros:
    mydb -- Conexión a la base de datos.

    Retorna una lista de tuplas con los datos de los productos o una lista vacía si falla.
    """
    if mydb is None or not mydb.is_connected():
        print("Error: Conexión a la base de datos no disponible.")
        return []

    try:
        with mydb.cursor() as cursor:
            sql = """
            SELECT producto_id, p.nombre, descripcion, precio_unitario, stock, c.nombre AS categoria
            FROM productos p JOIN categorias c ON p.categoria_id = c.categoria_id
            ORDER BY c.nombre, p.nombre
            """
            cursor.execute(sql)
            productos = cursor.fetchall()
            return productos          
    except Exception as e:
        print(f"Error al obtener productos de la BD: {e}")
        # En caso de error, siempre retornamos una lista vacía para evitar fallos
        return []

def obtener_producto_por_id(mydb, producto_id: int) -> tuple | None:
    """
    Busca un producto por su ID en la base de datos.
    
    Parámetros:
    mydb -- Conexión a la base de datos.
    producto_id -- ID del producto a buscar.

    Retorna una tupla con los datos del producto o None si no se encuentra.
    """
    if mydb is None or not mydb.is_connected():
        print("Error: Conexión a la base de datos no disponible.")
        return None

    if not isinstance(producto_id, int) or producto_id <= 0:
        raise ValueError("El ID del producto debe ser un entero positivo.")

    try:
        with mydb.cursor() as cursor:
            sql = """
            SELECT 
                p.producto_id, 
                p.nombre, 
                p.descripcion, 
                p.precio_unitario, 
                p.stock, 
                p.categoria_id,         
                c.nombre AS categoria_nombre
            FROM 
                Productos p 
            JOIN 
                Categorias c ON p.categoria_id = c.categoria_id
            WHERE 
                p.producto_id = %s;
            """
            val = (producto_id,)
            cursor.execute(sql, val)
            producto = cursor.fetchone()
            return producto          
    except Exception as e:
        print(f"Error al buscar producto en la BD: {e}")
        return None


def actualizar_producto(mydb, datos_producto: dict)->bool:
    """
    Función para actualizar un producto existente en la base de datos.

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_producto -- Diccionario con los datos actualizados del producto.

    Retorna True si la actualización fue exitosa, False en caso contrario.
    """
    
    if datos_producto is None:
        raise ValueError("No se proporcionaron datos para actualizar el producto.")

    if not isinstance(datos_producto, dict):
        raise ValueError("Los datos del producto deben proporcionarse en un diccionario.")

    id_producto = datos_producto["producto_id"]

    if mydb is None or not mydb.is_connected():
        print("Error: Conexión a la base de datos no disponible.")
        return False
    
    try:
        if obtener_producto_por_id(mydb, id_producto) is None:
            print(f"Error: No existe un producto con ID {id_producto}.")
            return False
        
        with mydb.cursor() as cursor:
            sql = """
            UPDATE productos
            SET nombre = %s, descripcion = %s, precio_unitario = %s, stock = %s, categoria_id = %s
            WHERE producto_id = %s
            """
            val = (
                datos_producto["nombre"],
                datos_producto["descripcion"],
                datos_producto["precio_unitario"],
                datos_producto["stock"],
                datos_producto["categoria_id"],
                id_producto
            )
            cursor.execute(sql, val)
            mydb.commit()
            return True
    except Exception as e:
        print(f"Error al actualizar producto en la BD: {e}")
        return False
    

def eliminar_producto(mydb, producto_id: int)->bool:
    """
    Función para eliminar un producto de la base de datos.
    Retorna True si la eliminación fue exitosa, False en caso contrario.
    """
    if mydb is None or not mydb.is_connected():
        print("Error: Conexión a la base de datos no disponible.")
        return False
    
    if not isinstance(producto_id, int) or producto_id <= 0:
        raise ValueError("El ID del producto debe ser un entero positivo.")
    
    try:
        if obtener_producto_por_id(mydb, producto_id) is None:
            print(f"Error: No existe un producto con ID {producto_id}.")
            return False
        
        with mydb.cursor() as cursor:
            sql = "DELETE FROM productos WHERE producto_id = %s"
            val = (producto_id,)
            cursor.execute(sql, val)
            mydb.commit()
            return True
    except Exception as e:
        print(f"Error al eliminar producto de la BD: {e}")
        return False


