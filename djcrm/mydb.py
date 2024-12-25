from mysql import connector

dataBase = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_basic")

print("Todo Bien!")