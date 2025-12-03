

import mysql.connector


def obtener_orden_por_cliente(mydb, cliente_id: int) -> list[dict]:

    """
    Obtiene todas las órdenes asociadas a un cliente específico.

    Parámetros:
    mydb -- Conexión a la base de datos.
    cliente_id -- ID del cliente cuyas órdenes se desean obtener.

    Retorna:
    Una lista de diccionarios con las órdenes del cliente o vacio si no tiene órdenes.
    """

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    if not isinstance(cliente_id, int):
        raise ValueError("El ID del cliente debe ser un número entero.")
    
    try:
        with mydb.cursor(dictionary=True) as cursor: # Usar dictionary=True para obtener resultados como dict
            
            sql = """
            SELECT
                -- Información del Cliente
                CONCAT(c.nombre, ' ', c.apellido) AS nombre_completo_cliente,
                
                -- Información de la Orden
                o.orden_id,
                o.fecha,
                o.tipo_pago,
                o.estado,
                o.monto_total,
                
                -- Información del Producto en el Detalle
                p.nombre AS nombre_producto,
                p.descripcion AS descripcion_producto,
                d.cantidad,
                d.precio_al_momento
            FROM
                Ordenes o
            JOIN 
                Clientes c ON o.cliente_id = c.cliente_id
            JOIN 
                DetallesOrden d ON o.orden_id = d.orden_id
            JOIN 
                Productos p ON d.producto_id = p.producto_id
            WHERE 
                o.cliente_id = %s;
            """
            
            cursor.execute(sql, (cliente_id,))
            ordenes = cursor.fetchall()
            
            if not ordenes:
                return []
            
            return ordenes
            
    except mysql.connector.Error as err:
        print(f"Error al obtener las órdenes del cliente {cliente_id}: {err}")
        return []
    except Exception as e:
        print(f"Error inesperado al consultar órdenes: {e}")
        return []
    


def obtener_productos_mas_vendidos(mydb, limite: int = 5) -> list[dict]:
    """
    Obtiene los productos más vendidos basándose en la cantidad total vendida.

    Parámetros:
    mydb -- Conexión a la base de datos.
    limite -- Número máximo de productos a retornar (por defecto 5).

    Retorna:
    Una lista de diccionarios con los productos.
    """

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    if not isinstance(limite, int) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo.")
    
    try:

        with mydb.cursor(dictionary=True) as cursor:
            sql = """
            SELECT 
                p.producto_id,
                p.nombre AS nombre_producto,
                SUM(d.cantidad) AS total_vendido
            FROM 
                DetallesOrden d
            JOIN 
                Productos p ON d.producto_id = p.producto_id
            GROUP BY 
                p.producto_id, p.nombre
            ORDER BY 
                total_vendido DESC
            LIMIT %s;
            """
            cursor.execute(sql, (limite,))
            productos = cursor.fetchall()

            if not productos:
                return []

            return productos
    except mysql.connector.Error as err:
        print(f"Error al obtener los productos más vendidos: {err}")
        return []
    except Exception as e:
        print(f"Error inesperado al consultar productos más vendidos: {e}")
        return []
    

def obtener_clientes_con_mas_ordenes(mydb, limite: int = 5) -> list[dict]:
    """
    Obtiene los clientes que han realizado más órdenes.

    Parámetros:
    mydb -- Conexión a la base de datos.
    limite -- Número máximo de clientes a retornar (por defecto 5).

    Retorna:
    Una lista de diccionarios con los clientes.
    """

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    if not isinstance(limite, int) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo.")
    
    try:
        with mydb.cursor(dictionary=True) as cursor:
            sql = """
            SELECT 
                c.cliente_id,
                CONCAT(c.nombre, ' ', c.apellido) AS nombre_completo,
                COUNT(o.orden_id) AS total_ordenes
            FROM 
                Clientes c
            JOIN 
                Ordenes o ON c.cliente_id = o.cliente_id
            GROUP BY 
                c.cliente_id, c.nombre, c.apellido
            ORDER BY 
                total_ordenes DESC
            LIMIT %s;
            """
            cursor.execute(sql, (limite,))
            clientes = cursor.fetchall()

            if not clientes:
                return []

            return clientes
        
    except mysql.connector.Error as err:
        print(f"Error al obtener los clientes con más órdenes: {err}")
        return []
    except Exception as e:
        print(f"Error inesperado al consultar clientes con más órdenes: {e}")
        return []


