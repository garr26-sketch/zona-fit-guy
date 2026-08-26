import os

from dotenv import load_dotenv
from mysql.connector import pooling
from mysql.connector import Error

load_dotenv()

class Conexion:
    DATABASE = os.getenv('ZONA_FIT_DB_NAME', 'zona_fit_db')
    USERNAME = os.getenv('ZONA_FIT_DB_USER', 'root')
    PASSWORD = os.getenv('ZONA_FIT_DB_PASSWORD')
    DB_PORT = int(os.getenv('ZONA_FIT_DB_PORT', '3306'))
    HOST = os.getenv('ZONA_FIT_DB_HOST', '127.0.0.1')
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None


    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size= cls.POOL_SIZE,
                    host= cls.HOST,
                    port= cls.DB_PORT,
                    database= cls.DATABASE,
                    user= cls.USERNAME,
                    password= cls.PASSWORD,
                )
                return cls.pool

            except Error as e:
                print(f'\nOcurrió un error al obtener pool: {e}.')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__': #Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion_1 = pool.get_connection()
    print(conexion_1)
    Conexion.liberar_conexion(conexion_1)
    print('\nSe ha cerrado la conexión.')
