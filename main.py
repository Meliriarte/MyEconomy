import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


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


class VentanaInicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.cargar_elementos()

    def cargar_elementos(self):
        # Logo
        try:
            logo_img = Image.open("datos/imagenes/logo1.png")
            logo_img = logo_img.resize((200, 200), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(self, image=self.logo, bg="#FFFFFF").pack(pady=20)
        except FileNotFoundError:
            tk.Label(self, text="LOGO", font=("Sans Serif", 24), bg="#FFFFFF", fg="black").pack(pady=20)

        # Formulario
        frame_form = tk.Frame(self, bg="#333333", padx=20, pady=20)
        frame_form.pack(pady=20)

        tk.Label(frame_form, text="Usuario:", bg="#333333", fg="white",
                 font=("Sans Serif", 12)).grid(row=0, column=0, pady=5)
        self.usuario = tk.Entry(frame_form, font=("Sans Serif", 12))
        self.usuario.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Contraseña:", bg="#333333", fg="white",
                 font=("Sans Serif", 12)).grid(row=1, column=0, pady=5)
        self.password = tk.Entry(frame_form, show="*", font=("Sans Serif", 12))
        self.password.grid(row=1, column=1, pady=5)

        tk.Button(frame_form, text="Iniciar Sesión", command=self.login,
                  bg="#4CAF50", fg="white", font=("Sans Serif", 12),
                  padx=20).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(self, text="Registrarse", command=lambda: self.controller.mostrar_ventana("VentanaRegistro"),
                  bg="#2196F3", fg="white", font=("Sans Serif", 12)).pack(pady=10)

    def login(self):
        if self.usuario.get() == "admin" and self.password.get() == "1234":
            self.controller.mostrar_ventana("VentanaPrincipal")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")


class VentanaPrincipal(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#EEEEEE")

        tk.Label(self, text="Bienvenido a la Ventana Principal", font=("Sans Serif", 16),
                 bg="#EEEEEE", fg="black").pack(pady=20)

        tk.Button(self, text="Cerrar Sesión", command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                  bg="#FF5722", fg="white", font=("Sans Serif", 12)).pack(pady=10)


class VentanaRegistro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")

        # Título
        tk.Label(self, text="Formulario de Registro", font=("Sans Serif", 16), bg="#FFFFFF", fg="black").pack(pady=10)

        # Frame contenedor del formulario
        frame_form = tk.Frame(self, bg="#F0F0F0", padx=20, pady=20)
        frame_form.pack(pady=20)

        # Nombre
        tk.Label(frame_form, text="Nombre:", bg="#F0F0F0", font=("Sans Serif", 12)).grid(row=0, column=0, pady=5,
                                                                                         sticky="e")
        self.nombre_entry = tk.Entry(frame_form, font=("Sans Serif", 12))
        self.nombre_entry.grid(row=0, column=1, pady=5)

        # Apellido
        tk.Label(frame_form, text="Apellido:", bg="#F0F0F0", font=("Sans Serif", 12)).grid(row=1, column=0, pady=5,
                                                                                           sticky="e")
        self.apellido_entry = tk.Entry(frame_form, font=("Sans Serif", 12))
        self.apellido_entry.grid(row=1, column=1, pady=5)

        # Fecha de nacimiento
        tk.Label(frame_form, text="Fecha de Nacimiento:", bg="#F0F0F0", font=("Sans Serif", 12)).grid(
            row=2, column=0, pady=5, sticky="e")
        self.fecha_nacimiento_entry = tk.Entry(frame_form, font=("Sans Serif", 12))
        self.fecha_nacimiento_entry.grid(row=2, column=1, pady=5)

        # Usuario
        tk.Label(frame_form, text="Usuario:", bg="#F0F0F0", font=("Sans Serif", 12)).grid(row=3, column=0, pady=5,
                                                                                          sticky="e")
        self.usuario_entry = tk.Entry(frame_form, font=("Sans Serif", 12))
        self.usuario_entry.grid(row=3, column=1, pady=5)

        # Contraseña
        tk.Label(frame_form, text="Contraseña:", bg="#F0F0F0", font=("Sans Serif", 12)).grid(row=4, column=0, pady=5,
                                                                                             sticky="e")
        self.contrasena_entry = tk.Entry(frame_form, show="*", font=("Sans Serif", 12))
        self.contrasena_entry.grid(row=4, column=1, pady=5)

        # Botón registrar
        tk.Button(self, text="Registrar", command=self.registrar_usuario, bg="#4CAF50", fg="white",
                  font=("Sans Serif", 12), padx=20).pack(pady=10)

        # Botón volver
        tk.Button(self, text="Volver", command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                  bg="#2196F3", fg="white", font=("Sans Serif", 12)).pack(pady=10)

    def registrar_usuario(self):
        """Registra al usuario con los datos del formulario."""
        nombre = self.nombre_entry.get().strip()
        apellido = self.apellido_entry.get().strip()
        fecha_nacimiento = self.fecha_nacimiento_entry.get().strip()
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        # Verificar que no haya campos vacíos
        if not (nombre and apellido and fecha_nacimiento and usuario and contrasena):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Registrar al usuario
        try:
            id_usuario = registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contrasena)
            messagebox.showinfo("Éxito", f"Usuario registrado con éxito. ID: {id_usuario}")
            # Limpiar el formulario después del registro exitoso
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

        # Centro del contenedor
        try:
            imagen_logo = Image.open("datos/imagenes/logo1.png")
            imagen_logo = imagen_logo.resize((200, 200), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(imagen_logo)
            etiqueta_logo = tk.Label(self, image=self.logo, bg="white")
            etiqueta_logo.image = self.logo
            etiqueta_logo.place(relx=0.5, rely=0.5, anchor="center")
        except FileNotFoundError:
            tk.Label(self, text="LOGO NO DISPONIBLE", bg="white", font=("Sans Serif", 20)).pack(expand=True)

        # Temporizador
        self.after(3000, lambda: controller.mostrar_ventana("VentanaInicio"))


class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry("600x800")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Relaciones entre pantallas
        for F in (PantallaInicio, VentanaInicio, VentanaPrincipal, VentanaRegistro):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar la pantalla de inicio
        self.mostrar_ventana("PantallaInicio")

    def mostrar_ventana(self, nombre_ventana):
        frame = self.frames[nombre_ventana]
        frame.tkraise()


if __name__ == "__main__":
    app = MyEconomyApp()
    app.mainloop()