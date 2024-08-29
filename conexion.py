import mysql.connector
from mysql.connector import Error

def conexion_base():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Diaz',
            user='root',
            password='12062007'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
