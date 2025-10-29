#Importamos el objetos para definir rutas
from flask import Blueprint, request

#importamos la conexion ala base de datos
import utils.db as db
from werkzeug.security import generate_password_hash, check_password_hash


#Construir el objeto para gestionar las rutas
user = Blueprint('user', __name__)

#Definir las rutas con sus funciones
@user.route('/user', methods=['GET'])
def list():
    try:
        conn = db.conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select id_user,name,address,phone,email,per_user,nom_perf from user,perfil where per_user=cod_perf")
        rows = cursor.fetchall()
        return rows 
    except Exception as e:
        return {"error":str(e)},500


#Guardar usuario
@user.route('/user', methods=['POST'])
def save():
    try:
        data = request.json
        conn = db.conexion()
        cursor = conn.cursor() 

        cursor.execute( "insert into user(name,address,phone,email,password,per_user) values(%s,%s,%s,%s,%s,%s)",
        (data['name'],
        data['address'],
        data['phone'],
        data['email'],
        generate_password_hash(data['password']),
        data['per_user']) )
        conn.commit()
        cursor.close()
        return {"message":"Usuario guardado"},201
    except Exception as e:
        return {"error":str(e)},500

    
