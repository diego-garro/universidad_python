from logger_base import logger
from psycopg2 import pool
import sys

class Conexion:

    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'postgres'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE
                )
                logger.debug(f'Creación de pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.error(f'Error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):
        # Obtener una conexión del pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexión obtenida de pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        # Regresar el objeto conexión al pool
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresando la conexión al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')
    
    @classmethod
    def cerrarConexiones(cls):
        # Cerrar el pool y todas las conexiones
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__pool}')

if __name__ == "__main__":
    # Obtener una conexión a partir del pool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()

    # Regresar las conexiones al pool
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)

    # Cerrar el pool
    Conexion.cerrarConexiones()

    # Si intentamos pedir una nueva conexión con el pool cerrado
    #conexion3 = Conexion.obtenerConexion() # Lanza error si el pool ya está cerrado
