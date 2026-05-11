# Estacionamiento El Santo
# Integantes: Bizzotto Gregorio, Oyola Adriano
# Descripcion
   Esta app es una estacionamiento autonomo,permitiendo que los precios se calculen
   automaticamente dependiendo vehiculo y tiempo ocupando un espacio vehicular
# requisitos 
  .python3 
  
  .mysql
# 1 crear y activar el entorno virtual 
  python -m venv <nombre_del_entorno>
  
  <nombre_del_entorno>\Scripts\activate
# 2 clonar el repositorio
  git clone https://github.com/adrianoop03/trabajo1.git
# 3 instalar dependencias y requerimientos
  pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv
  
  pip install -r requirements.txt
# 4 configurar la base de datos 
  MYSQL_USER=<tu_usuario>
  
  MYSQL_PASSWORD=<tu_contraseña>
  
  MYSQL_DATABASE=<nombre_de_la_base_de_datos>
  
  MYSQL_HOST=<host_de_mysql>
# 5 ejecucion 
  python app.py
# aportes por integrantes 
  adriano oyola app base, servidor , base de datos , verificacion de conexion, routes o rutas
  
  Gregorio Bizzotto : modelos vehiculos,cliente, ubicacion
