#Importamos el objetos para definir rutas
from flask import Blueprint, request, jsonify

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from datetime import datetime, timedelta

#importamos la conexion a la base de datos
import utils.db as db
from werkzeug.security import generate_password_hash, check_password_hash


#Construir el objeto para gestionar las rutas
user = Blueprint('user', __name__)

#Definir las rutas con sus funciones
@user.route('/user', methods=['GET'])
#Opcion para proteger la rutas el usuario debe estar logeado y enviar token para que ingrese a las rutas
@jwt_required()
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
#Opcion para proteger la rutas
@jwt_required()
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

    
#Buscar usuario por ID
@user.route('/user/<int:id>', methods=['GET'])
#Opcion para proteger la rutas
@jwt_required()
def get(id):
    try:
        conn = db.conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select id_user,name,address,phone,email,per_user,nom_perf from user,perfil where per_user=cod_perf and id_user=%s",(id,))
        row = cursor.fetchone()
        return row
    except Exception as e:
        return {"error":str(e)},500
    
#Actualizar un usuario
@user.route('/user/<int:id>', methods=['PUT'])
#Opcion para proteger la rutas
@jwt_required()
def update(id):
    try:
        data = request.json
        conn = db.conexion()
        cursor = conn.cursor()
        cursor.execute("update user set name=%s,address=%s,phone=%s,email=%s,password=%s,per_user=%s where id_user=%s",
        (data['name'],
        data['address'],
        data['phone'],
        data['email'],
        generate_password_hash(data['password']),
        data['per_user'],
        id))
        conn.commit()
        cursor.close()
        return {"message":"Usuario actualizado"}
    except Exception as e:
        return {"error":str(e)},500

#Eliminar un usuario
@user.route('/user/<int:id>', methods=['DELETE'])
#Opcion para proteger la rutas
@jwt_required()
def delete(id):
    try:
        conn = db.conexion()
        cursor = conn.cursor()
        cursor.execute("delete from user where id_user=%s",(id,))
        conn.commit()
        cursor.close()
        return {"message":"Usuario eliminado"}
    except Exception as e:
        return {"error":str(e)},500

#Función para realizar el inicio de sesion
@user.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        conn = db.conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select id_user,name,email,per_user,nom_perf,password from user,perfil where per_user=cod_perf and email=%s",(data['email'],))
        row = cursor.fetchone()
        if row and check_password_hash(row['password'],data['password']):
            access_token = create_access_token(
            identity=row['name'],
            expires_delta=timedelta(minutes=30),
            additional_claims={"role": row['nom_perf']}
            )


            return jsonify(access_token=access_token)
        else:
            return {"error":"Login o password incorecto"},401
    except Exception as e:
        return {"error":str(e)},500