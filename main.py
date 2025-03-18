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
        # Ocultar la pantalla de inicio con un efecto de fade-out
        self.fade_out(self.frame_inicio, self.frame_inicio, self.ventana_principal_fade_in)

    def ventana_principal_fade_in(self):
        # Mostrar la ventana principal con un efecto de fade-in
        self.ventana_principal = VentanaPrincipal(self)
        self.ventana_principal.pack(fill="both", expand=True)
        self.fade_in(self.ventana_principal)

    def mostrar_registro_fade_in(self):
        # Mostrar la ventana de registro con un efecto de fade-in
        from vistas.ventana_registro import RegistroFrame
        self.ventana_registro = RegistroFrame(self, self.ventana_principal.entrada_usuario, self.ventana_principal.entrada_contraseña)
        self.ventana_registro.pack(fill="both", expand=True)
        self.fade_in(self.ventana_registro)

    def mostrar_login_fade_in(self):
        # Mostrar la ventana de login con un efecto de fade-in
        self.ventana_principal.pack(fill="both", expand=True)
        self.fade_in(self.ventana_principal)

    def fade_out(self, widget, frame_to_hide, callback):
        """Efecto de fade-out (desvanecimiento)."""
        alpha = widget.winfo_toplevel().attributes("-alpha")
        if alpha > 0:
            alpha -= 0.05  # Reducir la transparencia
            widget.winfo_toplevel().attributes("-alpha", alpha)
            self.after(50, self.fade_out, widget, frame_to_hide, callback)
        else:
            frame_to_hide.pack_forget()
            callback()

    def fade_in(self, widget):
        """Efecto de fade-in (aparición gradual)."""
        alpha = 0
        widget.winfo_toplevel().attributes("-alpha", alpha)
        widget.pack(fill="both", expand=True)
        self.fade_in_step(widget, alpha)

    def fade_in_step(self, widget, alpha):
        """Paso intermedio para el efecto de fade-in."""
        if alpha < 1:
            alpha += 0.05  # Aumentar la transparencia
            widget.winfo_toplevel().attributes("-alpha", alpha)
            self.after(50, self.fade_in_step, widget, alpha)

if __name__ == "__main__":
    app = MyEconomyApp()
    app.mainloop()
    