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
    cursor.execute("SELECT * FROM menu ORDER BY father, id")
    rows = cursor.fetchall()
    
    menu_items = {item['id']: item for item in rows}
    
    root_items = []
    
    for item in rows:
        if item['father'] is 0:
            root_items.append(item)
        else:
            parent = menu_items.get(item['father'])
            if parent:
                if 'items' not in parent:
                    parent['items'] = []
                parent['items'].append(item)
                
    return root_items