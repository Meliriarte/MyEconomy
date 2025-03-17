import tkinter as tk
from PIL import Image, ImageTk  # Quitar ImageResampling, ya no es necesario


def mostrar_pantalla_inicio():
    # Crear la ventana de inicio
    ventana_inicio = tk.Tk()
    ventana_inicio.title("MyEconomy")
    ventana_inicio.geometry("600x500")
    ventana_inicio.configure(bg="black")  # Fondo negro

    # Centrar la ventana en la pantalla
    ventana_inicio.update_idletasks()
    ancho = ventana_inicio.winfo_width()
    alto = ventana_inicio.winfo_height()
    x = (ventana_inicio.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana_inicio.winfo_screenheight() // 2) - (alto // 2)
    ventana_inicio.geometry(f"+{x}+{y}")

    # Cargar el logo
    try:
        imagen_logo = Image.open("datos/imagenes/logo1.png")  # Cambia la ruta a la ubicación de tu logo
        imagen_logo = imagen_logo.resize((200, 200), Image.Resampling.LANCZOS)  # Usamos LANCZOS directamente
        logo = ImageTk.PhotoImage(imagen_logo)
        etiqueta_logo = tk.Label(ventana_inicio, image=logo, bg="black")
        etiqueta_logo.image = logo  # Evitar que la imagen sea eliminada por el recolector de basura

        # Colocar el logo exactamente en el centro usando place
        etiqueta_logo.place(relx=0.5, rely=0.5, anchor="center")
    except FileNotFoundError:
        print("El archivo del logo no se encontró.")

    # Mostrar la ventana de inicio durante 3 segundos
    ventana_inicio.after(3000, ventana_inicio.destroy)  # Cerrar después de 3 segundos
    ventana_inicio.mainloop()