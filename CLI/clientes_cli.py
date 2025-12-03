
def pedir_datos_cliente(mydb, datos_existentes: dict | None = None) -> dict | None:

    """
    Pide los datos del cliente para creación o actualización.

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_existentes -- Diccionario con los datos existentes del cliente (si se está actualizando

    Retorna un diccionario con los datos ingresados.
    """

    if datos_existentes is not None:
        # Estamos en modo actualización
    
        datos_nuevos = {}
        datos_nuevos["cliente_id"] = datos_existentes["cliente_id"]

        print("\n--- ACTUALIZAR CLIENTE ---")
        print("\nIngrese los nuevos datos del cliente (dejar en blanco para mantener el valor actual):")
    else:
        # Estamos en modo creación
        print("\n--- INGRESAR NUEVO CLIENTE ---")
        datos_nuevos = {}

    # PEDIR NOMBRE
    nombre = input("Ingrese el nombre del cliente: ").strip()

    if datos_existentes is None:
        # Si estamos creando Validamos
        while nombre == "":
            print("Error: El nombre no puede estar vacío. Intente de nuevo.")
            nombre = input("Ingrese el nombre del cliente: ").strip()
    else:
        # Si estamos actualizando mantenemos el existente si no se ingresa nada
        if nombre == "":
            nombre = datos_existentes['nombre']

    datos_nuevos['nombre'] = nombre

    # PEDIR APELLIDO
    apellido = input("Ingrese el apellido del cliente: ").strip()
    if datos_existentes is not None and apellido == "":
        apellido = datos_existentes['apellido']
    datos_nuevos['apellido'] = apellido

    # PEDIR DOMICILIO
    domicilio = input("Ingrese el domicilio del cliente: ").strip()
    if datos_existentes is not None and domicilio == "":
        domicilio = datos_existentes['domicilio']
    datos_nuevos['domicilio'] = domicilio

    # PEDIR TELÉFONO
    telefono = input("Ingrese el teléfono del cliente: ").strip()
    if datos_existentes is not None and telefono == "":
        telefono = datos_existentes['telefono']
    datos_nuevos['telefono'] = telefono

    # PEDIR CORREO ELECTRÓNICO
    correo_electronico = input("Ingrese el correo electrónico del cliente: ").strip()
    if datos_existentes is not None and correo_electronico == "":
        correo_electronico = datos_existentes['correo_electronico']
    datos_nuevos['correo_electronico'] = correo_electronico

    return datos_nuevos


def pedir_datos_contacto(mydb, datos_contacto_existentes: dict | None = None) -> dict | None:
    """
    Pide los datos de contacto del cliente (teléfono y correo electrónico) 

    Parámetros:
    mydb -- Conexión a la base de datos.
    datos_contacto_existentes -- Diccionario con los datos de contacto existentes del cliente

    Retorna un diccionario con los datos ingresados.
    """

    if datos_contacto_existentes is None:
        return None

    datos_nuevos = {}

    print("\n--- ACTUALIZAR DATOS DE CONTACTO DEL CLIENTE ---")
    print("\nIngrese los nuevos datos de contacto (dejar en blanco para mantener el valor actual):")

    # PEDIR TELÉFONO
    telefono = input("Ingrese el teléfono del cliente: ").strip()
    if datos_contacto_existentes is not None and telefono == "":
        telefono = datos_contacto_existentes['telefono']
    datos_nuevos['telefono'] = telefono

    # PEDIR CORREO ELECTRÓNICO
    correo_electronico = input("Ingrese el correo electrónico del cliente: ").strip()
    if datos_contacto_existentes is not None and correo_electronico == "":
        correo_electronico = datos_contacto_existentes['correo_electronico']
    datos_nuevos['correo_electronico'] = correo_electronico

    return datos_nuevos
