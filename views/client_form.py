import customtkinter as ctk

class ClientForm(ctk.CTkToplevel):
    """
    Ventana de formulario para Insertar/Editar clientes.
    No tiene funcionalidad de guardado; solo UI.
    mode: "insert" | "edit"
    initial_values: tupla o dict con valores iniciales (opcional)
    """
    def __init__(self, master, mode="insert", initial_values=None):
        super().__init__(master)
        self.title("Nuevo Cliente" if mode == "insert" else "Editar Cliente")
        self.geometry("520x460")
        self.minsize(480, 420)

        # Hacerla tipo modal (simple)
        self.grab_set()
        self.focus()

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkLabel(
            self,
            text="Insertar Cliente" if mode == "insert" else "Editar Cliente",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        header.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        form = ctk.CTkFrame(self, corner_radius=12)
        form.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 8))
        for i in range(2):
            form.grid_columnconfigure(i, weight=1)

        # Campos
        self.inp_id = _labeled_entry(form, "ID", 0, placeholder_text="(auto)")
        self.inp_nombre = _labeled_entry(form, "Nombre", 1, placeholder_text="Nombre completo")
        self.inp_telefono = _labeled_entry(form, "Teléfono", 2, placeholder_text="809-000-0000")
        self.inp_email = _labeled_entry(form, "Email", 3, placeholder_text="correo@dominio.com")

        ctk.CTkLabel(form, text="Estado").grid(row=4, column=0, sticky="w", padx=12, pady=(12, 4))
        self.cbo_estado = ctk.CTkOptionMenu(form, values=["Activo", "Inactivo", "Prospecto"])
        self.cbo_estado.grid(row=4, column=1, sticky="ew", padx=12, pady=(12, 4))

        ctk.CTkLabel(form, text="Notas").grid(row=5, column=0, sticky="nw", padx=12, pady=(12, 4))
        self.txt_notas = ctk.CTkTextbox(form, height=120)
        self.txt_notas.grid(row=5, column=1, sticky="nsew", padx=12, pady=(12, 12))

        # Inicializar valores si llegan (solo visual)
        if initial_values:
            # Si vienen como tupla (desde Treeview)
            try:
                _id, nombre, tel, email, estado = initial_values
                self.inp_id.insert(0, str(_id))
                self.inp_nombre.insert(0, nombre)
                self.inp_telefono.insert(0, tel)
                self.inp_email.insert(0, email)
                if estado in ["Activo", "Inactivo", "Prospecto"]:
                    self.cbo_estado.set(estado)
            except Exception:
                pass

        # Barra inferior
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=2, column=0, sticky="ew", padx=16, pady=(0, 16))
        actions.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkButton(actions, text="Guardar", height=36,
                        command=lambda: None).grid(row=0, column=0, padx=6, sticky="ew")
        ctk.CTkButton(actions, text="Limpiar", height=36,
                        command=lambda: self._clear()).grid(row=0, column=1, padx=6, sticky="ew")
        ctk.CTkButton(actions, text="Cancelar", height=36,
                        fg_color="#444", hover_color="#333",
                        command=self.destroy).grid(row=0, column=2, padx=6, sticky="ew")

    def _clear(self):
        for w in (self.inp_id, self.inp_nombre, self.inp_telefono, self.inp_email):
            w.delete(0, "end")
        self.cbo_estado.set("Activo")
        self.txt_notas.delete("1.0", "end")

def _labeled_entry(parent, label, row, placeholder_text=""):
    ctk.CTkLabel(parent, text=label).grid(row=row, column=0, sticky="w", padx=12, pady=(12, 4))
    entry = ctk.CTkEntry(parent, placeholder_text=placeholder_text)
    entry.grid(row=row, column=1, sticky="ew", padx=12, pady=(12, 4))
    return entry
