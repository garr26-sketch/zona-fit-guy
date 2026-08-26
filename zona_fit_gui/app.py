import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Cliente
from cliente_dao import ClienteDao


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.crear_widgets()
        self.cargar_datos()

    def configurar_ventana(self): #configuramos la ventana en dimensiones, colores y divisiones
        self.title("Zona Fit Gym")
        self.geometry("900x600")
        self.configure(bg="#44E517")
        #Se congifura el grid a partir de acá
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

    def crear_widgets(self):
        self.configurar_estilos()
        self.crear_titulo()
        self.crear_formulario()
        self.crear_tabla()
        self.crear_botones()

    def configurar_estilos(self):
        estilos = ttk.Style()
        estilos.theme_use("clam")
        estilos.configure("Treeview", background="black",
                          foreground="white", fieldbackground="black",
                          rowheight=25)
        estilos.configure("Treeview.Heading", background="#2d4a6e",
                          foreground="white", relief="flat")
        estilos.map("Treeview", background=[("selected", "#3a86ff")])

    def crear_titulo(self):
        titulo = tk.Label(self, text="CMCF Fitness Center",
                          font=("Arial", 30, "bold"),
                          bg="#44E517", fg="white")
        titulo.grid(row=0, column=0, columnspan=2, pady=30)

    def crear_formulario(self):
        frame_form = tk.Frame(self, bg="#44E517")
        frame_form.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        tk.Label(frame_form, text="Nombre:", bg="#44E517",
                 fg="white", font=("Arial", 11))\
            .grid(row=0, column=0, sticky="w", pady=15, padx=5)
        self.entry_nombre = ttk.Entry(frame_form, width=25)
        self.entry_nombre.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Apellido:", bg="#44E517",
                 fg="white", font=("Arial", 11))\
            .grid(row=1, column=0, sticky="w", pady=15, padx=5)
        self.entry_apellido = ttk.Entry(frame_form, width=25)
        self.entry_apellido.grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Membres\u00eda:", bg="#44E517",
                 fg="white", font=("Arial", 11))\
            .grid(row=2, column=0, sticky="w", pady=15, padx=5)
        self.entry_membresia = ttk.Entry(frame_form, width=25)
        self.entry_membresia.grid(row=2, column=1, pady=5)

    def crear_tabla(self):
        frame_tabla = tk.Frame(self, bg="#44E517")
        frame_tabla.grid(row=1, column=1, sticky="nsew", padx=20, pady=5)

        columnas = ("id", "nombre", "apellido", "membresia")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas,
                                  show="headings", height=15)

        #Agregamos los cabeceros de la tabla
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre", anchor=tk.W)
        self.tabla.heading("apellido", text="Apellido", anchor=tk.W)
        self.tabla.heading("membresia", text="Membres\u00eda", anchor=tk.W)

        #Definimos las columnas
        self.tabla.column("id", width=50, anchor=tk.CENTER)
        self.tabla.column("nombre", width=150)
        self.tabla.column("apellido", width=150)
        self.tabla.column("membresia", width=100, anchor=tk.W)

        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Asociar el evento select
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_cliente)

    def crear_botones(self):
        frame_botones = tk.Frame(self, bg="#44E517")
        frame_botones.grid(row=2, column=0, columnspan=2, pady=10)

        btn_guardar = tk.Button(frame_botones, text="Guardar",
                                bg="#3a86ff", fg="white",
                                font=("Arial", 10, "bold"), width=12,
                                command=self.guardar_cliente)
        btn_guardar.pack(side=tk.LEFT, padx=30)
        self.configurar_hover(btn_guardar, "#3a86ff", "#6ba3ff")

        btn_eliminar = tk.Button(frame_botones, text="Eliminar",
                                 bg="#e63946", fg="white",
                                 font=("Arial", 10, "bold"), width=12,
                                 command=self.eliminar_cliente)
        btn_eliminar.pack(side=tk.LEFT, padx=30)
        self.configurar_hover(btn_eliminar, "#e63946", "#f05a65")

        btn_limpiar = tk.Button(frame_botones, text="Limpiar",
                                bg="#457b9d", fg="white",
                                font=("Arial", 10, "bold"), width=12,
                                command=self.limpiar_campos)
        btn_limpiar.pack(side=tk.LEFT, padx=30)
        self.configurar_hover(btn_limpiar, "#457b9d", "#6ba3c4")

    def configurar_hover(self, boton, color_original, color_hover):
        boton.bind("<Enter>", lambda e: boton.configure(bg=color_hover))
        boton.bind("<Leave>", lambda e: boton.configure(bg=color_original))

    #Cargamos los datos de la base de datos
    def cargar_datos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        clientes = ClienteDao.seleccionar()
        if clientes:
            for cliente in clientes:
                self.tabla.insert("", tk.END, values=(
                    cliente.id, cliente.nombre,
                    cliente.apellido, cliente.membresia))

    def seleccionar_cliente(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            valores = self.tabla.item(seleccion[0], "values")
            self.id_cliente = valores[0]
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])
            self.entry_apellido.delete(0, tk.END)
            self.entry_apellido.insert(0, valores[2])
            self.entry_membresia.delete(0, tk.END)
            self.entry_membresia.insert(0, valores[3])

    def guardar_cliente(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        membresia = self.entry_membresia.get().strip()

        if not nombre or not apellido or not membresia:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not membresia.isdigit():
            messagebox.showerror("Error",
                                 "Membres\u00eda debe ser un valor num\u00e9rico")
            return

        if self.id_cliente:
            cliente = Cliente(int(self.id_cliente), nombre,
                              apellido, int(membresia))
            ClienteDao.actualizar(cliente)
            messagebox.showinfo("\u00c9xito",
                                "Cliente actualizado correctamente")
        else:
            cliente = Cliente(None, nombre, apellido, int(membresia))
            ClienteDao.insertar(cliente)
            messagebox.showinfo("\u00c9xito",
                                "Cliente guardado correctamente")

        self.limpiar_campos()
        self.cargar_datos()

    def eliminar_cliente(self):
        if not self.id_cliente:
            messagebox.showerror("Error",
                                 "Selecciona un cliente de la tabla")
            return

        if messagebox.askyesno("Confirmar",
                               "\u00bfEst\u00e1s seguro de eliminar este cliente?"):
            cliente = Cliente(int(self.id_cliente), "", "", 0)
            ClienteDao.eliminar(cliente)
            messagebox.showinfo("\u00c9xito",
                                "Cliente eliminado correctamente")
            self.limpiar_campos()
            self.cargar_datos()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_membresia.delete(0, tk.END)
        self.id_cliente = None
        self.tabla.selection_remove(self.tabla.selection())


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
