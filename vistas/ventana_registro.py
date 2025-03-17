import tkinter as tk
from tkinter import messagebox
from autenticacion.registro import registrar_usuario

def abrir_ventana_registro():
    def al_registrarse():
        nombre = entrada_nombre.get()
        apellido = entrada_apellido.get()
        fecha_nacimiento = entrada_fecha_nacimiento.get()
        usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()

        if nombre and apellido and fecha_nacimiento and usuario and contraseña:
            registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contraseña)
            messagebox.showinfo("Registro", "¡Usuario registrado con éxito!")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")

    # Crear la ventana de registro
    ventana_registro = tk.Toplevel()
    ventana_registro.title("MyEconomy - Registro")
    ventana_registro.geometry("500x500")
    ventana_registro.configure(bg="#000000")  # Fondo negro

    # Marco para organizar los elementos
    marco = tk.Frame(ventana_registro, bg="#000000")
    marco.pack(pady=50)

    # Campo de nombre
    etiqueta_nombre = tk.Label(marco, text="Nombre:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
    etiqueta_nombre.grid(row=0, column=0, pady=5)
    entrada_nombre = tk.Entry(marco, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
    entrada_nombre.grid(row=0, column=1, pady=5)

    # Campo de apellido
    etiqueta_apellido = tk.Label(marco, text="Apellido:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
    etiqueta_apellido.grid(row=1, column=0, pady=5)
    entrada_apellido = tk.Entry(marco, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
    entrada_apellido.grid(row=1, column=1, pady=5)

    # Campo de fecha de nacimiento
    etiqueta_fecha_nacimiento = tk.Label(marco, text="Fecha de Nacimiento (DD/MM/AAAA):", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
    etiqueta_fecha_nacimiento.grid(row=2, column=0, pady=5)
    entrada_fecha_nacimiento = tk.Entry(marco, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
    entrada_fecha_nacimiento.grid(row=2, column=1, pady=5)

    # Campo de usuario
    etiqueta_usuario = tk.Label(marco, text="Usuario:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
    etiqueta_usuario.grid(row=3, column=0, pady=5)
    entrada_usuario = tk.Entry(marco, bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
    entrada_usuario.grid(row=3, column=1, pady=5)

    # Campo de contraseña
    etiqueta_contraseña = tk.Label(marco, text="Contraseña:", bg="#000000", fg="#FFFFFF", font=("Rusilla Serif", 12))
    etiqueta_contraseña.grid(row=4, column=0, pady=5)
    entrada_contraseña = tk.Entry(marco, show="*", bg="#F0F0F0", fg="#000000", font=("Rusilla Serif", 12))
    entrada_contraseña.grid(row=4, column=1, pady=5)

    # Botón de registro
    boton_registro = tk.Button(marco, text="Registrarse", command=al_registrarse, bg="#32CD32", fg="#FFFFFF", font=("Rusilla Serif", 12))
    boton_registro.grid(row=5, column=0, columnspan=2, pady=20)

    ventana_registro.mainloop()