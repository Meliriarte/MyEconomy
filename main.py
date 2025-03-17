import tkinter as tk
from PIL import Image, ImageTk  # Necesitas instalar Pillow: pip install pillow
from vistas.ventana_principal import VentanaPrincipal

class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry("500x500")
        self.configure(bg="#000000")  # Fondo negro

        # Centrar la ventana en la pantalla
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"+{x}+{y}")

        # Crear un Frame para la pantalla de inicio
        self.frame_inicio = tk.Frame(self, bg="#000000")
        self.frame_inicio.pack(fill="both", expand=True)

        # Cargar el logo
        try:
            imagen_logo = Image.open("datos/imagenes/logo1.png")  # Ruta corregida del logo
            imagen_logo = imagen_logo.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensionar el logo
            self.logo = ImageTk.PhotoImage(imagen_logo)
            etiqueta_logo = tk.Label(self.frame_inicio, image=self.logo, bg="#000000")
            etiqueta_logo.image = self.logo  # Evitar que la imagen sea eliminada por el recolector de basura
            etiqueta_logo.pack(expand=True)  # Centrar el logo en el Frame
        except FileNotFoundError:
            print("El archivo del logo no se encontró.")

        # Cambiar a la ventana principal después de 3 segundos
        self.after(3000, self.mostrar_ventana_principal)

    def mostrar_ventana_principal(self):
        # Ocultar la pantalla de inicio
        self.frame_inicio.pack_forget()

        # Mostrar la ventana principal
        self.ventana_principal = VentanaPrincipal(self)
        self.ventana_principal.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MyEconomyApp()
    app.mainloop()