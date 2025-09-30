import customtkinter as ctk
from tkinter import ttk
from sqlalchemy import create_engine, MetaData, Table, select
from .client_form import ClientForm
from codes.select import select_cliente


def show_warning(parent, message="Seleccione un cliente para editar"):
    popup = ctk.CTkToplevel(parent)
    popup.overrideredirect(True)
    popup.geometry("380x180")
    popup.resizable(False, False)

    popup.update_idletasks()
    x = parent.winfo_x() + (parent.winfo_width() // 2 - 190)
    y = parent.winfo_y() + (parent.winfo_height() // 2 - 90)
    popup.geometry(f"+{x}+{y}")

    popup.grab_set()

    frame = ctk.CTkFrame(popup, corner_radius=16)
    frame.pack(expand=True, fill="both", padx=2, pady=2)

    label = ctk.CTkLabel(
        frame,
        text=message,
        font=ctk.CTkFont(size=15, weight="bold"),
        justify="center",
        wraplength=300
    )
    label.pack(pady=30, padx=20)

    btn = ctk.CTkButton(frame, text="Aceptar", width=100, command=popup.destroy)
    btn.pack(pady=10)


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Encabezado - Título
        title = ctk.CTkLabel(self, text="Clientes", font=ctk.CTkFont(size=22, weight="bold"))
        title.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        # 🆕 Campo de búsqueda
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Buscar por nombre", width=220)
        self.search_entry.grid(row=0, column=1, sticky="e", padx=16, pady=(16, 8))

        # Contenedor tabla
        table_frame = ctk.CTkFrame(self, corner_radius=12)
        table_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=16, pady=(0, 8))
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

        # Tabla
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

        # Barra inferior
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=3, column=0, columnspan=2, sticky="ew", padx=16, pady=(0, 12))
        for i in range(5):
            actions.grid_columnconfigure(i, weight=1)

        # Botones
        ctk.CTkButton(actions, text="Insertar", height=36,
                        command=self.open_insert_form).grid(row=0, column=0, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Editar", height=36,
                        command=self.open_edit_form).grid(row=0, column=1, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Eliminar", height=36,
                        fg_color="#c23b3b", hover_color="#a82f2f",
                        command=lambda: None).grid(row=0, column=2, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Refrescar", height=36,
                        command=self.load_clients).grid(row=0, column=3, padx=6, pady=4, sticky="ew")

        ctk.CTkButton(actions, text="Cerrar", height=36,
                        command=self.master.destroy).grid(row=0, column=4, padx=6, pady=4, sticky="ew")

        self.load_clients()
    def load_clients(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        result2 = self.select()
        for row in result2:
            self.tree.insert("", "end", values=(row.id, row.nombre, row.telefono, row.email, row.estado))

    def open_insert_form(self):
        ClientForm(self, mode="insert")

    def open_edit_form(self):
        selected = self.tree.focus()
        if not selected:
            show_warning(self, "Seleccione un cliente para editar")
            return

        initial_values = self.tree.item(selected, "values")
        ClientForm(self, mode="edit", initial_values=initial_values)

    def select(self):
        nombre = self.search_entry.get()
        result1 = select_cliente(nombre)
        return result1
