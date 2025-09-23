import customtkinter as ctk
from styles import setup_style
from views.main_view import MainView

def main():
    setup_style()

    app = ctk.CTk()
    app.title("Administrador de Clientes")
    app.geometry("960x560")
    app.minsize(860, 480)

    MainView(app).pack(fill="both", expand=True)

    app.mainloop()

if __name__ == "__main__":
    main()
