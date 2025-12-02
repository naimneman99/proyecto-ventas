
from db import conectar, desconectar
from CLI.menus import menu_inicio

def main():
    # Conectar a la base de datos
    mydb = conectar()
    
    if mydb is None:
        return
    
    # bucle principal de la aplicación
    salir = menu_inicio(mydb) 
    
    if salir:
        print("Programa finalizado.")
        # Desconectar de la base de datos
        desconectar(mydb)

if __name__ == "__main__":
    main()