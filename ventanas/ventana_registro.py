import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from .ventana_base import VentanaBase
from funciones import registrar_usuario

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

class VentanaRegistro(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame_principal = tk.Frame(self, bg=COLOR_FONDO, bd=0)
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")

        frame_form = tk.Frame(frame_principal, bg="white", padx=40, pady=40, 
                            relief="solid", borderwidth=0, 
                            highlightbackground="#bdc3c7", highlightthickness=1)
        frame_form.pack(pady=20, padx=20)

        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(frame_form, image=self.logo, bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))
        except:
            pass

        tk.Label(frame_form, text="Registro de Usuario", bg="white", fg=COLOR_PRIMARIO,
                font=FUENTE_TITULOS).grid(row=1, column=0, columnspan=2, pady=(0, 30))

        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.fecha_nacimiento = tk.StringVar()
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()
        
        self.crear_campo(frame_form, "Nombre:", 2, self.nombre)
        self.crear_campo(frame_form, "Apellido:", 3, self.apellido)
        self.crear_campo(frame_form, "Fecha de Nacimiento:", 4, self.fecha_nacimiento)
        self.crear_campo(frame_form, "Usuario:", 5, self.usuario)
        self.crear_campo(frame_form, "Contraseña:", 6, self.password, show="*")

        btn_registro = tk.Button(frame_form, text="Registrar", command=self.registrar_usuario,
                               bg=COLOR_CUARTO, fg="white", font=FUENTE_BOTONES,
                               width=20, height=2, bd=0, activebackground="#27ae60",
                               activeforeground="white")
        btn_registro.grid(row=7, column=0, columnspan=2, pady=(20, 10))

        btn_volver = tk.Button(frame_principal, text="Volver", 
                              command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                              bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                              width=20, height=2, bd=0, activebackground="#2980b9",
                              activeforeground="white")
        btn_volver.pack(pady=(0, 20))

    def crear_campo(self, frame, texto, fila, variable, show=None):
        tk.Label(frame, text=texto, bg="white", fg=COLOR_TEXTO,
                font=FUENTE_SUBTITULOS, anchor="w").grid(row=fila, column=0, pady=(10, 5), padx=10, sticky="ew")
        
        entry = tk.Entry(frame, textvariable=variable, font=FUENTE_TEXTO, width=25, bd=1, relief="solid",
                        highlightbackground="#bdc3c7", highlightthickness=1)
        if show:
            entry.config(show=show)
        entry.grid(row=fila, column=1, pady=(10, 5), padx=10)
        return entry

    def registrar_usuario(self):
        nombre = self.nombre.get().strip()
        apellido = self.apellido.get().strip()
        fecha_nacimiento = self.fecha_nacimiento.get().strip()
        usuario = self.usuario.get().strip()
        contrasena = self.password.get().strip()

        if not (nombre and apellido and fecha_nacimiento and usuario and contrasena):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            id_usuario = registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contrasena)
            messagebox.showinfo("Éxito", f"Usuario registrado con éxito. ID: {id_usuario}")
            self.nombre.set("")
            self.apellido.set("")
            self.fecha_nacimiento.set("")
            self.usuario.set("")
            self.password.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al registrar el usuario: {str(e)}")