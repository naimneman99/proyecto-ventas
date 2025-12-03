import mysql.connector

def conectar():
    try:
        mybd = mysql.connector.connect(
            host="localhost",                  # Host donde está la base de datos
            port='3306',                       # Puerto de conexión, es el mismo para todos
            user="admin",                       # Nombre del usuario que creamos en MySQL
            password="adminSistemaVentas",      # La contraseña que asignamos a ese usuario
            database="SistemaVentasEnLinea"  # Nombre de la base de datos
        )
        if mybd.is_connected():
            print("Conexión exitosa a la base de datos")
            return mybd
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    return None





def desconectar(mybd):
    if mybd.is_connected():
        mybd.close()
        print("Conexión cerrada")


