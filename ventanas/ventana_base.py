import tkinter as tk
from PIL import Image, ImageTk
import os

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

class VentanaBase(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg=COLOR_FONDO)
        self.cargar_fondo()
        
    def cargar_fondo(self):
        try:
            fondo_path = os.path.join("datos", "imagenes", "fondo2.jpg")
            
            if not os.path.exists(fondo_path):
                raise FileNotFoundError(f"No se encontró la imagen: {fondo_path}")
                
            imagen = Image.open(fondo_path)
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            imagen = imagen.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
            
            self.fondo = ImageTk.PhotoImage(imagen)
            
            self.background_label = tk.Label(self, image=self.fondo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.background_label.lower()
            
        except Exception as e:
            print(f"Error al cargar el fondo: {e}")
            self.configure(bg=COLOR_FONDO)