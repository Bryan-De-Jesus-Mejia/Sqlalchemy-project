import customtkinter as ctk
from tkinter import ttk
from .client_form import ClientForm

class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Encabezado
        title = ctk.CTkLabel(self, text="Clientes", font=ctk.CTkFont(size=22, weight="bold"))
        title.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        # Contenedor tabla
        table_frame = ctk.CTkFrame(self, corner_radius=12)
        table_frame.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 8))
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

        # Tabla (equivalente DGV)
        columns = ("id", "nombre", "telefono", "email", "estado")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("telefono", text="Teléfono")
        self.tree.heading("email", text="Email")
        self.tree.heading("estado", text="Estado")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("nombre", width=220, anchor="w")
        self.tree.column("telefono", width=150, anchor="center")
        self.tree.column("email", width=260, anchor="w")
        self.tree.column("estado", width=110, anchor="center")

        # Scrollbar
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll_y.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        # Filas demo SOLO para ver la UI
        demo_rows = [
            (1, "Ana Pérez", "809-555-1001", "ana@correo.com", "Activo"),
            (2, "Luis Gómez", "809-555-1002", "luis@correo.com", "Inactivo"),
            (3, "María López", "829-555-1003", "maria@correo.com", "Prospecto"),
        ]
        for r in demo_rows:
            self.tree.insert("", "end", values=r)

        # Barra inferior: acciones
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=2, column=0, sticky="ew", padx=16, pady=(0, 12))
        for i in range(5):
            actions.grid_columnconfigure(i, weight=1)

        # Botones (sin lógica de datos)
        ctk.CTkButton(actions, text="Insertar", height=36,
                        command=self.open_insert_form).grid(row=0, column=0, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Editar", height=36,
                        command=self.open_edit_form).grid(row=0, column=1, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Eliminar", height=36,
                        fg_color="#c23b3b", hover_color="#a82f2f",
                        command=lambda: None).grid(row=0, column=2, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Refrescar", height=36,
                        command=lambda: None).grid(row=0, column=3, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Cerrar", height=36,
                        command=self.master.destroy).grid(row=0, column=4, padx=6, pady=4, sticky="ew")

    # --- Navegación a formularios (solo UI) ---
    def open_insert_form(self):
        ClientForm(self, mode="insert")

    def open_edit_form(self):
        # Se podría pasar valores seleccionados; por ahora se abre vacío (UI only)
        selected = self.tree.focus()
        initial_values = self.tree.item(selected, "values") if selected else None
        ClientForm(self, mode="edit", initial_values=initial_values)
