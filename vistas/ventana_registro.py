import tkinter as tk
from tkinter import messagebox
from autenticacion.registro import registrar_usuario

class RegistroFrame(tk.Frame):
    def __init__(self, parent, entrada_usuario_login, entrada_contraseña_login):
        super().__init__(parent, bg="#000000")
        self.parent = parent
        self.entrada_usuario_login = entrada_usuario_login
        self.entrada_contraseña_login = entrada_contraseña_login

        # Fuente Sans Serif
        self.fuente = ("Sans Serif", 12)

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
        etiqueta_nombre = tk.Label(sub_frame, text="Nombre:", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_nombre.grid(row=0, column=0, pady=5, sticky="e")
        self.entrada_nombre = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_nombre.grid(row=0, column=1, pady=5, sticky="w")

        # Campo de apellido
        etiqueta_apellido = tk.Label(sub_frame, text="Apellido:", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_apellido.grid(row=1, column=0, pady=5, sticky="e")
        self.entrada_apellido = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_apellido.grid(row=1, column=1, pady=5, sticky="w")

        # Campo de fecha de nacimiento
        etiqueta_fecha_nacimiento = tk.Label(sub_frame, text="Fecha de Nacimiento (DD/MM/AAAA):", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_fecha_nacimiento.grid(row=2, column=0, pady=5, sticky="e")
        self.entrada_fecha_nacimiento = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_fecha_nacimiento.grid(row=2, column=1, pady=5, sticky="w")

        # Campo de usuario
        etiqueta_usuario = tk.Label(sub_frame, text="Usuario:", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_usuario.grid(row=3, column=0, pady=5, sticky="e")
        self.entrada_usuario = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_usuario.grid(row=3, column=1, pady=5, sticky="w")

        # Campo de contraseña
        etiqueta_contraseña = tk.Label(sub_frame, text="Contraseña:", bg="#000000", fg="#FFFFFF", font=self.fuente)
        etiqueta_contraseña.grid(row=4, column=0, pady=5, sticky="e")
        self.entrada_contraseña = tk.Entry(sub_frame, show="*", bg="#F0F0F0", fg="#000000", font=self.fuente)
        self.entrada_contraseña.grid(row=4, column=1, pady=5, sticky="w")

        # Botón de registro
        boton_registro = tk.Button(sub_frame, text="Registrarse", command=self.al_registrarse, bg="#32CD32", fg="#FFFFFF", font=self.fuente)
        boton_registro.grid(row=5, column=0, columnspan=2, pady=20)

        # Botón para volver al login
        boton_volver = tk.Button(sub_frame, text="Volver al Login", command=self.mostrar_login, bg="#32CD32", fg="#FFFFFF", font=self.fuente)
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

            # Llenar automáticamente los campos de usuario y contraseña en el login
            self.entrada_usuario_login.delete(0, tk.END)
            self.entrada_usuario_login.insert(0, usuario)
            self.entrada_contraseña_login.delete(0, tk.END)
            self.entrada_contraseña_login.insert(0, contraseña)

            # Volver al login
            self.mostrar_login()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")

    def mostrar_login(self):
        # Ocultar el frame de registro con un efecto de fade-out
        self.parent.fade_out(self, self, self.parent.mostrar_login_fade_in)