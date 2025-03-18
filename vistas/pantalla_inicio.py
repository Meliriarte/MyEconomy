import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesitas instalar Pillow: pip install pillow

class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry("500x700")  # Tamaño de la ventana
        self.configure(bg="#000000")  # Fondo negro

        # Fuente Sans Serif
        self.fuente = ("Sans Serif", 12)

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
            imagen_logo = Image.open("datos/imagenes/logo1.png")  # Ruta del logo
            imagen_logo = imagen_logo.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensionar el logo
            self.logo = ImageTk.PhotoImage(imagen_logo)
            etiqueta_logo = tk.Label(self.frame_inicio, image=self.logo, bg="#000000")
            etiqueta_logo.image = self.logo  # Evitar que la imagen sea eliminada por el recolector de basura
            etiqueta_logo.pack(pady=20)  # Centrar el logo en el Frame
        except FileNotFoundError:
            print("El archivo del logo no se encontró.")

        # Cargar la imagen personalizada
        try:
            imagen_personalizada = Image.open("datos/imagenes/fondo_login.png")  # Ruta de tu imagen
            imagen_personalizada = imagen_personalizada.resize((300, 300), Image.Resampling.LANCZOS)  # Redimensionar la imagen
            self.imagen_personalizada = ImageTk.PhotoImage(imagen_personalizada)
            etiqueta_imagen = tk.Label(self.frame_inicio, image=self.imagen_personalizada, bg="#000000")
            etiqueta_imagen.image = self.imagen_personalizada  # Evitar que la imagen sea eliminada por el recolector de basura
            etiqueta_imagen.pack(pady=20)  # Centrar la imagen en el Frame
        except FileNotFoundError:
            print("El archivo de la imagen personalizada no se encontró.")

        # Crear un Frame para el formulario de login
        frame_login = tk.Frame(self.frame_inicio, bg="#000000")
        frame_login.pack(pady=20)

        # Campo de usuario
        etiqueta_usuario = tk.Label(frame_login, text="Usuario:", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_usuario.grid(row=0, column=0, pady=5, sticky="e")
        self.entrada_usuario = tk.Entry(frame_login, bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_usuario.grid(row=0, column=1, pady=5, sticky="w")

        # Campo de contraseña
        etiqueta_contraseña = tk.Label(frame_login, text="Contraseña:", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_contraseña.grid(row=1, column=0, pady=5, sticky="e")
        self.entrada_contraseña = tk.Entry(frame_login, show="*", bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_contraseña.grid(row=1, column=1, pady=5, sticky="w")

        # Botón de inicio de sesión
        boton_inicio_sesion = tk.Button(frame_login, text="Iniciar Sesión", command=self.al_iniciar_sesion, bg="#32CD32", fg="#FFFFFF", font=self.fuente)
        boton_inicio_sesion.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón de registro
        boton_registro = tk.Button(frame_login, text="Registrarse", command=self.mostrar_registro, bg="#32CD32", fg="#FFFFFF", font=self.fuente)
        boton_registro.grid(row=3, column=0, columnspan=2, pady=10)

    def al_iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        # Aquí puedes agregar la lógica de autenticación
        if usuario == "admin" and contraseña == "1234":
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def mostrar_registro(self):
        # Aquí puedes agregar la lógica para mostrar la ventana de registro
        messagebox.showinfo("Registro", "Redirigiendo a la ventana de registro...")

if __name__ == "__main__":
    app = MyEconomyApp()
    app.mainloop()