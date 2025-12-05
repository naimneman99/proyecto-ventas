
import mysql.connector
from mysql.connector import Error


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


def modificar_valor_producto(mydb, producto_id, cantidad_maxima):
    """
    Llama al procedimiento almacenado 'ModificarCantidadOrdenesSegura' para ajustar la cantidad máxima del producto 
    en las órdenes. Manejando errores y transacciones.
    """
    try:
        with mydb.cursor() as cursor:
        
            # Llamada al procedimiento almacenado
            cursor.execute("CALL ModificarCantidadOrdenesSegura(%s, %s)", (producto_id, cantidad_maxima))
            print(f"Ordenes del Producto con id: {producto_id}, ajustadas con éxito a {cantidad_maxima}.")

    except mysql.connector.Error as err:
        print(f"Error al modificar la cantidad máxima del producto con id {producto_id}:")
        print(f"Detalle: {err}")
        print("La transacción ha sido revertida (ROLLBACK) para mantener la integridad.")

    except Exception as e:
        # 4. Manejo de otros errores (p. ej., de tipo en Python)
        print(f"Error al modificar la cantidad máxima del producto: {e}")

    