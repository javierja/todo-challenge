<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
# TaskApp

Esta app permite el manejo de tareas y gestion de usuarios que tienen acceso a la misma, desde el lado del backend. 
Cuenta con la autenticación por JWT para brindar las validaciones y seguridad a la aplicación.



## Instalación:

Para poder correr la app se necesitara lo siguiente

- [x] Python -> https://www.python.org/downloads/
- [x] Django -> python -m pip install Django
- [x] Django Rest Framework -> pip install djangorestframework
- [x] Simple JWT -> pip install djangorestframework-simplejwt
- [x] Corsheaders -> pip install django-cors-headers


## Uso de la app:
   
### Correr el servidor
   
Para correr el servidor debera situarse en a carpeta 'taskapp' del proyecto y colocar el script:
   
python manage.py runserver
   
### Creación del usuario

Para poder hacer uso de la aplicación lo primero que debera hacer es crear un usuario, el mismo se dedera hacer mediante la siguente URL:
   
http://127.0.0.1:8000/users/users/
   
Allí debera enviar la petición por metodo POST con los datos (json) requeridos para crear un nuevo usuario, por ejemplo:
   
 {
        "username": "juanp",
        "name": "Juan",
        "last_name": "Perez",
        "email": "juanperez@gmail.com",
        "password": "1234567"
}
   
- Una vez creado el usuario ya podra loguearse en el sistema para poder ingresar a manejar las tareas.
   
 ### Login 
   
Para hacer uso del sistema deberá estar Logueado, por lo cual deberan hacerlo con los datos correspondiente al usuario creado a la siguente url:
   
http://127.0.0.1:8000/users-login/
   
   
Allí debera enviar la petición por metodo POST con los datos (json) del usuario existente, por ejemplo:
   
{
   
        "email": "juanperez@gmail.com",
        "password": "1234567"
}
   
* El loguin solo requiere de los campos e-mail y password para dar el acceso
   
#### Obtención del JWT

Al loguearse la app devolverá un daccionario con los datos del usuario que se acaba de loguear en los cuales le proporcionara el token de autenticación que debera usar para poder hacer uso de las otra funcionalidades. Ese JWT deberá ser copiado y colocado en nuestro cliente HTTP (ej: postman, thunder client) a traves de tipo de autenticacion BEARER
   
{
    "message": "Logueado Correctamente",
    "jwt": `"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4NDc2NTI3LCJqdGkiOiI5NWE2MzNjZDkyMTA0NDBjOTlkMDM1YjFhYjkwMzEzYiIsInVzZXJfaWQiOjF9.MT6VrRI28SzVt8Y88mwGLyQ4C-en93M6ict5F8AUnLc"`,
    "user_id": 1
}





