import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os  # Importar para verificar la existencia de archivos


def generar_id_usuario(nombre, apellido):
    """Genera un ID único para el usuario basado en las iniciales y un número secuencial."""
    try:
        with open("datos/usuarios.txt", "r") as archivo:
            lineas = archivo.readlines()
            # Obtener las iniciales
            inicial_nombre = nombre[0].upper()
            inicial_apellido = apellido[0].upper()
            prefijo = f"{inicial_nombre}{inicial_apellido}"

            # Encontrar el último número usado para este prefijo
            ultimo_numero = 0
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) >= 6:  # Asegurarnos de que la línea tenga el campo ID
                    id_usuario = datos[0]
                    if id_usuario.startswith(prefijo):
                        try:
                            numero = int(id_usuario[2:])
                            ultimo_numero = max(ultimo_numero, numero)
                        except ValueError:
                            continue

            # Generar el nuevo número
            nuevo_numero = ultimo_numero + 1
            # Formatear el número con ceros a la izquierda (3 dígitos)
            return f"{prefijo}{nuevo_numero:03d}"
    except FileNotFoundError:
        # Si el archivo no existe, empezar desde 001
        return f"{nombre[0].upper()}{apellido[0].upper()}001"


def registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contraseña):
    """Registra un nuevo usuario en el archivo de texto."""
    # Generar ID único
    id_usuario = generar_id_usuario(nombre, apellido)

    # Verificar si el archivo existe, si no, crearlo
    try:
        with open("datos/usuarios.txt", "r"):
            pass
    except FileNotFoundError:
        with open("datos/usuarios.txt", "w"):
            pass

    # Agregar el nuevo usuario
    with open("datos/usuarios.txt", "a") as archivo:
        archivo.write(f"{id_usuario},{nombre},{apellido},{fecha_nacimiento},{usuario},{contraseña}\n")

    return id_usuario


