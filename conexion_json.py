import json
import mysql.connector

#diccionario con datos
base_datos ={
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "tienda_online",
    "port" : 3306
}

#imprimir
print(base_datos)
#escribir
archivo=open("bd.json", "w")
#guardar json
json.dump(base_datos,archivo)
#cerrar archivo
archivo.close()
#leer json
#escribir
archivo=open("bd.json", "r")
#leer json
contenido= json.load(archivo)
print(contenido)
#cerrar archivo
archivo.close()
#conexion bd

#establecer conexion con la base de datos
conexion = mysql.connector.connect (
    
    host=contenido["host"],
    user=contenido["user"],
    password=contenido["password"],
    database=contenido["database"],
    port=contenido["port"]
    
)

#crear un cursor para generar consultas
cursor = conexion.cursor()
#generar consultas en sql
sql = "SELECT *FROM clientes WHERE id = 1"
#comando
cursor.execute(sql)
#almacenar los datos
sensores = cursor.fetchall()
#recorrer los resultados e imprimirlos
for datos in sensores:
    print(f"datos tienda_online: {datos}")
#cerrar el cursor y la conexion a bd
cursor.close()
conexion.close()