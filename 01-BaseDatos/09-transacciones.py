import psycopg2 as pg

conexion = pg.connect(
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    # Para que se haga el commit en automático, esto solo se hace para pruebas
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Martha', 'Pereira', 'mpereira@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan1', 'Pérez1', 'jperez@mail.com', 1)
    cursor.execute(sentencia, valores)

    # Guardamos la información en la base de datos
    conexion.commit()
except Exception as e:
    #rollback da marcha atrás a todas las operaciones pendientes
    conexion.rollback()
    print(f'Ocurrió un error en la transacción: {e}')
finally:
    cursor.close()
    conexion.close()