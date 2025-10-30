# Backend de Pedidos

Este es el backend para el sistema de gestión de pedidos, desarrollado con Flask.

## Descripción

El backend proporciona una API REST para gestionar usuarios, menús y pedidos. Utiliza JWT (JSON Web Token) para la autenticación y se conecta a una base de datos MySQL.

## Instalación

Sigue estos pasos para configurar el entorno de desarrollo:

1.  **Clona el repositorio:**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd backend
    ```

2.  **Crea un entorno virtual:**

    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual:**

    -   En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```
    -   En Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando estando ubicando en el entorno virtual:

```bash
- python app.py 
- flask run
```

Deberían ver una salida que indica que el servidor se está ejecutando en modo de depuración. La API estará disponible en `http://127.0.0.1:5000`. o el puerto que colocaron en app.py

## Dependencias

El proyecto utiliza las siguientes librerías:

-   Flask
-   flask-cors
-   mysql-connector-python
-   Werkzeug
-   flask_jwt_extended

Recueden que le pueden agregar las cosas

* Nota:
- La libreria de conexión a la base de de datos mysql se actualizo de mysql-connector a mysql-connector-python
- Se instaló la libreria flask_jwt_extended para manejar la autenticaciEon de usuarios y se protegieron las rutas
- Se creo un archivo llamado extensions.py para gestionar la libreria de JWT
- Se modifico el menu para que retorne los hijos 
- hace falta una implentación en el login para que retorne el menu segun el perfil.
- Se


