import customtkinter as ctk
from tkinter import ttk

def setup_style(appearance: str = "dark", theme: str = "blue"):
    # Apariencia global
    ctk.set_appearance_mode(appearance)      # "light" | "dark" | "system"
    ctk.set_default_color_theme(theme)       # "blue" | "green" | "dark-blue"

    # Estilo moderno para Treeview (tabla)
    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "Treeview",
        background="#1f1f1f",
        foreground="#ffffff",
        fieldbackground="#1f1f1f",
        rowheight=28,
        borderwidth=0,
        highlightthickness=0,
    )
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
    style.map("Treeview", background=[("selected", "#0e639c")])