def modificar_cantidad_orden_producto(mydb, producto_id: int, cantidad_maxima: int) -> dict:
    """
    Modifica la cantidad de un producto en las órdenes que exceden una cantidad máxima.
    """

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")


    try:
        # Identificar órdenes con cantidades que exceden la cantidad máxima
        ordenes_a_recalcular = obtener_ordenes_afectadas(mydb, producto_id, cantidad_maxima)
        
        if not ordenes_a_recalcular:
            # Si no hay nada que corregir, salimos
            print("No se encontraron órdenes que excedan la cantidad máxima. No se requiere corrección.")
            return {"actualizados": 0, "recalculados": 0}
            
        # 2. Ajustar la cantidad en DetallesOrden
        filas_actualizadas = ajustar_detalle_orden(mydb, producto_id, cantidad_maxima)
        
        if filas_actualizadas == 0:
            # Esto puede pasar si las órdenes ya fueron corregidas o la consulta falló.
            return {"actualizados": 0, "recalculados": 0}

        # 3. Recalcular el Monto Total de las órdenes afectadas
        filas_recalculadas = recalcular_monto_orden(mydb, ordenes_a_recalcular)
        
        # 4. Confirmar la Transacción
        mydb.commit()
        
        return {
            "actualizados": filas_actualizadas, 
            "recalculados": filas_recalculadas
        }

    except Exception as e:
        # Si algo falla en cualquier parte del proceso, hacemos rollback
        print(f"Fallo crítico en la modificación de órdenes. Revirtiendo cambios. Error: {e}")
        mydb.rollback()
        return {"actualizados": 0, "recalculados": 0}
    
def obtener_ordenes_afectadas(mydb, producto_id: int, cantidad_maxima: int) -> set:
    """
    Obtiene los orden_id únicos que tienen el producto con cantidad > máxima.
    
    Parámetros:
    mydb -- Conexión a la base de datos.
    producto_id -- ID del producto a verificar.
    cantidad_maxima -- Cantidad máxima permitida para el producto.

    Retorna:
    Un conjunto de IDs de órdenes a modificar.
    """
    
    ordenes_a_recalcular = set()
    try:
        with mydb.cursor() as cursor:
            sql_select = """
            SELECT DISTINCT orden_id 
            FROM DetallesOrden 
            WHERE producto_id = %s AND cantidad > %s;
            """
            cursor.execute(sql_select, (producto_id, cantidad_maxima))
            for (orden_id,) in cursor.fetchall():
                ordenes_a_recalcular.add(orden_id)
        return ordenes_a_recalcular
    except mysql.connector.Error as err:
        print(f"Error al obtener IDs de órdenes afectadas: {err}")
        return set()

def ajustar_detalle_orden(mydb, producto_id: int, cantidad_maxima: int) -> int:
    """Actualiza la cantidad del producto al límite máximo. Retorna filas afectadas."""
    try:
        with mydb.cursor() as cursor:
            sql_update_detalle = """
            UPDATE DetallesOrden
            SET cantidad = %s 
            WHERE producto_id = %s 
              AND cantidad > %s;
            """
            cursor.execute(sql_update_detalle, (cantidad_maxima, producto_id, cantidad_maxima))
            return cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Error al actualizar la cantidad en DetallesOrden: {err}")
        return 0

def recalcular_monto_orden(mydb, ordenes_ids: set) -> int:
    """Recalcula el monto_total para las órdenes dadas. Retorna filas recalculadas."""
    if not ordenes_ids:
        return 0
        
    try:
        with mydb.cursor() as cursor:
            # Consulta para recalcular y actualizar el Monto Total de una Orden
            sql_recalc_template = """
            UPDATE Ordenes o
            SET monto_total = (
                SELECT SUM(d.cantidad * d.precio_al_momento)
                FROM DetallesOrden d
                WHERE d.orden_id = o.orden_id
            )
            WHERE o.orden_id IN ({});
            """
            
            # Formatea la consulta para incluir los IDs de forma segura
            placeholders = ', '.join(['%s'] * len(ordenes_ids))
            sql_recalc = sql_recalc_template.format(placeholders)

            cursor.execute(sql_recalc, tuple(ordenes_ids))
            return cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Error al recalcular Monto Total: {err}")
        return 0