import psycopg2 as pg

conexion = pg.connect(
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona las pk a buscas (separado por comas): ")
tupla = tuple(entrada.split(','))
print(tupla)
llaves_primarias = (tupla,)
cursor.execute(sentencia, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()