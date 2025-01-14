#SE EJECUTA SOLO UNA VEZ PARA LA CREACION Y LA CONEXION DE LA BASE DE DATOS

from mysql import connector

dataBase = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_basic")

print("Todo Bien!")