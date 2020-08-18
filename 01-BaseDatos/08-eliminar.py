import psycopg2 as pg

conexion = pg.connect(
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s'
#valores = (9,)
entrada = input('Proporciona la pk a eliminar: ')
valores = (entrada,)
cursor.execute(sentencia, valores)

# Guardamos la información en la base de datos
conexion.commit()
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

cursor.close()
conexion.close()