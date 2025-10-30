#1) Importar librerías necesarias
from flask import Flask
from flask_cors import CORS
from extensions import jwt
from datetime import timedelta

from controllers.menu import menu
from controllers.user import user

#2) Crear la aplicación Flask
app = Flask(__name__)

#3) Configurar CORS para permitir solicitudes desde el frontend
CORS(app)

#4 Configuración JWT
#Clave secreta para el token
SECRET_KEY = "sgs2025"
app.config["JWT_SECRET_KEY"] = SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30) 
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    
#5 Inicializar extensiones
jwt.init_app(app)

#6 Establecer las rutas de los diferentes objetos
app.register_blueprint(menu)
app.register_blueprint(user)


#7) Ruta principal para verificar que el backend está funcionando
@app.route('/')
def home():
    return "Mi primer api rest con Flask funcionando correctamente en python."

#8 ) Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)