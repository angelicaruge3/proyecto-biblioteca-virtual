import mysql.connector

conexion = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="",
    database = "tienda_online",
    port=3306
)

cursor=conexion.cursor()

sql = "SELECT *FROM clientes"

cursor.execute(sql)

sensores = cursor.fetchall()

for datos in sensores:
    print(f"datos tienda_online: {datos}")
    
cursor.close()
conexion.close()