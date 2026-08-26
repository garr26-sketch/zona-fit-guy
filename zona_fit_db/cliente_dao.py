from zona_fit_db.cliente import Cliente
from zona_fit_db.conexion import Conexion


class ClienteDao:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s'
    ELIMINAR = 'DELETE FROM cliente WHERE id = %s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #Mapeo de clase tabla-cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f"\nOcurrió un error al seleccionar clientes: {e}.")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"\nOcurrió un error al insertar cliente: {e}.")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) #regresa el cupo a pool

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"\nOcurrió un error al actualizar un cliente: {e}.")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) #regresa el cupo a pool

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"\nOcurrió un error al eliminar un cliente: {e}.")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) #regresa el cupo a pool