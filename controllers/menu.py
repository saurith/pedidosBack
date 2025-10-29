#Importar conexion a la base de datos
import utils.db as db

#Importar objeto o componente para gestionar las rutas
from flask import Blueprint, request

#Construir el objeto para gestionar las rutas
menu = Blueprint('menu', __name__)

#Definir las rutas con sus funciones
@menu.route('/menu', methods=['GET'])
def list():
    conn = db.conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from menu")
    rows = cursor.fetchall()
    return rows 