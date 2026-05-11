from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
 
# Obtener la variable de entorno para la configuración de la base de datos
user = os.getenv("db_user")
password = os.getenv("db_pasword")
host = os.getenv("db_host")
database = os.getenv("db_name")

DATABASE_CONNECTION_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"