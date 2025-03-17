import tkinter as tk
from tkinter import messagebox
from autenticacion.login import login
from autenticacion.registro import registrar_usuario

class VentanaPrincipal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#000000")
        self.parent = parent

        # Configurar el Frame para que ocupe todo el espacio disponible
        self.pack(fill="both", expand=True)

        # Marco para organizar los elementos
        marco = tk.Frame(self, bg="#000000")
        marco.pack(fill="both", expand=True)

        # Centrar el contenido en el marco
        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)

        # Crear un sub-frame para centrar los elementos
        sub_frame = tk.Frame(marco, bg="#000000")
        sub_frame.grid(row=0, column=0, sticky="nsew")

        # Centrar el contenido en el sub-frame
        sub_frame.grid_rowconfigure(0, weight=1)
        sub_frame.grid_rowconfigure(1, weight=1)
        sub_frame.grid_rowconfigure(2, weight=1)
        sub_frame.grid_rowconfigure(3, weight=1)
        sub_frame.grid_columnconfigure(0, weight=1)
        sub_frame.grid_columnconfigure(1, weight=1)

        # Campo de usuario
        etiqueta_usuario = tk.Label(sub_frame, text="Usuario:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_usuario.grid(row=0, column=0, pady=5, sticky="e")
        self.entrada_usuario = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_usuario.grid(row=0, column=1, pady=5, sticky="w")

        # Campo de contraseña
        etiqueta_contraseña = tk.Label(sub_frame, text="Contraseña:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_contraseña.grid(row=1, column=0, pady=5, sticky="e")
        self.entrada_contraseña = tk.Entry(sub_frame, show="*", bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_contraseña.grid(row=1, column=1, pady=5, sticky="w")

        # Botón de login
        boton_login = tk.Button(sub_frame, text="Iniciar Sesión", command=self.al_iniciar_sesion, bg="#32CD32", fg="#FFFFFF", font=("Rusilla Serif", 12))
        boton_login.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón de registro
        boton_registro = tk.Button(sub_frame, text="Registrarse", command=self.mostrar_registro, bg="#32CD32", fg="#FFFFFF", font=("Rusilla Serif", 12))
        boton_registro.grid(row=3, column=0, columnspan=2, pady=10)

    def al_iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        resultado, mensaje = login(usuario, contraseña)

        if resultado:
            messagebox.showinfo("Login", mensaje)
            # Aquí abriríamos la ventana principal
        else:
            messagebox.showerror("Error", mensaje)

    def mostrar_registro(self):
        # Ocultar el frame actual
        self.pack_forget()

        # Mostrar el frame de registro
        self.parent.ventana_registro = RegistroFrame(self.parent)
        self.parent.ventana_registro.pack(fill="both", expand=True)


class RegistroFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#000000")
        self.parent = parent

        # Configurar el Frame para que ocupe todo el espacio disponible
        self.pack(fill="both", expand=True)

        # Marco para organizar los elementos
        marco = tk.Frame(self, bg="#000000")
        marco.pack(fill="both", expand=True)

        # Centrar el contenido en el marco
        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)

        # Crear un sub-frame para centrar los elementos
        sub_frame = tk.Frame(marco, bg="#000000")
        sub_frame.grid(row=0, column=0, sticky="nsew")

        # Centrar el contenido en el sub-frame
        sub_frame.grid_rowconfigure(0, weight=1)
        sub_frame.grid_rowconfigure(1, weight=1)
        sub_frame.grid_rowconfigure(2, weight=1)
        sub_frame.grid_rowconfigure(3, weight=1)
        sub_frame.grid_rowconfigure(4, weight=1)
        sub_frame.grid_rowconfigure(5, weight=1)
        sub_frame.grid_columnconfigure(0, weight=1)
        sub_frame.grid_columnconfigure(1, weight=1)

        # Campo de nombre
        etiqueta_nombre = tk.Label(sub_frame, text="Nombre:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_nombre.grid(row=0, column=0, pady=5, sticky="e")
        self.entrada_nombre = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_nombre.grid(row=0, column=1, pady=5, sticky="w")

        # Campo de apellido
        etiqueta_apellido = tk.Label(sub_frame, text="Apellido:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_apellido.grid(row=1, column=0, pady=5, sticky="e")
        self.entrada_apellido = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_apellido.grid(row=1, column=1, pady=5, sticky="w")

        # Campo de fecha de nacimiento
        etiqueta_fecha_nacimiento = tk.Label(sub_frame, text="Fecha de Nacimiento (DD/MM/AAAA):", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_fecha_nacimiento.grid(row=2, column=0, pady=5, sticky="e")
        self.entrada_fecha_nacimiento = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_fecha_nacimiento.grid(row=2, column=1, pady=5, sticky="w")

        # Campo de usuario
        etiqueta_usuario = tk.Label(sub_frame, text="Usuario:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_usuario.grid(row=3, column=0, pady=5, sticky="e")
        self.entrada_usuario = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_usuario.grid(row=3, column=1, pady=5, sticky="w")

        # Campo de contraseña
        etiqueta_contraseña = tk.Label(sub_frame, text="Contraseña:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
        etiqueta_contraseña.grid(row=4, column=0, pady=5, sticky="e")
        self.entrada_contraseña = tk.Entry(sub_frame, show="*", bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
        self.entrada_contraseña.grid(row=4, column=1, pady=5, sticky="w")

        # Botón de registro
        boton_registro = tk.Button(sub_frame, text="Registrarse", command=self.al_registrarse, bg="#32CD32", fg="#FFFFFF", font=("Rusilla Serif", 12))
        boton_registro.grid(row=5, column=0, columnspan=2, pady=20)

        # Botón para volver al login
        boton_volver = tk.Button(sub_frame, text="Volver al Login", command=self.mostrar_login, bg="#32CD32", fg="#FFFFFF", font=("Rusilla Serif", 12))
        boton_volver.grid(row=6, column=0, columnspan=2, pady=10)

    def al_registrarse(self):
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        fecha_nacimiento = self.entrada_fecha_nacimiento.get()
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        if nombre and apellido and fecha_nacimiento and usuario and contraseña:
            registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contraseña)
            messagebox.showinfo("Registro", "¡Usuario registrado con éxito!")
            self.mostrar_login()  # Volver al login después del registro
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")

    def mostrar_login(self):
        # Ocultar el frame de registro
        self.pack_forget()

        # Mostrar el frame de login
        self.parent.ventana_principal.pack(fill="both", expand=True)