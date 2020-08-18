import psycopg2 as pg

conexion = pg.connect(
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = (
    ('Carlos', 'Lara', 'clara@mail.com'),
    ('Rosa', 'Madrigal', 'rmadrigal@mail.com'),
    ('Marcela', 'Garro', 'mgarro@mail.com')
)
cursor.executemany(sentencia, valores)

# Guardamos la información en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()