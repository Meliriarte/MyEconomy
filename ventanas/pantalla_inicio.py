import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from .ventana_base import VentanaBase

# Configuración de estilos
COLOR_PRIMARIO = "#2c3e50"
COLOR_SECUNDARIO = "#3498db"
COLOR_TERCIARIO = "#e74c3c"
COLOR_CUARTO = "#2ecc71"
COLOR_FONDO = "#ecf0f1"
COLOR_TEXTO = "#2c3e50"
COLOR_TEXTO_CLARO = "#ecf0f1"
FUENTE_TITULOS = ("Helvetica", 18, "bold")
FUENTE_SUBTITULOS = ("Helvetica", 14)
FUENTE_TEXTO = ("Helvetica", 12)
FUENTE_BOTONES = ("Helvetica", 12, "bold")

class PantallaInicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        
        center_frame = tk.Frame(self, bg="white")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((300, 300), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(center_frame, image=self.logo, bg="white").pack()
        except FileNotFoundError:
            tk.Label(center_frame, text="MYECONOMY", bg="white", 
                    font=("Helvetica", 48, "bold"), fg=COLOR_PRIMARIO).pack()
        
        tk.Label(center_frame, text="Cargando aplicación...", bg="white", 
                font=FUENTE_SUBTITULOS, fg="#7f8c8d").pack(pady=20)
        
        self.progress = ttk.Progressbar(center_frame, orient="horizontal", 
                                      length=300, mode="determinate")
        self.progress.pack(pady=10)
        self.progress.start()
        
        self.after(3000, lambda: controller.mostrar_ventana("VentanaInicio"))