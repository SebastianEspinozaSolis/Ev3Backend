Instrucciones para hacer funcionar el proyecto
1. seleccionar <> Code y en https, copiar la url
2. desde una carpeta abrir la cmd, y escribir git clone + la url copiada. esto hara una copia del repositorio de forma local para poder hacer funcionar el proyecto
3. abrir la carpeta desde visual studio code, asegurarse de tener la extension de python y crear el entorno virtual, para ello presionar: control + shift + P, y se abrira en la parte superior un buscador, a lo que hay que ingresar python create enviroment -> venv -> version de python -> seleccionar requeriments para que se instalen las librerias que necesita el proyecto
4. con eso instalado, ahora hara falta appserv, en caso de no tener instalada hace falta instalar, en su instalacion es siguiente hasta password, y en el añadir contraseña que sera importante de recordar.
5. con appserv instalado hara falta crear la base de datos, para ello hay que ir al navegador y buscar 127.0.0.1, en ella aparecera un apartado que hay que ingresar phpMyAdmin Database Manager Version, pedira credenciales que seran root como usuario y la contraseña colocada antes al instalar en la contraseña
6. ahora hay que crear una base de datos, luego de eso crear un usuario que tenga acceso a esta base de datos junto a  su contraseña. con eso hecho hay que regresar al proyecto a crear carpetas y archivos.
7. crear carpetas media y static a nivel de manage.py y readme, debido a que al estar vacias las carpetas no estan subidas en el repositorio.
8. crear el archivo .env, en el agregar lo siguiente:
DB_NAME=[nombre de la base de datos]
DB_USER=[nombre de el usuario de esa base de datos]
DB_PASSWORD=[contraseña de ese usuario en la base de datos]
9. con el archivo .env configurado con los parametros de la base de datos creada hay que abrir cmd, ingresar python manage.py makemigrations, con esa opcion deberia responder no changes detected, continuar con python manage.py migrate, que deberia crear tablas en la base de datos, python manage.py createsuperuser, que pedira nombre, correo y contraseña, y por ultimo para hacer funcionar la aplicacion python manage.py runserver, con esto hay que hacer control + click izquierdo en http://127.0.0.1:8000/ o abrirlo directo en el navegador
10. se podra crear un usuario entre admin, vendedor y comprador, admin podra ver publicaciones y ver usuarios
11. vendedor podra crear publicaciones para la venta, y tendra su listado de publicaciones
12. comprador podra ver las publicaciones y podra dejar su reseña