# Importar libreria para conectar con la base de datos
import mysql.connector

#Realizamos funcion para conectar con la base de datos
def conexion():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'admin_pedi',
            password = 'Pedi2025@',
            port = 3307,
            database ='pedido'
        )
        return conn
    
    except Exception as e:
        return {"error":str(e)},500