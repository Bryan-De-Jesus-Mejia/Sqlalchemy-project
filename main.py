import customtkinter as ctk
from styles import setup_style
from views.main_view import MainView

def run():
    root = ctk.CTk()
    root.title("Administrador de Clientes")
    root.geometry("960x560")
    root.minsize(860, 480)

    setup_style(root) 

    MainView(root).pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    run()
