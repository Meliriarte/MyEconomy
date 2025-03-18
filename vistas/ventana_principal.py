import tkinter as tk
from tkinter import messagebox
from autenticacion.login import login

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
        etiqueta_usuario = tk.Label(sub_frame, text="Usuario:", bg="#000000", fg="#FFFFFF", font=("Sanseriffic", 12))
        etiqueta_usuario.grid(row=0, column=0, pady=5, sticky="e")
        self.entrada_usuario = tk.Entry(sub_frame, bg="#F0F0F0", fg="#000000", font=("Sanseriffic", 12))
        self.entrada_usuario.grid(row=0, column=1, pady=5, sticky="w")

        # Campo de contraseña
        etiqueta_contraseña = tk.Label(sub_frame, text="Contraseña:", bg="#000000", fg="#FFFFFF", font=("Sanseriffic", 12))
        etiqueta_contraseña.grid(row=1, column=0, pady=5, sticky="e")
        self.entrada_contraseña = tk.Entry(sub_frame, show="*", bg="#F0F0F0", fg="#000000", font=("Sanseriffic", 12))
        self.entrada_contraseña.grid(row=1, column=1, pady=5, sticky="w")

        # Botón de login
        boton_login = tk.Button(sub_frame, text="Iniciar Sesión", command=self.al_iniciar_sesion, bg="#32CD32", fg="#FFFFFF", font=("Sanseriffic", 12))
        boton_login.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón de registro
        boton_registro = tk.Button(sub_frame, text="Registrarse", command=self.mostrar_registro, bg="#32CD32", fg="#FFFFFF", font=("Sanseriffic", 12))
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
        # Ocultar el frame actual con un efecto de fade-out
        self.parent.fade_out(self, self, self.parent.mostrar_registro_fade_in)