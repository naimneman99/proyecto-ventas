

def obtener_todas_categorias(mydb) -> list:
    """
    Consulta la base de datos para obtener la lista de todas las categorías.
    Retorna una lista de tuplas [(id, nombre)] o una lista vacía si falla.
    """
    if mydb is None or not mydb.is_connected():
        print("Error: Conexión a la base de datos no disponible.")
        return []

    try:
        with mydb.cursor() as cursor:
            sql = "SELECT categoria_id, nombre FROM categorias ORDER BY nombre"
            cursor.execute(sql)
            
            categorias = cursor.fetchall()
            
            # El cursor se cierra automáticamente al salir del bloque 'with'
            return categorias          
    except Exception as e:
        print(f"Error al obtener categorías de la BD: {e}")
        # En caso de error, siempre retornamos una lista vacía para evitar fallos
        return []
    