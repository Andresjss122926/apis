import sqlite3

# Ruta a la base de datos
DB_PATH = "/home/user/apis/Chinook_Sqlite.sqlite"
def get_db_connection():
    """
    DATABASE hola María GM teamo <3
    """
    try:
        # Establecer conexión a la base de datos
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row  # Permite acceder a columnas por nombres
        print("Conexión exitosa a la base de datos.")
        return connection
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
