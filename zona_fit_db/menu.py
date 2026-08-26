from zona_fit_db.cliente import Cliente
from zona_fit_db.cliente_dao import ClienteDao


class MenuClientes:
    def __init__(self):
        self.cliente_dao = ClienteDao()

    def iniciar_menu(self):
        salir = False
        print("\n\t*** ZONA FIT (MENÚ) ***")
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"\nOcurrió un error: {e}.")

    def mostrar_menu(self):
        print("""
        1. Listar clientes
        2. Agregar cliente
        3. Modificar cliente
        4. Eliminar cliente
        5. Salir""")
        return int(input("Elige una opción: "))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.listar_clientes()
        elif opcion == 2:
            self.agregar_cliente()
        elif opcion == 3:
            self.modificar_cliente()
        elif opcion == 4:
            self.eliminar_cliente()
        elif opcion == 5:
            print("¡Hasta luego!")
            return True
        else:
            print(f"Opción no válida: {opcion}.")
        return False

    def listar_clientes(self):
        clientes = self.cliente_dao.seleccionar()
        print("\n\t Lista de clientes:")
        for cliente in clientes:
            print(cliente)

    def agregar_cliente(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        membresia = int(input("Membresía: "))
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        self.cliente_dao.insertar(cliente)
        print("\tCliente añadido exitosamente.")

    def modificar_cliente(self):
        id = int(input("Id del cliente a modificar: "))
        clientes = self.cliente_dao.seleccionar()
        cliente_original = next((c for c in clientes if c.id == id), None)
        if not cliente_original:
            print(f"\tNo se encontró cliente con id {id}.")
            return
        print(f"\tDatos actuales: {cliente_original}")
        print("""\t¿Qué información quieres modificar?:
        1. Nombre.
        2. Apellido.
        3. Membresía.""")
        opcion = int(input("Elige una opción: "))
        nombre = cliente_original.nombre
        apellido = cliente_original.apellido
        membresia = cliente_original.membresia
        if opcion == 1:
            nombre = input("Nuevo nombre: ")
        elif opcion == 2:
            apellido = input("Nuevo apellido: ")
        elif opcion == 3:
            membresia = int(input("Nueva membresía: "))
        else:
            print("\tOpción no válida.")
            return
        cliente = Cliente(id, nombre, apellido, membresia)
        self.cliente_dao.actualizar(cliente)
        print("\tCliente actualizado exitosamente.")

    def eliminar_cliente(self):
        id = int(input("Id del cliente a eliminar: "))
        cliente = Cliente(id=id)
        self.cliente_dao.eliminar(cliente)
        print("\tCliente eliminado exitosamente.")


if __name__ == '__main__':
    menu = MenuClientes()
    menu.iniciar_menu()
