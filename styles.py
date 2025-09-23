import customtkinter as ctk
from tkinter import ttk

def setup_style(root, appearance: str = "dark", theme: str = "blue"):
    # Apariencia global
    ctk.set_appearance_mode(appearance)
    ctk.set_default_color_theme(theme)

    # ¡IMPORTANTE! Vincular el Style al root existente
    style = ttk.Style(master=root)
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
