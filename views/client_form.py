import customtkinter as ctk
from codes.insert import insert_cliente
from codes.edit import update_cliente

class ClientForm(ctk.CTkToplevel):
    def Insertar(self):
        nombre  = self.inp_nombre.get()
        telefono = self.inp_telefono.get()
        email   = self.inp_email.get()
        estado  = self.cbo_estado.get()
        insert_cliente(nombre, telefono, email, estado)
        print("Cliente insertado")
        self.load_clients()

    def Editar(self):
        id = self.inp_id.get()
        nombre  = self.inp_nombre.get()
        telefono = self.inp_telefono.get()
        email   = self.inp_email.get()
        estado  = self.cbo_estado.get()
        update_cliente(id, nombre, telefono, email, estado)
        print("Cliente Editado")
        self.load_clients()
    """
    Ventana de formulario para Insertar/Editar clientes.
    El campo ID se muestra pero no es editable.
    """
    def __init__(self, master, mode="insert", initial_values=None):
        super().__init__(master)
        self.title("Nuevo Cliente" if mode == "insert" else "Editar Cliente")
        self.geometry("520x460")
        self.minsize(480, 420)

        # Modal simple
        self.grab_set()
        self.focus_force()

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

        # --- Campo ID ---
        ctk.CTkLabel(form, text="ID").grid(row=0, column=0, sticky="w", padx=12, pady=(12, 4))
        self.inp_id = ctk.CTkEntry(form, placeholder_text="")
        self.inp_id.grid(row=0, column=1, sticky="ew", padx=12, pady=(12, 4))
        self.inp_id.insert(0, "auto")
        self.inp_id.configure(state="disabled")

        # --- Campos editables ---
        self.inp_nombre = _labeled_entry(form, "Nombre", 1, placeholder_text="Nombre completo")
        self.inp_telefono = _labeled_entry(form, "Teléfono", 2, placeholder_text="809-000-0000")
        self.inp_email = _labeled_entry(form, "Email", 3, placeholder_text="correo@dominio.com")

        ctk.CTkLabel(form, text="Estado").grid(row=4, column=0, sticky="w", padx=12, pady=(12, 4))
        self.cbo_estado = ctk.CTkOptionMenu(form, values=["Activo", "Inactivo", "Prospecto"])
        self.cbo_estado.grid(row=4, column=1, sticky="ew", padx=12, pady=(12, 4))

        ctk.CTkLabel(form, text="Notas").grid(row=5, column=0, sticky="nw", padx=12, pady=(12, 4))
        self.txt_notas = ctk.CTkTextbox(form, height=120)
        self.txt_notas.grid(row=5, column=1, sticky="nsew", padx=12, pady=(12, 12))

        # --- Valores iniciales (modo Editar) ---
        if initial_values:
            try:
                _id, nombre, tel, email, estado = initial_values

                self.inp_id.configure(state="normal")
                self.inp_id.delete(0, "end")
                self.inp_id.insert(0, str(_id))
                self.inp_id.configure(state="disabled")

                self.inp_nombre.insert(0, nombre)
                self.inp_telefono.insert(0, tel)
                self.inp_email.insert(0, email)
                if estado in ["Activo", "Inactivo", "Prospecto"]:
                    self.cbo_estado.set(estado)
            except Exception:
                pass

        
        # --- Barra inferior ---
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=2, column=0, sticky="ew", padx=16, pady=(0, 16))
        actions.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkButton(actions, text="Guardar", height=36,
                        command=lambda:self.Insertar() if mode == "insert" else  self.Editar()).grid(row=0, column=0, padx=6, sticky="ew")
        
        if mode == "insert":
            ctk.CTkButton(actions, text="Limpiar", height=36,
                            command=lambda: self._clear()).grid(row=0, column=1, padx=6, sticky="ew")
        ctk.CTkButton(actions, text="Cancelar", height=36,
                        fg_color="#444", hover_color="#333",
                        command=self.destroy).grid(row=0, column=2, padx=6, sticky="ew")

    def _clear(self):
        # Resetear ID a "auto"
        self.inp_id.configure(state="normal")
        self.inp_id.delete(0, "end")
        self.inp_id.insert(0, "auto")
        self.inp_id.configure(state="disabled")

        # Limpiar otros campos
        for w in (self.inp_nombre, self.inp_telefono, self.inp_email):
            w.delete(0, "end")
        self.cbo_estado.set("Activo")
        self.txt_notas.delete("1.0", "end")


def _labeled_entry(parent, label, row, placeholder_text=""):
    ctk.CTkLabel(parent, text=label).grid(row=row, column=0, sticky="w", padx=12, pady=(12, 4))
    entry = ctk.CTkEntry(parent, placeholder_text=placeholder_text)
    entry.grid(row=row, column=1, sticky="ew", padx=12, pady=(12, 4))
    return entry