class VentanaBase(tk.Frame):
    """Clase base para otras ventanas que requieren un fondo."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        try:
            # Verificar si el archivo existe antes de intentar abrirlo
            fondo_path = "datos/imagenes/fondo2.jpg"
            if not os.path.exists(fondo_path):
                raise FileNotFoundError(f"Archivo '{fondo_path}' no encontrado.")

            # Intentar cargar el fondo adaptado al tamaño de pantalla completa
            self.fondo_img = Image.open(fondo_path)
            self.fondo_img = self.fondo_img.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()),
                                                   Image.Resampling.LANCZOS)
            self.fondo = ImageTk.PhotoImage(self.fondo_img)
        except FileNotFoundError:
            # Si no se encuentra el archivo, establecer un fondo alternativo
            self.fondo = None
            print(f"Advertencia: no se encontró la imagen '{fondo_path}'. Usando fondo sólido.")

        if self.fondo:
            # Crear la etiqueta de imagen que actúa como fondo, si hay imagen cargada
            self.fondo_label = tk.Label(self, image=self.fondo)
            self.fondo_label.place(relwidth=1, relheight=1)  # Expandir en toda la ventana
        else:
            # Si no hay imagen, usar un color de fondo
            self.config(bg="#FFFFFF")


class VentanaInicio(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Contenido principal
        frame_form = tk.Frame(self, bg="#333333", padx=40, pady=40, relief="solid", borderwidth=2)
        frame_form.pack(pady=100)

        # Título
        tk.Label(frame_form, text="Iniciar Sesión", bg="#333333", fg="white",
                 font=("Sans Serif", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Usuario
        tk.Label(frame_form, text="Usuario:", bg="#333333", fg="white",
                 font=("Sans Serif", 14)).grid(row=1, column=0, pady=10, padx=10)
        self.usuario = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.usuario.grid(row=1, column=1, pady=10, padx=10)

        # Contraseña
        tk.Label(frame_form, text="Contraseña:", bg="#333333", fg="white",
                 font=("Sans Serif", 14)).grid(row=2, column=0, pady=10, padx=10)
        self.password = tk.Entry(frame_form, show="*", font=("Sans Serif", 14), width=25)
        self.password.grid(row=2, column=1, pady=10, padx=10)

        # Botón Iniciar Sesión
        tk.Button(frame_form, text="Iniciar Sesión", command=self.login,
                  bg="#4CAF50", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).grid(row=3, column=0, columnspan=2, pady=20)

        # Botón Registrarse
        tk.Button(self, text="Registrarse", command=lambda: self.controller.mostrar_ventana("VentanaRegistro"),
                  bg="#2196F3", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).pack(pady=20)

    def login(self):
        if self.usuario.get() == "admin" and self.password.get() == "1234":
            self.controller.mostrar_ventana("VentanaPrincipal")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")


class VentanaPrincipal(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Frame principal con borde
        frame_principal = tk.Frame(self, bg="#FFFFFF", padx=40, pady=40, relief="solid", borderwidth=2)
        frame_principal.pack(expand=True)

        # Título
        tk.Label(frame_principal, text="Bienvenido a MyEconomy", 
                 font=("Sans Serif", 24, "bold"), bg="#FFFFFF",
                 fg="black").pack(pady=(0, 30))

        # Botón Cerrar Sesión
        tk.Button(frame_principal, text="Cerrar Sesión", 
                  command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                  bg="#FF5722", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).pack(pady=20)


class VentanaRegistro(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Frame principal con borde
        frame_form = tk.Frame(self, bg="#F0F0F0", padx=40, pady=40, relief="solid", borderwidth=2)
        frame_form.pack(pady=40)

        # Título
        tk.Label(frame_form, text="Registro de Usuario", bg="#F0F0F0",
                 font=("Sans Serif", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 30))

        # Nombre
        tk.Label(frame_form, text="Nombre:", bg="#F0F0F0", 
                 font=("Sans Serif", 14)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.nombre_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.nombre_entry.grid(row=1, column=1, pady=10, padx=10)

        # Apellido
        tk.Label(frame_form, text="Apellido:", bg="#F0F0F0", 
                 font=("Sans Serif", 14)).grid(row=2, column=0, pady=10, padx=10, sticky="e")
        self.apellido_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.apellido_entry.grid(row=2, column=1, pady=10, padx=10)

        # Fecha de nacimiento
        tk.Label(frame_form, text="Fecha de Nacimiento:", bg="#F0F0F0", 
                 font=("Sans Serif", 14)).grid(row=3, column=0, pady=10, padx=10, sticky="e")
        self.fecha_nacimiento_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.fecha_nacimiento_entry.grid(row=3, column=1, pady=10, padx=10)

        # Usuario
        tk.Label(frame_form, text="Usuario:", bg="#F0F0F0", 
                 font=("Sans Serif", 14)).grid(row=4, column=0, pady=10, padx=10, sticky="e")
        self.usuario_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.usuario_entry.grid(row=4, column=1, pady=10, padx=10)

        # Contraseña
        tk.Label(frame_form, text="Contraseña:", bg="#F0F0F0", 
                 font=("Sans Serif", 14)).grid(row=5, column=0, pady=10, padx=10, sticky="e")
        self.contrasena_entry = tk.Entry(frame_form, show="*", font=("Sans Serif", 14), width=25)
        self.contrasena_entry.grid(row=5, column=1, pady=10, padx=10)

        # Botón Registrar
        tk.Button(frame_form, text="Registrar", command=self.registrar_usuario, 
                  bg="#4CAF50", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).grid(row=6, column=0, columnspan=2, pady=20)

        # Botón Volver
        tk.Button(self, text="Volver", command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                  bg="#2196F3", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).pack(pady=20)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get().strip()
        apellido = self.apellido_entry.get().strip()
        fecha_nacimiento = self.fecha_nacimiento_entry.get().strip()
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not (nombre and apellido and fecha_nacimiento and usuario and contrasena):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            id_usuario = registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contrasena)
            messagebox.showinfo("Éxito", f"Usuario registrado con éxito. ID: {id_usuario}")
            self.nombre_entry.delete(0, tk.END)
            self.apellido_entry.delete(0, tk.END)
            self.fecha_nacimiento_entry.delete(0, tk.END)
            self.usuario_entry.delete(0, tk.END)
            self.contrasena_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al registrar el usuario: {str(e)}")


class PantallaInicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        try:
            logo_img = Image.open("datos/imagenes/logo1.png")
            logo_img = logo_img.resize((200, 200), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(self, image=self.logo, bg="white").place(relx=0.5, rely=0.5, anchor="center")
        except FileNotFoundError:
            tk.Label(self, text="LOGO NO DISPONIBLE", bg="white", font=("Sans Serif", 20)).pack(expand=True)
        self.after(3000, lambda: controller.mostrar_ventana("VentanaInicio"))


class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")  # Pantalla completa
        self.state("zoomed")  # Maximizar ventana automáticamente también funciona con pantalla completa.

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PantallaInicio, VentanaInicio, VentanaPrincipal, VentanaRegistro):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.mostrar_ventana("PantallaInicio")

    def mostrar_ventana(self, nombre_ventana):
        self.frames[nombre_ventana].tkraise()


if __name__ == "__main__":
    app = MyEconomyApp()
    app.mainloop()
