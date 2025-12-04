
import mysql.connector

def agregar_cliente(mydb, datos_cliente)-> bool:
    """
    Agrega un nuevo cliente a la base de datos.

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_cliente -- Diccionario con los datos del cliente a agregar.

    Retorna:
    True si el cliente fue agregado exitosamente, False en caso contrario.
    """

       
    if datos_cliente is None:
        raise ValueError("No se proporcionaron datos para agregar el cliente.")

    # Varificar conexión
    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    try:
        with mydb.cursor() as cursor:

            sql = """
            INSERT INTO clientes (nombre, apellido, domicilio, telefono, correo_electronico)
            VALUES (%s, %s, %s, %s, %s)
            """

            valores_clientes = (
                datos_cliente['nombre'],
                datos_cliente['apellido'],
                datos_cliente['domicilio'],
                datos_cliente['telefono'],
                datos_cliente['correo_electronico']
            )

            cursor.execute(sql, valores_clientes)
            mydb.commit()
            return True
    except Exception as e:
        print(f"Error al agregar el cliente: {e}")
        return False
    

def obtener_todos_clientes(mydb) -> list:
    """
    Consulta la base de datos para obtener la lista de todos los clientes.

    Parámetros:
    mydb -- Conexión a la base de datos.

    Retorna una lista de tuplas con los datos de los clientes o una lista vacía si falla.
    """
    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    try:
        with mydb.cursor() as cursor:
            sql = "SELECT cliente_id, nombre, apellido, domicilio, telefono, correo_electronico FROM clientes"
            cursor.execute(sql)
            clientes = cursor.fetchall()

            if not clientes:
                return []

            return clientes
    except Exception as e:
        print(f"Error al obtener los clientes: {e}")
        return []
    

def obtener_cliente_por_id(mydb, cliente_id: int) -> tuple | None:
    """
    Busca un cliente por su ID en la base de datos.

    Parámetros:
    mydb -- Conexión a la base de datos.
    cliente_id -- ID del cliente a buscar.

    Retorna una tupla con los datos del cliente o None si no se encuentra.
    """
    if mydb is None or not mydb.is_connected():
        print("No hay conexión a la base de datos.")
        return None
    
    if not isinstance(cliente_id, int) or cliente_id <= 0:
        raise ValueError("El ID del cliente debe ser un entero positivo.")
    
    try:
        with mydb.cursor() as cursor:
            sql = "SELECT cliente_id, nombre, apellido, domicilio, telefono, correo_electronico FROM clientes WHERE cliente_id = %s"
            cursor.execute(sql, (cliente_id,))
            cliente = cursor.fetchone()

            if cliente is None:
                return None

            return cliente
    except Exception as e:
        print(f"Error al obtener el cliente: {e}")
        return None


def actualizar_cliente(mydb, datos_cliente: dict) -> bool:
    """
    Actualiza los datos de un cliente en la base de datos.

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_cliente -- Diccionario con los datos del cliente a actualizar.

    Retorna:
    True si el cliente fue actualizado exitosamente, False en caso contrario.
    """

    if not isinstance(datos_cliente, dict):
        raise ValueError("No se proporcionaron datos para actualizar el cliente.")

    cliente_id = datos_cliente["cliente_id"]

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    try:
        if obtener_cliente_por_id(mydb, cliente_id) is None:
            print(f"Error: No existe un cliente con ID {cliente_id}.")
            return False
        
        with mydb.cursor() as cursor:
            sql = """
            UPDATE clientes
            SET nombre = %s, apellido = %s, domicilio = %s, telefono = %s, correo_electronico = %s
            WHERE cliente_id = %s
            """
            val = (
                datos_cliente["nombre"],
                datos_cliente["apellido"],
                datos_cliente["domicilio"],
                datos_cliente["telefono"],
                datos_cliente["correo_electronico"],
                cliente_id
            )
            cursor.execute(sql, val)
            mydb.commit()
            return True
    except Exception as e:
        print(f"Error al actualizar el cliente: {e}")
        return False

def actualizar_contacto(mydb, datos_contacto: dict) -> bool:
    """
    Actualiza los datos de contacto de un cliente en la base de datos.

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_contacto -- Diccionario con los datos de contacto del cliente a actualizar.

    Retorna:
    True si el cliente fue actualizado exitosamente, False en caso contrario.
    """

    if not isinstance(datos_contacto, dict):
        raise ValueError("No se proporcionaron datos para actualizar el cliente.")

    cliente_id = datos_contacto["cliente_id"]

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    try:
        if obtener_cliente_por_id(mydb, cliente_id) is None:
            print(f"Error: No existe un cliente con ID {cliente_id}.")
            return False
        
        with mydb.cursor() as cursor:
            sql = """
            UPDATE clientes
            SET telefono = %s, correo_electronico = %s
            WHERE cliente_id = %s
            """
            val = (
                datos_contacto["telefono"],
                datos_contacto["correo_electronico"],
                cliente_id
            )

            cursor.execute(sql, val)
            mydb.commit()
            return True
    except Exception as e:
        print(f"Error al actualizar el cliente: {e}")
        return False


def obtener_clientes_por_nombre_parcial(mydb, texto_busqueda: str) -> list:
    """
    Busca clientes cuyo nombre o apellido contenga el texto de búsqueda proporcionado.

    Parámetros:
    mydb -- Conexión a la base de datos.
    texto_busqueda -- Texto parcial para buscar en nombres y apellidos.

    Retorna:
    Una lista de tuplas con los datos de los clientes que coinciden con la búsqueda o una lista vacía si no hay coincidencias.
    """

    if mydb is None or not mydb.is_connected():
        raise ConnectionError("No hay conexión a la base de datos.")
    
    if not isinstance(texto_busqueda, str) or not texto_busqueda.strip():
        raise ValueError("El texto de búsqueda debe ser una cadena no vacía.")
    
    try:
        with mydb.cursor() as cursor:
            sql = """
            SELECT cliente_id, nombre, apellido, domicilio, telefono, correo_electronico
            FROM clientes
            WHERE nombre LIKE %s OR apellido LIKE %s
            """
            patron_busqueda = f"%{texto_busqueda}%"
            cursor.execute(sql, (patron_busqueda, patron_busqueda))
            clientes = cursor.fetchall()

            if not clientes:
                return []

            return clientes
    except Exception as e:
        print(f"Error al buscar clientes: {e}")
        return []
    













