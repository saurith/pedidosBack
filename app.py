#1) Importar librerías necesarias
from flask import Flask
from flask_cors import CORS

from controllers.menu import menu
from controllers.user import user


#2) Crear la aplicación Flask
app = Flask(__name__)

#3) Configurar CORS para permitir solicitudes desde el frontend
CORS(app)

#5 Establecer las rutas de los diferentes objetos
app.register_blueprint(menu)
app.register_blueprint(user)


#4) Ruta principal para verificar que el backend está funcionando
@app.route('/')
def home():
    return "Mi primer api rest con Flask funcionando correctamente en python."

#5 ) Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)